# Wiring Diagrams for Day 2 Projects
## Visual Guides for Building Circuits

## Diagram Legend

```
Symbols:
[LED]     - Light Emitting Diode
[R]       - Resistor
[BTN]     - Button/Switch
[PHOTO]   - Photoresistor
[TEMP]    - Temperature Sensor
[SERVO]   - Servo Motor
[BUZZ]    - Buzzer
[ARDUINO] - Arduino Uno Board
```

**Colors:**
- Red: Power (5V)
- Black: Ground (GND)
- Green/Blue: Signal wires
- Orange: PWM/Servo control

---

## Project 1: Blinking LED

### Components
- 1x LED (any color)
- 1x 220Ω resistor
- Jumper wires
- Breadboard

### Wiring Diagram

```
Arduino Pin 13 ──[220Ω]──[LED +]──[LED -]── GND
```

### Breadboard Layout

```
     Arduino          Breadboard
     ───────          ─────────
Pin 13 ────────────── a1
                      |
                     [R 220Ω]
                      |
                      b1 ────[LED +]
                      |
                      c1 ────[LED -]────── GND
```

### Steps
1. Insert 220Ω resistor from Arduino pin 13 to breadboard row
2. Insert LED (long leg = +) in same row as resistor
3. Connect LED short leg to GND
4. Connect Arduino GND to breadboard ground rail

---

## Project 2: Button Control

### Components
- 1x Button/Switch
- 1x 10kΩ resistor (pull-down)
- 1x LED
- 1x 220Ω resistor (for LED)
- Jumper wires
- Breadboard

### Wiring Diagram

```
        5V ────[BTN]──── Digital Pin 2
                      │
                   [10kΩ]
                      │
                     GND

Digital Pin 13 ──[220Ω]──[LED +]──[LED -]── GND
```

### Breadboard Layout

```
     Arduino          Breadboard
     ───────          ─────────
5V ────────────────── + rail
                      |
                      a5 ────[BTN]──── a10
                      |                |
                     [R 10kΩ]         |
                      |                |
                      b5 ───────────── b10 ──── GND

Pin 2 ─────────────── c10

Pin 13 ────────────── d1
                      |
                     [R 220Ω]
                      |
                      e1 ────[LED +]
                      |
                      f1 ────[LED -]────── GND
```

### Steps
1. Connect button: 5V → one side, other side → Pin 2
2. Add 10kΩ pull-down: Pin 2 → Resistor → GND
3. Add LED circuit: Pin 13 → 220Ω → LED → GND

---

## Project 3: Multiple LEDs Light Show

### Components
- 3x LEDs (different colors)
- 3x 220Ω resistors
- Jumper wires
- Breadboard

### Wiring Diagram

```
Pin 13 ──[220Ω]──[LED1]── GND
Pin 12 ──[220Ω]──[LED2]── GND
Pin 11 ──[220Ω]──[LED3]── GND
```

### Breadboard Layout

```
     Arduino          Breadboard
     ───────          ─────────
Pin 13 ────────────── a1 ──[R]── b1 ──[LED1]── c1 ── GND
Pin 12 ────────────── a5 ──[R]── b5 ──[LED2]── c5 ── GND
Pin 11 ────────────── a9 ──[R]── b9 ──[LED3]── c9 ── GND
```

### Steps
1. Connect each LED to different digital pin
2. Each LED needs its own 220Ω resistor
3. All LED cathodes connect to common GND

---

## Project 4: Light Sensor

### Components
- 1x Photoresistor
- 1x 10kΩ resistor
- 1x LED
- 1x 220Ω resistor (for LED)
- Jumper wires
- Breadboard

### Wiring Diagram

```
5V ────[PHOTO]──── Analog Pin A0
            │
         [10kΩ]
            │
           GND

Digital Pin 13 ──[220Ω]──[LED]── GND
```

### Breadboard Layout

