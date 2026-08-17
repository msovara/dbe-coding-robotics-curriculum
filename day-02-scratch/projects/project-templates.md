# Advanced Scratch Project Templates
## Day 2 Project Ideas and Templates

Use these as classroom-ready project ideas for advanced Scratch. Each builds on Day 1 skills and introduces Day 2 concepts (cloning, broadcasting, complex games).

---

## Project 1: Catch Game (Cloning and Scoring)

**Time:** 45–60 minutes  
**Learning objectives:** Cloning, variables (score), conditions, collision detection

### Steps
1. **Player:** Create a sprite at the bottom (e.g. basket or character). Use arrow keys to move left/right.
2. **Falling objects:** Create a sprite (e.g. fruit, coin). When green flag clicked, `forever` → `create clone of [myself]`, `wait random 1 to 3 secs`.
3. **Clone behaviour:** `when I start as a clone` → `go to x: random -200 to 200, y: 180` (top), then `forever` → `change y by -5` (fall), `if touching [player]?` then `change [score] by 1`, `delete this clone`, `if y position < -180` (bottom) then `delete this clone`.
4. **Scoring:** Create variable `score`, show on stage. When touching player, increase score.
5. **Win condition:** If score ≥ 20, broadcast "win", show message.

### Extensions
- Add lives (if object reaches bottom, lose a life)
- Different objects (some worth more points, some subtract points)
- Speed increases over time

---

## Project 2: Interactive Quiz Game (Broadcasting and Lists)

**Time:** 60–75 minutes  
**Learning objectives:** Broadcasting, lists, conditions, user input

### Steps
1. **Question setup:** Create a list `questions` and a list `answers`. Add 3–5 questions and correct answers.
2. **Question sprite:** When green flag clicked, broadcast "show question 1". When received, `say item [1] of [questions]` for 3 secs, then `ask [item [1] of [questions]] and wait`.
3. **Answer check:** `if answer = item [1] of [answers]` then `change [score] by 1`, `say "Correct!"`, else `say "Incorrect"`. Broadcast "next question".
4. **Multiple questions:** Use a variable `question number` to track which question. When "next question" received, increase `question number`, check if all done, else show next question.
5. **Results:** After all questions, broadcast "show results", display final score.

### Extensions
- Multiple choice (use buttons or sprites instead of typing)
- Subject-specific: Maths problems, vocabulary, science facts
- Timer: add countdown timer for each question

---

## Project 3: Platformer Game (Complex Movement and Collision)

**Time:** 60–90 minutes  
**Learning objectives:** Advanced motion, collision detection, game mechanics

### Steps
1. **Player:** Create a sprite. Use arrow keys: left/right move, space or up = jump. Use `change y by` for gravity (falling).
2. **Platforms:** Create platforms (sprites or use pen to draw). Player should "stand" on platforms (if touching color [platform color], set y to platform y).
3. **Enemies or obstacles:** Create moving enemies. If player touches enemy, lose a life or game over.
4. **Collectibles:** Create items to collect (use cloning for multiple). When touching, increase score, delete clone.
5. **Levels:** Use broadcasts to change levels (new background, new platforms, reset player position).

### Extensions
- Multiple levels with increasing difficulty
- Power-ups (temporary speed, invincibility)
- Animated sprites (change costumes for walking/jumping)

---

## Project 4: Science Simulation (Curriculum Integration)

**Time:** 60–90 minutes  
**Learning objectives:** Simulation, data collection, curriculum link

### Example: Water Cycle Simulation

1. **Sprites:** Sun, cloud, water droplet, ground.
2. **Process:** When sun clicked, broadcast "evaporate". Water droplets move up (evaporation). When high enough, change to cloud sprite (condensation). After delay, change back to droplet and fall (precipitation). When touching ground, collect in a variable "ground water".
3. **Display:** Show variables for each stage (evaporated, condensed, precipitated, ground water).
4. **Interaction:** Click sun to start cycle, click cloud to speed up, reset button.

### Other simulation ideas
- Food chain (predator-prey relationships)
- Plant growth (stages, needs: water, sun)
- Simple physics (gravity, bouncing)

---

## Project 5: Interactive Story with Choices (Broadcasting and Conditions)

**Time:** 60–75 minutes  
**Learning objectives:** Broadcasting, conditions, user choices, storytelling

### Steps
1. **Story structure:** Plan 3–4 scenes with choices that branch the story.
2. **Scene 1:** Background 1, character says introduction, `ask "What do you do? (A or B)" and wait`.
3. **Branching:** `if answer contains "A"` then broadcast "path A", else broadcast "path B".
4. **Path A/B:** Different sprites receive messages, change background, continue story with new choices.
5. **Endings:** Multiple endings based on choices. Show ending message.

