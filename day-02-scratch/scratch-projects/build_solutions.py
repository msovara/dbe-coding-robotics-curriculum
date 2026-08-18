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
PY2SB3_STORY = ROOT / "interactive_story_py2sb3.py"
PY2SB3_DAY1_STORY = (
    ROOT.parent.parent / "day-01-scratch" / "scratch-projects" / "interactive_story_day1_py2sb3.py"
)
DAY1_OUTPUT_DIR = ROOT.parent.parent / "day-01-scratch" / "scratch-projects" / "solutions"
PY2SB3_OUTPUT = ROOT / "_py2sb3_build.sb3"
STAGE_COUNTERS = ("evaporated", "condensed", "precipitated", "ground_water")
STORY_VARS = ("choice",)
STORY_LISTS = ("story_choices",)
VAR_DISPLAY_NAMES = {
    "ground_water": "ground water",
    "story_choices": "story choices",
}
BROADCAST_DISPLAY_NAMES = {
    "scene_1": "scene 1",
    "scene_2": "scene 2",
    "path_A": "path A",
    "path_B": "path B",
    "ending_A": "ending A",
    "ending_B": "ending B",
}

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

COSTUME_AVERY = {
    "assetId": "f52bde34d8027aab14b53f228fe5cc14",
    "name": "avery-a",
    "bitmapResolution": 1,
    "md5ext": "f52bde34d8027aab14b53f228fe5cc14.svg",
    "dataFormat": "svg",
    "rotationCenterX": 39,
    "rotationCenterY": 94,
}
COSTUME_PICO = {
    "assetId": "e7ce31db37f7abd2901499db2e9ad83a",
    "name": "pico-a",
    "bitmapResolution": 1,
    "md5ext": "e7ce31db37f7abd2901499db2e9ad83a.svg",
    "dataFormat": "svg",
    "rotationCenterX": 55,
    "rotationCenterY": 66,
}
COSTUME_ROBOT = {
    "assetId": "89679608327ad572b93225d06fe9edda",
    "name": "robot-a",
    "bitmapResolution": 1,
    "md5ext": "89679608327ad572b93225d06fe9edda.svg",
    "dataFormat": "svg",
    "rotationCenterX": 58,
    "rotationCenterY": 96,
}

STORY_LAYOUT = {
    "Guide": {"costumes": [COSTUME_AVERY], "size": 80, "x": -100, "y": -80},
    "Scientist": {
        "costumes": [COSTUME_PICO],
        "size": 90,
        "x": 20,
        "y": -70,
        "visible": False,
    },
    "Robot": {
        "costumes": [COSTUME_ROBOT],
        "size": 85,
        "x": 30,
        "y": -60,
        "visible": False,
    },
}

