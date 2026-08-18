"""Build facilitator .sb3 solution files for Day 2 Scratch projects.

Uses py2sb3 for valid block JSON, then patches costumes and the shared score variable.

Run:
  python day-02-scratch/scratch-projects/build_solutions.py
"""

from __future__ import annotations

import json
import subprocess
import sys
import uuid
import zipfile
from pathlib import Path

ROOT = Path(__file__).parent
ASSETS_DIR = ROOT / "assets"
OUTPUT_DIR = ROOT / "solutions"
PY2SB3_SOURCE = ROOT / "catch_game_py2sb3.py"
PY2SB3_OUTPUT = ROOT / "_py2sb3_build.sb3"

COSTUME_BOWL = {
    "assetId": "d147f16e3e2583719c073ac5b55fe3ca",
    "name": "bowl-a",
    "bitmapResolution": 1,
    "md5ext": "d147f16e3e2583719c073ac5b55fe3ca.svg",
    "dataFormat": "svg",
    "rotationCenterX": 30,
    "rotationCenterY": 15,
}
COSTUME_APPLE = {
    "assetId": "3826a4091a33e4d26f87a2fac7cf796b",
    "name": "apple",
    "bitmapResolution": 1,
    "md5ext": "3826a4091a33e4d26f87a2fac7cf796b.svg",
    "dataFormat": "svg",
    "rotationCenterX": 31,
    "rotationCenterY": 31,
}
COSTUME_REFEREE = {
    "assetId": "46dde2baba61a7e48463ae8e58441470",
    "name": "referee-a",
    "bitmapResolution": 1,
    "md5ext": "46dde2baba61a7e48463ae8e58441470.svg",
    "dataFormat": "svg",
    "rotationCenterX": 44,
    "rotationCenterY": 63,
}
COSTUME_BACKDROP = {
    "assetId": "cd21514d0531fdffb22204e0ec5ed84a",
    "name": "backdrop1",
    "md5ext": "cd21514d0531fdffb22204e0ec5ed84a.svg",
    "dataFormat": "svg",
    "rotationCenterX": 240,
    "rotationCenterY": 180,
}

SPRITE_LAYOUT = {
    "Basket": {"costumes": [COSTUME_BOWL], "size": 130, "y": -145},
    "Fruit": {"costumes": [COSTUME_APPLE], "size": 75, "y": 0},
    "Referee": {"costumes": [COSTUME_REFEREE], "size": 85, "y": 40, "visible": False},
}

# Teaching notes attached as Scratch comment bubbles (same text as 01-catch-game-block-annotations.md).
BLOCK_ANNOTATIONS: dict[str, list[list[str]]] = {
    "Basket": [
        [
            "Start when the player clicks the green flag.",
            "Place the bowl at the bottom centre (x 0, y −145).",
            "Show the basket on the stage.",
            "Repeat movement checks for the whole game.",
            "If the left arrow key is pressed…",
            "Move the basket 10 steps left.",
            "If the right arrow key is pressed…",
            "Move the basket 10 steps right.",
        ],
    ],
    "Fruit": [
        [
            "Start when the game begins.",
            "Hide the original fruit — only clones should appear.",
            "Keep spawning clones for the whole game.",
            "Create a copy of this sprite (runs the clone script).",
            "Wait 1–3 seconds before spawning the next clone.",
        ],
        [
            "Runs once for each new fruit clone.",
            "Random x at the top of the stage (y 170).",
            "Show this clone (the original stays hidden).",
            "Fall until caught by the basket or off the bottom.",
            "Move down 5 steps (falling).",
            "Short pause so the fall looks smooth.",
            "Did this clone land on the basket?",
            "Add 1 point for a catch.",
            "Remove this clone (catch or miss).",
        ],
    ],
    "Referee": [
        [
            "Start when the game begins.",
            "Reset score to 0 for a new game.",
            "Hide the referee until the player wins.",
            "Keep checking the score.",
            "Brief pause (~20 checks per second).",
            "Has the player reached 20 points? (score > 19)",
            "Tell all sprites the game is won.",
            "Stop this script after broadcasting win.",
        ],
        [
            "Runs when the win message is broadcast.",
            "Show the referee on the stage.",
            'Say "You win!" for 3 seconds.',
            "Stop every script — game over.",
        ],
    ],
}

