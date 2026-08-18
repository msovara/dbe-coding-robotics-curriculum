"""Build facilitator .sb3 solution files for Day 2 Scratch projects.

Uses py2sb3 for valid block JSON, then patches costumes and the shared score variable.

Run:
  python day-02-scratch/scratch-projects/build_solutions.py
"""

from __future__ import annotations

import json
import shutil
import subprocess
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).parent
ASSETS_DIR = ROOT / "assets"
OUTPUT_DIR = ROOT / "solutions"
PY2SB3_CATCH = ROOT / "catch_game_py2sb3.py"
PY2SB3_WATER = ROOT / "water_cycle_py2sb3.py"
PY2SB3_OUTPUT = ROOT / "_py2sb3_build.sb3"
STAGE_COUNTERS = ("evaporated", "condensed", "precipitated", "ground_water")
VAR_DISPLAY_NAMES = {"ground_water": "ground water"}

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

COSTUME_SUN = {
    "assetId": "406808d86aff20a15d592b308e166a32",
    "name": "sun",
    "bitmapResolution": 1,
    "md5ext": "406808d86aff20a15d592b308e166a32.svg",
    "dataFormat": "svg",
    "rotationCenterX": 54,
    "rotationCenterY": 54,
}
COSTUME_DROPLET = {
    "assetId": "1c44b7494dec047371f74c705f1d99fc",
    "name": "ball-e",
    "bitmapResolution": 1,
    "md5ext": "1c44b7494dec047371f74c705f1d99fc.svg",
    "dataFormat": "svg",
    "rotationCenterX": 22,
    "rotationCenterY": 22,
}
COSTUME_CLOUD = {
    "assetId": "c9630e30e59e4565e785a26f58568904",
    "name": "cloud",
    "bitmapResolution": 1,
    "md5ext": "c9630e30e59e4565e785a26f58568904.svg",
    "dataFormat": "svg",
    "rotationCenterX": 71,
    "rotationCenterY": 45,
}
COSTUME_GROUND = {
    "assetId": "551b3fae8eab06b49013f54009a7767a",
    "name": "trees-a",
    "bitmapResolution": 1,
    "md5ext": "551b3fae8eab06b49013f54009a7767a.svg",
    "dataFormat": "svg",
    "rotationCenterX": 49,
    "rotationCenterY": 94,
}

WATER_LAYOUT = {
    "Sun": {"costumes": [COSTUME_SUN], "size": 90, "x": 170, "y": 120},
    "Droplet": {"costumes": [COSTUME_DROPLET], "size": 60, "x": -100, "y": -130},
    "Cloud": {"costumes": [COSTUME_CLOUD], "size": 110, "x": -70, "y": 120, "visible": False},
    "Ground": {"costumes": [COSTUME_GROUND], "size": 160, "x": 0, "y": -140},
}


