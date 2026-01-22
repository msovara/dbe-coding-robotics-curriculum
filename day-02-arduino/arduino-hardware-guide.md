# Arduino Hardware Guide
## A Comprehensive Guide to Arduino Components and Electronics

## Arduino Uno Board Overview

### Physical Components

```
                    ┌─────────────────────┐
                    │   USB Port          │
                    │   (Power & Data)    │
                    ├─────────────────────┤
                    │                     │
                    │   Digital Pins      │
                    │   0-13              │
                    │                     │
                    │   Analog Pins      │
                    │   A0-A5             │
                    │                     │
                    │   Power Pins        │
                    │   5V, 3.3V, GND    │
                    │                     │
                    │   Reset Button     │
                    │                     │
                    │   Microcontroller  │
                    │   (ATmega328P)     │
                    │                     │
                    │   Power LED        │
                    │   TX/RX LEDs       │
                    └─────────────────────┘
```

### Key Components Explained

#### 1. USB Port (Type B)
- **Purpose:** Power supply and communication
- **Voltage:** 5V from computer
- **Data:** Serial communication with computer
- **Usage:** Connect to computer for programming and power

#### 2. Power Jack
- **Purpose:** External power supply
- **Voltage:** 7-12V DC (recommended: 9V)
- **Usage:** When not connected to computer
- **Note:** Center positive, outer negative

#### 3. Digital Pins (0-13)
- **Purpose:** Digital input/output
- **Values:** HIGH (5V/1) or LOW (0V/0)
- **Special Pins:**
  - Pin 13: Built-in LED
  - Pins 0-1: Serial communication (RX/TX)
  - Pins 3, 5, 6, 9, 10, 11: PWM (analog output simulation)

#### 4. Analog Pins (A0-A5)
- **Purpose:** Analog input
- **Values:** 0-1023 (10-bit resolution)
- **Voltage Range:** 0-5V
- **Usage:** Reading sensors (light, temperature, etc.)

#### 5. Power Pins
- **5V:** 5 volt output (for components)
- **3.3V:** 3.3 volt output (for some sensors)
- **GND:** Ground (multiple pins)
- **VIN:** Voltage input (when using external power)

#### 6. Reset Button
- **Purpose:** Restart Arduino program
- **Usage:** Press to reset, program starts from beginning

#### 7. Microcontroller (ATmega328P)
- **Purpose:** The "brain" of Arduino
- **Features:**
  - 16 MHz clock speed
  - 32 KB flash memory
  - 2 KB RAM
  - 14 digital I/O pins
  - 6 analog input pins

---

## Basic Electronics Concepts

### Voltage (V)
- **Definition:** Electrical pressure or potential difference
- **Analogy:** Water pressure in a pipe
- **Units:** Volts (V)
- **Arduino:** 5V (digital HIGH), 0V (digital LOW)

### Current (I)
- **Definition:** Flow of electrical charge
- **Analogy:** Water flow rate
- **Units:** Amperes (A) or milliamperes (mA)
- **Arduino:** Can supply ~40mA per pin, 200mA total

### Resistance (R)
- **Definition:** Opposition to current flow
- **Analogy:** Pipe narrowness
- **Units:** Ohms (Ω)
- **Purpose:** Limits current to protect components

### Ohm's Law
**Formula:** V = I × R
- Voltage = Current × Resistance
- Used to calculate resistor values needed

### Circuits
- **Complete Circuit:** Power → Component → Ground
- **Open Circuit:** Broken path (nothing works)
- **Short Circuit:** Power directly to ground (dangerous!)

---

## Common Components

### LEDs (Light Emitting Diodes)

**Characteristics:**
- **Voltage:** ~2V forward voltage
- **Current:** 20mA typical
- **Polarity:** Anode (+) and Cathode (-)
- **Identification:** Longer leg = anode (+)

**Resistor Needed:**
- Formula: R = (V_supply - V_LED) / I_LED
- Example: (5V - 2V) / 0.02A = 150Ω
- Common: 220Ω resistor (safe for most LEDs)

**Wiring:**
```
Arduino Pin 13 → Resistor (220Ω) → LED Anode → LED Cathode → GND
```

### Resistors

**Types:**
- **Fixed Resistors:** Single resistance value
- **Variable Resistors (Potentiometer):** Adjustable resistance

**Color Code:**
- 4-band or 5-band color coding
- Common values: 220Ω, 1kΩ, 10kΩ

**Common Uses:**
- **220Ω:** LED current limiting
- **10kΩ:** Pull-up/pull-down resistors
- **Variable:** Sensor calibration, volume control