STORY_BACKDROP_SVG = {
    "Laboratory": (
        b'<svg version="1.1" width="480" height="360" viewBox="0 0 480 360" '
        b'xmlns="http://www.w3.org/2000/svg">'
        b'<rect width="480" height="360" fill="#d5e0ea"/>'
        b'<rect y="230" width="480" height="130" fill="#8b9aaa"/>'
        b'<rect x="36" y="70" width="130" height="90" fill="#b7d0e4"/>'
        b'<rect x="44" y="78" width="114" height="74" fill="#eef6fb"/>'
        b'<rect x="290" y="150" width="150" height="90" fill="#c5d2dc"/>'
        b'<rect x="300" y="128" width="130" height="28" fill="#5f7384"/>'
        b'<rect x="80" y="200" width="70" height="50" fill="#9aa8b5"/>'
        b"</svg>"
    ),
    "Forest": (
        b'<svg version="1.1" width="480" height="360" viewBox="0 0 480 360" '
        b'xmlns="http://www.w3.org/2000/svg">'
        b'<rect width="480" height="360" fill="#87ceeb"/>'
        b'<rect y="230" width="480" height="130" fill="#3d9e3a"/>'
        b'<rect x="70" y="160" width="22" height="90" fill="#6d4c41"/>'
        b'<circle cx="81" cy="140" r="48" fill="#2e7d32"/>'
        b'<rect x="220" y="140" width="26" height="110" fill="#5d4037"/>'
        b'<circle cx="233" cy="118" r="62" fill="#388e3c"/>'
        b'<rect x="370" y="170" width="20" height="80" fill="#6d4c41"/>'
        b'<circle cx="380" cy="150" r="42" fill="#43a047"/>'
        b"</svg>"
    ),
    "Space": (
        b'<svg version="1.1" width="480" height="360" viewBox="0 0 480 360" '
        b'xmlns="http://www.w3.org/2000/svg">'
        b'<rect width="480" height="360" fill="#0b1026"/>'
        b'<circle cx="60" cy="50" r="3" fill="#fff"/>'
        b'<circle cx="140" cy="90" r="2" fill="#ffe082"/>'
        b'<circle cx="220" cy="40" r="2.5" fill="#fff"/>'
        b'<circle cx="310" cy="70" r="2" fill="#fff"/>'
        b'<circle cx="400" cy="45" r="3" fill="#ffe082"/>'
        b'<circle cx="80" cy="180" r="2" fill="#fff"/>'
        b'<circle cx="180" cy="220" r="2.5" fill="#fff"/>'
        b'<circle cx="260" cy="160" r="2" fill="#ffe082"/>'
        b'<circle cx="350" cy="200" r="2" fill="#fff"/>'
        b'<circle cx="430" cy="140" r="2.5" fill="#fff"/>'
        b'<circle cx="400" cy="250" r="38" fill="#5c6bc0"/>'
        b'<circle cx="388" cy="238" r="12" fill="#7986cb"/>'
        b"</svg>"
    ),
    "Ending A": (
        b'<svg version="1.1" width="480" height="360" viewBox="0 0 480 360" '
        b'xmlns="http://www.w3.org/2000/svg">'
        b'<rect width="480" height="360" fill="#f6e27a"/>'
        b'<circle cx="240" cy="150" r="70" fill="#ffca28"/>'
        b'<rect y="260" width="480" height="100" fill="#f4d35e"/>'
        b"</svg>"
    ),
    "Ending B": (
        b'<svg version="1.1" width="480" height="360" viewBox="0 0 480 360" '
        b'xmlns="http://www.w3.org/2000/svg">'
        b'<rect width="480" height="360" fill="#5c4d7d"/>'
        b'<rect y="250" width="480" height="110" fill="#3f3560"/>'
        b'<circle cx="90" cy="70" r="4" fill="#efe6ff"/>'
        b'<circle cx="200" cy="50" r="3" fill="#efe6ff"/>'
        b'<circle cx="340" cy="80" r="3" fill="#efe6ff"/>'
        b'<circle cx="420" cy="40" r="4" fill="#efe6ff"/>'
        b"</svg>"
    ),
}


def write_svg_costume(name: str, svg: bytes, center_x: int, center_y: int) -> dict:
    asset_id = hashlib.md5(svg).hexdigest()
    ASSETS_DIR.mkdir(parents=True, exist_ok=True)
    path = ASSETS_DIR / f"{asset_id}.svg"
    if not path.exists() or path.read_bytes() != svg:
        path.write_bytes(svg)
    return {
        "assetId": asset_id,
        "name": name,
        "bitmapResolution": 1,
        "md5ext": f"{asset_id}.svg",
        "dataFormat": "svg",
        "rotationCenterX": center_x,
        "rotationCenterY": center_y,
    }


def story_backdrops() -> list[dict]:
    return [
        write_svg_costume(name, svg, 240, 180)
        for name, svg in STORY_BACKDROP_SVG.items()
    ]


