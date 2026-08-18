# Scratch solution projects (`.sb3`)

This folder holds **real Scratch block projects** you can open in the editor for testing — easier than reading the text memos in [project-templates.md](../projects/project-templates.md).

## Quick start

1. Open [scratch.mit.edu](https://scratch.mit.edu/projects/editor/) (or the Scratch desktop app).
2. **File → Load from your computer**
3. Choose a file from **`solutions/`**, for example `01-catch-game.sb3`.
4. Click the **green flag** to test.

You can also drag an `.sb3` onto [TurboWarp](https://turbowarp.org/) for a fast preview without signing in.

## What is in `solutions/`

| File | Project | Status |
|------|---------|--------|
| `01-catch-game.sb3` | Project 1: Catch Game | Generated (matches memo script) |
| [`01-catch-game-solution.mp4`](videos/01-catch-game-solution.mp4) | Catch Game **video walkthrough** (~8 min) | Generated (slides + narration) |
| `02-quiz-game.sb3` | Project 2: Interactive Quiz | *Add manually or extend build script* |
| `03-platformer.sb3` | Project 3: Platformer | *Planned* |
| `04-water-cycle.sb3` | Project 4: Water Cycle | *Planned* |
| `05-*` | Project 5 | *Planned* |

Sprites use the default Scratch cat costume so the logic loads reliably. After opening, swap in basket/fruit/backdrop art from the Scratch library.

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
