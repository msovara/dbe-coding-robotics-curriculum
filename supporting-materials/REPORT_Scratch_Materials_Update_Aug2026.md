# Report: Scratch Materials Update (August 2026)

**Programme:** DSTI–CHPC Coding and Robotics Workshop (train-the-trainer), 2026–2028  
**Focus:** Day 1 and Day 2 Scratch curriculum updates  
**Prepared by:** Mthetho Vuyo Sovara  
**Date:** August 2026  
**Upstream curriculum:** [msovara/dbe-coding-robotics-curriculum](https://github.com/msovara/dbe-coding-robotics-curriculum)  
**Official workshop site:** [ChpcTraining/dsi_coding_school](https://github.com/ChpcTraining/dsi_coding_school)  
**Live site:** https://chpctraining.github.io/dsi_coding_school/

---

## 1. Purpose

This report summarises updates made to the Scratch materials used in Days 1 and 2 of the DSTI–CHPC Coding and Robotics workshop. The updates improve facilitator readiness by providing working Scratch project files (`.sb3`), clear memo scripts, and separate facilitator annotation documents that explain what to say for each block without cluttering the Scratch projects themselves.

---

## 2. Scope of updates

### 2.1 Day 1 – Introduction to Scratch

| Item | Description |
|------|-------------|
| Interactive Story memo | Scripts and exercises on one page (Home → Road → School; click and right arrow to “turn the page”) |
| Facilitator annotations | Teaching notes for each block (what to say while demonstrating) |
| Solution project | Working `03-interactive-story.sb3` for demonstration and File → Load from your computer |
| Pedagogy note | Day 1 remains a **linear** story; `ask` / branching choices are reserved for Day 2 |

### 2.2 Day 2 – Advanced Scratch

| Item | Description |
|------|-------------|
| Catch Game | Facilitator annotations and working `01-catch-game.sb3` |
| Water Cycle | Facilitator annotations and working `04-water-cycle.sb3` (cycle starts from the pond; counters update correctly) |
| Interactive Story (with choices) | Facilitator annotations and working `05-interactive-story.sb3` (Forest / Space paths using `ask` and `if`) |

### 2.3 Workshop quality feedback session

A short three-slide deck was prepared for the closing feedback session, covering:

- how to run a 15–20 minute quality-focused feedback session;
- ten questions focused on workshop quality (content, pace, facilitation, materials, confidence, and improvement);
- facilitator tips and an exit ticket (*This workshop would be excellent if…*).

**File:** `Workshop_Quality_Feedback_Session.pptx`

---

## 3. Where the materials are published

### 3.1 Official CHPC repository / website

Materials were integrated into:

`scratch/2026-28-scratch-material/`

Homepage Monday and Tuesday sections were updated with direct links to lesson plans, guides, facilitator annotations, and `.sb3` downloads.

- **Merged update (Day 1 and Day 2 Scratch pack):** Pull request #43  
  https://github.com/ChpcTraining/dsi_coding_school/pull/43  
- **Pending (feedback slides):** Pull request #44  
  https://github.com/ChpcTraining/dsi_coding_school/pull/44  

**Live pack:**  
https://chpctraining.github.io/dsi_coding_school/scratch/2026-28-scratch-material/

### 3.2 Curriculum repository (source of truth)

Full Day 1–2 materials, including GitHub Pages memos and the feedback session page:

https://github.com/msovara/dbe-coding-robotics-curriculum  

Day 1 Interactive Story memo (scripts, exercises, `.sb3`):  
https://msovara.github.io/dbe-coding-robotics-curriculum/day-01-scratch/projects/03-interactive-story-code/

---

## 4. Key improvements for facilitators

1. **Working demos** — Facilitators can load complete `.sb3` files instead of rebuilding projects from text alone.  
2. **Clear split of materials** — Memo scripts (answer key) are separate from facilitator annotations (what to say).  
3. **Day 1 vs Day 2 progression** — Linear storytelling on Day 1; branching with conditions on Day 2.  
4. **Bug fixes** — Water Cycle project corrected so evaporation starts from the pond and the cycle runs reliably in Scratch.  
5. **Closing session support** — Structured questions for collecting workshop-quality feedback.

---

## 5. Recommendation / next steps

1. Merge pull request #44 so the workshop quality feedback slides appear under Presentations on the official site.  
2. Use the evaluation form and feedback slides in the Day 5 closing session.  
3. Continue treating the DBE curriculum repository as the upstream source, and sync updates into `scratch/2026-28-scratch-material/` for each workshop cycle.

---

## 6. Summary statement (for inclusion in a longer report)

> In August 2026, the Day 1 and Day 2 Scratch materials for the DSTI–CHPC Coding and Robotics workshop were updated and published to the official `dsi_coding_school` site. Updates include facilitator annotations, memo scripts with exercises, and working Scratch (`.sb3`) solution files for the Day 1 Interactive Story and for Day 2 Catch Game, Water Cycle, and Interactive Story with choices. Homepage links were added so trainers can download demos and open teaching notes directly. A workshop quality feedback slide deck was also prepared for the closing session (pending final merge to the official presentations folder).
