"""Generate narrated Catch Game solution video (MP4).

Requires: pip install pillow imageio imageio-ffmpeg edge-tts

Run from repo root:
  python day-02-scratch/scratch-projects/videos/generate_catch_game_video.py
"""

from __future__ import annotations

import asyncio
import subprocess
import textwrap
from pathlib import Path

import edge_tts
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).parent
OUTPUT = ROOT / "01-catch-game-solution.mp4"
WORK = ROOT / "_video_build"
VOICE = "en-GB-SoniaNeural"
SIZE = (1280, 720)

SCENES: list[dict[str, object]] = [
    {
        "title": "Catch Game — Video solution",
        "bullets": [
            "Day 2 Scratch project",
            "Cloning, score, collision",
            "About 8 minutes",
        ],
        "narration": (
            "This video walks through the Catch Game solution for Day 2 of the "
            "DBE Coding and Robotics workshop. You will see how the Basket, Fruit, "
            "and Referee sprites work together using cloning, variables, and "
            "broadcast messages."
        ),
    },
    {
        "title": "What we are building",
        "bullets": [
            "Basket moves with arrow keys",
            "Fruit clones fall from the top",
            "Score 20 points to win",
        ],
        "narration": (
            "The player moves a basket at the bottom of the stage. Fruit clones "
            "fall from random positions at the top. Each catch adds one to the "
            "score. When the score reaches twenty, the game shows a win message "
            "and stops."
        ),
    },
    {
        "title": "Open the solution file",
        "bullets": [
            "Download 01-catch-game.sb3",
            "Scratch: File → Load from your computer",
            "Or open in TurboWarp",
        ],
        "narration": (
            "You can follow along in Scratch by loading the solution file "
            "zero one catch game dot S B three from the curriculum folder. "
            "In Scratch, choose File, Load from your computer. You can also "
            "drag the file onto TurboWarp dot org for a quick preview."
        ),
    },
    {
        "title": "Setup: variables and messages",
        "bullets": [
            "Variable: score (for all sprites)",
            "Broadcast: win",
            "Sprites: Basket, Fruit, Referee",
        ],
        "narration": (
            "Before coding, create one variable called score for all sprites. "
            "Create a broadcast message called win. You need three sprites: "
            "Basket, Fruit, and an optional Referee that handles scoring and "
            "the win screen."
        ),
    },
    {
        "title": "Basket sprite",
        "bullets": [
            "when green flag clicked",
            "go to x 0 y minus 145, show",
            "forever: left arrow minus 10, right arrow plus 10",
        ],
        "narration": (
            "Select the Basket sprite. When the green flag is clicked, go to "
            "x zero and y minus one forty five, then show the sprite. "
            "Inside a forever loop, if the left arrow key is pressed, change x "
            "by minus ten. If the right arrow key is pressed, change x by plus ten."
        ),
    },
    {
        "title": "Fruit — script 1 (spawner)",
        "bullets": [
            "Both scripts on ONE Fruit sprite",
            "when green flag clicked → hide",
            "forever: create clone, wait 1 to 3 seconds",
        ],
        "narration": (
            "The Fruit sprite needs two separate scripts on the same sprite. "
            "Script one: when the green flag is clicked, hide the original fruit. "
            "Then forever, create a clone of myself, and wait a random time between "
            "one and three seconds. The original stays hidden; only clones appear."
        ),
    },
    {
        "title": "Fruit — script 2 (each clone)",
        "bullets": [
            "when I start as a clone",
            "random x, y 170, show, fall",
            "if touching Basket: score plus 1, delete clone",
        ],
        "narration": (
            "Script two starts with when I start as a clone. Go to a random x "
            "between minus two hundred and two hundred, and y one seventy, then show. "
            "Repeat until touching the Basket or y is below minus one seventy: "
            "change y by minus five and wait zero point zero three seconds. "
            "If touching the Basket, change score by one and delete this clone."
        ),
    },
    {
        "title": "Referee sprite",
        "bullets": [
            "Set score to 0 on green flag",
            "wait until score > 19 → broadcast win",
            "when I receive win: say You win, stop all",
        ],
        "narration": (
            "The Referee resets the game. When the green flag is clicked, set score "
            "to zero and hide the referee. Wait until score is greater than nineteen, "
            "which means twenty or more, then broadcast win. On a second script, "
            "when I receive win, show the sprite, say You win for three seconds, "
            "and stop all."
        ),
    },
    {
        "title": "Test the game",
        "bullets": [
            "Green flag to start",
            "Original Fruit must stay hidden",
            "Every clone must disappear",
        ],
        "narration": (
            "Click the green flag to test. Move the basket with the arrow keys. "
            "Check that the original Fruit never appears on stage. Every clone "
            "should disappear after a catch or a miss. The score should increase "
            "only when the basket touches a clone."
        ),
    },
    {
        "title": "Common fixes",
        "bullets": [
            "Clones not falling? Check hide on original",
            "Score stuck? score is for all sprites",
            "Win too early? use score > 19",
        ],
        "narration": (
            "If clones never appear, make sure script one hides the original fruit "
            "and uses create clone of myself. If the score does not update, confirm "
            "the score variable is for all sprites. For the win condition, score "
            "greater than nineteen is the same as reaching twenty points."
        ),
    },
    {
        "title": "Next steps",
        "bullets": [
            "Extensions: lives, speed, bonus fruit",
            "Memo + .sb3 on curriculum site",
            "Build your own curriculum project",
        ],
        "narration": (
            "Try extensions such as lives for missed fruit, faster falling over time, "
            "or bonus objects. The full memo and solution file are on the curriculum "
            "website. Use this project as a template for your own subject-linked "
            "Scratch activity."
        ),
    },
]