DAY1_STORY_BACKDROP_SVG = {
    "Home": (
        b'<svg version="1.1" width="480" height="360" viewBox="0 0 480 360" '
        b'xmlns="http://www.w3.org/2000/svg">'
        b'<rect width="480" height="360" fill="#f3e6d4"/>'
        b'<rect y="250" width="480" height="110" fill="#c4a484"/>'
        b'<rect x="70" y="90" width="160" height="160" fill="#e8c39e"/>'
        b'<rect x="90" y="120" width="50" height="50" fill="#7eb6d9"/>'
        b'<rect x="160" y="120" width="50" height="50" fill="#7eb6d9"/>'
        b'<rect x="130" y="180" width="40" height="70" fill="#8d6e63"/>'
        b'<rect x="300" y="140" width="110" height="110" fill="#d7ccc8"/>'
        b"</svg>"
    ),
    "Road": (
        b'<svg version="1.1" width="480" height="360" viewBox="0 0 480 360" '
        b'xmlns="http://www.w3.org/2000/svg">'
        b'<rect width="480" height="360" fill="#87ceeb"/>'
        b'<rect y="200" width="480" height="160" fill="#7cb342"/>'
        b'<rect y="250" width="480" height="70" fill="#616161"/>'
        b'<rect x="20" y="280" width="40" height="8" fill="#fdd835"/>'
        b'<rect x="90" y="280" width="40" height="8" fill="#fdd835"/>'
        b'<rect x="160" y="280" width="40" height="8" fill="#fdd835"/>'
        b'<rect x="230" y="280" width="40" height="8" fill="#fdd835"/>'
        b'<rect x="300" y="280" width="40" height="8" fill="#fdd835"/>'
        b'<rect x="370" y="280" width="40" height="8" fill="#fdd835"/>'
        b'<rect x="440" y="280" width="30" height="8" fill="#fdd835"/>'
        b"</svg>"
    ),
    "School": (
        b'<svg version="1.1" width="480" height="360" viewBox="0 0 480 360" '
        b'xmlns="http://www.w3.org/2000/svg">'
        b'<rect width="480" height="360" fill="#bbdefb"/>'
        b'<rect y="260" width="480" height="100" fill="#8d6e63"/>'
        b'<rect x="90" y="80" width="300" height="180" fill="#ef9a9a"/>'
        b'<polygon points="90,80 240,20 390,80" fill="#c62828"/>'
        b'<rect x="210" y="180" width="60" height="80" fill="#5d4037"/>'
        b'<rect x="120" y="110" width="50" height="40" fill="#fff59d"/>'
        b'<rect x="310" y="110" width="50" height="40" fill="#fff59d"/>'
        b'<rect x="120" y="170" width="50" height="40" fill="#fff59d"/>'
        b'<rect x="310" y="170" width="50" height="40" fill="#fff59d"/>'
        b"</svg>"
    ),
}


def day1_story_backdrops() -> list[dict]:
    return [
        write_svg_costume(name, svg, 240, 180)
        for name, svg in DAY1_STORY_BACKDROP_SVG.items()
    ]


