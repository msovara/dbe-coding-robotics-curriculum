# CHPC DSI Coding School Integration
## Mapping CHPC Training Materials to DBE Curriculum

This document integrates the [CHPC Training DSI Coding School](https://github.com/ChpcTraining/dsi_coding_school) repository content with the DBE Coding and Robotics Curriculum, providing cross-references and alignment between the two curricula.

**CHPC Repository:** https://github.com/ChpcTraining/dsi_coding_school  
**DBE Curriculum Repository:** https://github.com/msovara/dbe-coding-robotics-curriculum

---

## Overview

The CHPC DSI Coding School is a three-year flagship project (2022-2025) funded by the Department of Science and Innovation (DSI) to raise awareness of coding and robotics within the Department of Basic Education. This curriculum aligns with and complements that initiative.

---

## Repository Structure Mapping

### CHPC Repository Modules → DBE Curriculum Days

| CHPC Module | DBE Day | Integration Level | Notes |
|-------------|---------|-------------------|-------|
| **scratch/** | Day 1 | Direct Integration | CHPC Scratch materials complement Day 1 |
| **robotics/** | Day 2 | Direct Integration | CHPC robotics aligns with Arduino/S4A content |
| **cloud_computing/** | Day 3 | Direct Integration | CHPC cloud computing is primary reference |
| **computer_hardware/** | Day 4 | Direct Integration | CHPC hardware content aligns with Day 4 |
| **virtual_resources/** | Day 3, Day 5 | Supplementary | Virtual machines and cloud deployment |
| **codeclub/** | Day 1-5 | Supplementary | Additional activities and resources |
| **resources/** | All Days | Supplementary | General resources and materials |
| **presentations/** | All Days | Reference | Presentation materials for facilitators |

---

## Day-by-Day Integration

### Day 1: Introduction to Coding with Scratch

**CHPC Resources:**
- **Primary:** [CHPC Scratch Module](https://github.com/ChpcTraining/dsi_coding_school/tree/main/scratch)
- **Supplementary:** [CodeClub Resources](https://github.com/ChpcTraining/dsi_coding_school/tree/main/codeclub)

**Integration Points:**
- Use CHPC Scratch materials as additional examples
- Reference CHPC Scratch projects for inspiration
- Align computational thinking concepts
- Use CHPC presentation materials for teaching

**DBE Materials (Keep):**
- `day-01-scratch/lesson-plan.md` - Detailed DBE lesson plan
- `day-01-scratch/scratch-introduction-guide.md` - Teacher guide
- `day-01-scratch/activities/computational-thinking-exercises.md` - Activities
- `day-01-scratch/projects/project-templates.md` - Project templates
- `day-01-scratch/assessment/rubric.md` - Assessment framework

**How to Use:**
1. Start with DBE lesson plan structure
2. Supplement with CHPC Scratch examples
3. Use CHPC projects as extension activities
4. Reference CHPC presentations for visual aids

---

### Day 2: Physical Computing with Scratch for Arduino

**CHPC Resources:**
- **Primary:** [CHPC Robotics Module](https://github.com/ChpcTraining/dsi_coding_school/tree/main/robotics)
- **Reference:** CHPC Scratch for Arduino materials

**Integration Points:**
- Use CHPC robotics arm project as advanced example
- Reference CHPC Arduino/S4A setup procedures
- Align with CHPC robotics concepts
- Use CHPC presentation materials

**DBE Materials (Keep):**
- `day-02-arduino/lesson-plan.md` - Detailed DBE lesson plan
- `day-02-arduino/arduino-hardware-guide.md` - Hardware guide
- `day-02-arduino/s4a-setup-instructions.md` - Setup guide
- `day-02-arduino/activities/wiring-diagrams.md` - Wiring diagrams
- `day-02-arduino/projects/project-guides.md` - Project guides
- `day-02-arduino/assessment/rubric.md` - Assessment framework

**How to Use:**
1. Follow DBE lesson plan for structure
2. Reference CHPC robotics arm project (advanced)
3. Use CHPC materials for additional examples
4. Combine DBE wiring diagrams with CHPC projects

---

### Day 3: Cloud Computing Fundamentals

**CHPC Resources:**
- **Primary:** [CHPC Cloud Computing Module](https://github.com/ChpcTraining/dsi_coding_school/tree/main/cloud_computing)
- **Primary:** [CHPC Virtual Resources](https://github.com/ChpcTraining/dsi_coding_school/tree/main/virtual_resources)
- **Reference:** [Sebowa CHPC Cloud](https://github.com/ChpcTraining/dsi_coding_school/tree/main/cloud_computing) - Sebowa platform

**Integration Points:**
- CHPC cloud computing is the primary reference
- Sebowa cloud platform setup and usage
- Virtual machine creation (Windows for Scratch)
- Cloud deployment concepts

**DBE Materials (Keep):**
- `day-03-cloud/lesson-plan.md` - Detailed DBE lesson plan
- `day-03-cloud/CHPC_CLOUD_SETUP.md` - CHPC cloud setup reference
- `day-03-cloud/SEBOWA_GUIDE.md` - Sebowa platform guide
- `day-03-cloud/activities/cloud-platforms-guide.md` - Platforms guide
- `day-03-cloud/projects/data-visualization-templates.md` - Templates
- `day-03-cloud/assessment/rubric.md` - Assessment framework

**How to Use:**
1. Use CHPC cloud computing module as primary source
2. Follow DBE lesson plan for teacher-friendly structure
3. Reference Sebowa guide for CHPC-specific platform
4. Use CHPC virtual resources for VM setup
5. Combine DBE templates with CHPC examples

---

### Day 4: Computer and Arduino Hardware Deep Dive

**CHPC Resources:**
- **Primary:** [CHPC Computer Hardware Module](https://github.com/ChpcTraining/dsi_coding_school/tree/main/computer_hardware)

**Integration Points:**
- CHPC hardware disassembly/assembly procedures
- Component identification methods
- Hardware troubleshooting approaches
- Safety protocols

**DBE Materials (Keep):**
- `day-04-hardware/lesson-plan.md` - Detailed DBE lesson plan
- `day-04-hardware/troubleshooting-guide.md` - Troubleshooting guide

**How to Use:**
1. Follow CHPC hardware disassembly procedures
2. Use DBE lesson plan for educational context
3. Reference CHPC safety protocols
4. Combine DBE troubleshooting with CHPC methods

---

### Day 5: Integration, Assessment, and Capstone Project

**CHPC Resources:**
- **Reference:** All CHPC modules for integration examples
- **Supplementary:** [CHPC Resources](https://github.com/ChpcTraining/dsi_coding_school/tree/main/resources)
- **Reference:** [CHPC Presentations](https://github.com/ChpcTraining/dsi_coding_school/tree/main/presentations)

**Integration Points:**
- Use CHPC projects as capstone examples
- Reference CHPC assessment approaches
- Use CHPC resources for curriculum integration
- Access CHPC presentation materials

**DBE Materials (Keep):**
- `day-05-integration/lesson-plan.md` - Detailed DBE lesson plan
- `day-05-integration/resources/integration-planning-template.md` - Template

**How to Use:**
1. Use DBE integration planning template
2. Reference CHPC projects for capstone ideas
3. Combine DBE assessment strategies with CHPC approaches
4. Use CHPC resources for additional materials

---

## Key CHPC Concepts Integrated

### 1. Scratch Programming
**CHPC Focus:** Visual programming fundamentals, interactive projects  
**DBE Integration:** Day 1 - Foundation, Day 2 - Physical computing extension

### 2. Robotics with Scratch for Arduino
**CHPC Focus:** Robotic arm project, servo control, mechanics  
**DBE Integration:** Day 2 - Physical computing, Day 4 - Hardware deep dive

### 3. Cloud Computing and Virtual Resources
**CHPC Focus:** Sebowa cloud, virtual machines, cloud deployment  
**DBE Integration:** Day 3 - Cloud fundamentals, virtual resources

### 4. Computer Hardware
**CHPC Focus:** Disassembly, component identification, reassembly  
**DBE Integration:** Day 4 - Hardware deep dive, troubleshooting

### 5. Virtual Machines
**CHPC Focus:** Ubuntu on VirtualBox, Linux terminal, Windows VM for Scratch  
**DBE Integration:** Day 3 - Virtual resources, Day 5 - Extended learning

---

## Using Both Curricula Together

### For Workshop Facilitators

**Preparation:**
1. Review DBE lesson plans for structure
2. Access CHPC repository for technical details
3. Download CHPC presentations for visual aids
4. Prepare CHPC examples as extensions

**During Workshop:**
1. Follow DBE lesson plan timing and structure
2. Reference CHPC materials for technical depth
3. Use CHPC projects as advanced examples
4. Combine DBE activities with CHPC resources

**After Workshop:**
1. Share both repositories with teachers
2. Provide links to CHPC materials
3. Encourage exploration of CHPC content
4. Support integration of both approaches

### For Teachers

**Learning Path:**
1. Start with DBE curriculum (teacher-friendly)
2. Explore CHPC materials for technical depth
3. Use CHPC projects as inspiration
4. Combine approaches for classroom use

**Resource Access:**
- DBE Curriculum: https://github.com/msovara/dbe-coding-robotics-curriculum
- CHPC Training: https://github.com/ChpcTraining/dsi_coding_school
- Both repositories are complementary

---

## CHPC Repository Structure Reference

```
ChpcTraining/dsi_coding_school/
├── scratch/              → Day 1 Integration
├── robotics/             → Day 2 Integration
├── cloud_computing/      → Day 3 Primary Reference
├── computer_hardware/    → Day 4 Integration
├── virtual_resources/    → Day 3, Day 5 Supplementary
│   └── linux_os_install/ → Virtual machine setup
├── codeclub/             → All Days Supplementary
├── resources/            → All Days Reference
└── presentations/        → All Days Visual Aids
```

---

## Specific Integration Examples

### Example 1: Scratch Projects

**DBE Approach:**
- Teacher-friendly project templates
- Step-by-step instructions
- Assessment rubrics
- Curriculum integration focus

**CHPC Approach:**
- Technical Scratch projects
- Advanced concepts
- Research-oriented
- Community projects

**Combined Use:**
- Start with DBE templates (beginner-friendly)
- Progress to CHPC projects (advanced)
- Use both for differentiated instruction

### Example 2: Robotics

**DBE Approach:**
- Basic Arduino projects
- Simple sensors and actuators
- Classroom-friendly activities
- Educational focus

**CHPC Approach:**
- Robotic arm project
- Advanced servo control
- Mechanical assembly
- Research applications

**Combined Use:**
- DBE for foundational learning
- CHPC for advanced projects
- CHPC robotic arm as capstone

### Example 3: Cloud Computing

**DBE Approach:**
- General cloud concepts
- Educational platforms
- Teacher applications
- Student projects

**CHPC Approach:**
- Sebowa platform specifics
- Virtual machine setup
- Cloud deployment
- Technical implementation

**Combined Use:**
- DBE for concepts and applications
- CHPC for Sebowa platform setup
- CHPC for virtual machine creation

---

## Accessing CHPC Materials

### Direct Links

**Main Repository:**
- https://github.com/ChpcTraining/dsi_coding_school

**Specific Modules:**
- Scratch: https://github.com/ChpcTraining/dsi_coding_school/tree/main/scratch
- Robotics: https://github.com/ChpcTraining/dsi_coding_school/tree/main/robotics
- Cloud Computing: https://github.com/ChpcTraining/dsi_coding_school/tree/main/cloud_computing
- Computer Hardware: https://github.com/ChpcTraining/dsi_coding_school/tree/main/computer_hardware
- Virtual Resources: https://github.com/ChpcTraining/dsi_coding_school/tree/main/virtual_resources
- CodeClub: https://github.com/ChpcTraining/dsi_coding_school/tree/main/codeclub
- Resources: https://github.com/ChpcTraining/dsi_coding_school/tree/main/resources
- Presentations: https://github.com/ChpcTraining/dsi_coding_school/tree/main/presentations

### Downloading Materials

**Option 1: Clone Repository**
```bash
git clone https://github.com/ChpcTraining/dsi_coding_school.git
```

**Option 2: Download ZIP**
- Go to repository
- Click "Code" → "Download ZIP"
- Extract to local directory

**Option 3: Access Online**
- Browse repository on GitHub
- View files directly
- Download individual files as needed

---

## Best Practices for Integration

### 1. Start with DBE Structure
- Use DBE lesson plans as primary framework
- Follow DBE timing and pacing
- Maintain DBE educational focus

### 2. Supplement with CHPC Content
- Reference CHPC for technical details
- Use CHPC projects as extensions
- Access CHPC presentations for visuals

### 3. Maintain Both Approaches
- Keep DBE materials (teacher-friendly)
- Keep CHPC materials (technical depth)
- Use both as complementary resources

### 4. Customize for Context
- Adapt CHPC content for DBE context
- Simplify CHPC technical content for teachers
- Combine best of both approaches

---

## Workshop Timetable Alignment

### CHPC Timetable Structure
- 5 days (similar to DBE)
- Scratch, Robotics, Cloud, Hardware focus
- Virtual resources integration
- CodeClub activities

### DBE Timetable Structure
- 5 days (aligned with CHPC)
- Similar topics, teacher-focused
- Assessment and integration emphasis
- Curriculum alignment focus

### Combined Approach
- Use DBE timetable for structure
- Reference CHPC timetable for content depth
- Align sessions where topics overlap
- Maintain DBE timing (09:00-17:00)

---

## Assessment Integration

### DBE Assessment Approach
- Teacher-focused rubrics
- Curriculum integration assessment
- Pedagogical application evaluation
- Student learning outcomes

### CHPC Assessment Approach
- Technical skill evaluation
- Project completion assessment
- Research-oriented evaluation
- Advanced skill demonstration

### Combined Assessment
- Use DBE rubrics for teacher evaluation
- Reference CHPC projects for skill demonstration
- Combine both for comprehensive assessment
- Adapt CHPC assessments for educational context

---

## Resources and Support

### DBE Resources
- Teacher guides and templates
- Assessment rubrics
- Procurement guides
- Integration planning templates

### CHPC Resources
- Technical documentation
- Project examples
- Presentation materials
- CodeClub activities

### Combined Resources
- Access both repositories
- Use DBE for teaching materials
- Use CHPC for technical reference
- Combine for comprehensive support

---

## Version Compatibility

### CHPC Repository
- **Status:** Active (2022-2025 project)
- **Updates:** Regular updates expected
- **Version:** Check repository for latest

### DBE Curriculum
- **Status:** Active development
- **Version:** 1.0
- **Last Updated:** 2024

### Compatibility
- Both curricula are complementary
- CHPC provides technical depth
- DBE provides educational structure
- Use both together for best results

---

## Contributing and Feedback

### CHPC Repository
- Managed by CHPC Training team
- Part of DSI-funded project
- Contact CHPC for contributions

### DBE Curriculum
- Managed by curriculum developers
- Open for teacher feedback
- Continuous improvement

### Integration Feedback
- Share integration experiences
- Suggest improvements
- Report issues
- Contribute examples

---

## Quick Reference

### When to Use DBE Materials
- Lesson planning and structure
- Teacher training and support
- Curriculum integration
- Assessment and evaluation
- Classroom management

### When to Use CHPC Materials
- Technical implementation details
- Advanced project examples
- Platform-specific setup (Sebowa)
- Virtual machine configuration
- Research-oriented content

### When to Use Both
- Comprehensive training
- Differentiated instruction
- Advanced teacher development
- Extended learning opportunities
- Complete resource library

---

## Conclusion

The CHPC DSI Coding School and DBE Coding and Robotics Curriculum are complementary resources that work together to provide comprehensive coding and robotics education for South African teachers. Use both repositories to access the full range of materials, from teacher-friendly guides to technical implementation details.

**Remember:**
- DBE materials = Educational structure and teacher support
- CHPC materials = Technical depth and advanced content
- Both together = Comprehensive training program

---

**Last Updated:** 2024  
**Version:** 1.0

**References:**
- CHPC DSI Coding School: https://github.com/ChpcTraining/dsi_coding_school
- DBE Coding and Robotics Curriculum: https://github.com/msovara/dbe-coding-robotics-curriculum

