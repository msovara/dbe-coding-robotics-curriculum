# Interactive Story (Day 1) — Facilitator teaching guide

**Audience:** Facilitators and provincial specialists (Day 1 workshop)  
**Scratch scripts (copy these):** they are on this page under [Scratch code](#scratch-code) and on the short page [Interactive Story code](03-interactive-story-code.md).

**Companion files**

| File | Purpose |
|------|---------|
| **[Interactive Story code](03-interactive-story-code.md)** | Block scripts only — open this on GitHub Pages |
| [Project 3 memo](project-templates.md#memo-suggested-scratch-script) | Same scripts inside the Day 1 project list |
| [Day 2 branching story](../day-02-scratch/scratch-projects/05-interactive-story-facilitator-annotations.md) | Choices, `ask`, `if` — **tomorrow** |

---

## Scratch code

**Setup:** sprites `Child`, `Friend`. Backdrops `Home`, `Road`, `School` (in that order). Message `scene 2`.

### Stage

```text
when green flag clicked
switch backdrop to (Home)
```

```text
when I receive (scene 2)
switch backdrop to (Road)
```

### Child

```text
when green flag clicked
show
go to x: (-80) y: (-60)
switch backdrop to (Home)
say [I missed the taxi. I am late for school.] for (2) seconds
```

```text
when this sprite clicked
say [I need help. Press the right arrow.] for (2) seconds
```

```text
when [right arrow] key pressed
broadcast (scene 2)
hide
```

### Friend

```text
when green flag clicked
hide
go to x: (80) y: (-60)
```

```text
when I receive (scene 2)
show
say [Walk with me. Press the arrow again.] for (2) seconds
```

```text
when [right arrow] key pressed
switch backdrop to (next backdrop)
say [We arrived on time. Next time I will leave earlier.] for (2) seconds
```

**How to run:** green flag → click Child → right arrow → right arrow again.

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

**All block scripts are on this page under [Scratch code](#scratch-code)** and on [Interactive Story code](03-interactive-story-code.md).

Do not start with Exercise 6 unless the group has finished Exercise 2.

### Exercise 1 — Unplugged: broken instructions (10 min)

Give this storyboard. Ask what is missing.

> Scene 1: A child is late for school.  
> Scene 3: The child is on time and smiling.

**Task:** Write Scene 2 in three sentences. Then list **three Scratch events** you would use (flag, click, key).

**Sample Scene 2:** A friend sees the child and says they can walk together. They take the road to school.

**Three events:** `when green flag clicked` (Scene 1), `when this sprite clicked` (talk), `when [right arrow] key pressed` (next scene).

Then build the story from the [memo](project-templates.md#memo-suggested-scratch-script).

**Success:** Scene 2 connects the problem to the ending; events are named.

### Exercise 2 — Scratch: three named backdrops (15 min)

**Task:** Name backdrops `Home`, `Road`, `School` in that order. Build **Child** only from the memo (flag, click, arrow). You may skip Friend and `broadcast` until Exercise 4.

**Check:** Someone else can play it without explanation.

### Exercise 3 — Debug (pairs, 10 min)

Compare the broken line to the [memo](project-templates.md#memo-suggested-scratch-script). Each pair fixes **one**.

| Bug | What they see | Fix (as in the memo) |
|-----|----------------|----------------------|
| `say [Once upon a time...]` with no time | Bubble flashes | `say [] for (2) seconds` |
| Friend `show` on green flag | Two people in Scene 1 | Friend: `hide` on flag |
| Arrow script on a hidden sprite | Arrow seems dead | Put arrow / broadcast on **Child** |
| Backdrops in the wrong order | Story jumps Home → School | Order: Home, Road, School |

### Exercise 4 — Hide the unused character (10 min)

**Task:** Add **Friend** from the memo. Child `hide`s after the arrow; Friend `show`s on `scene 2`.

**Success:** Only the character who belongs in that scene is visible.

### Exercise 5 — Language / Life Skills story (15–20 min)

**Task:** Keep the memo scripts. Change only the `say` text using the table in the memo (kindness, water, or two languages).

**Success:** Same three scenes; at least two full-sentence `say` lines.

### Exercise 6 — Broadcast preview (optional, 10 min)

**Task:** Build the full memo: Stage + Child `broadcast (scene 2)` + Friend `when I receive (scene 2)`. Do **not** add Forest/Space choices.

**Success:** Two sprites react to **one** message.

### Exercise 7 — Exit ticket (3 min, paper)

1. Green flag should always start at scene ______ . **[Home / Scene 1]**  
2. `when this sprite clicked` is for ______ ; `when key pressed` is for ______ . **[talking / turning the page]**  
3. Tomorrow’s story will let the player **choose**. Today’s story only lets the player ______ . **[turn the page]**

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

- **Scratch code on GitHub Pages:** [Interactive Story code](03-interactive-story-code.md)  
- **Day 2 (do not teach today):** [Interactive Story with choices](../day-02-scratch/scratch-projects/05-interactive-story-facilitator-annotations.md) · [Download Day 2 `.sb3`](https://github.com/msovara/dbe-coding-robotics-curriculum/raw/main/day-02-scratch/scratch-projects/solutions/05-interactive-story.sb3)
