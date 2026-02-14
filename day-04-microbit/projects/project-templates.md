# Micro:bit Project Templates
## Day 4 Project Ideas and Step-by-Step Outlines

Use these as classroom-ready project ideas for Micro:bit Part 1. Each can be adapted for time and ability.

---

## Project 1: Name Badge (Beginner)

**Time:** 15–25 minutes  
**Learning objectives:** show leds, show string, on start, optional: button to switch message

### Steps
1. **New project** in MakeCode; name it “Name Badge”.
2. **on start:** Add **show leds** and draw a simple pattern (e.g. smiley or star). Add **show string** and type your name (or “Hello, I’m [Name]”).
3. **Test in simulator.** Adjust pattern or text if needed.
4. **Optional:** Add **on button A pressed** → **show string** "Coding!" and **on button B pressed** → **show string** "[Your name]". So: start shows pattern + name; A shows “Coding!”; B shows name again.
5. **Download** and flash to Micro:bit. Wear as a badge or display on desk.

### Extensions
- Add a second language (e.g. “Hello” and “Sawubona” on different buttons).
- Use **show icon** for a favourite animal or subject.
- In class: learners design their own badge and share with a partner.

---

## Project 2: Dice (Beginner–Intermediate)

**Time:** 20–30 minutes  
**Learning objectives:** on button pressed, random numbers, variables (optional)

### Steps
1. **New project** “Dice”.
2. **on button A pressed:** Add **show number** and **pick random 1 to 6**. Add **pause 200** so the number is visible.
3. **Test in simulator:** Click A several times; you should see numbers 1–6.
4. **Optional – score:** Create variable **score**. **on start** set **score** to 0. When A pressed: **change score by** **pick random 1 to 6**, then **show number** **score**. **on button B pressed** → **show number** **score** (show total) or set **score** to 0 (reset).
5. **Download** and flash. Use as a real dice for a board game or maths activity.

### Extensions
- Two dice: A = first die (1–6), B = second die (1–6); learners add them for maths.
- **show leds** to draw dice faces (1–6 dots) instead of numbers.
- Link to probability in maths (how often does 6 appear?).

---

## Project 3: Step Counter (Intermediate)

**Time:** 25–35 minutes  
**Learning objectives:** on shake (or gesture), variables, show number, reset

### Steps
1. **New project** “Step Counter”.
2. Create variable **steps**. **on start** set **steps** to 0.
3. **on shake:** **change steps by 1**, then **show number** **steps** (briefly). Or use **on gesture tilt left** (or **freefall** / **logo up**) if you want a different trigger.
4. **on button A pressed:** **show number** **steps** (display current count).
5. **on button B pressed:** set **steps** to 0 and **show string** "Reset".
6. **Test:** Shake (or tilt) a few times, press A to see count, press B to reset.
7. **Download** and flash. Discuss: real step counters use similar ideas (accelerometer data).

### Extensions
- Add a simple goal: if **steps** ≥ 10, **show icon** (e.g. happy) and play a sound if available.
- Compare with a real pedometer or phone step counter; discuss accuracy and calibration.

---

## Project 4: Light Meter / Dark Detector (Intermediate)

**Time:** 20–30 minutes  
**Learning objectives:** light level (sensor), conditions, repeat/forever

### Steps
1. **New project** “Light Meter”.
2. **forever:** **show number** **light level** and **pause 500**. Run in simulator (use light slider) or on device (cover and uncover the Micro:bit).
3. **Improve:** Use **if** **light level** **&lt;** **50** **then** **show icon** (moon) **else** **show icon** (sun). So: dark = moon, light = sun.
4. **Optional:** Three levels: dark (moon), medium (cloud?), bright (sun) using **if – else if – else**.
5. **Download** and flash. Use to compare “dark” in different places (under desk, by window).

### Extensions
- **show number** for light level when button A pressed (so screen isn’t always changing).
- Link to science: light and plants, or data logging (concept – we could record values).

---

## Project 5: Simple Robot “Brain” (Concept + Optional Pins)

**Time:** 20–40 minutes (depending on hardware)  
**Learning objectives:** Pins (optional), planning inputs and outputs, robotics idea

### Steps
1. **Discussion:** What should our “robot” do? Example: “When I press A, it goes; when I press B, it stops.” Or: “When it’s dark, show a light; when it’s bright, turn off.”
2. **In MakeCode:** Implement the “brain” part:
   - **on button A pressed** → e.g. **show icon** "go" or set variable **running** to 1.
   - **on button B pressed** → **show icon** "no" or set **running** to 0.
   - If using pins: **digital write pin P0 to 1** when “go”, **digital write pin P0 to 0** when “stop” (for a motor driver or LED).
3. **Test in simulator** (and on device if you have motor/LED on P0).
4. If you have a buggy/robot kit: follow kit instructions to connect Micro:bit and run this program.
5. **Plan for class:** List what you’d need (Micro:bits, batteries, buggy kits, time) to do this with learners.

### Extensions
- Add a sensor: e.g. “when light level &lt; 30, go (night mode); when light &gt; 200, stop.”
- Build a cardboard “robot” that holds the Micro:bit and discuss where motors or LEDs would go.

---

## General Tips

- **Simulator first:** Always run in the simulator before flashing; saves time and device use.
- **Names:** Save projects with clear names (e.g. “Dice – Maths Grade 4”) so you can reuse them.
- **Differentiation:** Name badge and Dice for beginners; Step counter and Light meter for intermediate; Robot brain for those ready for pins and planning.
- **DBE links:** Technology (inputs/outputs, algorithms), Maths (numbers, random, data), Science (sensors, light, temperature).
