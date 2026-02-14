# Micro:bit Activities
## Day 4 Hands-On Activities

These activities support the Day 4 lesson plan: introduction to Micro:bit, MakeCode, inputs and outputs, and flashing programs to the device.

---

## Activity 1: First Program – LED Pattern and Message

### Objective
Use the MakeCode simulator to display a pattern and scrolling text on the 5×5 LED grid.

### Instructions
1. Open [makecode.microbit.org](https://makecode.microbit.org/) and start a new project.
2. From **Basic**, drag **on start** and **show leds**. Click the grid to draw a simple pattern (e.g. heart, smiley, initial letter).
3. Add **show string** "Hello" (or your name). Run in the simulator: you should see the pattern, then the scrolling text.
4. Optional: put **show leds** inside **forever** and add **pause 500** and a second pattern so it alternates.
5. If you have a Micro:bit: **Download** the `.hex` file and copy it to the MICROBIT drive. Check that the same program runs on the device.

### Discussion Questions
- How is this similar to or different from Scratch (blocks, stage, output)?
- What would you change to make a “name badge” for a learner?

### Extension
- Use **show number** with a variable that increases in a loop (simple counter).
- Use **plot x y** and **unplot x y** to animate one LED moving across the grid.

---

## Activity 2: Buttons A and B – Events and Program Flow

### Objective
Use **on button A pressed** and **on button B pressed** to trigger different actions (events).

### Instructions
1. New project (or new tab). Add **on button A pressed** and **show string** "A".
2. Add **on button B pressed** and **show string** "B".
3. Run in simulator: click A and B on the virtual Micro:bit and see the messages.
4. Add **on button A+B pressed** and **show icon** (e.g. heart). Discuss: when do we use “both buttons”?
5. Try: **on button A pressed** → **show number** and use **pick random 1 to 6** to make a dice. Run several times.
6. Flash to device if available; test with real buttons.

### Discussion
- How are “on button pressed” blocks like “when green flag” or “when key pressed” in Scratch?
- What other “events” does the Micro:bit have? (shake, pin pressed, etc.)

### Extension
- Dice game: press A to roll, show number 1–6; use variable to count total score and show it when B is pressed.
- Two-player: use A for “player 1 roll” and B for “player 2 roll”; compare numbers.

---

## Activity 3: Sensors – Light, Temperature, Tilt

### Objective
Read built-in sensors and show values or use them in conditions.

### Instructions
1. **Light:** From **Input**, use **light level** (0–255). In **forever**, **show number** **light level** and **pause 500**. Run in simulator (use the light slider) or on device (cover the Micro:bit to see value change).
2. **Temperature:** Use **temperature** in the same way. Discuss: this is the chip temperature, not always room temperature, but it changes with environment.
3. **Tilt / accelerometer:** Use **on shake** → **show icon** or **show string** "Shake!". Try **acceleration (mg)** in **forever** with **show number** to see values change when you tilt.
4. **Condition:** Use **if** **light level** **&lt;** **50** **then** **show leds** (dark pattern) **else** **show leds** (bright pattern). Run and test.

### Discussion
- How could we use the light sensor in a “night light” or “sunshine detector”?
- How could tilt or shake be used in a game or a “step counter” idea?

### Extension
- Simple step counter (concept): on shake, add 1 to variable `steps`, then show `steps` when button A is pressed. Reset when B is pressed.
- Thermometer: show temperature and show different icons for “cold” / “warm” / “hot” using if-else.

---

## Activity 4: From Screen to Device – Download and Troubleshoot

### Objective
Practice downloading a project and flashing it to a Micro:bit; list common issues and fixes.

### Instructions
1. Finish any small program (e.g. button A = dice, button B = show score).
2. Click **Download** in MakeCode. Locate the `.hex` file.
3. Connect Micro:bit via USB. When the MICROBIT drive appears, copy the `.hex` file onto it.
4. Wait for the yellow LED on the back to stop flashing. Press reset if needed. Test the program.
5. As a group, list: What can go wrong? (cable, drive not appearing, wrong file, need to eject safely.) Write a short “troubleshooting” list for your class.

### Discussion
- Why is it important to test on the real device as well as the simulator?
- How will you manage one Micro:bit shared by two or more learners (turns, saving projects with names)?

### Extension
- Save the project with a clear name (e.g. “Dice Game – [Your name]”). Download again and keep the `.hex` for reuse.
- Try a second project (e.g. name badge); flash it to the same Micro:bit and note that it replaces the previous program.

---

## Activity 5: Micro:bit and Robotics Ideas (Concept and Optional Pins)

### Objective
Discuss how the Micro:bit could be the “brain” of a simple robot; optionally use pins for an external output.

### Instructions
1. **Discussion:** What could we connect to the Micro:bit to make something move or make sound? (Small motor, servo, buzzer – often via pins.)
2. **In MakeCode:** Open **Pins**. Use **digital write pin P0 to 1** and **digital write pin P0 to 0** in a loop or with a button. (If you have a buzzer or LED on P0 and GND, you can test on device.)
3. **Plan:** In pairs, sketch or describe a “simple robot” that uses the Micro:bit: what would it sense (buttons, tilt, light)? What would it do (show LEDs, move, beep)? One sentence: “Our robot will …”
4. Share one idea with the group. Note which ideas need only the Micro:bit and which need extra components (motors, buggy kit, etc.).

### Discussion
- How is the Micro:bit like the “brain” and the motors/LEDs like “body”?
- What would you need to run this as a classroom project (time, kit, space)?

### Extension
- If you have a Micro:bit buggy or robot kit, follow its instructions to connect and run a simple “forward/back” program from MakeCode.
- Research one Micro:bit robotics project online and summarise it for the group (e.g. cardboard robot, buggy, arm).

---

## Notes for Facilitators

- If Micro:bits are limited, use the simulator for most activities and rotate who flashes to the device.
- Emphasise naming and saving projects so teachers can reuse them.
- Link each activity to the Day 4 sessions: Introduction (Activity 1), Inputs and Outputs (2–3), From Screen to Device (4), Robotics Ideas (5).
- Day 5 will extend with radio, variables, and Code Club; avoid going too deep into radio or complex logic here unless time allows.