```
     Arduino          Breadboard
     ───────          ─────────
5V ────────────────── + rail
                      |
                      a1 ────[PHOTO]──── a5
                      |                  |
A0 ─────────────────── b1               b5 ────[R 10kΩ]─── c5 ──── GND

Pin 13 ────────────── d10 ──[R 220Ω]── e10 ──[LED]── f10 ──── GND
```

### Steps
1. Create voltage divider: 5V → Photoresistor → A0 → 10kΩ → GND
2. Add LED output: Pin 13 → 220Ω → LED → GND
3. More light = higher A0 value
4. Less light = lower A0 value

---

## Project 5: Temperature Sensor

### Components
- 1x TMP36 temperature sensor
- 1x LED (for indicator)
- 1x 220Ω resistor (for LED)
- Optional: Buzzer
- Jumper wires
- Breadboard

### Wiring Diagram

```
TMP36:
Left Pin (facing flat side)  ──── 5V
Center Pin                   ──── Analog Pin A0
Right Pin                    ──── GND

Digital Pin 13 ──[220Ω]──[LED]── GND
```

### Breadboard Layout

```
     Arduino          Breadboard
     ───────          ─────────
5V ────────────────── + rail ──── a1 (TMP36 left)
                      |
A0 ─────────────────── b2 (TMP36 center)
                      |
GND ────────────────── - rail ──── c3 (TMP36 right)

Pin 13 ────────────── d10 ──[R 220Ω]── e10 ──[LED]── f10 ──── GND
```

### Steps
1. Insert TMP36: Flat side facing you
   - Left pin → 5V
   - Center pin → A0
   - Right pin → GND
2. Add LED indicator: Pin 13 → 220Ω → LED → GND
3. Temperature formula: (A0 reading × 0.488) - 50

---

## Project 6: Servo Motor

### Components
- 1x Servo motor (standard)
- Jumper wires
- Optional: External 5V power supply

### Wiring Diagram

```
Servo:
Red Wire    ──── 5V
Black/Brown ──── GND
Orange/Yellow ──── Digital Pin 9 (PWM)
```

### Breadboard Layout

```
     Arduino          Breadboard
     ───────          ─────────
5V ────────────────── + rail ──── Servo Red
                      |
GND ────────────────── - rail ──── Servo Black
                      |
Pin 9 ──────────────── Servo Orange
```

### Steps
1. Connect servo power: Red → 5V, Black → GND
2. Connect control: Orange → Pin 9 (PWM pin)
3. For multiple servos or high load, use external power

**External Power (Optional):**
```
External 5V ──── Servo Red
External GND ──── Servo Black
                  Arduino GND ──── External GND (common ground)
Pin 9 ─────────── Servo Orange
```

---

## Project 7: Smart Plant Monitor

### Components
- 1x Moisture sensor (or DIY)
- 1x Photoresistor
- 1x TMP36 temperature sensor
- 3x LEDs (Green, Yellow, Red)
- 3x 220Ω resistors
- 1x Buzzer
- Jumper wires
- Breadboard

### Wiring Diagram

```
Moisture Sensor ──── Analog Pin A0
Photoresistor ────── Analog Pin A1
TMP36 ────────────── Analog Pin A2

Digital Pin 13 ──[220Ω]──[LED Green]── GND
Digital Pin 12 ──[220Ω]──[LED Yellow]── GND
Digital Pin 11 ──[220Ω]──[LED Red]── GND
Digital Pin 10 ────────────[BUZZER]── GND
```

### Breadboard Layout

```
     Arduino          Breadboard
     ───────          ─────────
A0 ─────────────────── Moisture Sensor
A1 ─────────────────── Photoresistor (with voltage divider)
A2 ─────────────────── TMP36 Center Pin

Pin 13 ────────────── [R]──[LED Green]── GND
Pin 12 ────────────── [R]──[LED Yellow]── GND
Pin 11 ────────────── [R]──[LED Red]── GND
Pin 10 ────────────── [BUZZER]── GND
```

