# DBE Coding and Robotics Curriculum
## Week-Long Teacher Training Workshop

**Repository:** [https://github.com/msovara/dbe-coding-robotics-curriculum](https://github.com/msovara/dbe-coding-robotics-curriculum)

This curriculum is designed for the Department of Basic Education (DBE) in South Africa to train teachers in coding and robotics education.

**Integrated with:** [CHPC Training DSI Coding School](https://github.com/ChpcTraining/dsi_coding_school) - See [CHPC_INTEGRATION.md](CHPC_INTEGRATION.md) for details.

## Curriculum Overview

- **Duration:** 5 days (full-day workshops, 6-8 hours per day)
- **Target Audience:** DBE teachers with mixed experience levels
- **Resources:** Full resources available (Arduino kits, computers, internet, cloud access)

## Structure

- **Day 1:** Introduction to Coding with Scratch
- **Day 2:** Advanced Scratch Programming
- **Day 3:** Physical Computing with Scratch for Arduino
- **Day 4:** Coding & Robotics with Micro:bit – Part 1
- **Day 5:** Coding & Robotics with Micro:bit – Part 2 (Code Club Intro)

Reference material from the former cloud and hardware days is in `resources/cloud-computing/` and `resources/hardware/`.

## Learning Outcomes

Upon completion, teachers will be able to:
1. Teach basic coding and robotics concepts to students
2. Run similar workshops for their students
3. Integrate coding/robotics into existing DBE curriculum subjects

## Directory Structure

```
dbe-coding-robotics-curriculum/
├── README.md (this file)
├── day-01-scratch/
│   ├── lesson-plan.md
│   ├── activities/
│   ├── projects/
│   └── assessment/
├── day-02-scratch/
│   ├── lesson-plan.md
│   ├── scratch-advanced-guide.md
│   ├── activities/
│   │   └── advanced-scratch-activities.md
│   ├── projects/
│   │   └── project-templates.md
│   └── assessment/
│       └── rubric.md
├── day-03-arduino/
│   ├── lesson-plan.md
│   ├── arduino-robotics-guide.md
│   ├── activities/
│   │   └── robotics-activities.md
│   ├── projects/
│   │   └── project-guides.md
│   └── assessment/
│       └── rubric.md
├── day-04-microbit/
│   ├── lesson-plan.md
│   ├── microbit-introduction-guide.md
│   ├── activities/
│   │   └── microbit-activities.md
│   ├── projects/
│   │   └── project-templates.md
│   └── assessment/
│       └── rubric.md
├── day-05-microbit-codeclub/
│   ├── lesson-plan.md
│   ├── code-club-guide.md
│   ├── activities/
│   │   └── code-club-activities.md
│   ├── projects/
│   │   └── first-code-club-session-template.md
│   └── assessment/
│       └── rubric.md
├── resources/
│   ├── cloud-computing/     (reference: former Day 3)
│   ├── hardware/           (reference: former Day 4)
│   ├── templates/
│   ├── rubrics/
│   └── guides/
└── supporting-materials/
    ├── pre-workshop-survey.md
    ├── daily-reflection-template.md
    └── evaluation-form.md
```

## Streamlit App (Browse Curriculum in the Browser)

**App URL (when running locally):** [http://localhost:8501](http://localhost:8501)

From the repo root, install and run:

```bash
pip install -r requirements.txt
streamlit run app.py
```

Then open the URL above (or the one shown in the terminal) to browse the curriculum by day, view timetables, and access resources and supporting materials.

## How to Use This Curriculum

1. Review the overall plan in the main README
2. Each day has a detailed lesson plan with timing
3. Activities and projects are provided for hands-on learning
4. Assessment rubrics help track progress
5. Supporting materials facilitate workshop management

## Resources Needed

See `resources/procurement-guide.md` for detailed hardware and software requirements.

## Contact and Support

For questions or support, refer to the integration planning templates in `resources/templates/` and resource sharing guides in Day 5 materials.