### Buttons/Switches

**Types:**
- **Momentary:** Press to activate, release to deactivate
- **Toggle:** Switch on/off, stays in position

**Wiring:**
- One side to digital pin
- Other side to 5V or GND
- Pull-down resistor (10kΩ) to GND
- Pull-up resistor (10kΩ) to 5V

**Pull-Down Configuration:**
```
5V → Button → Digital Pin
              ↓
           10kΩ Resistor → GND
```

### Breadboards

**Purpose:** Temporary circuit building without soldering

**Layout:**
```
     a  b  c  d  e    f  g  h  i  j
 1  [·] [·] [·] [·] [·] | [·] [·] [·] [·] [·]
 2  [·] [·] [·] [·] [·] | [·] [·] [·] [·] [·]
 ...
30  [·] [·] [·] [·] [·] | [·] [·] [·] [·] [·]
     +  -  (power rails)
```

**Rules:**
- Rows a-e connected horizontally (except center gap)
- Rows f-j connected horizontally (except center gap)
- Power rails (+ and -) connected vertically
- Center gap separates top and bottom halves

### Sensors

#### Photoresistor (Light Sensor)
- **Resistance:** Decreases with more light
- **Wiring:** Voltage divider circuit
- **Reading:** Analog pin (0-1023)
- **Use:** Detect light levels

#### Temperature Sensor (TMP36)
- **Output:** Voltage proportional to temperature
- **Range:** -40°C to 125°C
- **Accuracy:** ±2°C
- **Wiring:** Power, ground, analog output
- **Formula:** Temp = (voltage - 0.5) × 100

#### Motion Sensor (PIR)
- **Purpose:** Detect movement
- **Output:** Digital (HIGH when motion detected)
- **Range:** ~7 meters
- **Use:** Security systems, automation

#### Potentiometer
- **Purpose:** Variable resistor
- **Use:** Volume control, sensor calibration
- **Wiring:** Two ends to 5V and GND, wiper to analog pin

### Actuators

#### Servo Motors
- **Purpose:** Precise angular positioning
- **Range:** 0-180 degrees
- **Power:** 5V, ~100mA
- **Control:** PWM signal on digital pin
- **Use:** Robotics, automation

#### DC Motors
- **Purpose:** Continuous rotation
- **Power:** Requires motor driver (H-bridge)
- **Control:** Speed and direction
- **Use:** Wheels, fans, pumps

#### Buzzer/Speaker
- **Purpose:** Sound output
- **Types:**
  - Passive buzzer: Needs frequency signal
  - Active buzzer: Built-in oscillator
- **Control:** Digital pin (on/off) or PWM (tone)

---

## Wiring Basics

### Power Distribution
```
Arduino 5V → Breadboard + rail
Arduino GND → Breadboard - rail
```

### Component Connections

**LED:**
```
Digital Pin → Resistor → LED Anode
LED Cathode → GND
```

**Button (Pull-Down):**
```
5V → Button → Digital Pin
Digital Pin → 10kΩ Resistor → GND
```

**Analog Sensor:**
```
5V → Sensor → Analog Pin
Sensor → GND
(May need voltage divider)
```

**Servo:**
```
5V → Servo Red Wire
GND → Servo Black/Brown Wire
Digital Pin 9 → Servo Orange/Yellow Wire
```

---

## Safety Guidelines

### Electrical Safety
1. **Never connect Arduino directly to wall outlet**
   - Use USB or proper 9V adapter only
   - Maximum 12V on power jack

2. **Check connections before powering on**
   - Verify no short circuits
   - Ensure correct polarity for components

3. **Use appropriate resistors**
   - Always use current-limiting resistors with LEDs
   - Calculate resistor values using Ohm's Law

4. **Disconnect power when making changes**
   - Turn off or unplug before rewiring
   - Prevents accidental short circuits

5. **Handle components carefully**
   - Avoid static electricity (touch metal first)
   - Don't bend component legs excessively
   - Store components properly

### Component Protection
- **LEDs:** Always use resistor (220Ω minimum)
- **Arduino Pins:** Maximum 40mA per pin
- **Total Current:** Maximum 200mA from 5V pin
- **Reverse Polarity:** Can damage components

### Classroom Safety
- **Supervision:** Always supervise students
- **Age Appropriate:** Consider student age and maturity
- **First Aid:** Know location of first aid kit
- **Emergency:** Have emergency procedures

---

## Troubleshooting Guide

### Problem: Nothing Works
**Possible Causes:**
- Arduino not powered (check USB connection)
- Wrong pin numbers in code
- Loose connections
- Components not properly connected