### Steps
1. Connect all sensors to analog pins
2. Connect each LED to different digital pin with resistor
3. Connect buzzer to digital pin
4. Code logic:
   - Green: Good conditions
   - Yellow: Warning
   - Red: Alert + buzzer

---

## Project 8: Security System

### Components
- 1x PIR motion sensor (or button for simulation)
- 1x Photoresistor
- 1x Buzzer
- 2x LEDs (Red, Green)
- 2x 220Ω resistors
- 1x Servo motor
- Jumper wires
- Breadboard

### Wiring Diagram

```
PIR Motion Sensor:
VCC ──── 5V
OUT ──── Digital Pin 2
GND ──── GND

Photoresistor ──── Analog Pin A0 (with voltage divider)

Digital Pin 13 ──[220Ω]──[LED Green]── GND
Digital Pin 12 ──[220Ω]──[LED Red]── GND
Digital Pin 11 ────────────[BUZZER]── GND
Digital Pin 9 ───────────── Servo Orange
Servo Red ──── 5V
Servo Black ──── GND
```

### Breadboard Layout

```
     Arduino          Breadboard
     ───────          ─────────
5V ────────────────── + rail
GND ────────────────── - rail

PIR: VCC→5V, OUT→Pin 2, GND→GND
A0 ─────────────────── Photoresistor circuit

Pin 13 ────────────── [R]──[LED Green]── GND
Pin 12 ────────────── [R]──[LED Red]── GND
Pin 11 ────────────── [BUZZER]── GND
Pin 9 ─────────────── Servo Orange
Servo Red ──── 5V
Servo Black ──── GND
```

### Steps
1. Connect PIR sensor (3 pins)
2. Connect photoresistor for light detection
3. Connect LEDs for status indication
4. Connect buzzer for alarm
5. Connect servo for camera simulation

---

## General Wiring Tips

### Power Distribution
- Use breadboard power rails for multiple components
- Connect Arduino 5V to breadboard + rail
- Connect Arduino GND to breadboard - rail
- All components share common ground

### Resistor Placement
- Always in series with component
- For LEDs: Resistor before LED (either side works, but standard is before)
- For pull-up/pull-down: Between signal and power/ground

### Wire Management
- Use different colors for organization
- Red = Power, Black = Ground, Other colors = Signals
- Keep wires neat to avoid confusion
- Use appropriate wire length

### Testing
- Test each component individually first
- Verify power and ground connections
- Check pin numbers match code
- Use multimeter if available

### Safety
- Double-check connections before powering on
- Verify no short circuits
- Use appropriate resistor values
- Disconnect power when making changes

---

## Troubleshooting Wiring

### Problem: Nothing Works
- Check power connections (5V and GND)
- Verify Arduino is powered (LED on board)
- Check all connections are secure

### Problem: Component Doesn't Work
- Verify correct pin number
- Check component orientation (LED, sensors)
- Test component individually
- Verify resistor values

### Problem: Wrong Values
- Check wiring matches diagram
- Verify analog vs digital pins
- Check voltage divider calculations
- Test with multimeter

### Problem: Components Overheat
- Check for short circuits
- Verify resistor values
- Reduce current draw
- Check power supply capacity

---

## Quick Reference

### Common Pin Assignments
- **Pin 13:** Built-in LED, general use
- **Pin 9:** Servo control (PWM)
- **A0-A5:** Analog sensors
- **Digital 2-12:** General I/O

### Resistor Values
- **220Ω:** LEDs (most colors)
- **330Ω:** Blue/white LEDs
- **10kΩ:** Pull-up/pull-down, voltage dividers

### Component Polarity
- **LEDs:** Long leg = + (anode)
- **Electrolytic Capacitors:** Marked leg = -
- **Diodes:** Band = cathode (-)
- **Most Sensors:** Check datasheet

---

Remember: When in doubt, refer to component datasheets and double-check connections before powering on!

