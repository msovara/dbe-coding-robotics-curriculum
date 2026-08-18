"""Build facilitator .sb3 solution files for Day 2 Scratch projects.

Run from repo root:
  python day-02-scratch/scratch-projects/build_solutions.py
"""

from __future__ import annotations

import json
import uuid
import zipfile
from contextlib import contextmanager
from pathlib import Path
from typing import Any, Iterator

ROOT = Path(__file__).parent
TEMPLATE_DIR = ROOT / "_template_extracted"
OUTPUT_DIR = ROOT / "solutions"


def _id() -> str:
    return uuid.uuid4().hex[:20]


def _num(value: str | int | float) -> list[Any]:
    return [4, str(value)]


class Blocks:
    def __init__(self) -> None:
        self.data: dict[str, dict[str, Any]] = {}
        self._stack_last: str | None = None
        self._mouth: str | None = None

    def hat(self, opcode: str, *, x: int, y: int, fields: dict | None = None) -> str:
        bid = _id()
        self.data[bid] = {
            "opcode": opcode,
            "next": None,
            "parent": None,
            "inputs": {},
            "fields": fields or {},
            "shadow": False,
            "topLevel": True,
            "x": x,
            "y": y,
        }
        self._stack_last = bid
        self._mouth = None
        return bid

    def _append(self, bid: str) -> None:
        if self._mouth:
            if self._stack_last is None:
                self.data[self._mouth]["inputs"]["SUBSTACK"] = [2, bid]
            else:
                self.data[self._stack_last]["next"] = bid
            self.data[bid]["parent"] = self._mouth
        elif self._stack_last:
            self.data[self._stack_last]["next"] = bid
        self._stack_last = bid

    def stmt(self, opcode: str, *, inputs: dict | None = None, fields: dict | None = None) -> str:
        bid = _id()
        self.data[bid] = {
            "opcode": opcode,
            "next": None,
            "parent": None,
            "inputs": inputs or {},
            "fields": fields or {},
            "shadow": False,
            "topLevel": False,
        }
        self._append(bid)
        return bid

    def bool_block(self, opcode: str, *, inputs: dict | None = None, fields: dict | None = None) -> str:
        bid = _id()
        self.data[bid] = {
            "opcode": opcode,
            "next": None,
            "parent": None,
            "inputs": inputs or {},
            "fields": fields or {},
            "shadow": False,
            "topLevel": False,
        }
        return bid

    def menu_shadow(self, opcode: str, field_name: str, value: str) -> str:
        bid = _id()
        self.data[bid] = {
            "opcode": opcode,
            "next": None,
            "parent": None,
            "inputs": {},
            "fields": {field_name: [value, None]},
            "shadow": True,
            "topLevel": False,
        }
        return bid

    @contextmanager
    def mouth(self, opcode: str, *, condition: str | None = None) -> Iterator[str]:
        bid = _id()
        inputs: dict[str, list[Any]] = {}
        if condition is not None:
            inputs["CONDITION"] = [2, condition]
        self.data[bid] = {
            "opcode": opcode,
            "next": None,
            "parent": self._mouth,
            "inputs": inputs,
            "fields": {},
            "shadow": False,
            "topLevel": False,
        }
        self._append(bid)

        saved_mouth = self._mouth
        saved_last = self._stack_last
        self._mouth = bid
        self._stack_last = None
        try:
            yield bid
        finally:
            self._mouth = saved_mouth
            # The closed C-block is the sibling anchor for the parent mouth/stack.
            self._stack_last = bid

    def var_reporter(self, name: str, var_id: str) -> str:
        return self.bool_block("data_variable", fields={"VARIABLE": [name, var_id]})

    def key_pressed(self, key: str) -> str:
        return self.bool_block(
            "sensing_keypressed",
            inputs={"KEY_OPTION": [1, _num(key)]},
            fields={"KEY_OPTION": [key, None]},
        )

    def touching(self, sprite: str) -> str:
        menu = self.menu_shadow("sensing_touchingobjectmenu", "TOUCHINGOBJECTMENU", sprite)
        return self.bool_block("sensing_touchingobject", inputs={"TOUCHINGOBJECTMENU": [1, menu]})

    def compare(self, op: str, left: Any, right: Any) -> str:
        def input_for(value: Any) -> list[Any]:
            if isinstance(value, str) and value in self.data:
                return [3, value, [10, ""]]
            if isinstance(value, list):
                return [1, value]
            return [1, _num(value)]

        return self.bool_block(op, inputs={"OPERAND1": input_for(left), "OPERAND2": input_for(right)})

    def or_bool(self, left: str, right: str) -> str:
        return self.bool_block("operator_or", inputs={"OPERAND1": [2, left], "OPERAND2": [2, right]})

    def pick_random(self, low: int, high: int) -> str:
        bid = _id()
        self.data[bid] = {
            "opcode": "operator_random",
            "next": None,
            "parent": None,
            "inputs": {"FROM": [1, _num(low)], "TO": [1, _num(high)]},
            "fields": {},
            "shadow": False,
            "topLevel": False,
        }
        return bid


