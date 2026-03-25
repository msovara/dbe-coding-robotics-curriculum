# Open a PR: Scratch materials → [ChpcTraining/dsi_coding_school](https://github.com/ChpcTraining/dsi_coding_school)

This guide follows **add remote → branch → copy files → push → open PR**. Your personal curriculum lives in **[msovara/dbe-coding-robotics-curriculum](https://github.com/msovara/dbe-coding-robotics-curriculum)**; the CHPC work repo is **[ChpcTraining/dsi_coding_school](https://github.com/ChpcTraining/dsi_coding_school)** (see its [Scratch folder](https://github.com/ChpcTraining/dsi_coding_school/tree/main/scratch)).

---

## Why `git checkout chpc/main` often fails on Windows

`dsi_coding_school` contains paths with a **trailing space** in the name (`cloud_computing/resources /…`). Windows Git reports **invalid path** and refuses to check out `main`. That blocks a full clone or `git checkout chpc/main` inside your DBE repo on Windows.

**Use one of these instead:**

- **GitHub Codespaces** on `ChpcTraining/dsi_coding_school` (Linux filesystem)
- **macOS or Linux** (including WSL **with a distro installed**)
- Ask a maintainer to **rename** `cloud_computing/resources ` → `cloud_computing/resources` on `main` (fixes Windows for everyone)

---

## Recommended: Linux / macOS / Codespaces (clean import, no broken Windows paths)

Run in a normal Unix shell (not Windows `cmd` for the clone of `dsi_coding_school`).

```bash
# 1) Clone CHPC work repo (full clone works on Linux/macOS)
git clone https://github.com/ChpcTraining/dsi_coding_school.git
cd dsi_coding_school

# 2) New branch for the PR
git checkout -b import/dbe-scratch-curriculum

# 3) Add your DBE repo as a remote (read-only fetch is enough)
git remote add dbe https://github.com/msovara/dbe-coding-robotics-curriculum.git
git fetch dbe main

# 4) Import only Day 1 & Day 2 Scratch trees into scratch/dbe_teacher_workshop/
mkdir -p scratch/dbe_teacher_workshop
git archive dbe/main day-01-scratch day-02-scratch | tar -x -C scratch/dbe_teacher_workshop

# 5) Add the workshop README (copy from exports/chpc-upstream/README.md in this repo, or paste below)
#    File: scratch/dbe_teacher_workshop/README.md

git add scratch/dbe_teacher_workshop
git status
git commit -m "feat(scratch): add DBE teacher workshop Scratch Days 1–2"

# 6) Push branch
#    If you have write access to ChpcTraining:
git push -u origin import/dbe-scratch-curriculum

#    If you use a FORK (replace YOURUSER):
# git remote add myfork https://github.com/YOURUSER/dsi_coding_school.git
# git push -u myfork import/dbe-scratch-curriculum
```

**7) Open the PR**

- On GitHub: **Compare & pull request** for `import/dbe-scratch-curriculum` → `main` on `ChpcTraining/dsi_coding_school` (or from your fork to upstream).

---

## Windows-only: create a zip without checking out CHPC

From your **dbe-coding-robotics-curriculum** clone (already on disk):

```powershell
cd path\to\dbe-coding-robotics-curriculum
git fetch origin
git archive --format=zip -o ..\dbe-scratch-days-1-2.zip origin/main day-01-scratch day-02-scratch
```

Upload **`dbe-scratch-days-1-2.zip`** to a Codespace or Linux machine, unzip into `scratch/dbe_teacher_workshop/`, add `README.md`, then `git add`, `commit`, `push` as above.

A copy is also kept in this repo under **`exports/dbe-scratch-days-1-2.zip`** (when present) for convenience.

---

## Optional: `chpc` remote in your personal repo

Your DBE repo can keep:

```bash
git remote add chpc https://github.com/ChpcTraining/dsi_coding_school.git
git fetch chpc
```

Useful for **`git fetch`** and **`git archive chpc/main …`** from a machine that **can** read that history. On Windows, **`git checkout chpc/main`** or **`git worktree`** may still fail until upstream path names are fixed.

---

## Suggested link from CHPC `scratch/README` (maintainers)

After merge, add one line pointing to `scratch/dbe_teacher_workshop/README.md` so trainers find the DBE five-day workshop Scratch track.

---

## Licence / attribution

Content is the same as in **msovara/dbe-coding-robotics-curriculum**; ensure CHPC repo policy (licence, attribution) is satisfied when merging.
