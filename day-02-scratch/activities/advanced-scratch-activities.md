# Advanced Scratch Activities
## Day 2 Hands-On Activities

These activities support the Day 2 lesson plan: advanced Scratch concepts, complex projects, and curriculum integration.

---

## Activity 1: Cloning – Multiple Sprites

### Objective
Use cloning to create multiple copies of a sprite that act independently.

### Instructions
1. **Simple clone:** Create a sprite (e.g. a ball or star). When green flag clicked, `create clone of [myself]` 5 times. Each clone should move in a different direction or pattern.
2. **Clone with behaviour:** Add `when I start as a clone` → move, bounce, change color, or other action. Use `delete this clone` when it reaches the edge or after a timer.
3. **Example projects:**
   - Falling rain or snow (clones fall from top)
   - Multiple enemies in a game
   - Particle effects (sparks, stars)
4. **Test:** Run and observe multiple clones moving independently.

### Example block scripts (build these in Scratch)

*Tip: In Scratch, create a new message or variable only when the block asks for one—type the name exactly (e.g. `raindrop`).*

**A) Launcher – create 8 clones (Sprite: “Raindrop”)**

```text
When green flag clicked
  hide
  go to x: (0) y: (180)
  repeat (8)
    create clone of (myself)
    change x by (40)
```

**B) Each clone falls and deletes at the bottom**

```text
When I start as a clone
  show
  go to x: (pick random (-200) to (200)) y: (180)
  repeat until <touching (edge)?>
    change y by (-5)
    wait (0.05) seconds
  delete this clone
```

**C) Simple “spark burst” (clone moves outward then vanishes)**

```text
When green flag clicked
  repeat (12)
    create clone of (myself)
    turn cw (30) degrees

When I start as a clone
  point in direction (pick random (0) to (360))
  repeat (20)
    move (5) steps
    change (color) effect by (5)
    wait (0.05) seconds
  delete this clone
```

**D) Optional – only the original sprite creates clones (avoid double-firing)**  
Put all `create clone of` blocks under **When green flag clicked** on a **hidden** parent sprite; clones only run **When I start as a clone**.

### Discussion
- How is cloning useful in games and animations?
- What would be hard without cloning? (Creating many sprites manually)

### Extension
- Clones that create more clones (recursive effect)
- Clones that interact with the player (collision detection)

---

## Activity 2: Broadcasting – Sprite Communication

### Objective
Use broadcasting to coordinate actions between multiple sprites.

### Instructions
1. **Simple broadcast:** Create 2–3 sprites. When sprite 1 is clicked, `broadcast [message]`. Other sprites use `when I receive [message]` to react (e.g. change color, move, say something).
2. **Game example:** Create a simple game with:
   - Player sprite (arrow keys to move)
   - Goal sprite (when player touches goal, broadcast "win")
   - Background or other sprites react to "win" (change color, play sound, show message)
3. **Scene change:** Use broadcasts to switch backgrounds or start new scenes in a story.

### Example block scripts (build these in Scratch)

**Step 1 – Make two new messages:** `dance` and `stopDance` (Broadcast menu → New message).

**Sprite 1 – “Leader” (e.g. cat)**

```text
When this sprite clicked
  broadcast (dance)

When green flag clicked
  go to x: (-150) y: (0)
```

**Sprite 2 – “Follower” (e.g. duck)**

```text
When I receive (dance)
  say [Here we go!] for (1) seconds
  repeat (8)
    turn cw (15) degrees
    change (color) effect by (10)
    wait (0.1) seconds
  say [] for (0) seconds

When green flag clicked
  go to x: (150) y: (0)
```

**Sprite 3 – “Announcer” (optional)**

```text
When I receive (dance)
  say [Everyone dance!] for (2) seconds
```

**Simple “win” flow (touching goal)**

*Variables: none required. Messages: `win`.*

**Player**

