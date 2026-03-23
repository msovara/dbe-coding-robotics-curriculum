# Advanced Scratch Programming Guide
## Day 2 – Extending Scratch Skills

This guide supports Day 2 of the DBE Coding and Robotics workshop. It builds on Day 1 Scratch basics and introduces advanced concepts: cloning, broadcasting, complex games, and curriculum integration.

**Prerequisites:** Completion of Day 1 (Scratch basics, variables, conditions, custom blocks).  
**Reference:** [day-01-scratch](../day-01-scratch/) for review of basics.

---

## Advanced Scratch Concepts

### Cloning

**What it is:** Creating multiple copies (clones) of a sprite that can act independently.

**Use cases:**
- Multiple enemies in a game
- Falling objects (rain, snow, coins)
- Particle effects
- Multiple characters doing the same action

**Key blocks:**
- `create clone of [myself]` – Create a clone
- `when I start as a clone` – Code that runs for each clone
- `delete this clone` – Remove a clone when done

**Example:** Create 10 clones of a sprite, each moving in different directions.

**Ready-to-type scripts:** Step-by-step block stacks for cloning, broadcasting, a catch game, lives, and a list-based quiz are in **[activities/advanced-scratch-activities.md](activities/advanced-scratch-activities.md)** (“Example block scripts” under each activity).

---

### Broadcasting

**What it is:** Sending messages between sprites (and the stage) to coordinate actions.

**Use cases:**
- Starting a new level or scene
- Triggering actions in multiple sprites
- Game over or win conditions
- Coordinating animations

**Key blocks:**
- `broadcast [message]` – Send a message
- `broadcast [message] and wait` – Send and wait for receivers to finish
- `when I receive [message]` – React to a message

**Example:** When player reaches goal, broadcast "level complete" → all sprites react (show celebration, play sound, etc.).

---

### Advanced Lists

**Beyond basics:** Using lists for:
- High scores (sort, find max/min)
- Inventory systems
- Multiple choice questions
- Data collection and analysis

**Key operations:**
- `add [thing] to [list]`
- `delete [1] of [list]`
- `item [1] of [list]`
- `length of [list]`
- `contains [thing]?` – Check if list includes an item

---

## Complex Projects and Games

### Game Design Elements

- **Scoring:** Variables for score, lives, level
- **Collision detection:** `touching [sprite]?` or `touching color [color]?`
- **Levels:** Use variables or broadcasts to change difficulty
- **Win/lose conditions:** Check conditions and broadcast game over
- **Multiple sprites:** Player, enemies, collectibles, obstacles

### Interactive Story Elements

- **Multiple scenes:** Use broadcasts to change backgrounds
- **Character dialogue:** Use "say" blocks with timing
- **User choices:** Use "ask and wait" and conditions to branch the story
- **Sound and music:** Add background music and sound effects

---

## Scratch and Curriculum Integration

### Mathematics

- **Geometry:** Draw shapes, calculate angles, explore symmetry
- **Data:** Collect data, create graphs, calculate averages
- **Number operations:** Practice tables, fractions, percentages
- **Simulations:** Probability experiments, random events

### Languages

- **Storytelling:** Create interactive stories with dialogue
- **Vocabulary:** Word games, spelling, definitions
- **Grammar:** Sentence building, parts of speech
- **Reading comprehension:** Quiz games, comprehension activities

### Science

- **Simulations:** Water cycle, food chains, ecosystems
- **Experiments:** Data collection, hypothesis testing
- **Models:** Solar system, cell structure, forces
- **Data visualization:** Charts, graphs, patterns

### Social Studies / History

- **Timelines:** Interactive historical events
- **Maps:** Location-based activities
- **Biographies:** Interactive character presentations
- **Quizzes:** Knowledge checks, review games

---

## Assessment Strategies

- **Project rubrics:** Functionality, creativity, code quality, explanation
- **Portfolios:** Collection of projects showing growth
- **Peer review:** Learners review and remix each other's projects
- **Self-reflection:** "What did I learn? What was hard? What would I change?"
- **Demonstrations:** Show and explain projects to class

---

## Classroom Management Tips

- **Pair programming:** Two learners, one computer, take turns
- **Showcase time:** Regular sharing sessions (weekly or per project)
- **Offline editor:** Use Scratch Desktop if internet is unreliable
- **Account management:** Create class accounts or use school accounts
- **Differentiation:** Provide starter projects for beginners, challenges for advanced

---

## Next Steps (Day 3)

Day 3 moves from screen to physical world: connecting Scratch to Arduino hardware for physical computing projects.

---

**Last updated:** For use with DBE Coding and Robotics Curriculum, Day 2.
