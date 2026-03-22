# Publishing the curriculum on GitHub Pages

This repository includes a **static documentation site** built with [MkDocs](https://www.mkdocs.org/) and the [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) theme. It mirrors the curriculum structure (days, timetable, resources, supporting materials).

## Live URL (after setup)

**Project site:** [https://msovara.github.io/dbe-coding-robotics-curriculum/](https://msovara.github.io/dbe-coding-robotics-curriculum/)

*(The link works once GitHub Pages is enabled and the workflow has run successfully.)*

## One-time GitHub repository settings

1. On GitHub, open the repo **msovara/dbe-coding-robotics-curriculum**.
2. Go to **Settings → Pages**.
3. Under **Build and deployment**, set **Source** to **GitHub Actions** (not “Deploy from a branch” using `/docs` unless you switch to that model).
4. Save if prompted.

## How deployment works

- Workflow file: `.github/workflows/github-pages.yml`
- On every push to **`main`**, GitHub Actions installs `mkdocs-material`, runs `mkdocs build`, and publishes the `site/` output to GitHub Pages.
- You can also run the workflow manually: **Actions → Deploy MkDocs to GitHub Pages → Run workflow**.

## Preview on your computer

MkDocs is configured with `docs_dir: docs`. The real curriculum files stay at the **repo root**; a small script links them into `docs/` before building (same as CI).

**Linux / macOS / Git Bash:**

```bash
cd dbe-coding-robotics-curriculum
pip install -r mkdocs-requirements.txt
bash scripts/link-docs-for-mkdocs.sh
mkdocs serve
```

**Windows (PowerShell):**

```powershell
cd dbe-coding-robotics-curriculum
pip install -r mkdocs-requirements.txt
powershell -ExecutionPolicy Bypass -File scripts/link-docs-for-mkdocs.ps1
python -m mkdocs serve
```

Then open the URL shown in the terminal (often **http://127.0.0.1:8000**). With `site_url` set for GitHub Pages, local paths may include `/dbe-coding-robotics-curriculum/`—use the link MkDocs prints.

Linked paths under `docs/` are listed in `.gitignore` so they are not committed; only `docs/index.md` is tracked.

## Streamlit vs GitHub Pages

| | **Streamlit** (`app.py`) | **GitHub Pages** (this site) |
|--|--------------------------|------------------------------|
| Hosting | Your machine or Streamlit Cloud | GitHub (free) |
| Tech | Python app | Static HTML |
| Editing | Same Markdown files in the repo | Same Markdown files in the repo |

You can keep both: use Pages for a public link, and Streamlit for interactive local browsing if you prefer.

## Changing the published URL

If the repo is renamed or moved under an organization, update **`site_url`** in `mkdocs.yml` to match GitHub’s project Pages URL pattern: `https://<user-or-org>.github.io/<repo>/`.
