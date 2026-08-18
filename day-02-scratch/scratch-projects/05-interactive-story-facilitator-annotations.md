# Interactive Story — Facilitator block annotations

**Audience:** Facilitators and provincial specialists (Day 2 workshop)  
**Use this for:** What to **say** while explaining each block — not text to paste into Scratch.

**Companion files**

| File | Purpose |
|------|---------|
| [Project 5 memo](../projects/project-templates.md#project-5-interactive-story-with-choices) | Clean block scripts (answer key) |
| [`05-interactive-story.sb3`](solutions/05-interactive-story.sb3) | Working project to demo |
| [Day 1 linear story](../../day-01-scratch/projects/03-interactive-story-code/) | Click/arrow “turn the page” — teach this **before** choices |

---

## Before you demo (2 minutes)

Say something like:

> This is a **branching story**. The player types a choice, and that answer picks the next scene.  
> The coding idea is **broadcast plus `if`**: one sprite asks the question; other sprites only run when they receive their path.

**Check on screen before coding**

| Item | Setting | What to say |
|------|---------|-------------|
| Variable `choice` | **For all sprites** | “We store the first answer so the `if` can read it.” |
| List `story choices` | **For all sprites** | “A list remembers *every* answer, in order — like a diary.” |
| Messages `scene 1`, `path A`, `path B`, `ending A`, `ending B` | In **Messages** | “Each message is a scene. Names must match exactly, including the space.” |
| Sprites | `Guide`, `Scientist`, `Robot` | “Guide starts the story. Scientist is the forest. Robot is space.” |
| Backdrops | `Laboratory`, `Forest`, `Space`, `Ending A`, `Ending B` | “The Stage changes the picture when it hears a message.” |

**How the demo runs**

1. Click the **green flag**. Laboratory appears; Guide asks Forest **(A)** or Space **(B)**.  
2. Type `A` or `a` for forest, anything else for space.  
3. Answer **YES** or **yes** for the happy ending; anything else for the other ending.  
4. Watch `story choices` fill with the typed answers.

---

## The story in five broadcasts

```text
Green flag → Laboratory → scene 1
  Guide asks: Forest (A) or Space (B)?
    A / a → path A → Forest → Scientist YES/NO → ending A or B
    anything else → path B → Space → Robot YES/NO → ending A or B
```

---

## Stage

**Role:** Change the backdrop when the story moves. Clear the list on a new play.

| Block | What it does | What to say |
|-------|----------------|-------------|
| `when green flag clicked` | Start a new play. | “Green flag resets the world before anyone speaks.” |
| `switch backdrop to (Laboratory)` | Opening scene. | “The Stage owns backdrops. Sprites do not need to draw the room.” |
| `delete (all) of (story choices)` | Empty the diary. | “Without this, yesterday’s answers stay in the list.” |
| `broadcast (scene 1)` | Tell the Guide to start talking. | “The Stage does not ask the question — it only starts the first scene.” |
| `when I receive (path A)` | Forest branch. | “Same hat type as the characters, but here we only change the picture.” |
| `switch backdrop to (Forest)` | Trees / green scene. | “Backdrop names must match the names in the Backdrops pane.” |
| `when I receive (path B)` | Space branch. | “Anything other than A/a from the Guide lands here.” |
| `switch backdrop to (Space)` | Night sky. | “Learners can swap art later; keep the *names* the same.” |
| `when I receive (ending A)` / `(ending B)` | The two endings. | “Two endings, two messages — do not reuse `path A` for an ending.” |

---

## Guide sprite — start position

**Costume in the `.sb3`:** Scratch library **Avery**, sprite name **Guide**.

| Block | What it does | What to say |
|-------|----------------|-------------|
| `when green flag clicked` | Place the Guide. | “Setup only — talking happens on `scene 1`, not on the flag.” |
| `show` | Guide is visible in the lab. | “Scientist and Robot start hidden; Guide must be seen.” |
| `go to x: (-100) y: (-80)` | Left side of the stage. | “Leave the centre for the next character.” |

---

## Guide — first choice (`when I receive scene 1`)

| Block | What it does | What to say |
|-------|----------------|-------------|
| `when I receive (scene 1)` | Starts after the Stage broadcasts. | “This hat does not run on green flag by itself.” |
| `say [The laboratory alarm is sounding!]` | Opening line. | “`say for 2 seconds` gives time to read before the ask box.” |
| `ask [Do you investigate the forest (A) or launch into space (B)?] and wait` | Typed input. | “`answer` is a reporter — it holds whatever they typed.” |
| `set (choice) to (answer)` | Copy into a variable. | “We need a variable so the `if` can test A *or* a.” |
| `add (choice) to (story choices)` | Remember this answer. | “Lists grow. Variables hold one value.” |
| `if ‹(choice) = [A] or (choice) = [a]›` | Forest only for A/a. | “Scratch string tests are case-sensitive. That is why we check both.” |
| `broadcast (path A)` | Forest scene. | “The Guide does not become the Scientist. It only shouts the next scene.” |
| `else` `broadcast (path B)` | Space for everything else. | “B, b, banana — all go to space. That is the spec.” |
| `hide` | Guide leaves the stage. | “Must be **after** the `if` so both paths hide the Guide.” |

**Demo tip:** Run once with `A`, then green flag and type `B`, so both branches are visible.

---

## Scientist — Path A (Forest)

**Costume in the `.sb3`:** Scratch library **Pico**, sprite name **Scientist**.

| Block | What it does | What to say |
|-------|----------------|-------------|
| `when green flag clicked` `hide` | Stay off stage until forest. | “If you forget `hide`, Pico stands in the laboratory.” |
| `when I receive (path A)` | Only the forest branch. | “Robot never hears this message — that is how scenes stay separate.” |
| `go to x: (20) y: (-70)` | Stand in the forest. | “Optional but tidy — library sprites are tall.” |
| `show` | Scientist appears. | “Show *this* sprite only. Guide is already hidden.” |
| `say` then `ask [Help the animal? Type YES or NO.]` | Second choice. | “The prompt says YES — so the `if` must accept `YES` as well as `yes`.” |
| `add (answer) to (story choices)` | Second diary entry. | “We do not overwrite `choice`; we append to the list.” |
| `if ‹(answer) = [yes] or [YES] or [Yes]›` | Happy ending. | “Three checks because typing is messy. `NO` falls through to `else`.” |
| `say [Your kindness saves the animal!]` | Ending A line. | “Say **before** hide so learners can read it.” |
| `hide` then `broadcast (ending A)` | Leave, then change scene. | “Hide the character so they do not sit on the ending backdrop.” |
| `else` laboratory line + `ending B` | Other ending. | “`else` is ‘anything that is not yes’ — including a blank answer.” |

---

## Robot — Path B (Space)

**Costume in the `.sb3`:** Scratch library **Robot**.

Same pattern as Scientist: hide on flag, show on `path B`, YES/NO, hide, broadcast an ending.

| Block | What it does | What to say |
|-------|----------------|-------------|
| `when I receive (path B)` | Space branch only. | “Copy the Scientist script, then change the words and the message.” |
| `ask [Use the shield? Type YES or NO.]` | Space dilemma. | “Same YES test as the forest — one rule, two stories.” |
| `broadcast (ending A)` / `(ending B)` | Shared endings. | “Both paths can reach the same two endings. That is the point of messages.” |

---

## Facilitator pitfalls

| Mistake | Symptom | Fix |
|---------|---------|-----|
| Message `pathA` vs `path A` | Backdrop never changes | Names must match, including the space |
| Variables/lists “for this sprite only” | List stays empty or `choice` is 0 | Recreate as **for all sprites** |
| `if (choice) = [A]` only | Typing `a` goes to space | Check **A** or **a** |
| `if (answer) = [yes]` only | Typing `YES` (as the prompt asks) goes to ending B | Check **yes**, **YES**, and **Yes** |
| Scientist/Robot not hidden on flag | Wrong character in the lab | `hide` on green flag |
| `hide` before `broadcast` on Guide | Fine — Guide is done talking | Keep `hide` **after** the `if` |
| Unused sprite still showing on the ending | Pico/Robot on the gold/purple slide | `hide` then `broadcast` the ending |
| Backdrop name `forest` vs `Forest` | Stage stays on Laboratory | Match the Backdrops pane exactly |

---

## Suggested teaching order (60–75 min)

1. **Story map on paper** (5 min) — two paths, two endings. No code.  
2. **Sprites, backdrops, messages** (10 min).  
3. **Stage: flag + four receives** (10 min) — prove backdrops change with a test `broadcast`.  
4. **Guide asks A/B** (15 min).  
5. **Scientist path** (15 min).  
6. **Robot path** (10 min) — copy and change.  
7. **Play both routes** (10 min) and read `story choices`.

---

## Quick demo script (60 seconds)

> “Green flag puts us in the laboratory. Type **A** for the forest — the Scientist asks if we help the animal. Type **YES** and we get the gold ending. Green flag again, type **B**, then **NO** — space path, other ending. The list at the side is the trail of answers.”

---

## Links

- **Download `.sb3`:** [raw GitHub file](https://github.com/msovara/dbe-coding-robotics-curriculum/raw/main/day-02-scratch/scratch-projects/solutions/05-interactive-story.sb3)  
- **Run guide:** [scratch-projects README](README.md)
