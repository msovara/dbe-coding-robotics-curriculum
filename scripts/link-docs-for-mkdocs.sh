#!/usr/bin/env bash
# Symlink curriculum content into docs/ so MkDocs can use docs_dir: docs
# Run from repo root: bash scripts/link-docs-for-mkdocs.sh
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"
mkdir -p docs

link_dir() {
  local name="$1"
  rm -rf "docs/${name}"
  ln -sfn "../${name}" "docs/${name}"
}

link_file() {
  local name="$1"
  rm -f "docs/${name}"
  ln -sfn "../${name}" "docs/${name}"
}

for name in day-01-scratch day-02-scratch day-03-arduino day-04-microbit day-05-microbit-codeclub resources supporting-materials; do
  link_dir "$name"
done

for f in \
  WORKSHOP_TIMETABLE_ONE_PAGE.md \
  WORKSHOP_TIMETABLE.md \
  CURRICULUM-SUMMARY.md \
  CHPC_INTEGRATION.md \
  MEETING_AGENDA.md \
  EMAIL_TEMPLATE.md \
  EMAIL_WORKSHOP_SUMMARY.md \
  GITHUB_SETUP.md \
  GITHUB_PAGES.md \
  CHPC_DSI_CODING_SCHOOL_PR.md; do
  link_file "$f"
done

echo "Linked curriculum into docs/. You can run: mkdocs serve"