```text
When green flag clicked
  go to x: (-170) y: (0)

When [left arrow] key pressed
  change x by (-10)

When [right arrow] key pressed
  change x by (10)

forever
  if <touching (Goal)?> then
    broadcast (win)
    wait (2) seconds
    stop [all]
```

**Goal** (static sprite)

```text
When green flag clicked
  go to x: (170) y: (0)
```

**Stage**

```text
When I receive (win)
  switch backdrop to (Backdrop2)
  start sound (Cheer) until done
```

*(Add **Backdrop2** and a **Cheer** sound from the library, or remove those lines.)*

**Celebration sprite** (optional – Stage cannot `say`)

```text
When I receive (win)
  say [You reached the goal!] for (3) seconds
```

**`broadcast and wait` example** – run receivers *before* the next line:

```text
When green flag clicked
  broadcast (dance) and wait
  say [That was fun!] for (2) seconds
```

### Discussion
- How does broadcasting help coordinate multiple sprites?
- When would you use "broadcast and wait" vs. just "broadcast"?

### Extension
- Multiple broadcasts for different events (start, pause, game over, level complete)
- Chain reactions: one broadcast triggers another

---

## Activity 3: Complex Game Design

### Objective
Design and build a complete game with scoring, levels, and win/lose conditions.

### Instructions
1. **Choose game type:** Platformer, maze, quiz, catch game, or your own idea.
2. **Plan:**
   - Player controls (arrow keys, mouse, etc.)
   - Objective (collect items, avoid enemies, answer questions)
   - Scoring system (variables: score, lives, level)
   - Win/lose conditions
3. **Build:**
   - Create player sprite and controls
   - Add collectibles or enemies (use cloning if multiple)
   - Implement scoring (when touching collectible, change score by 1)
   - Add win condition (if score ≥ 10, broadcast "win")
   - Add lose condition (if lives = 0, broadcast "game over")
4. **Test and refine:** Play the game, fix bugs, adjust difficulty.

### Example block scripts – mini “catch” game

*Sprites: **Player** (paddle), **Apple** (falling thing). Variables: **For all sprites** → `score` (starts at 0).*

**Player (paddle at bottom)**

```text
When green flag clicked
  go to x: (0) y: (-150)
  set (score) to (0)

forever
  set x to (mouse x)
```

**Apple**

```text
When green flag clicked
  go to x: (pick random (-220) to (220)) y: (180)

forever
  change y by (-4)
  if <touching (Player)?> then
    change (score) by (1)
    go to x: (pick random (-220) to (220)) y: (180)
  if <(y position) < (-170)> then
    go to x: (pick random (-220) to (220)) y: (180)
```

**Show score on screen**  
The **Stage** in Scratch 3 does **not** have a `say` block. Do one of the following:
- In **Variables**, tick the checkbox next to `score` to show a **number monitor** on the stage (right-click it → *Large readout* if you want it bigger), **or**
- Add a tiny **ScoreLabel** sprite:

```text
When green flag clicked
  go to front layer

forever
  say (join [Score: ] (score)) for (0.2) seconds
```

**Win at 10 points** – create message `gameWon`. Put this on **Player** or a **Referee** sprite (not the Stage):

```text
When green flag clicked
  forever
    if <(score) > (9)> then
      broadcast (gameWon)
      stop [other scripts in sprite]

When I receive (gameWon)
  say [You win!] for (3) seconds
  stop [all]
```

*(Use only **one** script that checks `score > 9`, or the message will spam.)*

### Example – lives + “game over”

*Variable **lives** (for all sprites), start at 3. Message `gameOver`.*

**Apple – full loop with lives** (replace your simple “miss” branch with this version)

```text
When green flag clicked
  go to x: (pick random (-220) to (220)) y: (180)

forever
  change y by (-4)
  if <touching (Player)?> then
    change (score) by (1)
    go to x: (pick random (-220) to (220)) y: (180)
  if <(y position) < (-170)> then
    change (lives) by (-1)
    if <(lives) < (1)> then
      broadcast (gameOver)
      stop [other scripts in sprite]
    go to x: (pick random (-220) to (220)) y: (180)

When I receive (gameOver)
  hide
  stop [other scripts in sprite]
```