def default_costume() -> list[dict[str, Any]]:
    return [
        {
            "assetId": "bcf454acf82e4504149f7ffe07081dbc",
            "name": "costume1",
            "bitmapResolution": 1,
            "md5ext": "bcf454acf82e4504149f7ffe07081dbc.svg",
            "dataFormat": "svg",
            "rotationCenterX": 48,
            "rotationCenterY": 50,
        }
    ]


def make_sprite(name: str, blocks: Blocks, layer: int, **kwargs: Any) -> dict[str, Any]:
    return {
        "isStage": False,
        "name": name,
        "variables": {},
        "lists": {},
        "broadcasts": {},
        "blocks": blocks.data,
        "comments": {},
        "currentCostume": 0,
        "costumes": default_costume(),
        "sounds": [],
        "volume": 100,
        "layerOrder": layer,
        "visible": kwargs.get("visible", True),
        "x": kwargs.get("x", 0),
        "y": kwargs.get("y", 0),
        "size": 100,
        "direction": 90,
        "draggable": False,
        "rotationStyle": "all around",
    }


def make_stage(**kwargs: Any) -> dict[str, Any]:
    return {
        "isStage": True,
        "name": "Stage",
        "variables": kwargs.get("variables", {}),
        "lists": kwargs.get("lists", {}),
        "broadcasts": kwargs.get("broadcasts", {}),
        "blocks": kwargs.get("blocks", {}),
        "comments": {},
        "currentCostume": 0,
        "costumes": [
            {
                "assetId": "cd21514d0531fdffb22204e0ec5ed84a",
                "name": "backdrop1",
                "md5ext": "cd21514d0531fdffb22204e0ec5ed84a.svg",
                "dataFormat": "svg",
                "rotationCenterX": 240,
                "rotationCenterY": 180,
            }
        ],
        "sounds": [],
        "volume": 100,
        "layerOrder": 0,
        "tempo": 60,
        "videoTransparency": 50,
        "videoState": "on",
        "textToSpeechLanguage": None,
    }


