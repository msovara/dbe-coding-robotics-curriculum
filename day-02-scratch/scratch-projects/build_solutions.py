"""Build facilitator .sb3 solution files for Day 2 Scratch projects.

Uses py2sb3 for valid block JSON, then patches costumes and the shared score variable.

Run:
  python day-02-scratch/scratch-projects/build_solutions.py
"""

from __future__ import annotations

import hashlib
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

GRASS_SVG = (
    b'<svg version="1.1" width="480" height="70" viewBox="0 0 480 70" '
    b'xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">'
    b'<rect x="0" y="28" width="480" height="42" fill="#3d9e3a"/>'
    b'<rect x="0" y="22" width="480" height="14" fill="#4caf50"/>'
    b'<rect x="0" y="58" width="480" height="12" fill="#2e7d32"/>'
    b'<rect x="8" y="10" width="6" height="22" fill="#57c257"/>'
    b'<rect x="28" y="6" width="5" height="26" fill="#66bb6a"/>'
    b'<rect x="52" y="12" width="6" height="20" fill="#57c257"/>'
    b'<rect x="76" y="8" width="5" height="24" fill="#66bb6a"/>'
    b'<rect x="104" y="11" width="6" height="21" fill="#57c257"/>'
    b'<rect x="132" y="7" width="5" height="25" fill="#66bb6a"/>'
    b'<rect x="160" y="10" width="6" height="22" fill="#57c257"/>'
    b'<rect x="190" y="6" width="5" height="26" fill="#66bb6a"/>'
    b'<rect x="220" y="12" width="6" height="20" fill="#57c257"/>'
    b'<rect x="250" y="8" width="5" height="24" fill="#66bb6a"/>'
    b'<rect x="280" y="11" width="6" height="21" fill="#57c257"/>'
    b'<rect x="310" y="7" width="5" height="25" fill="#66bb6a"/>'
    b'<rect x="340" y="10" width="6" height="22" fill="#57c257"/>'
    b'<rect x="370" y="6" width="5" height="26" fill="#66bb6a"/>'
    b'<rect x="400" y="12" width="6" height="20" fill="#57c257"/>'
    b'<rect x="430" y="8" width="5" height="24" fill="#66bb6a"/>'
    b'<rect x="458" y="11" width="6" height="21" fill="#57c257"/>'
    b"</svg>"
)


def grass_costume() -> dict:
    asset_id = hashlib.md5(GRASS_SVG).hexdigest()
    ASSETS_DIR.mkdir(parents=True, exist_ok=True)
    path = ASSETS_DIR / f"{asset_id}.svg"
    if not path.exists() or path.read_bytes() != GRASS_SVG:
        path.write_bytes(GRASS_SVG)
    return {
        "assetId": asset_id,
        "name": "grass",
        "bitmapResolution": 1,
        "md5ext": f"{asset_id}.svg",
        "dataFormat": "svg",
        "rotationCenterX": 240,
        "rotationCenterY": 35,
    }


COSTUME_GROUND = grass_costume()

WATER_LAYOUT = {
    "Sun": {"costumes": [COSTUME_SUN], "size": 90, "x": 170, "y": 120},
    "Droplet": {"costumes": [COSTUME_DROPLET], "size": 60, "x": -100, "y": -100},
    "Cloud": {"costumes": [COSTUME_CLOUD], "size": 110, "x": -70, "y": 120, "visible": False},
    "Ground": {"costumes": [COSTUME_GROUND], "size": 100, "x": 0, "y": -165},
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


def patch_stop_mutations(project: dict) -> None:
    """Scratch requires a mutation on control_stop; without it, stop can be ignored."""
    for target in project["targets"]:
        for block in target.get("blocks", {}).values():
            if block.get("opcode") != "control_stop":
                continue
            option = (block.get("fields") or {}).get("STOP_OPTION", ["all"])[0]
            hasnext = "true" if option == "other scripts in sprite" else "false"
            block["mutation"] = {
                "tagName": "mutation",
                "children": [],
                "hasnext": hasnext,
            }


def patch_stage_broadcasts(project: dict) -> None:
    """Scratch stores message names on the Stage; py2sb3 leaves that object empty."""
    stage = project["targets"][0]
    merged: dict[str, str] = dict(stage.get("broadcasts") or {})
    for target in project["targets"]:
        merged.update(target.get("broadcasts") or {})
        if not target["isStage"]:
            target["broadcasts"] = {}
    stage["broadcasts"] = merged


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
        target["sounds"] = []


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
    patch_stop_mutations(project)
    patch_stage_broadcasts(project)
    patch_sprites(project, SPRITE_LAYOUT)
    score_id = next(iter(set(id_map.values())))
    project["monitors"] = [make_monitor(score_id, "score", 5, 5)]
    return project


def build_water_cycle_project() -> dict:
    project = load_py2sb3(PY2SB3_WATER)
    id_map = collect_stage_variable_ids(project, STAGE_COUNTERS)
    patch_variable_fields(project, id_map)
    patch_stop_mutations(project)
    patch_stage_broadcasts(project)
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
        grass_costume()["md5ext"],
    ]
    missing = [name for name in required if not (ASSETS_DIR / name).exists()]
    if not missing:
        return
    import urllib.request

    base = "https://cdn.assets.scratch.mit.edu/internalapi/asset"
    for name in missing:
        urllib.request.urlretrieve(f"{base}/{name}/get/", ASSETS_DIR / name)


def collect_project_assets(project: dict) -> set[str]:
    names: set[str] = set()
    for target in project["targets"]:
        for item in target.get("costumes", []) + target.get("sounds", []):
            md5ext = item.get("md5ext")
            if md5ext:
                names.add(md5ext)
    return names


def write_sb3(project: dict, output_path: Path) -> None:
    ensure_sprite_assets()
    grass_costume()
    output_path.parent.mkdir(parents=True, exist_ok=True)
    needed = collect_project_assets(project)
    with zipfile.ZipFile(output_path, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        for name in sorted(needed):
            asset = ASSETS_DIR / name
            if not asset.exists():
                raise FileNotFoundError(f"Missing costume/sound in zip: {name}")
            zf.write(asset, arcname=name)
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
