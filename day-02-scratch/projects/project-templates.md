# Advanced Scratch Project Templates
## Day 2 — Tasks, requirements, and memo scripts

**How to facilitate this page**

1. Introduce **one project at a time**.
2. Read the **task** (what we are making) and the **requirements** (what must work).
3. Let participants plan sprites, variables, and messages.
4. Use the **memo** under that same project to write the correct Scratch script together.
5. Only then look at **extensions**.

Do **not** start from the memo. The memo is the answer key, not the briefing.

**How to read memo scripts:** Each indented line is a block nested inside the block above it. Scratch has no `end` block. Close C-shaped blocks by snapping the next block underneath. Two hats on one sprite means **two scripts on the same sprite**, not two sprites.

**Open real Scratch blocks (for testing):** Download `.sb3` files from [`scratch-projects/solutions/`](../scratch-projects/README.md) and use **File → Load from your computer** in Scratch. See the [scratch-projects README](../scratch-projects/README.md) for the full list and how to add more solutions.

---

## Project 1: Catch Game

**Time:** 45–60 minutes  
**Concepts:** cloning, score variable, conditions, collision

### Task

Make a game where a basket at the bottom of the stage catches falling fruit. The player wins at 20 points.

### Requirements

- A **Basket** sprite moves left and right with the arrow keys.
- A **Fruit** sprite creates clones that fall from the top at random x positions.
- The original Fruit stays hidden. Only clones fall.
- Catching a clone adds **1** to `score` and deletes that clone.
- A clone that reaches the bottom is deleted (miss).
- When `score` reaches **20**, the game shows a win message and stops.

### Extensions

- Add lives (a miss costs a life).
- Different objects (bonus points or penalty).
- Speed increases over time.

### Memo: suggested Scratch script

**Scratch file:** [`01-catch-game.sb3`](../scratch-projects/solutions/01-catch-game.sb3) — open in Scratch to see and test the blocks.