def build_catch_game() -> dict[str, Any]:
    score_id = _id()
    win_id = _id()

    basket = Blocks()
    basket.hat("event_whenflagclicked", x=40, y=40)
    basket.stmt("motion_gotoxy", inputs={"X": [1, _num(0)], "Y": [1, _num(-145)]})
    basket.stmt("looks_show")
    with basket.mouth("control_forever"):
        with basket.mouth("control_if", condition=basket.key_pressed("left arrow")):
            basket.stmt("motion_changexby", inputs={"DX": [1, _num(-10)]})
        with basket.mouth("control_if", condition=basket.key_pressed("right arrow")):
            basket.stmt("motion_changexby", inputs={"DX": [1, _num(10)]})

    fruit = Blocks()
    fruit.hat("event_whenflagclicked", x=40, y=40)
    fruit.stmt("looks_hide")
    with fruit.mouth("control_forever"):
        clone_menu = fruit.menu_shadow("control_create_clone_of_menu", "CLONE_OPTION", "myself")
        fruit.stmt("control_create_clone_of", inputs={"CLONE_OPTION": [1, clone_menu]})
        wait_rand = fruit.pick_random(1, 3)
        fruit.stmt("control_wait", inputs={"DURATION": [3, wait_rand, [4, "1"]]})

    clone = Blocks()
    clone.hat("control_start_as_clone", x=40, y=220)
    rand_x = clone.pick_random(-200, 200)
    clone.stmt(
        "motion_gotoxy",
        inputs={"X": [3, rand_x, [4, "0"]], "Y": [1, _num(170)]},
    )
    clone.stmt("looks_show")
    y_pos = clone.bool_block("motion_yposition")
    stop_cond = clone.or_bool(clone.touching("Basket"), clone.compare("operator_lt", y_pos, -170))
    with clone.mouth("control_repeat_until", condition=stop_cond):
        clone.stmt("motion_changeyby", inputs={"DY": [1, _num(-5)]})
        clone.stmt("control_wait", inputs={"DURATION": [1, _num(0.03)]})
    with clone.mouth("control_if", condition=clone.touching("Basket")):
        clone.stmt(
            "data_changevariableby",
            fields={"VARIABLE": ["score", score_id]},
            inputs={"VALUE": [1, _num(1)]},
        )
    clone.stmt("control_delete_this_clone")

    referee = Blocks()
    referee.hat("event_whenflagclicked", x=40, y=40)
    referee.stmt(
        "data_setvariableto",
        fields={"VARIABLE": ["score", score_id]},
        inputs={"VALUE": [1, _num(0)]},
    )
    referee.stmt("looks_hide")
    referee.stmt(
        "control_wait_until",
        inputs={
            "CONDITION": [
                2,
                referee.compare("operator_gt", referee.var_reporter("score", score_id), 19),
            ]
        },
    )
    referee.stmt("event_broadcast", fields={"BROADCAST_OPTION": ["win", win_id]})

    referee.hat(
        "event_whenbroadcastreceived",
        x=40,
        y=220,
        fields={"BROADCAST_OPTION": ["win", win_id]},
    )
    referee.stmt("looks_show")
    referee.stmt(
        "looks_sayforsecs",
        inputs={"MESSAGE": [1, [4, "You win!"]], "SECS": [1, _num(3)]},
    )
    stop_menu = referee.menu_shadow("control_stop_menu", "STOP_OPTION", "all")
    referee.stmt("control_stop", inputs={"STOP_OPTION": [1, stop_menu]})

    fruit_all = Blocks()
    fruit_all.data.update(fruit.data)
    fruit_all.data.update(clone.data)

    return {
        "targets": [
            make_stage(variables={score_id: ["score", 0]}, broadcasts={win_id: "win"}),
            make_sprite("Basket", basket, 1, y=-145),
            make_sprite("Fruit", fruit_all, 2, visible=True),
            make_sprite("Referee", referee, 3, visible=False),
        ],
        "monitors": [
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
        ],
        "extensions": [],
        "meta": {
            "semver": "3.0.0",
            "vm": "11.5.0",
            "agent": "dbe-coding-robotics-curriculum",
        },
    }


def ensure_template_assets() -> None:
    if TEMPLATE_DIR.exists():
        return
    template_sb3 = ROOT / "_template.sb3"
    if not template_sb3.exists():
        raise FileNotFoundError(
            "Missing _template_extracted/ and _template.sb3. "
            "See scratch-projects/README.md for setup."
        )
    with zipfile.ZipFile(template_sb3, "r") as zf:
        zf.extractall(TEMPLATE_DIR)


def write_sb3(project: dict[str, Any], output_path: Path) -> None:
    ensure_template_assets()
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(output_path, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        for asset in TEMPLATE_DIR.iterdir():
            if asset.name != "project.json":
                zf.write(asset, arcname=asset.name)
        zf.writestr("project.json", json.dumps(project, separators=(",", ":")))


def main() -> None:
    projects = {
        "01-catch-game.sb3": build_catch_game,
    }
    for filename, builder in projects.items():
        path = OUTPUT_DIR / filename
        write_sb3(builder(), path)
        print(f"Wrote {path}")


if __name__ == "__main__":
    main()