DAY1_STORY_LAYOUT = {
    "Child": {"costumes": [COSTUME_AVERY], "size": 80, "x": -80, "y": -60},
    "Friend": {
        "costumes": [COSTUME_PICO],
        "size": 90,
        "x": 80,
        "y": -60,
        "visible": False,
    },
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


def collect_stage_list_ids(project: dict, names: tuple[str, ...]) -> dict[str, str]:
    """Move named lists to the stage (for all sprites). Returns old_id -> stage_id."""
    import uuid

    stage = project["targets"][0]
    found: dict[str, list[str]] = {name: [] for name in names}
    for target in project["targets"]:
        for list_id, data in target.get("lists", {}).items():
            if data[0] in found:
                found[data[0]].append(list_id)

    id_map: dict[str, str] = {}
    canonical: set[str] = set()
    for name, old_ids in found.items():
        stage_id = old_ids[0] if old_ids else uuid.uuid4().hex[:20]
        display = VAR_DISPLAY_NAMES.get(name, name)
        stage.setdefault("lists", {})[stage_id] = [display, []]
        canonical.add(stage_id)
        for old in old_ids:
            id_map[old] = stage_id

    mapped_names = {VAR_DISPLAY_NAMES.get(n, n) for n in names} | set(names)
    stage["lists"] = {
        k: v
        for k, v in stage.get("lists", {}).items()
        if v[0] not in mapped_names or k in canonical
    }

    for target in project["targets"]:
        if target["isStage"]:
            continue
        target["lists"] = {
            k: v for k, v in target.get("lists", {}).items() if v[0] not in names
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


def patch_list_fields(project: dict, id_map: dict[str, str]) -> None:
    rename = {**VAR_DISPLAY_NAMES}
    for target in project["targets"]:
        for block in target.get("blocks", {}).values():
            list_field = block.get("fields", {}).get("LIST")
            if not list_field:
                continue
            old_id = list_field[1]
            if old_id in id_map:
                list_field[1] = id_map[old_id]
            if list_field[0] in rename:
                list_field[0] = rename[list_field[0]]


def patch_broadcast_display_names(project: dict, mapping: dict[str, str]) -> None:
    """Rename py2sb3 identifiers (scene_1) to memo names (scene 1)."""
    if not mapping:
        return
    for target in project["targets"]:
        broadcasts = target.get("broadcasts") or {}
        if broadcasts:
            target["broadcasts"] = {mapping.get(name, name): bid for name, bid in broadcasts.items()}
        for block in target.get("blocks", {}).values():
            option = (block.get("fields") or {}).get("BROADCAST_OPTION")
            if option:
                option[0] = mapping.get(option[0], option[0])
            broadcast_input = (block.get("inputs") or {}).get("BROADCAST_INPUT")
            if (
                isinstance(broadcast_input, list)
                and len(broadcast_input) > 1
                and isinstance(broadcast_input[1], list)
                and len(broadcast_input[1]) >= 2
            ):
                broadcast_input[1][1] = mapping.get(broadcast_input[1][1], broadcast_input[1][1])


def merge_sprite_onto_stage(project: dict, sprite_name: str) -> None:
    """Move a dummy sprite's scripts onto Stage, then delete the sprite."""
    dummy = next((t for t in project["targets"] if t.get("name") == sprite_name), None)
    if not dummy:
        return
    stage = project["targets"][0]
    stage.setdefault("blocks", {}).update(dummy.get("blocks") or {})
    stage.setdefault("lists", {}).update(dummy.get("lists") or {})
    stage.setdefault("variables", {}).update(dummy.get("variables") or {})
    project["targets"] = [t for t in project["targets"] if t.get("name") != sprite_name]


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


def patch_sprites(
    project: dict,
    layout_map: dict,
    stage_costumes: list[dict] | None = None,
) -> None:
    stage = project["targets"][0]
    stage["costumes"] = stage_costumes if stage_costumes else [COSTUME_BACKDROP]
    if stage_costumes:
        stage["currentCostume"] = 0
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


def make_list_monitor(list_id: str, name: str, x: int, y: int) -> dict:
    return {
        "id": list_id,
        "mode": "list",
        "opcode": "data_listcontents",
        "params": {"LIST": name},
        "spriteName": None,
        "targetId": None,
        "value": [],
        "width": 140,
        "height": 130,
        "x": x,
        "y": y,
        "visible": True,
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


def build_story_project() -> dict:
    project = load_py2sb3(PY2SB3_STORY)
    merge_sprite_onto_stage(project, "StageBackdrops")
    var_map = collect_stage_variable_ids(project, STORY_VARS)
    list_map = collect_stage_list_ids(project, STORY_LISTS)
    patch_variable_fields(project, var_map)
    patch_list_fields(project, list_map)
    patch_broadcast_display_names(project, BROADCAST_DISPLAY_NAMES)
    patch_stop_mutations(project)
    patch_stage_broadcasts(project)
    patch_sprites(project, STORY_LAYOUT, stage_costumes=story_backdrops())
    stage = project["targets"][0]
    monitors = []
    choice_id = next(iter(set(var_map.values())), None)
    if choice_id:
        monitors.append(make_monitor(choice_id, "choice", 5, 5))
    list_id = next(iter(set(list_map.values())), None)
    if list_id:
        monitors.append(make_list_monitor(list_id, "story choices", 5, 40))
    # Keep unused stage vars from leaking as extra monitors.
    project["monitors"] = monitors
    stage["currentCostume"] = 0
    return project


def build_day1_story_project() -> dict:
    project = load_py2sb3(PY2SB3_DAY1_STORY)
    merge_sprite_onto_stage(project, "StageBackdrops")
    patch_broadcast_display_names(project, BROADCAST_DISPLAY_NAMES)
    patch_stop_mutations(project)
    patch_stage_broadcasts(project)
    patch_sprites(project, DAY1_STORY_LAYOUT, stage_costumes=day1_story_backdrops())
    project["monitors"] = []
    project["targets"][0]["currentCostume"] = 0
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
        COSTUME_AVERY["md5ext"],
        COSTUME_PICO["md5ext"],
        COSTUME_ROBOT["md5ext"],
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
    story_backdrops()
    day1_story_backdrops()
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
    story = build_story_project()
    story_out = OUTPUT_DIR / "05-interactive-story.sb3"
    write_sb3(story, story_out)
    print(f"Wrote {story_out}")
    day1 = build_day1_story_project()
    day1_out = DAY1_OUTPUT_DIR / "03-interactive-story.sb3"
    write_sb3(day1, day1_out)
    print(f"Wrote {day1_out}")
    day1_pages = (
        ROOT.parent.parent
        / "day-01-scratch"
        / "projects"
        / "03-interactive-story-code"
        / "03-interactive-story.sb3"
    )
    shutil.copy2(day1_out, day1_pages)
    print(f"Wrote {day1_pages}")


if __name__ == "__main__":
    main()