def _font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    candidates = [
        "C:/Windows/Fonts/segoeuib.ttf" if bold else "C:/Windows/Fonts/segoeui.ttf",
        "C:/Windows/Fonts/arialbd.ttf" if bold else "C:/Windows/Fonts/arial.ttf",
    ]
    for path in candidates:
        if Path(path).exists():
            return ImageFont.truetype(path, size=size)
    return ImageFont.load_default()


def render_slide(title: str, bullets: list[str], index: int, total: int) -> Image.Image:
    img = Image.new("RGB", SIZE, (24, 36, 68))
    draw = ImageDraw.Draw(img)
    title_font = _font(46, bold=True)
    body_font = _font(30)
    small_font = _font(22)

    draw.rectangle((0, 0, SIZE[0], 8), fill=(0, 180, 170))
    draw.text((60, 52), title, fill=(255, 255, 255), font=title_font)

    y = 150
    for bullet in bullets:
        wrapped = textwrap.wrap(bullet, width=52) or [bullet]
        for line in wrapped:
            draw.text((84, y), f"• {line}", fill=(220, 230, 245), font=body_font)
            y += 42
        y += 8

    draw.text((60, SIZE[1] - 48), f"Catch Game solution — slide {index} of {total}", fill=(140, 155, 180), font=small_font)
    draw.text((SIZE[0] - 320, SIZE[1] - 48), "DBE Coding & Robotics", fill=(140, 155, 180), font=small_font)
    return img


async def tts_to_file(text: str, path: Path) -> None:
    communicate = edge_tts.Communicate(text, VOICE)
    await communicate.save(str(path))


def ffprobe_duration(ffmpeg: str, path: Path) -> float:
    cmd = [
        ffmpeg.replace("ffmpeg", "ffprobe") if "ffmpeg" in ffmpeg else "ffprobe",
        "-v",
        "error",
        "-show_entries",
        "format=duration",
        "-of",
        "default=noprint_wrappers=1:nokey=1",
        str(path),
    ]
    # imageio_ffmpeg only ships ffmpeg; use ffmpeg -i fallback
    try:
        out = subprocess.check_output(cmd, stderr=subprocess.DEVNULL, text=True)
        return float(out.strip())
    except (subprocess.CalledProcessError, FileNotFoundError, ValueError):
        cmd2 = [ffmpeg, "-i", str(path)]
        proc = subprocess.run(cmd2, capture_output=True, text=True)
        import re

        match = re.search(r"Duration: (\d+):(\d+):(\d+\.\d+)", proc.stderr)
        if not match:
            return 5.0
        h, m, s = match.groups()
        return int(h) * 3600 + int(m) * 60 + float(s)


def make_segment(ffmpeg: str, image: Path, audio: Path, out: Path) -> None:
    duration = ffprobe_duration(ffmpeg, audio)
    cmd = [
        ffmpeg,
        "-y",
        "-loop",
        "1",
        "-i",
        str(image),
        "-i",
        str(audio),
        "-c:v",
        "libx264",
        "-tune",
        "stillimage",
        "-c:a",
        "aac",
        "-b:a",
        "192k",
        "-pix_fmt",
        "yuv420p",
        "-shortest",
        "-t",
        f"{duration:.2f}",
        str(out),
    ]
    subprocess.run(cmd, check=True, capture_output=True)


def concat_segments(ffmpeg: str, segments: list[Path], out: Path) -> None:
    list_file = WORK / "concat.txt"
    list_file.write_text("\n".join(f"file '{p.as_posix()}'" for p in segments), encoding="utf-8")
    cmd = [
        ffmpeg,
        "-y",
        "-f",
        "concat",
        "-safe",
        "0",
        "-i",
        str(list_file),
        "-c",
        "copy",
        str(out),
    ]
    subprocess.run(cmd, check=True, capture_output=True)


async def main() -> None:
    import imageio_ffmpeg

    ffmpeg = imageio_ffmpeg.get_ffmpeg_exe()
    if WORK.exists():
        for p in WORK.iterdir():
            p.unlink()
    else:
        WORK.mkdir(parents=True)

    segments: list[Path] = []
    total = len(SCENES)

    for i, scene in enumerate(SCENES, start=1):
        title = str(scene["title"])
        bullets = list(scene["bullets"])  # type: ignore[arg-type]
        narration = str(scene["narration"])

        png = WORK / f"slide_{i:02d}.png"
        mp3 = WORK / f"slide_{i:02d}.mp3"
        mp4 = WORK / f"slide_{i:02d}.mp4"

        render_slide(title, bullets, i, total).save(png)
        await tts_to_file(narration, mp3)
        make_segment(ffmpeg, png, mp3, mp4)
        segments.append(mp4)
        print(f"Built segment {i}/{total}: {title}")

    concat_segments(ffmpeg, segments, OUTPUT)
    print(f"Wrote {OUTPUT}")


if __name__ == "__main__":
    asyncio.run(main())