SKIP_COMMENT_OPCODES = frozenset(
    {
        "control_create_clone_of_menu",
        "sensing_touchingobjectmenu",
        "sensing_touchingobject",
        "sensing_keyoptions",
        "sensing_keypressed",
        "operator_random",
        "operator_not",
        "operator_or",
        "operator_lt",
        "operator_gt",
        "motion_yposition",
        "data_variable",
    }
)


def run_py2sb3() -> None:
    cmd = [sys.executable, "-m", "scratch.cli", "py2sb3", str(PY2SB3_SOURCE), str(PY2SB3_OUTPUT)]
    # scratch CLI entry point
    result = subprocess.run(
        ["scratch", "py2sb3", str(PY2SB3_SOURCE), str(PY2SB3_OUTPUT)],
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        raise RuntimeError(f"py2sb3 failed:\n{result.stdout}\n{result.stderr}")


def collect_score_ids(project: dict) -> dict[str, str]:
    """Move score to the stage (for all sprites) and return old_id -> stage_id map."""
    import uuid

    stage = project["targets"][0]
    old_ids: list[str] = []
    for target in project["targets"]:
        for var_id, (name, _) in target.get("variables", {}).items():
            if name == "score":
                old_ids.append(var_id)

    stage_score_id = old_ids[0] if old_ids else uuid.uuid4().hex[:20]
    stage.setdefault("variables", {})[stage_score_id] = ["score", 0]

    for target in project["targets"]:
        if target["isStage"]:
            continue
        target["variables"] = {
            k: v for k, v in target.get("variables", {}).items() if v[0] != "score"
        }

    return {old: stage_score_id for old in old_ids} or {stage_score_id: stage_score_id}


def patch_score_fields(project: dict, id_map: dict[str, str]) -> None:
    for target in project["targets"]:
        for block in target.get("blocks", {}).values():
            var_field = block.get("fields", {}).get("VARIABLE")
            if var_field and var_field[0] == "score":
                old_id = var_field[1]
                if old_id in id_map:
                    var_field[1] = id_map[old_id]
    for monitor in project.get("monitors", []):
        if monitor.get("params", {}).get("VARIABLE") == "score":
            monitor["id"] = next(iter(set(id_map.values())))


def patch_clone_menus(project: dict) -> None:
    """py2sb3 emits 'myself'; Scratch VM expects '_myself_' in clone menus."""
    for target in project["targets"]:
        for block in target.get("blocks", {}).values():
            if block.get("opcode") != "control_create_clone_of_menu":
                continue
            field = block.get("fields", {}).get("CLONE_OPTION")
            if field and field[0] == "myself":
                field[0] = "_myself_"


def _walk_script_blocks(blocks: dict, start_id: str):
    """Yield blocks in execution order (substack before next sibling)."""
    current = start_id
    while current:
        block = blocks[current]
        yield current, block
        for key in sorted(block.get("inputs", {})):
            value = block["inputs"][key]
            if (
                isinstance(value, list)
                and len(value) > 1
                and isinstance(value[1], str)
                and value[1] in blocks
            ):
                yield from _walk_script_blocks(blocks, value[1])
        current = block.get("next")


def _annotatable_blocks(blocks: dict, start_id: str) -> list[str]:
    ids: list[str] = []
    for block_id, block in _walk_script_blocks(blocks, start_id):
        if block.get("shadow"):
            continue
        if block["opcode"] in SKIP_COMMENT_OPCODES:
            continue
        ids.append(block_id)
    return ids


def _attach_comment(
    target: dict,
    block_id: str,
    text: str,
    blocks: dict,
    index: int,
) -> None:
    comment_id = uuid.uuid4().hex[:20]
    block = blocks[block_id]
    anchor_x = block.get("x", 0)
    anchor_y = block.get("y", index * 24)
    target.setdefault("comments", {})[comment_id] = {
        "blockId": block_id,
        "x": anchor_x + 260,
        "y": anchor_y,
        "width": 220,
        "height": min(120, 40 + text.count("\n") * 16),
        "minimized": False,
        "text": text,
    }
    block["comment"] = comment_id


def patch_block_comments(project: dict) -> None:
    """Attach Scratch comment bubbles to main blocks (visible in the editor)."""
    for target in project["targets"]:
        if target["isStage"]:
            continue
        sprite = target["name"]
        scripts = BLOCK_ANNOTATIONS.get(sprite)
        if not scripts:
            continue
        blocks = target["blocks"]
        hats = [(bid, b) for bid, b in blocks.items() if b.get("topLevel")]
        hats.sort(key=lambda item: item[1].get("y", 0))
        if len(hats) != len(scripts):
            raise RuntimeError(
                f"{sprite}: expected {len(scripts)} scripts, found {len(hats)} top-level blocks"
            )
        for (hat_id, _), notes in zip(hats, scripts):
            block_ids = _annotatable_blocks(blocks, hat_id)
            if len(block_ids) != len(notes):
                raise RuntimeError(
                    f"{sprite}: annotation count {len(notes)} != blocks {len(block_ids)} "
                    f"({[blocks[b]['opcode'] for b in block_ids]})"
                )
            for index, (block_id, text) in enumerate(zip(block_ids, notes)):
                _attach_comment(target, block_id, text, blocks, index)


def patch_sprites(project: dict) -> None:
    stage = project["targets"][0]
    stage["costumes"] = [COSTUME_BACKDROP]
    for target in project["targets"]:
        if target["isStage"]:
            continue
        layout = SPRITE_LAYOUT.get(target["name"])
        if not layout:
            continue
        target["costumes"] = layout["costumes"]
        target["size"] = layout["size"]
        if "y" in layout:
            target["y"] = layout["y"]
        if "visible" in layout:
            target["visible"] = layout["visible"]


def build_catch_game_project() -> dict:
    run_py2sb3()
    with zipfile.ZipFile(PY2SB3_OUTPUT, "r") as zf:
        project = json.loads(zf.read("project.json"))
    id_map = collect_score_ids(project)
    patch_score_fields(project, id_map)
    patch_clone_menus(project)
    patch_sprites(project)
    patch_block_comments(project)
    project.setdefault("monitors", [])
    score_id = next(iter(set(id_map.values())))
    project["monitors"] = [
        {
            "id": score_id,
            "mode": "default",
            "opcode": "data_variable",
            "params": {"VARIABLE": "score"},
            "spriteName": None,
            "targetId": None,
            "value": 0,
            "width": 0,
            "height": 0,
            "x": 5,
            "y": 5,
            "visible": True,
            "sliderMin": 0,
            "sliderMax": 100,
            "isDiscrete": True,
        }
    ]
    return project


def ensure_sprite_assets() -> None:
    ASSETS_DIR.mkdir(parents=True, exist_ok=True)
    required = [
        COSTUME_BOWL["md5ext"],
        COSTUME_APPLE["md5ext"],
        COSTUME_REFEREE["md5ext"],
        COSTUME_BACKDROP["md5ext"],
    ]
    missing = [name for name in required if not (ASSETS_DIR / name).exists()]
    if not missing:
        return
    import urllib.request

    base = "https://cdn.assets.scratch.mit.edu/internalapi/asset"
    for name in missing:
        urllib.request.urlretrieve(f"{base}/{name}/get/", ASSETS_DIR / name)


def write_sb3(project: dict, output_path: Path) -> None:
    ensure_sprite_assets()
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(output_path, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        for asset in ASSETS_DIR.iterdir():
            if asset.is_file() and asset.suffix.lower() in {".svg", ".png", ".wav", ".jpg", ".jpeg"}:
                zf.write(asset, arcname=asset.name)
        zf.writestr("project.json", json.dumps(project, separators=(",", ":")))


def main() -> None:
    project = build_catch_game_project()
    out = OUTPUT_DIR / "01-catch-game.sb3"
    write_sb3(project, out)
    print(f"Wrote {out}")


if __name__ == "__main__":
    main()
