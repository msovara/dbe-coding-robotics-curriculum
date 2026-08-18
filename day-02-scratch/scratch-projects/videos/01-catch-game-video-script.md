# Catch Game — Video solution script

Facilitator recording guide and narration source for **`01-catch-game-solution.mp4`**.

## Watch the video

<video controls width="100%" style="max-width: 960px; border-radius: 8px;">
  <source src="01-catch-game-solution.mp4" type="video/mp4">
  Your browser does not support embedded video. 
  <a href="01-catch-game-solution.mp4">Download the MP4</a>.
</video>

**Length:** ~8 minutes  
**Audience:** Teachers / provincial specialists (Day 2 workshop)  
**Companion files:** [project-templates.md](../../projects/project-templates.md) · [01-catch-game.sb3](../solutions/01-catch-game.sb3)

---

## Before you record

1. Open Scratch or TurboWarp with `01-catch-game.sb3` loaded.
2. Zoom the block palette so blocks are readable on video.
3. Record at **1280×720** or **1920×1080**.
4. Optional: show your face in a small corner for the intro only.

Regenerate the packaged MP4 (slides + voice):

```bash
python day-02-scratch/scratch-projects/videos/generate_catch_game_video.py
```

---

## Scene breakdown

| # | On screen | Narration (summary) | ~sec |
|---|-----------|---------------------|------|
| 1 | Title slide | Intro: Catch Game Day 2 solution overview | 25 |
| 2 | Requirements list | Basket, falling clones, score 20 to win | 22 |
| 3 | Load `.sb3` in Scratch | File → Load from your computer / TurboWarp | 22 |
| 4 | Stage: variables | `score` for all sprites; broadcast `win` | 20 |
| 5 | **Basket** code area | Green flag, go to y −145, forever + arrow keys | 35 |
| 6 | **Fruit** script 1 | Hide original; forever create clone + wait | 35 |
| 7 | **Fruit** script 2 | Clone hat: random x, fall, score, delete | 45 |
| 8 | **Referee** scripts | Reset score; wait score > 19; broadcast win | 40 |
| 9 | Green flag demo | Play game; catch fruit until win | 30 |
| 10 | Debug tips | Hidden original, for all sprites, score > 19 | 30 |
| 11 | Outro | Extensions + curriculum links | 25 |

---

## Full narration (matches generated video)

### 1 — Intro

This video walks through the Catch Game solution for Day 2 of the DBE Coding and Robotics workshop. You will see how the Basket, Fruit, and Referee sprites work together using cloning, variables, and broadcast messages.

### 2 — What we are building

The player moves a basket at the bottom of the stage. Fruit clones fall from random positions at the top. Each catch adds one to the score. When the score reaches twenty, the game shows a win message and stops.

### 3 — Open the solution file

You can follow along in Scratch by loading the solution file `01-catch-game.sb3` from the curriculum folder. In Scratch, choose **File → Load from your computer**. You can also drag the file onto [TurboWarp](https://turbowarp.org/) for a quick preview.

### 4 — Setup

Before coding, create one variable called **score** (for all sprites). Create a broadcast message called **win**. You need three sprites: **Basket**, **Fruit**, and an optional **Referee** that handles scoring and the win screen.

### 5 — Basket

Select the Basket sprite. When the green flag is clicked, go to x 0 and y −145, then show the sprite. Inside a **forever** loop: if the **left arrow** key is pressed, change x by −10; if the **right arrow** key is pressed, change x by +10.

### 6 — Fruit script 1

The Fruit sprite needs **two separate scripts on the same sprite**. Script one: when the green flag is clicked, **hide** the original fruit. Then **forever**, **create clone of myself**, and **wait** a random time between 1 and 3 seconds. The original stays hidden; only clones appear.

### 7 — Fruit script 2

Script two starts with **when I start as a clone**. Go to a random x between −200 and 200, and y 170, then **show**. Inside **forever**: **if** touching the Basket **or** y is below −170, **stop this script**; otherwise change y by −5 and wait 0.03 seconds. After the loop, **if** touching the Basket, change **score** by 1, then **delete this clone**.

### 8 — Referee

The Referee resets the game. When the green flag is clicked, set **score** to 0 and hide the referee. **Wait until** score is greater than 19 (twenty or more), then **broadcast win**. On a second script, **when I receive win**, show the sprite, **say** “You win!” for 3 seconds, and **stop all**.

### 9 — Test

Click the green flag. Move the basket with the arrow keys. Check that the original Fruit never appears. Every clone should disappear after a catch or a miss. The score should increase only when the basket touches a clone.

### 10 — Common fixes

If clones never appear, make sure script one **hides** the original and uses **create clone of myself**. If fruit clones appear but **do not fall**, check script two: use **forever** with **if touching or off bottom → stop this script**, not `repeat until not touching`. If the score does not update, confirm **score** is **for all sprites**. For the win condition, **score > 19** equals twenty points.

### 11 — Next steps

Try extensions: lives for misses, faster falling over time, or bonus fruit. The full memo and `.sb3` are on the curriculum website. Use this project as a template for your own subject-linked Scratch activity.

---

## Publishing checklist

- [ ] Upload MP4 to YouTube (unlisted) or host on CHPC / DBE share drive
- [ ] Add the watch link below in `project-templates.md` under Project 1
- [ ] Re-run GitHub Pages deploy if only the markdown link changed

**Local / site file:** [01-catch-game-solution.mp4](./01-catch-game-solution.mp4)
