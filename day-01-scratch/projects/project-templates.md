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
**Time:** 60-90 minutes
**Learning Objectives:**
- Use multiple events
- Create scenes with backgrounds
- Add user interaction

### Instructions

1. **Plan your story:**
   - Beginning, middle, end
   - Characters
   - Settings (backgrounds)
   - User interactions

2. **Set up backgrounds:**
   - Add at least 3 backgrounds
   - Name them clearly

3. **Create opening scene:**
   ```
   when green flag clicked
   switch backdrop to [Scene 1]
   say [Once upon a time...] for 2 seconds
   ```

4. **Add character interactions:**
   ```
   when this sprite clicked
   say [Hello! Click the arrow to continue] for 2 seconds
   ```

5. **Add scene transitions:**
   ```
   when [right arrow] key pressed
   switch backdrop to [next backdrop]
   ```

6. **Add multiple characters:**
   - Each character can have different scripts
   - Use "broadcast" to coordinate actions

### Story Template Structure

**Scene 1: Introduction**
- Introduce characters
- Set the scene
- Present a problem

**Scene 2: Development**
- Character tries to solve problem
- User makes choices
- Consequences of choices

**Scene 3: Resolution**
- Problem is solved
- Lesson learned
- Happy ending

### Extensions
- Add sound effects
- Create multiple endings based on choices
- Add animations
- Include educational content

---

## Project 4: Score Keeper (Variables)
**Time:** 45-60 minutes
**Learning Objectives:**
- Create and use variables
- Understand variable values
- Use operators

### Instructions

1. **Create a variable:**
   - Go to Variables section
   - Click "Make a Variable"
   - Name it "Score"
   - Choose "For all sprites" or "For this sprite only"

2. **Set initial score:**
   ```
   when green flag clicked
   set [Score] to 0
   ```

3. **Increase score on click:**
   ```
   when this sprite clicked
   change [Score] by 1
   play sound [pop]
   ```

4. **Add visual feedback:**
   ```
   when this sprite clicked
   change [Score] by 1
   change size by 10
   play sound [pop]
   wait 0.2 seconds
   change size by -10
   ```

5. **Add win condition:**
   ```
   when green flag clicked
   set [Score] to 0
   forever
      if [Score] > 10 then
         say [You Win!] for 2 seconds
         stop [all]
      end
   end
   ```

### Extensions
- Add multiple scoring objects
- Create a timer
- Add different point values
- Create a high score system

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




