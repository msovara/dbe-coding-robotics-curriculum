# Day 3 Project Guides
## Coding & Robotics with Arduino – Step-by-Step Projects

These projects extend Day 2 skills with multi-sensor logic, variables, and simple robotics behaviours. Use [day-02-arduino/activities/wiring-diagrams.md](../../day-02-arduino/activities/wiring-diagrams.md) for component wiring where relevant.

---

## Project 1: Smart Night Light (Multi-Sensor)

### Learning Objectives
- Use analog input (light sensor) and a threshold variable
- Use digital output (LED) with conditional logic
- Optional: add button to enable/disable

### Components
- Arduino Uno, breadboard, jumper wires
- 1× photoresistor (light sensor) + 1× 10kΩ resistor (voltage divider)
- 1× LED + 1× 220Ω resistor
- Optional: 1× button + 1× 10kΩ pull-down resistor

### Wiring
- **Light sensor:** 5V → photoresistor → A0; A0 → 10kΩ → GND (voltage divider).
- **LED:** Pin 13 → 220Ω → LED → GND.
- **Button (optional):** 5V → button → Pin 2; Pin 2 → 10kΩ → GND.

### Logic (words)
- Read light level from A0. If light level &lt; threshold (e.g. 300), turn LED on; else turn LED off. If using button: only apply this when button is pressed.

### S4A Outline
```
when green flag clicked
forever
  set [lightLevel] to (analog pin 0)
  if (lightLevel) < (300) then
    digital pin 13 on
  else
    digital pin 13 off
  end
  wait 0.5 secs
end
```

### Extensions
- Add a variable for “threshold” and change it with buttons (up/down).
- Add a second LED (e.g. dim when light is medium, bright when dark).
- Discuss with learners: how could we use this in a real “smart” device?

---

## Project 2: Reaction Game (Variables and Timing)

### Learning Objectives
- Use variables for state and timing
- Use digital input (button) and digital output (LEDs)
- Create a simple “game” (who reacts faster?)

### Components
- Arduino Uno, breadboard, jumper wires
- 2× LEDs (e.g. pins 13 and 12) + 2× 220Ω resistors
- 1× button + 1× 10kΩ pull-down resistor (e.g. Pin 2)

### Wiring
- **LEDs:** Pin 13 → 220Ω → LED1 → GND; Pin 12 → 220Ω → LED2 → GND.
- **Button:** 5V → button → Pin 2; Pin 2 → 10kΩ → GND.

### Logic (words)
- “Ready” state: one LED on. After random delay (2–5 s), turn that LED off and turn “go” LED on. When player presses button, record time (or just show “win” by blinking). Reset and repeat.

### S4A Outline (simplified)
- Use a variable `state` (e.g. 0 = waiting, 1 = go). When green flag: set state to 0, LED on pin 13 on, wait random 2–5 secs, set state to 1, pin 13 off, pin 12 on. In forever or when key/button pressed: if state = 1, blink both LEDs (win), then reset.

### Extensions
- Two players: two buttons; first to press wins (compare which digital pin went high first).
- Use “timer” or millis concept if available in S4A to show reaction time.
- Link to maths (probability, averages) or PE (reaction time).

---

## Project 3: Simple Servo “Sweep” with Sensor Control

### Learning Objectives
- Control a servo from S4A
- Use a sensor to change servo position (e.g. light or distance)
- Introduce “robotics” (actuator responding to environment)

### Components
- Arduino Uno, breadboard, jumper wires
- 1× servo motor (signal to digital pin, e.g. 9; 5V and GND)
- 1× light sensor (or potentiometer) for input

### Wiring
- **Servo:** Signal → Pin 9; V+ → 5V; GND → GND. (Check servo wiring for your model.)
- **Light sensor:** As in Project 1 (A0).

### Logic (words)
- Read light level. Map it to an angle (e.g. dark → 0°, bright → 180°). Set servo to that angle. Repeat in a loop.

### S4A Outline
- In “forever”: read analog pin 0; scale to 0–180 (may need to use “map” or simple maths blocks if available); set servo on pin 9 to (angle); wait a short time.

### Extensions
- Add a button: when pressed, sweep servo slowly 0→180→0; when released, go back to light-controlled mode.
- Use two light sensors (left/right) to “point” servo toward brighter side (light-following behaviour).
- Discuss: how could this be part of a bigger robot (e.g. solar tracker, head that looks at light)?

---

## Project 4: Distance Warning (Ultrasonic Sensor – If Available)

### Learning Objectives
- Use distance (ultrasonic) sensor
- Use conditions to trigger output (LED/buzzer) when object is close
- Design a simple “safety” or “parking” style behaviour

### Components
- Arduino Uno, breadboard, jumper wires
- Ultrasonic sensor (e.g. HC-SR04) – check S4A compatibility; some need special firmware or blocks
- 1× LED + 220Ω or 1× buzzer

### Note
If your S4A setup does not support ultrasonic directly, use a potentiometer or second light sensor to “simulate” distance (turn knob = “closer/farther”) and keep the same logic.

### Logic (words)
- Read distance. If distance &lt; 20 cm, turn on warning LED/buzzer; else turn off. Optionally: different outputs for “close” vs “very close.”

### S4A Outline
- In “forever”: read distance (from appropriate block or analog); if &lt; 20 then digital pin 13 on, else off; wait 0.1 s.

### Extensions
- Add a second threshold (e.g. &lt; 10 cm = fast beep, &lt; 20 cm = slow beep).
- Link to real-world applications: parking sensors, obstacle avoidance in robotics.

---

## General Tips

- **Troubleshooting:** See [resources/hardware/troubleshooting-guide.md](../../../resources/hardware/troubleshooting-guide.md).
- **Wiring details:** See [day-02-arduino/activities/wiring-diagrams.md](../../day-02-arduino/activities/wiring-diagrams.md) and [day-02-arduino/projects/project-guides.md](../../day-02-arduino/projects/project-guides.md).
- **Classroom use:** Choose one project as a “must do” and others as extensions; adapt thresholds and components to your kit.
