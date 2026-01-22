# Scratch Introduction Guide
## A Teacher's Guide to Getting Started with Scratch

## What is Scratch?

Scratch is a free, visual programming language developed by MIT. It allows users to create interactive stories, games, animations, and more by dragging and dropping code blocks instead of typing text.

**Key Features:**
- Visual, block-based programming (no typing required)
- Free and available online or offline
- Designed for ages 8-16, but used by all ages
- Large community with millions of shared projects
- Available in many languages, including isiZulu, Afrikaans, and English

---

## Why Use Scratch in Education?

### Benefits for Students
1. **Engagement:** Students are motivated by creating their own projects
2. **Computational Thinking:** Develops problem-solving and logical thinking
3. **Creativity:** Encourages creative expression through coding
4. **Collaboration:** Sharing and remixing projects builds community
5. **Low Barrier to Entry:** No prior coding experience needed
6. **Immediate Feedback:** See results instantly

### Benefits for Teachers
1. **Easy to Learn:** Intuitive interface, quick to master
2. **Free Resources:** Extensive tutorials and community support
3. **Curriculum Integration:** Can be used across subjects
4. **Assessment Tools:** Built-in sharing and portfolio features
5. **Student Engagement:** Increases motivation and participation

---

## Getting Started

### Creating an Account

1. **Go to:** https://scratch.mit.edu
2. **Click:** "Join Scratch" (top right)
3. **Fill in:**
   - Username (must be unique)
   - Password (at least 8 characters)
   - Email address
   - Date of birth
   - Country
4. **Verify email** (check your inbox)
5. **Start creating!**

### Offline Editor (Alternative)

If internet is unreliable:
1. Download Scratch Desktop from: https://scratch.mit.edu/download
2. Install on computers
3. Projects can be saved locally
4. Can be shared online later

---

## Scratch Interface Overview

### Main Components

```
┌─────────────────────────────────────────────────┐
│  [Menu Bar]  Scratch - Project Name            │
├──────────┬──────────────────────┬───────────────┤
│          │                      │               │
│  Stage   │   Scripts Area      │  Blocks       │
│  Area    │   (Code Building)   │  Palette      │
│          │                      │               │
│          │                      │               │
│          ├──────────────────────┤               │
│          │   Sprite List        │               │
│          │   (Characters)       │               │
│          └──────────────────────┘               │
└─────────────────────────────────────────────────┘
```

### 1. Stage Area
- **Location:** Top left
- **Purpose:** Where your project runs
- **Features:**
  - Green flag: Start project
  - Red stop sign: Stop project
  - Full screen mode
  - Stage size: 480x360 pixels

### 2. Sprite List
- **Location:** Bottom left
- **Purpose:** Shows all sprites (characters/objects) in your project
- **Actions:**
  - Click sprite to select it
  - Right-click for options (duplicate, delete, etc.)
  - Click "+" to add new sprite

### 3. Blocks Palette
- **Location:** Left side, middle
- **Purpose:** Contains all coding blocks
- **Categories:**
  - Motion (blue): Move, turn, position
  - Looks (purple): Appearance, say, think
  - Sound (pink): Play sounds, notes
  - Events (yellow): Start scripts
  - Control (orange): Loops, conditions
  - Sensing (light blue): Detect input
  - Operators (green): Math, logic
  - Variables (orange): Store data
  - My Blocks (dark blue): Custom blocks

### 4. Scripts Area
- **Location:** Center
- **Purpose:** Where you build your code
- **How it works:**
  - Drag blocks from palette
  - Snap blocks together
  - Click blocks to test
  - Right-click to delete/duplicate

### 5. Tabs
- **Scripts:** Write code (default)
- **Costumes:** Edit sprite appearance
- **Sounds:** Add/edit sounds

---

## Essential Blocks for Beginners

### Motion Blocks (Blue)

```
move 10 steps          → Move sprite forward
turn 15 degrees        → Rotate sprite
go to x: 0 y: 0        → Move to specific position
point in direction 90  → Face a direction
```

### Looks Blocks (Purple)

```
say Hello! for 2 secs   → Display text bubble
think Hmm... for 2 secs → Display thought bubble
change size by 10       → Make bigger/smaller
switch costume to [ ]   → Change appearance
```

### Events Blocks (Yellow)

```
when green flag clicked → Start when flag clicked
when [space] key pressed → Start when key pressed
when this sprite clicked → Start when clicked
```

### Control Blocks (Orange)

```
wait 1 secs            → Pause execution
repeat 10              → Loop a set number of times
forever                → Loop forever
if <> then             → Conditional statement
```

### Sound Blocks (Pink)

```
play sound [meow]      → Play a sound
play note 60 for 0.5 beats → Play musical note
```

---

## Your First Project: Moving Cat

### Step 1: Start a New Project
1. Click "File" → "New"
2. You'll see the default cat sprite

### Step 2: Make the Cat Move
1. Click on the **Motion** category (blue)
2. Drag `move 10 steps` block to scripts area
3. Click the block - cat moves!
4. Try changing the number (e.g., move 50 steps)

### Step 3: Add an Event
1. Click **Events** category (yellow)
2. Drag `when green flag clicked` to top of `move 10 steps`
3. Blocks snap together
4. Click green flag - cat moves!

### Step 4: Make it Continuous
1. Click **Control** category (orange)
2. Drag `forever` block around `move 10 steps`
3. Click green flag - cat moves continuously!

### Step 5: Add Bouncing
1. From **Motion**, drag `if on edge, bounce` inside `forever`
2. Cat now bounces off edges!