**Download (use this link — not “Save as” from the preview page):**  
[Download `01-catch-game.sb3`](https://github.com/msovara/dbe-coding-robotics-curriculum/raw/main/day-02-scratch/scratch-projects/solutions/01-catch-game.sb3)

**Video solution:** [`01-catch-game-solution.mp4`](../scratch-projects/videos/01-catch-game-solution.mp4) (~8 min walkthrough). Facilitator script: [video script](../scratch-projects/videos/01-catch-game-video-script.md).

**Facilitator annotations (what to say for each block):** [Catch Game facilitator annotations](../scratch-projects/01-catch-game-facilitator-annotations.md) — separate from the scripts below; use while explaining, not in Scratch.

**How to run:** Load the `.sb3` in Scratch (**File → Load from your computer**), click the **green flag** once, move the basket with **←/→**. See [scratch-projects README](../scratch-projects/README.md#how-to-run-01-catch-gamesb3).

**Setup:** sprites `Basket`, `Fruit`, optional `Referee`. Variable `score` (for all sprites). Message `win`.

**Basket sprite**

```text
when green flag clicked
go to x: (0) y: (-145)
show
forever
  if <key (left arrow) pressed?> then
    change x by (-10)
  if <key (right arrow) pressed?> then
    change x by (10)
```

**Fruit sprite — both scripts on this one sprite**

Put **both** hats on the same `Fruit` sprite.

Script 1 — original Fruit (hidden): spawn clones

```text
when green flag clicked
hide
forever
  create clone of (myself)
  wait (pick random (1) to (3)) seconds
```

Script 2 — each clone: appear, fall, score or miss

```text
when I start as a clone
go to x: (pick random (-200) to (200)) y: (170)
show
forever
  if <<touching (Basket)?> or <(y position) < (-170)>> then
    if <touching (Basket)?> then
      change (score) by (1)
    delete this clone
    stop (this script)
  change y by (-5)
  wait (0.03) seconds
```

**Referee sprite**

```text
when green flag clicked
set (score) to (0)
hide
wait until <(score) > (19)>
broadcast (win)
```

```text
when I receive (win)
show
say [You win!] for (3) seconds
stop (all)
```

**Check:** original Fruit is hidden; every clone is deleted; `score` is for all sprites; `score > 19` is the same as 20 or more.

---

## Project 2: Interactive Quiz Game

**Time:** 60–75 minutes  
**Concepts:** lists, user input, conditions, score

### Task

Make a quiz that asks several questions, checks the typed answer, and shows a final score.

### Requirements

- Two lists: `questions` and `answers` (same length; matching items at the same position).
- A variable `question number` tracks which question is current.
- A variable `score` starts at 0.
- The sprite asks each question in order and waits for an answer.
- A correct answer adds 1 to `score` and says **Correct!**
- A wrong answer shows the correct answer.
- After the last question, the sprite shows the **final score**.

### Extensions

- Multiple choice with button sprites.
- Subject-specific questions (maths, vocabulary, science).
- A countdown timer per question.

### Memo: suggested Scratch script

**Setup:** sprite `QuizMaster`. Lists `questions`, `answers`. Variables `question number`, `score`. Message `show results`.

**QuizMaster — ask all questions**

```text
when green flag clicked
delete (all) of (questions)
delete (all) of (answers)

add [What is 5 + 3?] to (questions)
add [8] to (answers)
add [What planet do we live on?] to (questions)
add [Earth] to (answers)
add [How many provinces are in South Africa?] to (questions)
add [9] to (answers)

set (score) to (0)
set (question number) to (1)

repeat until <(question number) > (length of (questions))>
  ask (item (question number) of (questions)) and wait
  if <(answer) = (item (question number) of (answers))> then
    change (score) by (1)
    say [Correct!] for (1) seconds
  else
    say (join [Incorrect. The answer is: ] (item (question number) of (answers))) for (2) seconds
  change (question number) by (1)

broadcast (show results)
```

**QuizMaster — results**

```text
when I receive (show results)
say (join [Final score: ] (score)) for (3) seconds
```

**Check:** lists are the same length; `question number` increases once per answer; results run after the loop; spelling of typed answers must match.

---

## Project 3: Platformer Game

**Time:** 60–90 minutes  
**Concepts:** gravity, colour collision, lives, cloning collectibles

### Task

Make a simple platformer: walk, jump, avoid an enemy, collect coins.

### Requirements

- **Player** moves left and right, falls with gravity, and jumps from a platform.
- Platforms use **one colour** that does not appear elsewhere.
- Touching an **Enemy**, or falling off the stage, costs a life and resets the player.
- **Coins** are clones. Touching a coin adds 1 to `score` and deletes that clone.
- Start with **3 lives**. Lives at 0 shows **Game over** and stops.
- Collecting **8 coins** shows **Level complete** and stops.

### Extensions

- More levels with harder platforms.
- Power-ups (speed or invincibility).
- Walking and jumping costumes.

### Memo: suggested Scratch script

**Setup:** sprites `Player`, `Platform`, `Enemy`, `Coin`. Variables `score`, `lives` (all sprites) and `y speed` (Player only). Messages `game over`, `level complete`.

**Player — movement, gravity, collision**

```text
when green flag clicked
set (score) to (0)
set (lives) to (3)
set (y speed) to (0)
go to x: (-180) y: (-100)
show

forever
  if <key (left arrow) pressed?> then
    change x by (-5)
  if <key (right arrow) pressed?> then
    change x by (5)

  change (y speed) by (-1)
  change y by (y speed)

  if <touching color (platform colour)?> then
    repeat until <not <touching color (platform colour)?>>
      change y by (1)
    set (y speed) to (0)

  if <<key (up arrow) pressed?> and <touching color (platform colour)?>> then
    set (y speed) to (13)

  if <touching (Enemy)?> then
    change (lives) by (-1)
    go to x: (-180) y: (-100)
    wait (1) seconds

  if <(y position) < (-170)> then
    change (lives) by (-1)
    go to x: (-180) y: (-100)

  if <(lives) < (1)> then
    broadcast (game over)
```

If jump fails after leaving the platform colour, use an `on ground` variable set during collision.

**Enemy**

```text
when green flag clicked
go to x: (80) y: (-100)
point in direction (90)
forever
  move (3) steps
  if on edge, bounce
```

**Coin — both scripts on this one sprite**

```text
when green flag clicked
hide
repeat (8)
  create clone of (myself)
```

```text
when I start as a clone
go to (random position)
show
wait until <touching (Player)?>
change (score) by (1)
delete this clone
```

**Player — outcomes**

```text
when I receive (game over)
say [Game over!] for (3) seconds
stop (all)
```

```text
when green flag clicked
wait until <(score) > (7)>
broadcast (level complete)
```

```text
when I receive (level complete)
say [Level complete!] for (3) seconds
stop (all)
```

**Check:** `y speed` is for this sprite only; platform colour matches exactly; player is pushed out of the platform before `y speed` is set to 0.

---

## Project 4: Water Cycle Simulation

**Time:** 60–90 minutes  
**Concepts:** broadcasting, variables as counters, curriculum link

### Task

Simulate the water cycle: evaporation, condensation, precipitation, collection.

### Requirements

- Sprites: **Sun**, **Droplet**, **Cloud**, **Ground**.
- Clicking the **Sun** starts evaporation (droplet moves up).
- At the top, the droplet hides and the **Cloud** appears (condensation).
- Then the droplet falls as rain (precipitation).
- Touching **Ground** increases `ground water` and resets the droplet.
- Variables show counts: `evaporated`, `condensed`, `precipitated`, `ground water`.
- Green flag resets all counts.

### Other simulation ideas

- Food chain (predator–prey).
- Plant growth (water and sun).
- Simple physics (gravity, bouncing).

### Memo: suggested Scratch script

**Scratch file:** [`04-water-cycle.sb3`](../scratch-projects/solutions/04-water-cycle.sb3) — open in Scratch to see and test the blocks.

**Download:** [Download `04-water-cycle.sb3`](https://github.com/msovara/dbe-coding-robotics-curriculum/raw/main/day-02-scratch/scratch-projects/solutions/04-water-cycle.sb3)

**Facilitator annotations (what to say for each block):** [Water Cycle facilitator annotations](../scratch-projects/04-water-cycle-facilitator-annotations.md) — separate from the scripts below.

**How to run:** Load the `.sb3` and click the **green flag**. After a short pause the sun starts evaporation (you can also **click the Sun**). The droplet rises, the cloud appears, rain falls onto the **grass**, and `ground water` increases.

**Setup:** messages `evaporate`, `condense`, `rain`, `collected`. Cloud starts hidden. Variables `evaporated`, `condensed`, `precipitated`, `ground water` (for all sprites).

**Stage (or Sun on green flag):** reset counters

```text
when green flag clicked
set (evaporated) to (0)
set (condensed) to (0)
set (precipitated) to (0)
set (ground water) to (0)
```

**Sun**

```text
when green flag clicked
go to x: (170) y: (120)
show
say [Click me, or wait...] for (2) seconds
wait (1) seconds
broadcast (evaporate)
```

```text
when this sprite clicked
broadcast (evaporate)
```

**Droplet — start position**

```text
when green flag clicked
go to x: (-100) y: (-100)
show
```

**Droplet — evaporation**

```text
when I receive (evaporate)
go to x: (-100) y: (-100)
show
forever
  change y by (5)
  wait (0.05) seconds
  if <(y position) > (90)> then
    change (evaporated) by (1)
    hide
    broadcast (condense)
    stop (this script)
```

**Cloud**

```text
when green flag clicked
go to x: (-70) y: (120)
hide
```

```text
when I receive (condense)
show
change (condensed) by (1)
say [Condensation] for (2) seconds
wait (1) seconds
broadcast (rain)
hide
```

**Droplet — rain**

```text
when I receive (rain)
go to x: (-70) y: (100)
show
forever
  change y by (-6)
  wait (0.05) seconds
  if <<touching (Ground)?> or <(y position) < (-150)>> then
    change (precipitated) by (1)
    broadcast (collected)
    stop (this script)
```

**Droplet — collection (same sprite)**

```text
when I receive (collected)
change (ground water) by (1)
go to x: (-100) y: (-100)
say [Collection] for (2) seconds
```

**Ground**

```text
when green flag clicked
go to x: (0) y: (-165)
show
```

Optional: clicking the Cloud can also `broadcast (rain)`.

**Check:** message names match everywhere; Ground is where the droplet can touch it; Cloud starts hidden; evaporation **starts at y −100** (do not check height before the first move); `broadcast` is **inside** the `if`, **before** `stop (this script)`.

---

## Project 5: Interactive Story with Choices

**Time:** 60–75 minutes  
**Concepts:** broadcasting, conditions, branching story

Builds on the [Day 1 linear story](../../day-01-scratch/projects/03-interactive-story-code/) (click and arrow to turn the page). This project adds **choices**.

### Task

Make a short story with two paths and two endings, driven by the player’s answers.

### Requirements

- Scene 1 asks: Forest **(A)** or Space **(B)**.
- Answer **A** (or **a**) goes to Path A. Anything else goes to Path B.
- Each path asks a **YES/NO** question and leads to **Ending A** or **Ending B**.
- Backdrops change with the path.
- Sprites that are not in the current scene stay hidden.
- A list `story choices` stores the answers.

### Extensions

- Sound and music per scene.
- More characters and dialogue.
- Show the full list of choices at the end.

### Memo: suggested Scratch script

**Scratch file:** [`05-interactive-story.sb3`](../scratch-projects/solutions/05-interactive-story.sb3) — open in Scratch to see and test the blocks.

**Download:** [Download `05-interactive-story.sb3`](https://github.com/msovara/dbe-coding-robotics-curriculum/raw/main/day-02-scratch/scratch-projects/solutions/05-interactive-story.sb3)

**Facilitator annotations (what to say for each block):** [Interactive Story facilitator annotations](../scratch-projects/05-interactive-story-facilitator-annotations.md) — separate from the scripts below.

**How to run:** Load the `.sb3` and click the **green flag**. Type `A` or `a` for the forest, or anything else for space. On the next question type `YES` or `yes` for ending A; anything else for ending B.

**Setup:** sprites `Guide`, `Scientist`, `Robot`. Backdrops `Laboratory`, `Forest`, `Space`, `Ending A`, `Ending B`. Messages `scene 1`, `path A`, `path B`, `ending A`, `ending B`. Variable `choice`. List `story choices`.

**Stage**

```text
when green flag clicked
switch backdrop to (Laboratory)
delete (all) of (story choices)
broadcast (scene 1)
```

```text
when I receive (path A)
switch backdrop to (Forest)
```

```text
when I receive (path B)
switch backdrop to (Space)
```

```text
when I receive (ending A)
switch backdrop to (Ending A)
```

```text
when I receive (ending B)
switch backdrop to (Ending B)
```

**Guide — first choice**

```text
when green flag clicked
show
go to x: (-100) y: (-80)
```

```text
when I receive (scene 1)
say [The laboratory alarm is sounding!] for (2) seconds
ask [Do you investigate the forest (A) or launch into space (B)?] and wait
set (choice) to (answer)
add (choice) to (story choices)
if <<(choice) = [A]> or <(choice) = [a]>> then
  broadcast (path A)
else
  broadcast (path B)
hide
```

**Scientist — Path A**

```text
when green flag clicked
hide
```

```text
when I receive (path A)
show
go to x: (20) y: (-70)
say [The forest sensor has found an injured animal.] for (2) seconds
ask [Help the animal? Type YES or NO.] and wait
add (answer) to (story choices)
if <<<(answer) = [yes]> or <(answer) = [YES]>> or <(answer) = [Yes]>> then
  say [Your kindness saves the animal!] for (2) seconds
  hide
  broadcast (ending A)
else
  say [You return to the laboratory.] for (2) seconds
  hide
  broadcast (ending B)
```

**Robot — Path B**

```text
when green flag clicked
hide
```

```text
when I receive (path B)
show
go to x: (30) y: (-60)
say [An asteroid is approaching the spacecraft!] for (2) seconds
ask [Use the shield? Type YES or NO.] and wait
add (answer) to (story choices)
if <<<(answer) = [yes]> or <(answer) = [YES]>> or <(answer) = [Yes]>> then
  say [The shield protects the spacecraft!] for (2) seconds
  hide
  broadcast (ending A)
else
  say [The crew returns safely to Earth.] for (2) seconds
  hide
  broadcast (ending B)
```

Optional **Narrator** can join the first stored choice to **The end!** on `ending A` or `ending B`.

**Check:** message names match (including spaces); unused sprites stay hidden; first choice accepts `A` or `a`; YES/NO accepts `yes`, `YES`, and `Yes`.

---

## General tips

- Start with one feature, then add the next requirement.
- Run the project often.
- Use `say` to check variable values if something fails.
- Link the project to a DBE subject where you can.

## Assessment ideas

- Does it meet the requirements?
- Is the design clear?
- Are scripts organised by sprite?
- Can the maker explain how it works?
- Is there a curriculum link?
