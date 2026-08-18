# Scratch Project Templates
## Day 1 Project Ideas and Templates

## Project 1: Moving Cat (Beginner)
**Time:** 30-45 minutes
**Learning Objectives:**
- Navigate Scratch interface
- Use motion blocks
- Understand events

### Instructions

1. **Open Scratch** and create a new project

2. **Make the cat move:**
   ```
   when green flag clicked
   move 10 steps
   ```

3. **Add continuous movement:**
   ```
   when green flag clicked
   forever
      move 10 steps
   end
   ```

4. **Add turning:**
   ```
   when green flag clicked
   forever
      move 10 steps
      if on edge, bounce
   end
   ```

5. **Add sound:**
   ```
   when green flag clicked
   forever
      move 10 steps
      if on edge, bounce
      play sound [meow]
   end
   ```

### Extensions
- Change the sprite
- Add more sprites
- Change speed
- Add different sounds

---

## Project 2: Dancing Sprite (Intermediate)
**Time:** 45-60 minutes
**Learning Objectives:**
- Use looks blocks
- Combine motion and appearance
- Use repeat loops

### Instructions

1. **Choose a sprite** (or create your own)

2. **Create a dance sequence:**
   ```
   when green flag clicked
   repeat 4
      move 20 steps
      turn 90 degrees
      next costume
      wait 0.5 seconds
   end
   ```

3. **Add size changes:**
   ```
   when green flag clicked
   repeat 4
      change size by 10
      move 20 steps
      turn 90 degrees
      next costume
      wait 0.5 seconds
   end
   ```

4. **Make it continuous:**
   ```
   when green flag clicked
   forever
      repeat 4
         change size by 10
         move 20 steps
         turn 90 degrees
         next costume
         wait 0.5 seconds
      end
      repeat 4
         change size by -10
         move 20 steps
         turn 90 degrees
         next costume
         wait 0.5 seconds
      end
   end
   ```

### Extensions
- Add background music
- Create multiple dancing sprites
- Add color effects
- Create a synchronized dance

---

## Project 3: Interactive Story (Intermediate)

**Time:** 60–90 minutes  
**Concepts:** events, backdrops, broadcast

