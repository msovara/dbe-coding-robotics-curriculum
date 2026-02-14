# Robotics and Coding Activities
## Day 3 Hands-On Activities

These activities support the Day 3 lesson plan: extended Arduino concepts, multi-sensor projects, and simple robotics applications.

---

## Activity 1: Multi-Sensor Decision-Making

### Objective
Combine at least two inputs (e.g. light sensor + button) to control an output using conditions and variables.

### Prerequisites
- S4A connected; Arduino with at least one analog sensor and one digital input (e.g. button) wired (see Day 2 wiring diagrams).
- Optional: second sensor (e.g. second light sensor or temperature).

### Instructions
1. **Wire the circuit:** One analog sensor (e.g. photoresistor on A0), one button (e.g. digital pin 2), one or two LEDs (e.g. pins 13 and 12).
2. **Create variables:** e.g. `lightLevel` (from analog pin), `threshold` (number you choose).
3. **Logic:** When button is pressed, read light sensor. If `lightLevel` &gt; `threshold`, turn on LED 1; else turn on LED 2 (or different pattern).
4. **Test:** Change threshold; discuss how the “decision” changes.

### Discussion Questions
- How did using two inputs change the behaviour compared to one sensor?
- Where could this kind of logic be used in a real project (e.g. automatic light, security)?

### Extension
- Add a second sensor and use both in one condition (e.g. “if light low AND button pressed”).
- Use a variable to count how many times the button was pressed and change behaviour after N presses.

---

## Activity 2: Sequence with Timing (Traffic Light or Step-by-Step Robot)

### Objective
Use loops and “wait” blocks to create a timed sequence (e.g. traffic light: red → amber → green, or a simple “robot” sequence: move → pause → turn → move).

### Instructions
1. **Choose outputs:** e.g. three LEDs (red, amber, green) on three pins, or one servo.
2. **Plan the sequence:** Write the order and approximate times (e.g. red 3 s, amber 1 s, green 3 s).
3. **Code in S4A:** Use “turn pin on” / “turn pin off” and “wait X secs” in a “forever” or “repeat” loop.
4. **Run and refine:** Adjust times; add a button to “start” the sequence if desired.

### Discussion
- How is this like a simple “program” for a robot (do step 1, wait, do step 2, …)?
- What other sequences could be useful in the classroom (e.g. science experiment steps, timer)?

### Extension
- Add a sensor to start the sequence only when something is detected (e.g. when light drops).
- Use a variable as a “state” (1 = red, 2 = amber, 3 = green) and change it in a loop.

---

## Activity 3: Simple “Follow the Light” or “React to Distance” Behaviour

### Objective
Implement a simple robotic behaviour: change an output (e.g. LED or servo) based on sensor input in a continuous loop.

### Option A: Follow the Light (one sensor)
- **Input:** One light sensor (analog).
- **Output:** LED brightness or servo angle based on light level (e.g. map analog value to LED or servo).
- **Logic:** In “forever,” read sensor, set output; repeat.

### Option B: React to Distance (ultrasonic if available)
- **Input:** Distance sensor (if in kit).
- **Output:** LED or buzzer: e.g. if distance &lt; 20 cm, turn on “warning” LED.
- **Logic:** In “forever,” read distance, use “if … then … else …” to set output.

### Instructions
1. Wire the sensor and output (refer to Day 2 wiring diagrams and project guides).
2. In S4A, create a “forever” loop that reads the sensor and updates the output.
3. Calibrate: note the range of sensor values and choose thresholds.
4. Test and describe the “behaviour” in words (e.g. “When it gets dark, the LED gets brighter”).

### Discussion
- How does this compare to a “robot” that reacts to its environment?
- What other behaviours could you design with the same components?

### Extension
- Use two light sensors (left/right) and a servo or two LEDs to “point” toward the brighter side (concept of light-following robot).

---

## Activity 4: Project Planning – From Idea to Circuit and Code

### Objective
Practice breaking a robotics/coding idea into: inputs, outputs, logic, and steps.

### Instructions
1. **Choose a scenario** (e.g. “Night light,” “Plant water reminder,” “Reaction game with LED and button,” “Simple alarm”).
2. **Fill in:**
   - **Behaviour:** One sentence: “The system will …”
   - **Inputs:** List sensors/buttons.
   - **Outputs:** List LEDs, servos, buzzers, etc.
   - **Logic (in words):** “When … then …”
3. **Sketch:** Simple diagram of components and pins (or list pins).
4. **Implement:** If time, build and code one of the plans; otherwise swap plans with a partner and give feedback.

### Discussion
- Why is planning before building helpful?
- How would you use this planning process with learners in class?

---

## Notes for Facilitators

- Ensure all participants have a working S4A setup from Day 2 before starting.
- If components are limited, some activities can be done in pairs or small groups.
- Refer to [resources/hardware](../resources/hardware/) for troubleshooting and to [day-02-arduino](../day-02-arduino/) for wiring and S4A details.
- Link each activity to the Day 3 lesson plan sessions (review, coding projects, robotics applications, project development).
