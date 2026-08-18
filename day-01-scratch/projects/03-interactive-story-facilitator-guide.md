# Interactive Story — Facilitator block annotations

**Audience:** Facilitators and provincial specialists (Day 1 workshop)  
**Use this for:** What to **say** while explaining each block — not text to paste into Scratch.

**Companion files**

| File | Purpose |
|------|---------|
| [Project 3 memo](project-templates.md#project-3-interactive-story-intermediate) | Clean block scripts (answer key) |
| [Interactive Story memo](03-interactive-story-code.md) | Same scripts on a short GitHub Pages page |
| [`03-interactive-story.sb3`](../scratch-projects/solutions/03-interactive-story.sb3) | Working project to demo |

---

## Before you demo (2 minutes)

Say something like:

> Today the story is a **picture book**. The player turns the page with a **click** or the **right arrow**. There is **one path**: beginning, middle, end.  
> Tomorrow the player will **choose** Forest or Space. That needs `ask` and `if`. We do not need those yet.

**Check on screen before coding**

| Item | Setting | What to say |
|------|---------|-------------|
| Backdrops `Home`, `Road`, `School` | Named, in that order | “Name them. `backdrop1` is not a scene.” |
| Message `scene 2` | In **Messages** | “A broadcast is like shouting a page number.” |
| Sprites | `Child`, `Friend` | “Child starts the story. Friend only appears on the road.” |

**How the demo runs**

1. Click the **green flag** (Home; Child speaks).  
2. **Click** Child.  
3. **Right arrow** → Road; Friend appears; Child hides.  
4. **Right arrow** again → School; ending line.

---

## The story in two broadcasts

```text
Green flag → Home
  Click Child → talk
    Right arrow → scene 2 → Road (Friend)
      Right arrow → School (ending)
```

Day 1 vs Day 2:

```text
Day 1:  Green flag → click / arrow → next scene
        One path. Player turns pages.

Day 2:  Green flag → ask A or B → path A or path B → ending A or B
        Two paths. Player chooses.
```

---

## Stage

**Role:** Change the picture when the story moves.

| Block | What it does | What to say |
|-------|----------------|-------------|
| `when green flag clicked` | Start a new play. | “Green flag always opens page 1.” |
| `switch backdrop to (Home)` | Opening scene. | “Switch **by name**, not by hoping `next backdrop` is in order.” |
| `when I receive (scene 2)` | Road scene. | “The Stage does not talk. It only changes the picture.” |
| `switch backdrop to (Road)` | Second setting. | “Backdrop names must match the Backdrops pane.” |

---

## Child sprite — start position

| Block | What it does | What to say |
|-------|----------------|-------------|
| `when green flag clicked` | Place the Child. | “Setup on the flag. Talking on click is a **second** script.” |
| `show` | Child is visible at Home. | “Friend starts hidden; Child must be seen.” |
| `go to x: (-80) y: (-60)` | Left side of the stage. | “Leave the right side for the Friend.” |
| `switch backdrop to (Home)` | Open on page 1. | “Same idea as Catch Game: flag resets the world.” |
| `say [I missed the taxi...] for (2) seconds` | Opening line. | “`for (2) seconds` lets them read. A plain `say` flashes.” |

**Demo tip:** Stop after this script. Check: flag → Home → bubble.

---

## Child — click

| Block | What it does | What to say |
|-------|----------------|-------------|
| `when this sprite clicked` | Player talks to the character. | “Different hat from the green flag — two scripts on **one** sprite.” |
| `say [I need help. Press the right arrow.] for (2) seconds` | Dialogue. | “Click is **talk**. The arrow is **turn the page**.” |

---

## Child — next scene

| Block | What it does | What to say |
|-------|----------------|-------------|
| `when [right arrow] key pressed` | Turn the page. | “Keys are good for ‘continue’.” |
| `broadcast (scene 2)` | Tell Stage and Friend. | “The Child does not move the Friend. It only shouts the next scene.” |
| `hide` | Child leaves the stage. | “Must be **after** the broadcast so Friend can still appear.” |

---

## Friend sprite — start hidden

| Block | What it does | What to say |
|-------|----------------|-------------|
| `when green flag clicked` | Stay off stage until the road. | “If you forget `hide`, two people stand at Home.” |
| `hide` | Invisible in Scene 1. | “Same rule as Water Cycle Cloud and Day 2 Scientist.” |
| `go to x: (80) y: (-60)` | Right side, ready for Scene 2. | “Place them before they show, so they do not jump.” |

---

## Friend — scene 2

| Block | What it does | What to say |
|-------|----------------|-------------|
| `when I receive (scene 2)` | Only the road scene. | “This hat does not run on green flag.” |
| `show` | Friend appears. | “Show *this* sprite only. Child is already hiding.” |
| `say [Walk with me...] for (2) seconds` | Road dialogue. | “Same `say for 2 seconds` rule as Child.” |

---

## Friend — ending

| Block | What it does | What to say |
|-------|----------------|-------------|
| `when [right arrow] key pressed` | Last page. | “`next backdrop` works if Home, Road, School are in that order.” |
| `switch backdrop to (next backdrop)` | School. | “If the story jumps, drag the backdrops into order.” |
| `say [We arrived on time...] for (2) seconds` | Lesson / ending. | “Languages: a full sentence. Life Skills: a lesson.” |

---

## Facilitator pitfalls

| Mistake | Symptom | Fix |
|---------|---------|-----|
| Starting with `ask` and `if` | Group is lost; afternoon content in the morning | Linear pages only today |
| Building all three scenes in one demo | Copying without understanding | One scene, then click, then arrow |
| Unnamed backdrops | `next backdrop` feels random | Name them `Home`, `Road`, `School` |
| Two hats explained as two sprites | Extra unused sprites | “Two scripts, one character.” |
| Friend `show` on green flag | Two people in Scene 1 | `hide` on Friend’s flag script |
| `hide` before `broadcast` on Child | Friend never appears | Broadcast **then** hide |
| Message `scene2` vs `scene 2` | Backdrop never changes | Names must match, including the space |

---

## Suggested teaching order (45 min)

1. **Story on paper** (8 min) — beginning, middle, end. No code.  
2. **Sprites and backdrops** (5 min) — Child, Friend, Home / Road / School.  
3. **Child flag + click** (10 min).  
4. **Message `scene 2`** (5 min).  
5. **Friend hide / show** (10 min).  
6. **Play and retell** (7 min).

If you have 60–90 minutes, add the exercises below.

---

## Quick demo script (60 seconds)

> “Green flag puts us **home**. Click the **child**. Press the **right arrow** — we are on the **road**, and the **friend** appears. Arrow again — **school**, and the lesson. One path. Tomorrow they will **choose**.”

---

## Exercises

Use the [memo](03-interactive-story-code.md) for the scripts. These are classroom tasks only.

| # | Task | Time |
|---|------|------|
| 1 | Paper: Scene 1 late for school, Scene 3 on time. Write Scene 2. Name three events. | 10 min |
| 2 | Build **Child** only from the memo. | 15 min |
| 3 | Debug: missing `for (2) seconds`; Friend visible on flag; wrong backdrop order. | 10 min |
| 4 | Add **Friend** hide/show from the memo. | 10 min |
| 5 | Change only `say` text (kindness / water / two languages). | 15 min |
| 6 | Full memo with `broadcast (scene 2)`. No Forest/Space choices. | 10 min |
| 7 | Exit ticket: flag starts at _____; click is for _____; arrow is for _____. | 3 min |

---

## Links

- **Download `.sb3`:** [raw GitHub file](https://github.com/msovara/dbe-coding-robotics-curriculum/raw/main/day-01-scratch/scratch-projects/solutions/03-interactive-story.sb3)  
- **Memo (scripts):** [Interactive Story memo](03-interactive-story-code.md)  
- **Day 2 (do not teach today):** [Interactive Story with choices](../day-02-scratch/scratch-projects/05-interactive-story-facilitator-annotations.md) · [Download Day 2 `.sb3`](https://github.com/msovara/dbe-coding-robotics-curriculum/raw/main/day-02-scratch/scratch-projects/solutions/05-interactive-story.sb3)