**Player – set lives at start**

```text
When green flag clicked
  go to x: (0) y: (-150)
  set (score) to (0)
  set (lives) to (3)
```

**Any character sprite (e.g. Player)**

```text
When I receive (gameOver)
  say [Game over!] for (3) seconds
```

### Discussion
- What makes a game fun and engaging?
- How could you adapt this game for your subject area?

### Extension
- Add levels (increase difficulty, change background)
- Add sound effects and music
- Add instructions screen (broadcast "show instructions" at start)

---

## Activity 4: Curriculum-Integrated Project

### Objective
Create a Scratch project that teaches or practices a topic from your curriculum subject.

### Instructions
1. **Choose subject and topic:** e.g. Maths (fractions), Science (water cycle), Languages (vocabulary), Social Studies (timeline).
2. **Design the project:**
   - What will learners do? (interact, answer questions, explore, create)
   - What will they learn? (learning objectives)
   - How will you assess? (quiz, demonstration, reflection)
3. **Build:** Implement the project in Scratch using concepts from Day 1 and Day 2.
4. **Test:** Try it yourself; ask a colleague to test it.
5. **Share:** Present your project idea to the group (2–3 minutes).

### Example block scripts – vocabulary quiz with a **list**

*List **words**, variable **index** (For this sprite only), sprite **QuizCat**. First, add the list and variable in the **Variables** tab. Optionally fill **words** in the list monitor instead of using the first script’s `add` lines.*

**When green flag clicked – setup + show first word**

```text
When green flag clicked
  delete (all) of (words)
  add [sun] to (words)
  add [moon] to (words)
  add [star] to (words)
  set (index) to (1)
  say (join [Spell: ] (item (index) of (words))) for (2) seconds
```

**When [space] key pressed – check answer and go to next word**

```text
When [space] key pressed
  ask [Type the word:] and wait
  if <(answer) = (item (index) of (words))> then
    say [Correct!] for (1) seconds
    change (index) by (1)
    if <(index) > (length of (words))> then
      say [Quiz finished!] for (3) seconds
      stop [all]
    say (join [Spell: ] (item (index) of (words))) for (2) seconds
  else
    say [Try again] for (1) seconds
```

*Adapt for your subject: use **numbers** (maths answers), **definitions** (science), or **dates** (history) instead of spelling.*

### Discussion
- How does Scratch help learners understand your subject?
- What challenges did you face? How did you solve them?

### Extension
- Create a lesson plan using this project (use template from resources)
- Plan differentiation: how will you support different learners?

---

## Activity 5: Assessment and Sharing

### Objective
Explore assessment strategies and practice sharing Scratch projects.

### Instructions
1. **Review rubric:** Look at the assessment rubric for Day 2. What criteria matter most for your project?
2. **Self-assess:** Use the rubric to assess your own project (or a practice project).
3. **Peer review:** Share your project with a partner. Partner gives feedback using the rubric.
4. **Sharing options:**
   - Share on Scratch online (if accounts allow)
   - Export project file (.sb3) to share offline
   - Present to group (demo and explain)
5. **Remix:** Remix a partner's project and add one feature.

### Discussion
- How will you assess Scratch projects in your classroom?
- How can sharing and remixing support learning?

### Extension
- Create a portfolio plan: how will learners collect and showcase their Scratch projects?
- Plan a showcase event: how will you celebrate learner projects?

---

## Notes for Facilitators

- Ensure everyone has Day 1 skills (variables, conditions) before starting cloning/broadcasting.
- Allow time for extended project development; this is a key outcome of Day 2.
- Emphasise curriculum integration; this helps teachers see immediate classroom value.
- Link to Day 3: "Tomorrow we'll connect Scratch to physical hardware!"
