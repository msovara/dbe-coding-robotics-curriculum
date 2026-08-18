# Interactive Story (Day 1) — Facilitator teaching guide

**Audience:** Facilitators and provincial specialists (Day 1 workshop)  
**Use this for:** How to **teach** the linear story, what to **say**, and classroom **exercises** — not text to paste into Scratch.

**Companion files**

| File | Purpose |
|------|---------|
| [Project 3 memo](project-templates.md#project-3-interactive-story-intermediate) | Short build steps (answer key) |
| [Day 2 branching story](../day-02-scratch/scratch-projects/05-interactive-story-facilitator-annotations.md) | Choices, `ask`, `if`, broadcasts — **tomorrow** |

---

## Before you teach (2 minutes)

Say something like:

> Today the story is a **picture book**. The player turns the page with a **click** or the **right arrow**. There is **one path**: beginning, middle, end.  
> Tomorrow the player will **choose** Forest or Space. That needs `ask` and `if`. We do not need those yet.

Day 1 **morning** has not taught variables, lists, or `if`. Stay with **events**, **say**, and **backdrops**.

**Check on screen before coding**

| Item | Setting | What to say |
|------|---------|-------------|
| At least 3 backdrops | Named `Scene 1`, `Scene 2`, `Scene 3` (or Home / Road / School) | “Name them. `backdrop1` is not a scene.” |
| One main sprite | Visible | “This character talks when you click it.” |
| Events | Green flag, sprite clicked, right arrow | “Three different hats — three ways the story can start a script.” |

**Day 1 vs Day 2**

```text
Day 1:  Green flag → Scene 1 → click / arrow → Scene 2 → Scene 3
        One path. Player turns pages.

Day 2:  Green flag → ask A or B → path A or path B → ending A or B
        Two paths. Player chooses.
```

---

## Teaching sequence (45 minutes)

The lesson plan slot is **Events and Control**. Do not build the whole story in one demo.

### 1. Paper first (8 min) — no computers

Give a 3-box storyboard. Learners fill:

| Scene | Where? | Who is on stage? | What do they say? | How does the player continue? |
|-------|--------|------------------|-------------------|-------------------------------|
| 1 Introduction | | | | Click the character |
| 2 Development | | | | Right arrow |
| 3 Resolution | | | | (the end) |

Say:

> A computer story is the same as a picture book: **one page at a time**. The green flag opens page 1.

**Curriculum hook:** Languages (beginning–middle–end); Life Skills (a problem and a lesson).

### 2. Demo only Scene 1 (7 min)

On the main sprite (or Stage):

```text
when green flag clicked
switch backdrop to (Scene 1)
say [Once upon a time...] for (2) seconds
```

| Block | What it does | What to say |
|-------|----------------|-------------|
| `when green flag clicked` | Starts the book. | “Every replay must open on page 1.” |
| `switch backdrop to (Scene 1)` | Shows the first setting. | “Switch **by name**, not by hoping `next backdrop` is in the right order.” |
| `say [Once upon a time...] for (2) seconds` | Opening line. | “`for (2) seconds` lets them read. A plain `say` flashes and vanishes.” |

**Stop.** Let them copy this only. Check: flag → Scene 1 → bubble.

### 3. Click = talk to the character (8 min)

```text
when this sprite clicked
say [Hello! Press the right arrow to continue] for (2) seconds
```

| Block | What it does | What to say |
|-------|----------------|-------------|
| `when this sprite clicked` | Player talks to the character. | “Different hat from the green flag — two scripts on **one** sprite.” |
| `say [...] for (2) seconds` | Dialogue. | “Click is **interaction**. The flag was only **start**.” |

### 4. Arrow = next page (10 min)

```text
when [right arrow] key pressed
switch backdrop to (next backdrop)
```

| Block | What it does | What to say |
|-------|----------------|-------------|
| `when [right arrow] key pressed` | Turn the page. | “Keys are good for ‘continue’. Clicks are good for ‘talk to me’.” |
| `switch backdrop to (next backdrop)` | Moves to the next costume of the Stage. | “Backdrops must be in story order: 1, then 2, then 3.” |

If they have already met `if` (afternoon), you may switch **by name** instead of `next backdrop`. Morning groups should keep `next backdrop`.

### 5. Second character + hide/show (8 min, if time)

Sprite B: `hide` on green flag. `show` when Scene 2 starts (arrow script, or optional `broadcast` — see Exercise 6).

Say: “Characters who are not in this scene must `hide`. Tomorrow Scientist and Robot follow the same rule.”

### 6. Play and retell (4 min)

Partner A runs it. Partner B retells the story **without looking at the blocks**. If they cannot retell it, the story is not clear yet.

---

## Suggested story shape (what to put in each scene)

The memo’s Scene 2 says “user makes choices.” On **Day 1** that means click or arrow — **not** `ask` / `if A or B`.

| Scene | Job | Example (Languages / Life Skills) |
|-------|-----|-----------------------------------|
| 1 Introduction | Who, where, problem | A learner is late. “I missed the taxi.” |
| 2 Development | Try to solve it | Click: a friend offers a walk. Arrow: they set off. |
| 3 Resolution | Lesson / ending | They arrive. “Next time I will leave earlier.” |

---

## Exercises

### Exercise 1 — Unplugged: broken instructions (10 min)

Give this storyboard. Ask what is missing.

> Scene 1: A child is late for school.  
> Scene 3: The child is on time and smiling.

**Task:** Write Scene 2 in three sentences. Then list **three Scratch events** you would use (flag, click, key).

**Success:** Scene 2 connects the problem to the ending; events are named.

### Exercise 2 — Scratch: three named backdrops (15 min)

**Must have**

1. Backdrops named `Home`, `Road`, `School` (or their own three names).  
2. Green flag → first backdrop and a `say` line.  
3. Click the sprite → one line of dialogue.  
4. Right arrow → next backdrop.

**Check:** Someone else can play it without explanation.

### Exercise 3 — Debug (pairs, 10 min)

Write these bugs on the board. Each pair finds and fixes **one**.

| Bug | What they see | Fix |
|-----|----------------|-----|
| Backdrop still called `backdrop1` | Arrow seems to do nothing useful | Rename to Scene 1, 2, 3 |
| Speech on green flag with plain `say` (no time) | Bubble flashes and vanishes | Use `say [] for (2) seconds` |
| Second character visible in Scene 1 | Two people in the opening | `hide` that sprite on green flag |
| Arrow script on the unused sprite | Arrow works only if that sprite is selected | Put the key script on the sprite they use, or on **Stage** |
| `next backdrop` with backdrops in the wrong order | Story jumps Home → School | Drag backdrops into order 1–2–3 |

### Exercise 4 — Hide the unused character (10 min)

Add a second sprite.

- Green flag: Sprite A `show`, Sprite B `hide`.  
- When they move to Scene 2: Sprite A `hide`, Sprite B `show`.

**Success:** Only the character who belongs in that scene is visible.

### Exercise 5 — Language / Life Skills story (15–20 min)

Pick **one** prompt:

- A learner helps a classmate (kindness).  
- Water is wasted, then saved (vocabulary that returns on Day 2 Water Cycle).  
- A character greets in English and one home language.

Same three-scene rule. At least **two** `say` lines in full sentences.

### Exercise 6 — Broadcast preview (optional, 10 min, stronger groups)

Do **not** add Forest/Space choices yet. This is the Day 1 homework preview (“try broadcasting”).

```text
when [right arrow] key pressed
broadcast (scene 2)
```

```text
when I receive (scene 2)
switch backdrop to (Scene 2)
show
```

**Success:** Two sprites react to **one** message. That is the seed of Day 2 Guide / Scientist / Robot.

### Exercise 7 — Exit ticket (3 min, paper)

Complete:

1. Green flag should always start at scene ______ .  
2. `when this sprite clicked` is for ______ ; `when key pressed` is for ______ .  
3. Tomorrow’s story will let the player **choose**. Today’s story only lets the player ______ .

---

## Facilitator pitfalls

| Mistake | Symptom | Fix |
|---------|---------|-----|
| Starting with `ask` and `if` | Group is lost; afternoon content in the morning | Linear pages only today |
| Building all three scenes in one demo | Copying without understanding | One scene, then click, then arrow |
| Unnamed backdrops | `next backdrop` feels random | Name them before coding |
| Two hats explained as two sprites | Extra unused sprites | “Two scripts, one character.” |
| No `hide` on extra characters | Crowd on Scene 1 | Hide everyone who is not in the opening |
| Calling Day 1 “choices” | Teachers expect Day 2 blocks | Click and arrow are interaction, not branching |

---

## Mini rubric

| | Developing | Meeting | Extending |
|--|------------|---------|-----------|
| Structure | One scene | Three named scenes, beginning–middle–end | Hide/show extra character **or** a broadcast |
| Events | Only green flag | Flag + click **or** key | Flag + click + key |
| Clarity | Hard to follow | Partner can play it | Partner can retell the lesson of the story |

---

## Suggested teaching order (inside the 45 min slot)

1. Storyboard on paper (8 min).  
2. Scene 1 only (7 min).  
3. Click dialogue (8 min).  
4. Arrow / next backdrop (10 min).  
5. Exercise 2 or 3 (10 min).  
6. Exit ticket (2 min).

If you have the full 60–90 minutes from the project template, add Exercise 4, then 5, then 6 for the extension group.

---

## Links

- **Day 1 memo:** [Project 3: Interactive Story](project-templates.md#project-3-interactive-story-intermediate)  
- **Day 2 (do not teach today):** [Interactive Story with choices](../day-02-scratch/scratch-projects/05-interactive-story-facilitator-annotations.md) · [Download Day 2 `.sb3`](https://github.com/msovara/dbe-coding-robotics-curriculum/raw/main/day-02-scratch/scratch-projects/solutions/05-interactive-story.sb3)