def run_py2sb3(source: Path) -> None:
    result = subprocess.run(
        ["scratch", "py2sb3", str(source), str(PY2SB3_OUTPUT)],
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        raise RuntimeError(f"py2sb3 failed:\n{result.stdout}\n{result.stderr}")


def collect_stage_variable_ids(project: dict, names: tuple[str, ...]) -> dict[str, str]:
    """Move named variables to the stage (for all sprites). Returns old_id -> stage_id."""
    import uuid

    stage = project["targets"][0]
    found: dict[str, list[str]] = {name: [] for name in names}
    for target in project["targets"]:
        for var_id, (name, _) in target.get("variables", {}).items():
            if name in found:
                found[name].append(var_id)

    id_map: dict[str, str] = {}
    for name, old_ids in found.items():
        stage_id = old_ids[0] if old_ids else uuid.uuid4().hex[:20]
        display = VAR_DISPLAY_NAMES.get(name, name)
        stage.setdefault("variables", {})[stage_id] = [display, 0]
        for old in old_ids:
            id_map[old] = stage_id

    for target in project["targets"]:
        if target["isStage"]:
            continue
        target["variables"] = {
            k: v for k, v in target.get("variables", {}).items() if v[0] not in names
        }
    return id_map


def patch_variable_fields(project: dict, id_map: dict[str, str]) -> None:
    rename = {**VAR_DISPLAY_NAMES}
    for target in project["targets"]:
        for block in target.get("blocks", {}).values():
            var_field = block.get("fields", {}).get("VARIABLE")
            if not var_field:
                continue
            old_id = var_field[1]
            if old_id in id_map:
                var_field[1] = id_map[old_id]
            if var_field[0] in rename:
                var_field[0] = rename[var_field[0]]


def patch_clone_menus(project: dict) -> None:
    """py2sb3 writes 'myself'; Scratch only spawns clones when the menu value is '_myself_'."""
    for target in project["targets"]:
        for block in target.get("blocks", {}).values():
            if block.get("opcode") != "control_create_clone_of_menu":
                continue
            field = block.get("fields", {}).get("CLONE_OPTION")
            if field and field[0] == "myself":
                field[0] = "_myself_"


def patch_sprites(project: dict, layout_map: dict) -> None:
    stage = project["targets"][0]
    stage["costumes"] = [COSTUME_BACKDROP]
    for target in project["targets"]:
        if target["isStage"]:
            continue
        layout = layout_map.get(target["name"])
        if not layout:
            continue
        target["costumes"] = layout["costumes"]
        target["size"] = layout["size"]
        if "x" in layout:
            target["x"] = layout["x"]
        if "y" in layout:
            target["y"] = layout["y"]
        if "visible" in layout:
            target["visible"] = layout["visible"]


def make_monitor(var_id: str, name: str, x: int, y: int) -> dict:
    return {
        "id": var_id,
        "mode": "default",
        "opcode": "data_variable",
        "params": {"VARIABLE": name},
        "spriteName": None,
        "targetId": None,
        "value": 0,
        "width": 0,
        "height": 0,
        "x": x,
        "y": y,
        "visible": True,
        "sliderMin": 0,
        "sliderMax": 100,
        "isDiscrete": True,
    }


def load_py2sb3(source: Path) -> dict:
    run_py2sb3(source)
    with zipfile.ZipFile(PY2SB3_OUTPUT, "r") as zf:
        return json.loads(zf.read("project.json"))


def build_catch_game_project() -> dict:
    project = load_py2sb3(PY2SB3_CATCH)
    id_map = collect_stage_variable_ids(project, ("score",))
    patch_variable_fields(project, id_map)
    patch_clone_menus(project)
    patch_sprites(project, SPRITE_LAYOUT)
    score_id = next(iter(set(id_map.values())))
    project["monitors"] = [make_monitor(score_id, "score", 5, 5)]
    return project


def build_water_cycle_project() -> dict:
    project = load_py2sb3(PY2SB3_WATER)
    id_map = collect_stage_variable_ids(project, STAGE_COUNTERS)
    patch_variable_fields(project, id_map)
    patch_sprites(project, WATER_LAYOUT)
    stage_vars = project["targets"][0].get("variables", {})
    monitors = []
    y = 5
    for var_id, (name, _) in stage_vars.items():
        if name in {VAR_DISPLAY_NAMES.get(n, n) for n in STAGE_COUNTERS}:
            monitors.append(make_monitor(var_id, name, 5, y))
            y += 32
    project["monitors"] = monitors
    return project


def ensure_sprite_assets() -> None:
    ASSETS_DIR.mkdir(parents=True, exist_ok=True)
    required = [
        COSTUME_BOWL["md5ext"],
        COSTUME_APPLE["md5ext"],
        COSTUME_REFEREE["md5ext"],
        COSTUME_BACKDROP["md5ext"],
        COSTUME_SUN["md5ext"],
        COSTUME_DROPLET["md5ext"],
        COSTUME_CLOUD["md5ext"],
        COSTUME_GROUND["md5ext"],
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
    catch = build_catch_game_project()
    catch_out = OUTPUT_DIR / "01-catch-game.sb3"
    write_sb3(catch, catch_out)
    print(f"Wrote {catch_out}")
    water = build_water_cycle_project()
    water_out = OUTPUT_DIR / "04-water-cycle.sb3"
    write_sb3(water, water_out)
    print(f"Wrote {water_out}")


if __name__ == "__main__":
    main()