**Solutions:**
- Check USB connection and power LED
- Verify pin numbers match wiring
- Re-seat all connections
- Test components individually

### Problem: LED Doesn't Light
**Possible Causes:**
- Wrong polarity (LED backwards)
- Missing or wrong resistor value
- Wrong pin number
- LED burned out

**Solutions:**
- Check LED orientation (long leg = +)
- Verify resistor is 220Ω
- Check pin number in code
- Test LED with known good circuit

### Problem: Sensor Reading Wrong Values
**Possible Causes:**
- Wrong wiring (power/ground reversed)
- Incorrect pin number
- Sensor damaged
- Need calibration

**Solutions:**
- Verify wiring diagram
- Check pin number in code
- Test sensor with multimeter
- Calibrate sensor (adjust code)

### Problem: Servo Doesn't Move
**Possible Causes:**
- Not enough power
- Wrong pin
- Servo damaged
- Code error

**Solutions:**
- Use external power for servo
- Verify pin 9 (or PWM pin)
- Test servo with simple code
- Check code syntax

### Problem: Arduino Not Recognized
**Possible Causes:**
- USB driver not installed
- Faulty USB cable
- Wrong USB port
- Arduino board issue

**Solutions:**
- Install Arduino drivers
- Try different USB cable
- Try different USB port
- Test with another computer

---

## Component Specifications Reference

### Arduino Uno
- **Operating Voltage:** 5V
- **Input Voltage:** 7-12V (recommended)
- **Digital I/O Pins:** 14 (6 PWM)
- **Analog Input Pins:** 6
- **DC Current per I/O Pin:** 40mA
- **DC Current for 3.3V Pin:** 50mA
- **Flash Memory:** 32KB
- **SRAM:** 2KB
- **Clock Speed:** 16MHz

### Common Resistor Values
- **220Ω:** LED current limiting (red, yellow, green LEDs)
- **330Ω:** LED current limiting (blue, white LEDs)
- **1kΩ:** General purpose, pull-up/pull-down
- **10kΩ:** Pull-up/pull-down, voltage dividers
- **100kΩ:** High-resistance applications

### LED Specifications
- **Forward Voltage:** 1.8-3.4V (depends on color)
- **Forward Current:** 20mA typical
- **Red/Yellow:** ~2V, 20mA
- **Green/Blue:** ~3V, 20mA
- **White:** ~3.4V, 20mA

### Servo Motor (Standard)
- **Operating Voltage:** 4.8-6V
- **Current Draw:** 100-250mA (depends on load)
- **Rotation Range:** 0-180 degrees
- **Control Signal:** PWM, 50Hz frequency

---

## Quick Reference: Pin Functions

### Digital Pins
- **0-1:** Serial communication (RX/TX) - avoid for I/O
- **2-12:** General purpose digital I/O
- **13:** Built-in LED, general purpose I/O
- **3, 5, 6, 9, 10, 11:** PWM capable (analog output)

### Analog Pins
- **A0-A5:** Analog input (0-1023), can also be digital I/O

### Power Pins
- **5V:** 5 volt output
- **3.3V:** 3.3 volt output
- **GND:** Ground (multiple pins)
- **VIN:** Voltage input (external power)

---

## Best Practices

1. **Plan Before Building**
   - Draw circuit diagram
   - List components needed
   - Plan code structure

2. **Build Incrementally**
   - Test each component separately
   - Add components one at a time
   - Verify each step works

3. **Document Your Work**
   - Take photos of circuits
   - Comment your code
   - Keep notes on what works

4. **Use Proper Tools**
   - Multimeter for testing
   - Proper wire strippers
   - Organized component storage

5. **Learn from Mistakes**
   - Document what went wrong
   - Understand why it failed
   - Try different approaches

---

## Resources

### Online Resources
- **Arduino Official:** https://www.arduino.cc
- **Arduino Reference:** https://www.arduino.cc/reference
- **Fritzing:** Circuit diagram software
- **Tinkercad Circuits:** Online circuit simulator

### Books
- "Getting Started with Arduino" by Massimo Banzi
- "Arduino Cookbook" by Michael Margolis

### Communities
- Arduino Forum: https://forum.arduino.cc
- Reddit: r/arduino
- Stack Overflow: Arduino tag

---

## Next Steps

After understanding hardware basics:
1. Practice building simple circuits
2. Experiment with different components
3. Combine multiple components
4. Move to Day 2 projects
5. Design your own projects

Remember: Start simple, build complexity gradually, and always prioritize safety!

