# Water Cycle — Facilitator block annotations

**Audience:** Facilitators and provincial specialists (Day 2 workshop)  
**Use this for:** What to **say** while explaining each block — not text to paste into Scratch.

**Companion files**

| File | Purpose |
|------|---------|
| [Project 4 memo](../projects/project-templates.md#project-4-water-cycle-simulation) | Clean block scripts (answer key) |
| [`04-water-cycle.sb3`](solutions/04-water-cycle.sb3) | Working project to demo |

---

## Before you demo (2 minutes)

Say something like:

> We are simulating the **water cycle**: water evaporates, condenses into a cloud, falls as rain, and collects on the ground.  
> The science is the story. The coding idea is **broadcast**: one sprite shouts a message, another sprite listens and continues the cycle.

**Check on screen before coding**

| Item | Setting | What to say |
|------|---------|-------------|
| Variables `evaporated`, `condensed`, `precipitated`, `ground water` | **For all sprites** | “Counters live on the stage so every sprite can change them.” |
| Messages `evaporate`, `condense`, `rain`, `collected` | In **Messages** | “Each message is one step of the cycle — like handing the baton.” |
| Sprites | `Sun`, `Droplet`, `Cloud`, `Ground` | “Sun starts the cycle; droplet moves; cloud appears; ground is the landing.” |

**How the demo runs**

1. Click the **green flag** (reset counters; after a short pause evaporation starts).  
2. Or **click the Sun** to start another cycle.  
3. Watch: droplet rises → cloud says “Condensation” → droplet falls onto the **grass** → “Collection”.

---

## The cycle in four broadcasts

```text
Click Sun → evaporate
  Droplet rises → condense
    Cloud appears → rain
      Droplet falls, touches Ground → collected
        Droplet returns to the start (ready for another click)
```

---

## Stage / counters (green flag)

In the memo, **Stage** resets the four counters. In the `.sb3`, the **Sun** does this on green flag (same effect).

| Block | What it does | What to say |
|-------|----------------|-------------|
| `set (evaporated) to (0)` | Reset evaporation counter. | “Green flag must zero everything so a replay is fair.” |
| `set (condensed) to (0)` | Reset condensation counter. | “Tick the four variables so monitors show on the stage.” |
| `set (precipitated) to (0)` | Reset rain counter. | “Precipitated = rain that has fallen.” |
| `set (ground water) to (0)` | Reset collection counter. | “Space in the name is fine: `ground water`.” |

---

## Sun sprite

**Role:** Starts evaporation when the learner **clicks** it.

| Block | What it does | What to say |
|-------|----------------|-------------|
| `when green flag clicked` | Place the sun and reset the game. | “Setup on green flag; the *start of science* is a **click**, not the flag.” |
| `go to x: (170) y: (120)` | Top-right of the stage. | “Keep the sun out of the droplet’s path.” |
| `show` | Make the sun visible. | “Learners must see what to click.” |
| `say [Click me, or wait...]` | Hint that the sun starts the cycle. | “Green flag resets; the sun *starts* evaporation.” |
| `wait (1) seconds` then `broadcast (evaporate)` | First cycle starts on its own. | “So ‘running the project’ is not a blank stage. Clicking the sun still works for extra cycles.” |
| `when this sprite clicked` | Hat for a mouse click on the sun. | “Different hat from green flag — Events palette.” |
| `broadcast (evaporate)` | Tell the droplet to rise. | “The sun does not move the water. It only sends a message.” |

**Demo tip:** Green flag waits a few seconds, then the droplet should rise. Click the sun for another cycle.

---

## Droplet sprite — start position

| Block | What it does | What to say |
|-------|----------------|-------------|
| `when green flag clicked` | Put the droplet at the “surface”. | “x −100, y −100 sits just above the grass.” |
| `go to x: (-100) y: (-100)` | Starting collection point. | “This is also where it returns after rain — just above the grass.” |
| `show` | Show the droplet at the start. | “One droplet sprite plays *all* stages of the cycle.” |

---

## Droplet — evaporation (`when I receive evaporate`)

| Block | What it does | What to say |
|-------|----------------|-------------|
| `when I receive (evaporate)` | Starts when the sun is clicked. | “This hat only runs after the broadcast — not on green flag.” |
| `show` | Make sure the droplet is visible. | “It may have been hidden at the top from the last cycle.” |
| `forever` | Keep rising until high enough. | “Same pattern as Catch Game: `forever` + `if` + `stop`, not a broken `repeat until not`.” |
| `if ‹(y position) > (90)›` | Near the top of the stage. | “90 is just below the cloud. Teachers can change this height.” |
| `hide` | Droplet becomes vapour (unseen). | “We hide it so the **cloud** can take over the story.” |
| `broadcast (condense)` | Next step of the cycle. | “Cleanup (hide) **before** `stop` — same lesson as deleting fruit clones.” |
| `stop (this script)` | Leave the rise loop. | “Must be last inside the `if`.” |
| `change y by (5)` | Move **up**. | “Positive y = up. Evaporation is water going into the air.” |
| `change (evaporated) by (1)` | Count rise steps. | “This counts motion steps, not ‘one evaporation’. That is OK for a first model.” |
| `wait (0.05) seconds` | Slow the rise so it is visible. | “Without `wait`, it jumps to the cloud instantly.” |

---

## Cloud sprite

**Role:** Condensation — water gathers as a cloud, then rain is triggered.

| Block | What it does | What to say |
|-------|----------------|-------------|
| `when green flag clicked` | Place the cloud and hide it. | “Cloud starts **hidden** — it only appears when vapour arrives.” |
| `go to x: (-70) y: (120)` | Top of the stage, above the pond. | “Align x with where rain will fall.” |
| `hide` | Invisible until condensation. | “If you forget `hide`, the cloud sits there the whole time.” |
| `when I receive (condense)` | Vapour has reached the sky. | “Cloud’s job is the middle of the cycle.” |
| `show` | Cloud becomes visible. | “Learners should see condensation as ‘cloud appears’.” |
| `change (condensed) by (1)` | One condensation event. | “Here we count **once per cycle**, not every pixel.” |
| `say [Condensation] for (2) seconds` | Label the science word. | “Use `say` to teach vocabulary, not only movement.” |
| `wait (1) seconds` | Short pause before rain. | “Gives time to read the speech bubble.” |
| `broadcast (rain)` | Start precipitation. | “Cloud does not draw the rain — it tells the droplet to fall.” |
| `hide` | Cloud clears after raining. | “Ready for the next evaporation.” |

---

## Droplet — rain (`when I receive rain`)

| Block | What it does | What to say |
|-------|----------------|-------------|
| `when I receive (rain)` | Starts precipitation. | “Same sprite, third hat — still the droplet.” |
| `go to x: (-70) y: (100)` | Appear under the cloud. | “Teleport to the sky; we are not showing every vapour molecule.” |
| `show` | Raindrop becomes visible. | “After hide during evaporation, we must `show` again.” |
| `forever` | Fall until the ground. | “Mirror of rising: now y decreases.” |
| `if ‹touching (Ground)? or (y position) < (-150)›` | Has rain reached the land? | “Grass strip across the bottom, plus a y check so rain cannot fall forever.” |
| `broadcast (collected)` | Start collection. | “Broadcast **before** `stop` so the next script can run.” |
| `stop (this script)` | Stop falling. | “If you only `stop` and never broadcast, the cycle hangs.” |
| `change y by (-6)` | Move **down**. | “Negative y = falling rain.” |
| `change (precipitated) by (1)` | Count fall steps. | “Again: steps of motion, useful as a visible counter.” |
| `wait (0.05) seconds` | Visible fall speed. | “Match the evaporation wait so up and down feel related.” |

---

## Droplet — collection (`when I receive collected`)

| Block | What it does | What to say |
|-------|----------------|-------------|
| `when I receive (collected)` | Rain has hit the ground. | “Fourth hat on Droplet — one sprite, four jobs.” |
| `change (ground water) by (1)` | One collection event. | “This is the ‘water in rivers / soil’ counter.” |
| `go to x: (-100) y: (-100)` | Return to the pond. | “The cycle can start again when they click the sun.” |
| `say [Collection] for (2) seconds` | Label the last stage. | “Four science words in the project: evaporate, condense, precipitate, collect.” |

---

## Ground sprite

| Block | What it does | What to say |
|-------|----------------|-------------|
| `when green flag clicked` | Place the land at the bottom. | “Ground is mostly a **target** for `touching`.” |
| `go to x: (0) y: (-165)` | Full-width **grass** along the bottom. | “A tree is too narrow — rain can miss it. Continuous grass is a landing strip.” |
| `show` | Land is visible. | “Keep the sprite name **Ground** so `touching (Ground)` still works.” |

---

## Facilitator pitfalls

| Mistake | Symptom | Fix |
|---------|---------|-----|
| Clicking green flag and waiting 0 seconds | Cycle has a 3-second hint before it starts | Wait for the sun speech bubble, or click the sun |
| Ground is a small tree | Rain never “lands”; droplet falls off stage | Use a **full-width grass** costume named **Ground** |
| Cloud not hidden on green flag | Cloud visible from the start | Add `hide` on Cloud’s flag script |
| `repeat until not …` for rising/falling | Droplet never moves (same Catch Game bug) | Use `forever` + `if` + `stop this script` |
| `stop` before `broadcast` | Cycle stops in the sky or mid-fall | Broadcast **then** stop, inside the `if` |
| Sprite named “Trees” but code says `Ground` | Rain never “lands” | Rename sprite to **Ground** |
| Variables “for this sprite only” | Counters stay 0 | Recreate as **for all sprites** |
| `ground water` vs `groundwater` | Score-like mismatch | Use the same name everywhere |

---

## Suggested teaching order (60–90 min)

1. **Science story first** (5 min) — four words, no code.  
2. **Sprites and names** (5 min) — Sun, Droplet, Cloud, Ground.  
3. **Messages** (5 min) — create the four broadcasts.  
4. **Sun click → evaporate** (10 min) — droplet rises and hides.  
5. **Cloud condenses → rain** (10 min).  
6. **Fall + touch Ground → collected** (15 min).  
7. **Counters on stage** (10 min).  
8. **Play the full cycle** twice (10 min).

---

## Quick demo script (60 seconds)

> “Green flag resets the counters. Click the **sun**. The droplet **evaporates** upward, then hides. The cloud appears — **condensation**. It broadcasts **rain**, the droplet falls, touches the **ground**, and we **collect** groundwater. Click the sun again to run the cycle once more.”

---

## Links

- **Download `.sb3`:** [raw GitHub file](https://github.com/msovara/dbe-coding-robotics-curriculum/raw/main/day-02-scratch/scratch-projects/solutions/04-water-cycle.sb3)  
- **Run guide:** [scratch-projects README](README.md)
