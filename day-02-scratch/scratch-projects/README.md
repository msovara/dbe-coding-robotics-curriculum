# Scratch solution projects (`.sb3`)

This folder holds **real Scratch block projects** you can open in the editor for testing — easier than reading the text memos in [project-templates.md](../projects/project-templates.md).

## How to run `01-catch-game.sb3`

You were **not** running it wrong — an earlier version of the generated file had broken block links. Re-download or rebuild after pulling the latest fix.

1. **Load the project** — Scratch → **File → Load from your computer** → choose `01-catch-game.sb3`.
2. **Use the editor stage** (normal size is fine). Full screen is optional; it does not change how scripts run.
3. Click the **green flag** once (top of the stage, not the “Full screen” button alone).
4. You should see:
   - **score** in the top-left corner (stage monitor)
   - **Basket** (Scratch **Bowl** costume) at the bottom — move with **←** and **→**
   - **Apple** clones falling from the top every 1–3 seconds (original Fruit hides on flag)
   - **Referee** (Scratch library sprite) hidden until **score 20**, then says “You win!”
5. Click the **red stop sign** to reset, then green flag again for a new game.

**Block annotations:** Open each sprite’s code — yellow **comment bubbles** on blocks explain what each one does. Printable tables: [01-catch-game-block-annotations.md](01-catch-game-block-annotations.md).

**If something still looks wrong**

| Symptom | Likely cause |
|---------|----------------|
| Only the basket moves | Old `.sb3` — re-download or run `build_solutions.py` again |
| No fruit falling | Green flag not clicked, or project did not load fully — reload the file |
| Cannot catch fruit | Move the **bowl** under the falling **apple**; widen catch by moving early |
| No win message | Score must reach **20**; watch the score monitor |

**Sprites:** The `.sb3` uses official Scratch library art — **Bowl** (Basket), **Apple** (Fruit), **Referee** — stored in [`assets/`](assets/README.md).

## What is in `solutions/`

| File | Project | Status |
|------|---------|--------|
| `01-catch-game.sb3` | Project 1: Catch Game | Generated (matches memo script; blocks annotated) |
| [01-catch-game-block-annotations.md](01-catch-game-block-annotations.md) | Catch Game **block guide** | What each block does |
| [`01-catch-game-solution.mp4`](videos/01-catch-game-solution.mp4) | Catch Game **video walkthrough** (~8 min) | Generated (slides + narration) |
| `02-quiz-game.sb3` | Project 2: Interactive Quiz | *Add manually or extend build script* |
| `03-platformer.sb3` | Project 3: Platformer | *Planned* |
| `04-water-cycle.sb3` | Project 4: Water Cycle | *Planned* |
| `05-*` | Project 5 | *Planned* |

You can also drag an `.sb3` onto [TurboWarp](https://turbowarp.org/) for a fast preview without signing in.

## For facilitators: save your own solution

If you build or tweak a project in Scratch:

1. **File → Save to your computer**
2. Save into `solutions/` using the naming pattern above.
3. Commit and push so other facilitators can download the same file.

Keep solutions aligned with the **memo** in `project-templates.md` so they stay answer keys, not alternate designs.

## Regenerate generated files

The catch game is built from Python (not hand-edited in Scratch):

```bash
python day-02-scratch/scratch-projects/build_solutions.py
```

Requires `_template_extracted/` (assets extracted from `_template.sb3`). To refresh the template on Windows:

```powershell
Copy-Item _template.sb3 _template.zip
Expand-Archive -Force _template.zip _template_extracted
```

## Day 1

Day 1 solution projects can live in `day-01-scratch/scratch-projects/solutions/` using the same layout. Copy this README pattern when you add them.

## Links from the curriculum site

On GitHub, download raw files:

`https://github.com/msovara/dbe-coding-robotics-curriculum/raw/main/day-02-scratch/scratch-projects/solutions/01-catch-game.sb3`

The text memos on the workshop site remain the primary teaching reference; these files are for **facilitator testing and demo**.