### Extensions
- Add sound effects and music for each scene
- Multiple characters with dialogue
- Save choices in a list to show "your story" at the end

---

## Facilitator Memo: Suggested Code Solutions

The solutions below are reference implementations for facilitators. Learners may use different sprites, messages, variable names, or block arrangements and still produce a correct project.

**How to read the scripts:** Each indented line represents a block nested inside the block above it. Scratch does not have a literal `end` block. Close C-shaped blocks by snapping the next block below them.

---

### Memo 1: Catch Game

#### Project setup

- Sprites: `Basket`, `Fruit`, and an optional `Referee`
- Variable for all sprites: `score`
- Message: `win`
- Keep the original `Fruit` hidden; only its clones should fall.

#### Basket sprite

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

#### Fruit sprite — create clones

```text
when green flag clicked
hide
forever
  create clone of (myself)
  wait (pick random (1) to (3)) seconds
```

#### Fruit sprite — make each clone fall

```text
when I start as a clone
go to x: (pick random (-200) to (200)) y: (170)
show
repeat until <<touching (Basket)?> or <(y position) < (-170)>>
  change y by (-5)
  wait (0.03) seconds
if <touching (Basket)?> then
  change (score) by (1)
delete this clone
```

#### Referee sprite — initialise and check the score

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

#### Expected result

- The basket moves left and right.
- Fruit clones appear at random horizontal positions and fall.
- Catching a fruit increases the score by one.
- Fruit that reaches the bottom disappears.
- The game ends when the score reaches 20.

#### Memo checks

- The original fruit is hidden.
- Every clone is deleted after it is caught or missed.
- `score` is created **for all sprites**.
- The win test uses `score > 19`, which is equivalent to `score ≥ 20`.

---

### Memo 2: Interactive Quiz Game

#### Project setup

- Sprite: `QuizMaster`
- Lists for all sprites: `questions`, `answers`
- Variables for all sprites: `question number`, `score`
- Message: `show results`

#### QuizMaster sprite — complete solution

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

#### QuizMaster sprite — results

```text
when I receive (show results)
say (join [Final score: ] (score)) for (3) seconds
```

#### Expected result

- The game asks all three questions in order.
- Correct answers add one point.
- Incorrect answers display the correct answer.
- After the final question, the sprite displays the final score.

#### Memo checks

- `questions` and `answers` contain the same number of items.
- Corresponding question and answer items use the same list position.
- `question number` increases once after every answer.
- The results message runs only after the loop ends.
- Typed answers must match the stored text. Scratch ignores letter case in normal text comparisons, but spelling and spaces should still be checked.

---

### Memo 3: Platformer Game

#### Project setup

- Sprites: `Player`, `Platform`, `Enemy`, and `Coin`
- Variables for all sprites: `score`, `lives`
- Variable for the Player only: `y speed`
- Messages: `game over`, `level complete`
- Draw the platforms using one clearly defined colour that does not appear elsewhere in the backdrop.

#### Player sprite — movement, gravity, and collision

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

> **Facilitator note:** In some Scratch projects, testing the jump immediately after pushing the player out of a platform can make the colour-touch condition false. If that happens, create a Boolean-style variable such as `on ground`, set it during collision handling, and use it for the jump test.

#### Enemy sprite

```text
when green flag clicked
go to x: (80) y: (-100)
point in direction (90)
forever
  move (3) steps
  if on edge, bounce
```

#### Coin sprite — cloned collectibles

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

#### Player sprite — outcomes

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

#### Expected result

- The player moves horizontally, falls under gravity, and can jump from platforms.
- Touching an enemy or falling off the stage removes one life.
- Collecting all eight coins completes the level.
- Losing all three lives ends the game.

#### Memo checks

- `y speed` is created **for this sprite only** on the Player.
- The collision colour exactly matches the platform colour.
- The player is moved out of the platform before `y speed` is reset.
- Coins are deleted after collection.

---

### Memo 4: Water Cycle Simulation

#### Project setup

- Sprites: `Sun`, `Droplet`, `Cloud`, and `Ground`
- Variables for all sprites: `evaporated`, `condensed`, `precipitated`, `ground water`
- Messages: `evaporate`, `condense`, `rain`, `collected`
- The Cloud starts hidden.

#### Stage — reset the simulation