Day 1 is a **linear** story (click and arrow to turn the page). Branching choices (`ask`, `if`, path A/B) are [Day 2 Project 5](../day-02-scratch/projects/project-templates.md#project-5-interactive-story-with-choices).

### Task

Make a three-scene story: Home → Road → School. The player turns the page with a **click** and the **right arrow**.

### Requirements

- Sprites: **Child**, **Friend**.
- Backdrops: **Home**, **Road**, **School** (in that order).
- Green flag starts at Home. Friend stays **hidden**.
- Clicking **Child** shows a line of dialogue.
- Right arrow broadcasts `scene 2`: backdrop Road, Child hides, Friend appears.
- Right arrow again goes to School and the ending line.

### Extensions

- Change only the `say` text (kindness, water, two languages — table in the memo).
- Sound effects.
- Day 2: two paths with `ask` and `if`.

### Memo: suggested Scratch script

**Scratch file:** [`03-interactive-story.sb3`](../scratch-projects/solutions/03-interactive-story.sb3) — open in Scratch to see and test the blocks.

**Download:** [Download `03-interactive-story.sb3`](https://github.com/msovara/dbe-coding-robotics-curriculum/raw/main/day-01-scratch/scratch-projects/solutions/03-interactive-story.sb3)

**Scratch scripts (GitHub Pages):** [Interactive Story memo](03-interactive-story-code.md)

**Facilitator annotations (what to say for each block):** [Interactive Story facilitator annotations](03-interactive-story-facilitator-guide.md) — separate from the scripts below; use while explaining, not in Scratch.

**How to run:** Green flag (Home, Child speaks) → **click** Child → **right arrow** (Road, Friend appears) → **right arrow** (School, ending line).

**Setup:** sprites `Child`, `Friend`. Backdrops `Home`, `Road`, `School` (in that order). Message `scene 2`. Friend starts hidden.

**Stage**

```text
when green flag clicked
switch backdrop to (Home)
```

```text
when I receive (scene 2)
switch backdrop to (Road)
```

**Child — start position**

```text
when green flag clicked
show
go to x: (-80) y: (-60)
switch backdrop to (Home)
say [I missed the taxi. I am late for school.] for (2) seconds
```

**Child — click**

```text
when this sprite clicked
say [I need help. Press the right arrow.] for (2) seconds
```

**Child — next scene**

```text
when [right arrow] key pressed
broadcast (scene 2)
hide
```

**Friend — start hidden**

```text
when green flag clicked
hide
go to x: (80) y: (-60)
```

**Friend — scene 2**

```text
when I receive (scene 2)
show
say [Walk with me. Press the arrow again.] for (2) seconds
```

**Friend — ending**

```text
when [right arrow] key pressed
switch backdrop to (next backdrop)
say [We arrived on time. Next time I will leave earlier.] for (2) seconds
```

**Check:** three named backdrops; Friend hidden on green flag; `scene 2` spelled the same on broadcast and receive.

**Other say lines (same scripts, change only the text)**

| Prompt | Child on flag | Child on click | Friend on `scene 2` | Friend on last arrow |
|--------|---------------|----------------|---------------------|----------------------|
| Kindness | My classmate dropped their books. | I will help you pick them up. | Thank you. Press the arrow. | We did it together. Kindness helps. |
| Water | The tap is running. We are wasting water. | Close the tap. Save water. | The tap is closed. Press the arrow. | We saved water. |
| Two languages | Hello! Sawubona! | How are you? Unjani? | I am fine. Ngiyaphila. | Goodbye! Hamba kahle! |

---

## Project 4: Score Keeper with timer (Variables + loops)
**Time:** 45–60 minutes  
**Learning Objectives:**
- Create and use variables (`score`, `time`)
- Use `forever`, `repeat until`, and conditions together
- Coordinate two scripts that both start with the green flag

### Instructions

1. **Create two variables** (For all sprites is easiest so you can show monitors on the stage):
   - `score` — how many times the player caught the sprite
   - `time` — seconds left in the round

2. **Build three scripts** on the **same** sprite (e.g. the cat). Together they give: reset score, countdown, click to score, sprite jumps to a new random place every second while time is left, then **Game Over!**

**Script 1 — reset score when the game starts**

```text
When green flag clicked
  set (score) to (0)
```

**Script 2 — click adds a point; sprite keeps jumping while time remains**

```text
When this sprite clicked
  change (score) by (1)
  forever
    if <(time) > (0)> then
      go to (random position)
      wait (1) seconds
```

*Motion:* use **`go to`** and choose **random position** from the dropdown (Scratch 3).

**Script 3 — 10 second countdown, then message**

```text
When green flag clicked
  set (time) to (10)
  repeat until <(time) = (0)>
    wait (1) seconds
    change (time) by (-1)

  say [Game Over!] for (2) seconds
```

*The final **`say [Game Over!]`** attaches **under** the green flag, **after** the `repeat until` loop—not inside the loop.*

### What you should see when you run it

1. Green flag: **`score`** resets to **0**, **`time`** counts down from **10** to **0** (about 10 seconds).  
2. Before time runs out, each **click** on the sprite adds **1** to **`score`** and starts the sprite jumping to a **random position** every **1** second (only while **`time` > 0**).  
3. When **`time`** reaches **0**, the sprite says **`Game Over!`** for 2 seconds.

### Common mistake: many `forever` loops from repeated clicks

Every time the player **clicks**, Script 2 starts **another** `forever` loop. Several clicks → several loops running at once (weird speed / behaviour).

**Recommended fix** — keep **one** movement loop on the green flag, and use the click **only** for scoring:

```text
When green flag clicked
  forever
    if <(time) > (0)> then
      go to (random position)
      wait (1) seconds

When this sprite clicked
  if <(time) > (0)> then
    change (score) by (1)
```

*Then the sprite moves automatically during the round; clicks only increase `score`. Remove the old “click + forever” stack if you use this pattern.*

### Extensions
- Add **`play sound [pop] until done`** when the sprite is clicked  
- Show **`join [Score: ] (score)`** with a `say` block or variable monitor  
- Change starting time (e.g. 20) or count faster  
- Add **You Win!** if `score` reaches a target before time runs out  
- Use several sprites, each with its own click script sharing the same `score` and `time`

---

## Project 5: Number Guessing Game (Conditions)
**Time:** 60-90 minutes
**Learning Objectives:**
- Use operators
- Apply conditions (if-then-else)
- Use `repeat until` for a game loop
- Create interactive games

### Instructions

1. **Create variables** (For all sprites or for this sprite only—your choice):
   - `secret number` — the hidden value (1–10)
   - `guess` — the player’s latest answer
   - `attempts` — how many guesses so far

2. **Build this complete script** on one sprite (e.g. the cat).  
   It matches the usual classroom layout: intro → loop with **Too low** / **Too high** → final line **`Correct! Attempts: …`**.

```text
When green flag clicked
  set (secret number) to (pick random (1) to (10))
  set (attempts) to (0)
  say [I am thinking of a number between 1 and 10, can you guess it?] for (2) seconds
  repeat until <(guess) = (secret number)>
    ask [Enter your guess:] and wait
    set (guess) to (answer)
    change (attempts) by (1)
    if <(guess) < (secret number)> then
      say [Too low!] for (2) seconds
    else
      if <(guess) > (secret number)> then
        say [Too high!] for (2) seconds

  say (join [Correct! Attempts: ] (attempts)) for (2) seconds
```

*Nest the `if` / `else` blocks inside the `repeat until`. The final **`say (join …)`** block attaches **under** the `when green flag clicked` hat, **after** the whole `repeat until` loop—not inside the loop.*

3. **What you should see when you run it**
   - After each wrong guess: **Too low!** or **Too high!** (for 2 seconds).
   - When the guess is correct, the loop stops (no “too low/high” on that turn).
   - Then the sprite says **`Correct! Attempts: `** followed by the number of tries, e.g. `Correct! Attempts: 4`.

### Common mistake (wrong `if` inside the loop)

Some scripts use an **else** branch like “if guess = secret number then say Too high”. That is **backwards**: when the guess **equals** the secret, the game is **correct**, not too high.

- **Too low** → `guess < secret number`
- **Too high** → `guess > secret number`
- **Correct** → handled by **exiting** `repeat until`; the **join** line runs **after** the loop.

### Extensions
- Increase number range
- Add maximum attempts limit
- Create difficulty levels
- Add hints
- Track best score

---

## Project 6: Shape Drawer (Custom Blocks)
**Time:** 60-90 minutes
**Learning Objectives:**
- Create custom blocks (functions)
- Understand code reuse
- Apply mathematical concepts

### Instructions

1. **Create custom block for square:**
   - Go to "My Blocks"
   - Click "Make a Block"
   - Name it "draw square"
   - Click "OK"

2. **Define the square function:**
   ```
   define draw square
   repeat 4
      move 50 steps
      turn 90 degrees
   end
   ```

3. **Use the custom block:**
   ```
   when green flag clicked
   go to x: 0 y: 0
   draw square
   ```

4. **Create triangle function:**
   ```
   define draw triangle
   repeat 3
      move 50 steps
      turn 120 degrees
   end
   ```

5. **Create pattern:**
   ```
   when green flag clicked
   go to x: 0 y: 0
   repeat 4
      draw square
      turn 90 degrees
   end
   ```

6. **Add parameters:**
   - Create block "draw square with size"
   - Add number input parameter
   - Use parameter in function

### Extensions
- Create functions for other shapes
- Add color parameters
- Create complex patterns
- Build geometric art

---

## Assessment Criteria

### Beginner Projects (Moving Cat, Dancing Sprite)
- Uses basic blocks correctly
- Project runs without errors
- Shows understanding of events

### Intermediate Projects (Interactive Story, Score Keeper)
- Uses multiple concepts together
- Includes user interaction
- Code is organized and readable

### Advanced Projects (Number Guessing Game, Shape Drawer)
- Uses variables and conditions effectively
- Creates reusable code (custom blocks)
- Solves problems creatively

---

## Tips for Teachers

1. **Start Simple:** Begin with basic projects and add complexity
2. **Encourage Experimentation:** Let students explore and modify
3. **Celebrate Mistakes:** Errors are learning opportunities
4. **Share Projects:** Use Scratch community for inspiration
5. **Connect to Curriculum:** Link projects to subject content

---

## Student Handout Template

**Project Name:** _________________

**Learning Goal:** _________________

**Steps:**
1. _________________
2. _________________
3. _________________

**Challenge:** _________________

**Extension:** _________________

**What I Learned:** _________________