### Step 6: Add Sound
1. Click **Sound** category (pink)
2. Drag `play sound [meow]` inside `forever`
3. Cat makes sound while moving!

**Your code should look like:**
```
when green flag clicked
forever
    move 10 steps
    if on edge, bounce
    play sound [meow]
end
```

---

## Common Patterns and Concepts

### Pattern 1: Starting Scripts
**Always start with an event block:**
- `when green flag clicked` - Most common
- `when [key] key pressed` - For keyboard control
- `when this sprite clicked` - For clickable sprites

### Pattern 2: Loops
**Three types of loops:**
1. `repeat 10` - Do something 10 times
2. `forever` - Do something continuously
3. `repeat until <>` - Do until condition is met

### Pattern 3: Conditions
**Making decisions:**
```
if <> then
    [do something]
end
```

**Or with alternatives:**
```
if <> then
    [do this]
else
    [do that]
end
```

### Pattern 4: Variables
**Storing information:**
1. Create variable: Click "Variables" → "Make a Variable"
2. Name it (e.g., "Score")
3. Use it: `set [Score] to 0` or `change [Score] by 1`

---

## Teaching Tips

### For Beginners
1. **Start Simple:** Begin with basic movement
2. **One Concept at a Time:** Don't overwhelm
3. **Hands-On:** Let them explore and experiment
4. **Celebrate Small Wins:** Every working script is success
5. **Use Analogies:** Compare to real-world actions

### For Mixed Levels
1. **Differentiated Tasks:**
   - Beginners: Follow step-by-step
   - Intermediate: Modify examples
   - Advanced: Create from scratch
2. **Peer Support:** Pair advanced with beginners
3. **Extension Challenges:** Provide extra tasks for fast finishers

### Classroom Management
1. **Pair Programming:** Two students, one computer
2. **Showcase Time:** Regular sharing of projects
3. **Troubleshooting:** Teach students to help each other
4. **Save Often:** Remind students to save work
5. **Account Management:** Use class accounts or student accounts

---

## Common Mistakes and Solutions

### Mistake 1: Blocks Don't Snap
**Problem:** Blocks won't connect
**Solution:** Make sure you're dragging to the right place (top or bottom of block)

### Mistake 2: Nothing Happens
**Problem:** Clicked green flag, nothing happens
**Solution:** 
- Check if script is attached to sprite
- Make sure event block is at top
- Check if blocks are connected

### Mistake 3: Sprite Disappears
**Problem:** Sprite goes off screen
**Solution:** Use `go to x: 0 y: 0` to bring it back

### Mistake 4: Too Fast/Slow
**Problem:** Animation too fast or slow
**Solution:** 
- Add `wait` blocks
- Change number of steps
- Adjust speed in motion blocks

### Mistake 5: Can't Find Block
**Problem:** Looking for specific block
**Solution:** 
- Check correct category
- Use search function (top of blocks palette)
- Some blocks only appear with certain sprites

---

## Assessment Ideas

### Formative Assessment
- **Observation:** Watch students work
- **Quick Checks:** "Show me your code"
- **Peer Review:** Students share and give feedback
- **Exit Tickets:** "What did you learn today?"

### Summative Assessment
- **Project Rubric:** Evaluate completed projects
- **Portfolio:** Collection of student work
- **Reflection:** Students write about their learning
- **Presentation:** Students present their projects

### What to Look For
- **Understanding:** Can they explain their code?
- **Problem-Solving:** How do they debug errors?
- **Creativity:** Do they add original elements?
- **Collaboration:** Do they help others?

---

## Resources for Teachers

### Official Resources
- **Scratch Website:** https://scratch.mit.edu
- **ScratchEd:** https://scratched.gse.harvard.edu (teacher community)
- **Getting Started Guide:** https://scratch.mit.edu/ideas
- **Video Tutorials:** https://scratch.mit.edu/help/videos

### Curriculum Integration
- **Scratch for Educators:** https://scratch.mit.edu/educators
- **Lesson Plans:** Search ScratchEd for subject-specific plans
- **Coding Cards:** Printable cards with project ideas

### Community
- **ScratchEd Community:** Connect with other teachers
- **Scratch Forums:** Get help and share ideas
- **Twitter:** #ScratchEd, #Scratch

---

## Next Steps

1. **Practice:** Create your own projects
2. **Explore:** Look at community projects
3. **Plan:** Design a lesson using Scratch
4. **Share:** Connect with other teachers
5. **Implement:** Try Scratch with your students!

---

## Quick Reference Card

### Essential Blocks
- `when green flag clicked` - Start
- `move 10 steps` - Move
- `turn 15 degrees` - Rotate
- `say Hello!` - Display text
- `repeat 10` - Loop
- `if <> then` - Condition
- `set [variable] to 0` - Variable

### Keyboard Shortcuts
- **Space:** Start/stop project
- **Right-click:** Options menu
- **Delete key:** Delete selected blocks
- **Ctrl+Z:** Undo
- **Ctrl+S:** Save (if offline)

### Tips
- Start with events
- Use forever for continuous actions
- Test frequently
- Save often
- Ask for help!

---

## Support

**Need Help?**
- Scratch Help: https://scratch.mit.edu/help
- ScratchEd Forums: https://scratched.gse.harvard.edu/discussions
- Contact workshop facilitators

**Remember:** Everyone starts as a beginner. Be patient with yourself and your students. Coding is about experimentation and learning from mistakes!