```text
when green flag clicked
set (evaporated) to (0)
set (condensed) to (0)
set (precipitated) to (0)
set (ground water) to (0)
switch backdrop to (Water Cycle)
```

#### Sun sprite

```text
when green flag clicked
go to x: (170) y: (120)
show
```

```text
when this sprite clicked
broadcast (evaporate)
```

#### Droplet sprite — evaporation

```text
when green flag clicked
go to x: (-100) y: (-130)
show
```

```text
when I receive (evaporate)
repeat until <(y position) > (90)>
  change y by (5)
  change (evaporated) by (1)
  wait (0.05) seconds
hide
broadcast (condense)
```

#### Cloud sprite — condensation

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

#### Droplet sprite — precipitation and collection

```text
when I receive (rain)
go to x: (-70) y: (100)
show
repeat until <touching (Ground)?>
  change y by (-6)
  change (precipitated) by (1)
  wait (0.05) seconds
broadcast (collected)
```

```text
when I receive (collected)
change (ground water) by (1)
go to x: (-100) y: (-130)
say [Collection] for (2) seconds
```

#### Optional Cloud interaction

```text
when this sprite clicked
broadcast (rain)
```

#### Expected result

- Clicking the sun starts evaporation.
- The droplet rises and disappears.
- The cloud appears to represent condensation.
- The droplet then falls as precipitation.
- Touching the ground increases `ground water` and resets the droplet.

#### Memo checks

- Each message name is spelled consistently.
- The Ground sprite is positioned where the droplet can touch it.
- The Cloud begins hidden and appears only during condensation.
- Variables reset when the green flag is clicked.

---

### Memo 5: Interactive Story with Choices

#### Project setup

- Sprites: `Guide`, `Scientist`, and `Robot`
- Backdrops: `Laboratory`, `Forest`, `Space`, `Ending A`, and `Ending B`
- Messages: `scene 1`, `path A`, `path B`, `ending A`, `ending B`
- Variable for all sprites: `choice`
- List for all sprites: `story choices`

#### Stage

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

#### Guide sprite — first choice

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

#### Scientist sprite — Path A

```text
when green flag clicked
hide
```

```text
when I receive (path A)
show
say [The forest sensor has found an injured animal.] for (2) seconds
ask [Help the animal? Type YES or NO.] and wait
add (answer) to (story choices)
if <(answer) = [yes]> then
  say [Your kindness saves the animal!] for (2) seconds
  broadcast (ending A)
else
  say [You return to the laboratory.] for (2) seconds
  broadcast (ending B)
```

#### Robot sprite — Path B

```text
when green flag clicked
hide
```

```text
when I receive (path B)
show
say [An asteroid is approaching the spacecraft!] for (2) seconds
ask [Use the shield? Type YES or NO.] and wait
add (answer) to (story choices)
if <(answer) = [yes]> then
  say [The shield protects the spacecraft!] for (2) seconds
  broadcast (ending A)
else
  say [The crew returns safely to Earth.] for (2) seconds
  broadcast (ending B)
```

#### Optional ending summary

Add a `Narrator` sprite:

```text
when green flag clicked
hide
```

```text
when I receive (ending A)
show
say (join [Your first choice was: ] (item (1) of (story choices))) for (2) seconds
say [The end!] for (2) seconds
```

```text
when I receive (ending B)
show
say (join [Your first choice was: ] (item (1) of (story choices))) for (2) seconds
say [The end!] for (2) seconds
```

#### Expected result

- The first answer selects the Forest or Space path.
- Each path presents a second decision.
- Messages coordinate backdrop and character changes.
- The list records the learner's choices.
- The story reaches one of two endings and can display the first choice.

#### Memo checks

- The Stage and sprites use exactly the same message names.
- Sprites that are not part of the current scene remain hidden.
- The first choice accepts both uppercase and lowercase `A`.
- Responses other than `A` follow Path B; facilitators may add validation if only `A` or `B` should be accepted.

---

## General Tips

- **Start simple:** Begin with one feature, then add complexity.
- **Test often:** Run the project frequently to catch bugs early.
- **Debugging:** Use "say" blocks to check variable values, use "stop all" to pause and check code.
- **Curriculum links:** Choose projects that connect to your subject area.
- **Differentiation:** Provide starter code for beginners; add challenges for advanced learners.

---

## Assessment Ideas

- **Functionality:** Does the project work as intended?
- **Creativity:** Original ideas, engaging design
- **Code quality:** Organized scripts, comments, efficient code
- **Explanation:** Can the creator explain how it works?
- **Curriculum link:** Clear learning objectives and subject connection
