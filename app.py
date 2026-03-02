"""
DBE Coding and Robotics Curriculum – Streamlit App
Browse the 5-day workshop structure, lesson plans, guides, and resources.
Run from repo root: streamlit run app.py
"""

import streamlit as st
from pathlib import Path

# Base path: directory where app.py lives (repo root)
BASE = Path(__file__).resolve().parent


def load_markdown(relative_path: str) -> str | None:
    """Load markdown file; return None if missing."""
    path = BASE / relative_path
    if path.exists() and path.suffix.lower() == ".md":
        try:
            return path.read_text(encoding="utf-8", errors="replace")
        except Exception:
            return None
    return None


def render_md(path: str) -> None:
    """Load and render a markdown file, or show a message if missing."""
    content = load_markdown(path)
    if content:
        st.markdown(content, unsafe_allow_html=False)
    else:
        st.info(f"Content not found: `{path}`")


def day_files(day_folder: str) -> dict[str, str]:
    """Return a dict of label -> path for known files in a day folder."""
    # Common pattern: lesson-plan, guide(s), activities/*.md, projects/*.md, assessment/rubric.md
    candidates = [
        ("Lesson plan", f"{day_folder}/lesson-plan.md"),
    ]
    day_path = BASE / day_folder
    if day_path.is_dir():
        for sub in ["activities", "projects", "assessment"]:
            subdir = day_path / sub
            if subdir.is_dir():
                for f in sorted(subdir.glob("*.md")):
                    name = f.stem.replace("-", " ").title()
                    candidates.append((f"{sub.title()} – {name}", str(f.relative_to(BASE))))
        for f in sorted(day_path.glob("*.md")):
            if f.name != "lesson-plan.md":
                name = f.stem.replace("-", " ").title()
                candidates.append((name, str(f.relative_to(BASE))))
    return dict(candidates)


def main():
    st.set_page_config(
        page_title="DBE Coding & Robotics Curriculum",
        page_icon="📚",
        layout="wide",
        initial_sidebar_state="expanded",
    )

    st.sidebar.title("📚 DBE Curriculum")
    st.sidebar.markdown("Coding and Robotics Teacher Training")
    st.sidebar.divider()

    page = st.sidebar.radio(
        "Navigate",
        [
            "Overview",
            "Day 1: Scratch",
            "Day 2: Advanced Scratch",
            "Day 3: Arduino",
            "Day 4: Micro:bit Part 1",
            "Day 5: Micro:bit & Code Club",
            "Timetable",
            "Resources",
            "Supporting Materials",
        ],
        label_visibility="collapsed",
    )

    if page == "Overview":
        st.title("DBE Coding and Robotics Curriculum")
        st.caption("Week-long teacher training workshop")
        render_md("README.md")

    elif page == "Day 1: Scratch":
        st.title("Day 1: Introduction to Coding with Scratch")
        files = day_files("day-01-scratch")
        tab_names = list(files.keys())
        tabs = st.tabs(tab_names) if tab_names else [st.container()]
        for tab, (label, path) in zip(tabs, files.items()):
            with tab:
                render_md(path)

    elif page == "Day 2: Advanced Scratch":
        st.title("Day 2: Advanced Scratch Programming")
        files = day_files("day-02-scratch")
        tab_names = list(files.keys())
        tabs = st.tabs(tab_names) if tab_names else [st.container()]
        for tab, (label, path) in zip(tabs, files.items()):
            with tab:
                render_md(path)

    elif page == "Day 3: Arduino":
        st.title("Day 3: Physical Computing with Scratch for Arduino")
        files = day_files("day-03-arduino")
        tab_names = list(files.keys())
        tabs = st.tabs(tab_names) if tab_names else [st.container()]
        for tab, (label, path) in zip(tabs, files.items()):
            with tab:
                render_md(path)

    elif page == "Day 4: Micro:bit Part 1":
        st.title("Day 4: Coding & Robotics with Micro:bit – Part 1")
        files = day_files("day-04-microbit")
        tab_names = list(files.keys())
        tabs = st.tabs(tab_names) if tab_names else [st.container()]
        for tab, (label, path) in zip(tabs, files.items()):
            with tab:
                render_md(path)

    elif page == "Day 5: Micro:bit & Code Club":
        st.title("Day 5: Micro:bit Part 2 & Code Club Intro")
        files = day_files("day-05-microbit-codeclub")
        tab_names = list(files.keys())
        tabs = st.tabs(tab_names) if tab_names else [st.container()]
        for tab, (label, path) in zip(tabs, files.items()):
            with tab:
                render_md(path)

    elif page == "Timetable":
        st.title("Workshop Timetable")
        if load_markdown("WORKSHOP_TIMETABLE_ONE_PAGE.md"):
            render_md("WORKSHOP_TIMETABLE_ONE_PAGE.md")
        else:
            render_md("WORKSHOP_TIMETABLE.md")

    elif page == "Resources":
        st.title("Resources")
        res_choices = [
            ("Curriculum summary", "CURRICULUM-SUMMARY.md"),
            ("CHPC integration", "CHPC_INTEGRATION.md"),
            ("Procurement guide", "resources/procurement-guide.md"),
            ("CHPC references", "resources/chpc-references.md"),
            ("Integration template", "resources/templates/integration-planning-template.md"),
            ("Cloud (reference)", "resources/cloud-computing/README.md"),
            ("Hardware (reference)", "resources/hardware/README.md"),
        ]
        choice = st.selectbox("Select resource", [c[0] for c in res_choices], label_visibility="collapsed")
        path = next(p for n, p in res_choices if n == choice)
        render_md(path)

    elif page == "Supporting Materials":
        st.title("Supporting Materials")
        supp_choices = [
            ("Meeting agenda", "MEETING_AGENDA.md"),
            ("Pre-workshop survey", "supporting-materials/pre-workshop-survey.md"),
            ("Daily reflection template", "supporting-materials/daily-reflection-template.md"),
            ("Workshop evaluation form", "supporting-materials/workshop-evaluation-form.md"),
            ("Email template", "EMAIL_TEMPLATE.md"),
            ("Email workshop summary", "EMAIL_WORKSHOP_SUMMARY.md"),
        ]
        choice = st.selectbox("Select document", [c[0] for c in supp_choices], label_visibility="collapsed")
        path = next(p for n, p in supp_choices if n == choice)
        render_md(path)

    st.sidebar.divider()
    st.sidebar.caption("[GitHub repo](https://github.com/msovara/dbe-coding-robotics-curriculum)")


if __name__ == "__main__":
    main()
