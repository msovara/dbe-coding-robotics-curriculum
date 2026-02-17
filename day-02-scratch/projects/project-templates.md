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
