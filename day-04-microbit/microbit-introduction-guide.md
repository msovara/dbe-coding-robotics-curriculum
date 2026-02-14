# Micro:bit Introduction Guide
## Day 4 – A Teacher's Guide to Coding & Robotics with Micro:bit

This guide supports Day 4 of the DBE Coding and Robotics workshop. It introduces the Micro:bit hardware and the MakeCode editor so you can run Micro:bit activities in your classroom.

**Prerequisites:** Days 1–3 (Scratch and Arduino experience helpful but not required).  
**Platform:** [MakeCode for Micro:bit](https://makecode.microbit.org/) (free, runs in browser).

---

## What is the Micro:bit?

The Micro:bit is a small, programmable computer designed for education. It has:

- **25 programmable LEDs** in a 5×5 grid (output and display)
- **Two buttons** (A and B) for input
- **Built-in sensors:** accelerometer (tilt, shake), compass (direction), temperature (on-chip)
- **Edge connector / pins** to connect external components (motors, buzzers, extra sensors)
- **USB** for connecting to a computer to program and power it
- **Battery option** (2× AAA in a battery pack) for portable use

**Why use it in schools?**
- Low cost and robust
- Block-based (MakeCode) and text-based (Python) options
- Strong curriculum links (coding, technology, science, maths)
- Works in the browser; no installation required for MakeCode
- Many free projects and lesson ideas online

---

## MakeCode Editor

### Getting Started

1. **Open:** [makecode.microbit.org](https://makecode.microbit.org/)
2. **New project:** Click “New Project” and name it (e.g. “First Program”).
3. **Interface:**
   - **Left:** Block categories (Input, Logic, Loops, etc.) – similar to Scratch
   - **Centre:** Coding area where you drag blocks
   - **Right:** Simulator – shows a virtual Micro:bit; you can test without hardware
4. **First program:** From “Basic,” drag “show leds” and draw a pattern. Click the pattern to toggle LEDs. Run in the simulator.

### Key Block Categories (for Day 4)

- **Basic:** show leds, show number, show string, pause, clear screen
- **Input:** on button A/B pressed, on shake, on pin pressed, temperature, light level, compass heading, acceleration
- **Logic:** if-then-else, comparison (&lt;, &gt;, =), and/or/not
- **Loops:** repeat, forever
- **Variables:** set, change
- **LED:** plot x y, unplot, toggle (for more control than “show leds”)
- **Pins:** digital write/read, analog write/read (for external components)
- **Radio:** (Day 5) send number/string, on received – for Micro:bit-to-Micro:bit communication

---

## From Screen to Device: Downloading and Flashing

1. **Connect** the Micro:bit to the computer with a USB cable. It may appear as a drive (e.g. MICROBIT).
2. **Download:** In MakeCode, click “Download” (bottom left). A `.hex` file is saved.
3. **Flash:** Copy the `.hex` file to the MICROBIT drive (drag and drop, or “Save as” to the drive). The Micro:bit LED will blink; when it stops, the program is loaded.
4. **Run:** The program starts automatically. Buttons A and B work on the device; the simulator does not control the physical Micro:bit.

### Troubleshooting

- **Micro:bit not appearing:** Try another USB cable/port; ensure it’s a data cable, not charge-only.
- **Download doesn’t run on device:** Ensure the full file was copied and the drive was safely ejected.
- **Wrong program on device:** Re-download the correct project and copy to the Micro:bit again (new program replaces the previous one).

---

## Inputs and Outputs – Quick Reference

| Type    | Examples in MakeCode |
|--------|------------------------|
| **Buttons** | `on button A pressed` → do something |
| **Sensors** | `temperature`, `light level`, `compass heading`, `acceleration` |
| **LED grid** | `show leds`, `show number`, `show string`, `plot x y` |
| **Pins**   | `digital write pin P0 to 1`, `analog read pin P0` (for buzzers, servos, external LEDs) |

---

## Managing Micro:bits in the Classroom

- **Storage:** Label each Micro:bit (e.g. number or name) and store in a box or tray; same for USB cables and battery packs.
- **Pairing:** Micro:bits remember the last program; if learners swap devices, they may get a different program until you re-flash.
- **Sharing:** One Micro:bit per pair is often enough; rotate who downloads and who holds the device.
- **Simulator first:** If devices are limited, do most of the coding in the simulator, then rotate who flashes to the real Micro:bit.
- **Saving work:** Save MakeCode projects (name them); download and keep `.hex` files if you want to re-use the same program later.

---

## Links to DBE and Curriculum

- **Technology / Coding:** Algorithms, sequencing, inputs and outputs, debugging.
- **Mathematics:** Numbers, coordinates (LED grid), variables, conditions.
- **Science:** Sensors (temperature, light), data logging (concept), experimentation.
- **Life Orientation / STEM:** Problem-solving, collaboration, design of solutions.

---

## Next Steps (Day 5)

Day 5 extends Micro:bit with radio, variables, and one larger project, then introduces Code Club and a mini Code Club session. Use this guide as reference when planning your first Micro:bit lessons or club sessions.

---

**Last updated:** For use with DBE Coding and Robotics Curriculum, Day 4.
