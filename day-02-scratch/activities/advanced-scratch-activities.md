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
