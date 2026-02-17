# Arduino Coding & Robotics Guide
## Day 3 – Extending Physical Computing to Robotics

This guide supports Day 3 of the DBE Coding and Robotics workshop. It extends the Arduino basics covered in Day 3 and focuses on more complex projects, multi-sensor integration, and simple robotics applications.

**Prerequisites:** Completion of Days 1-2 (Scratch) and Day 3 Arduino basics (S4A setup, first projects).  
**Reference:** [resources/hardware](../resources/hardware/) for troubleshooting and hardware deep-dive.

---

## What We Build On (Day 2 Recap)

- **S4A:** Scratch for Arduino – block-based control of Arduino pins
- **Digital I/O:** Turn outputs on/off (e.g. LEDs), read buttons
- **Analog input:** Read sensors (light, temperature, distance)
- **Actuators:** Servos, motors (basic control)
- **Control structures:** Loops, conditions, variables in Scratch blocks

---

## Day 3 Focus: From Coding to Robotics

### Key Ideas

1. **Multi-sensor projects** – Combine two or more inputs to make decisions (e.g. light and button, distance and LED).
2. **Variables and logic** – Use variables for thresholds, counters, and state; use conditions for decision-making.
3. **Sequences and timing** – Use loops and wait blocks to create sequences (e.g. traffic light, step-by-step robot behaviour).
4. **Robotics behaviours** – Simple “behaviours” such as: follow light, react to distance, avoid obstacles (conceptually with sensors and motors/servos).

### Why This Matters for Classrooms

- Links to DBE Technology and coding outcomes
- Reusable project ideas (science, maths, technology)
- Low-cost robotics without full robot kits (Arduino + a few components)
- Builds on equipment many schools already have (Arduino from Day 2)

---

## Planning a Robotics/Coding Project

### Steps

1. **Define the behaviour** – What should the “robot” or system do? (e.g. “When it’s dark, turn on a light.”)
2. **List inputs** – Which sensors? (light, distance, button, etc.)
3. **List outputs** – Which actuators or indicators? (LEDs, servo, motor, buzzer)
4. **Plan the logic** – In words or pseudocode: “If sensor &gt; X then do Y.”
5. **Wire and code** – Build the circuit, then implement in S4A.
6. **Test and iterate** – Try it, fix wiring or logic, improve.

### Example: “Light Follower” Idea

- **Input:** Light sensor (e.g. photoresistor on analog pin).
- **Output:** Two LEDs or a servo (e.g. “point” toward light).
- **Logic:** If left sensor &gt; right sensor, turn “left”; else turn “right”; repeat.

---

## Using Variables and Logic in S4A

- **Variables:** Create variables for sensor readings, thresholds, counters. Use “set [variable] to (value)” and “change [variable] by (value)”.
- **Conditions:** Use “if &lt;condition&gt; then … else …” with comparison blocks (e.g. “analog pin 0 &gt; 500”).
- **Loops:** Use “forever” or “repeat” to keep reading sensors and updating outputs.
- **Timing:** Use “wait” blocks to create delays and sequences.

---

## Motors and Servos (Recap and Extension)

- **Servo:** Often connected to a digital pin; in S4A use “set servo on pin X to (angle)” (e.g. 0–180).
- **Motor:** May need a motor driver or transistor; control with digital on/off or PWM if supported.
- **Safety:** Check wiring (no short circuits); ensure power is correct for motors.

For detailed wiring and troubleshooting, see [resources/hardware](../resources/hardware/) (e.g. troubleshooting-guide.md).

---

## CHPC and Further Resources

- **CHPC Robotics Module:** [CHPC DSI Coding School – robotics](https://github.com/ChpcTraining/dsi_coding_school/tree/main/robotics) for advanced projects (e.g. robotic arm).
- **DBE Day 3 materials:** [day-03-arduino](../day-03-arduino/) for wiring diagrams, project guides, and S4A setup.

---

## Quick Reference

| Topic            | Where to look                          |
|------------------|----------------------------------------|
| S4A setup         | day-02-arduino/s4a-setup-instructions.md |
| Wiring diagrams   | day-02-arduino/activities/wiring-diagrams.md |
| Project ideas     | day-03-arduino/projects/project-guides.md |
| Troubleshooting   | resources/hardware/troubleshooting-guide.md |

---

**Last updated:** For use with DBE Coding and Robotics Curriculum, Day 3.
