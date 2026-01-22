# Day 2 Project Guides
## Step-by-Step Instructions for Arduino Projects

## Project 1: Blinking LED (Beginner)

### Learning Objectives
- Understand digital output
- Control LED with code
- Use loops and timing

### Components Needed
- Arduino Uno
- 1x LED (any color)
- 1x 220Ω resistor
- Breadboard
- Jumper wires

### Wiring
1. Connect 220Ω resistor from Pin 13 to breadboard
2. Connect LED long leg (anode) to resistor
3. Connect LED short leg (cathode) to GND
4. See wiring diagram for details

### Code in S4A

```
when green flag clicked
forever
    digital pin 13 on
    wait 1 secs
    digital pin 13 off
    wait 1 secs
end
```

### Steps
1. Wire the circuit
2. Open S4A
3. Connect Arduino
4. Build the code
5. Click green flag
6. LED should blink!

### Extensions
- Change blink speed (adjust wait time)
- Use different pin
- Add multiple LEDs
- Create patterns

---

## Project 2: Button Control (Beginner)

### Learning Objectives
- Understand digital input
- Read button state
- Use conditions (if-then)

### Components Needed
- Arduino Uno
- 1x Button/Switch
- 1x 10kΩ resistor (pull-down)
- 1x LED
- 1x 220Ω resistor
- Breadboard
- Jumper wires

### Wiring
1. Connect button: 5V → Button → Pin 2
2. Add pull-down: Pin 2 → 10kΩ → GND
3. Add LED: Pin 13 → 220Ω → LED → GND

### Code in S4A

```
when green flag clicked
forever
    if digital pin 2 = 1 then
        digital pin 13 on
    else
        digital pin 13 off
    end
end
```

### Steps
1. Wire the circuit
2. Build the code
3. Test: Press button, LED should light
4. Release button, LED should turn off

### Understanding
- Button pressed = Pin 2 reads HIGH (1)
- Button not pressed = Pin 2 reads LOW (0)
- Condition checks button state
- LED follows button state

### Extensions
- Toggle LED (on/off with each press)
- Control multiple LEDs
- Add sound feedback
- Create game controller

---

## Project 3: Multiple LEDs Light Show (Intermediate)

### Learning Objectives
- Control multiple outputs
- Create patterns
- Use loops creatively

### Components Needed
- Arduino Uno
- 3x LEDs (different colors)
- 3x 220Ω resistors
- Breadboard
- Jumper wires

### Wiring
- LED 1: Pin 13 → 220Ω → LED → GND
- LED 2: Pin 12 → 220Ω → LED → GND
- LED 3: Pin 11 → 220Ω → LED → GND

### Code in S4A

```
when green flag clicked
forever
    digital pin 13 on
    wait 0.2 secs
    digital pin 13 off
    digital pin 12 on
    wait 0.2 secs
    digital pin 12 off
    digital pin 11 on
    wait 0.2 secs
    digital pin 11 off
end
```

### Pattern Ideas

**Chase Pattern:**
```
LED 1 → LED 2 → LED 3 → repeat
```

**All On/Off:**
```
All on → wait → All off → repeat
```

**Random:**
```
Turn random LED on/off
```

### Steps
1. Wire all three LEDs
2. Plan your pattern
3. Write code
4. Test and refine

### Extensions
- Add more LEDs
- Create complex patterns
- Sync with music
- Add button to change patterns

---

## Project 4: Light Sensor (Intermediate)

### Learning Objectives
- Read analog sensors
- Understand analog values (0-1023)
- Use sensor data in decisions

### Components Needed
- Arduino Uno
- 1x Photoresistor
- 1x 10kΩ resistor
- 1x LED
- 1x 220Ω resistor
- Breadboard
- Jumper wires

### Wiring
- Voltage divider: 5V → Photoresistor → A0 → 10kΩ → GND
- LED: Pin 13 → 220Ω → LED → GND

### Code in S4A

```
when green flag clicked
forever
    if analog pin A0 > 500 then
        digital pin 13 on
    else
        digital pin 13 off
    end
end
```

### Understanding
- More light = Higher A0 value (closer to 1023)
- Less light = Lower A0 value (closer to 0)
- Threshold (500) determines when LED turns on
- Adjust threshold for different sensitivity

### Testing
1. Cover sensor → LED should turn off
2. Shine light → LED should turn on
3. Adjust threshold value as needed

### Extensions
- Use value to control LED brightness
- Add multiple thresholds (dim, medium, bright)
- Log light levels over time
- Create automatic night light

---

## Project 5: Temperature Monitor (Intermediate)

### Learning Objectives
- Read temperature sensor
- Convert analog values to temperature
- Use data for decision-making

### Components Needed
- Arduino Uno
- 1x TMP36 temperature sensor
- 1x LED (for indicator)
- 1x 220Ω resistor
- Optional: Buzzer
- Breadboard
- Jumper wires

### Wiring
- TMP36: Left pin → 5V, Center → A0, Right → GND
- LED: Pin 13 → 220Ω → LED → GND

### Code in S4A

```
when green flag clicked
forever
    set [temperature] to ((analog pin A0 * 0.488) - 50)
    
    if [temperature] > 25 then
        digital pin 13 on
        play note 60 for 0.5 beats
    else
        digital pin 13 off
    end
    
    wait 1 secs
end
```

### Understanding
- TMP36 outputs voltage proportional to temperature
- Formula: Temp = (voltage × 100) - 50
- In S4A: (A0 reading × 0.488) - 50
- Adjust threshold (25°C) for your needs

### Calibration
- Room temperature should read ~20-25°C
- Adjust formula if readings are off
- Test with known temperature source

### Extensions
- Display temperature on screen
- Add multiple thresholds
- Log temperature data
- Create temperature alarm system

---

## Project 6: Servo Motor Control (Intermediate)

### Learning Objectives
- Control servo motors
- Understand PWM (Pulse Width Modulation)
- Create precise movements

### Components Needed
- Arduino Uno
- 1x Servo motor
- Jumper wires
- Optional: External 5V power

### Wiring
- Servo Red → 5V
- Servo Black/Brown → GND
- Servo Orange/Yellow → Pin 9

### Code in S4A

```
when green flag clicked
repeat 2
    servo pin 9 to 0
    wait 1 secs
    servo pin 9 to 90
    wait 1 secs
    servo pin 9 to 180
    wait 1 secs
end
```

### Understanding
- Servos rotate to specific angles
- Range: 0-180 degrees
- 0° = one extreme
- 90° = center
- 180° = other extreme
- Pin 9 is PWM-capable (required)

### Movements

**Sweep:**
```
0° → 180° → 0° (repeat)
```

**Point to Positions:**
```
0° → 45° → 90° → 135° → 180°
```

**Follow Sensor:**
```
Angle based on sensor value
```

### Extensions
- Control multiple servos
- Create robotic arm
- Follow light source
- Create clock face

---

## Project 7: Smart Plant Monitor (Advanced)

### Learning Objectives
- Combine multiple sensors
- Use data for complex decisions
- Create practical application

### Components Needed
- Arduino Uno
- 1x Moisture sensor (or DIY)
- 1x Photoresistor
- 1x TMP36 temperature sensor
- 3x LEDs (Green, Yellow, Red)
- 3x 220Ω resistors
- 1x Buzzer
- Breadboard
- Jumper wires

### Wiring
- Moisture → A0
- Light → A1 (with voltage divider)
- Temperature → A2
- Green LED → Pin 13
- Yellow LED → Pin 12
- Red LED → Pin 11
- Buzzer → Pin 10

### Code in S4A

```
when green flag clicked
forever
    set [moisture] to analog pin A0
    set [light] to analog pin A1
    set [temperature] to ((analog pin A2 * 0.488) - 50)
    
    if ([moisture] > 500) and ([light] > 400) and ([temperature] > 20) and ([temperature] < 30) then
        digital pin 13 on  // Green: Good
        digital pin 12 off
        digital pin 11 off
    else
        if ([moisture] < 300) or ([temperature] > 35) then
            digital pin 13 off
            digital pin 12 off
            digital pin 11 on  // Red: Alert
            play note 60 for 0.5 beats
        else
            digital pin 13 off
            digital pin 12 on  // Yellow: Warning
            digital pin 11 off
        end
    end
    
    wait 2 secs
end
```

### Logic
- **Green:** All conditions good
- **Yellow:** Some conditions need attention
- **Red:** Critical condition + buzzer alert

### Steps
1. Wire all sensors and outputs
2. Test each sensor individually
3. Write code with conditions
4. Test and adjust thresholds
5. Calibrate for your environment

### Extensions
- Add data logging
- Connect to cloud (Day 3)
- Add LCD display
- Create mobile app interface

---

## Project 8: Security System (Advanced)

### Learning Objectives
- Combine motion and light sensors
- Create alarm system
- Use multiple outputs effectively

### Components Needed
- Arduino Uno
- 1x PIR motion sensor (or button for simulation)
- 1x Photoresistor
- 1x Buzzer
- 2x LEDs (Green, Red)
- 2x 220Ω resistors
- 1x Servo motor
- Breadboard
- Jumper wires

### Wiring
- PIR: VCC → 5V, OUT → Pin 2, GND → GND
- Photoresistor → A0 (with voltage divider)
- Green LED → Pin 13
- Red LED → Pin 12
- Buzzer → Pin 11
- Servo → Pin 9

### Code in S4A

```
when green flag clicked
forever
    if (digital pin 2 = 1) and (analog pin A0 < 300) then
        // Motion detected + dark = alarm
        digital pin 12 on  // Red LED
        digital pin 13 off
        digital pin 11 on  // Buzzer
        servo pin 9 to 90  // Point camera
        wait 2 secs
        digital pin 11 off
    else
        // No alarm
        digital pin 12 off
        digital pin 13 on  // Green LED
        servo pin 9 to 0
    end
    wait 0.5 secs
end
```

### Logic
- Motion detected + Dark = Alarm
- Motion detected + Light = No alarm (daytime)
- No motion = Safe (green LED)

### Features
- Motion detection
- Light level check (night mode)
- Visual indicators
- Audio alarm
- Servo camera simulation

### Extensions
- Add delay before alarm
- Record alarm events
- Add keypad to arm/disarm
- Connect to cloud notification

---

## General Project Tips

### Planning
1. **Define Goal:** What do you want to achieve?
2. **List Components:** What do you need?
3. **Design Circuit:** Draw wiring diagram
4. **Plan Code:** Outline logic
5. **Build Incrementally:** Test as you go

### Building
1. **Start Simple:** Get one thing working
2. **Add Complexity:** Add features one at a time
3. **Test Frequently:** Verify each addition works
4. **Debug Systematically:** Fix one issue at a time

### Troubleshooting
1. **Check Wiring:** Verify all connections
2. **Check Code:** Verify pin numbers and logic
3. **Test Components:** Test individually
4. **Check Power:** Verify Arduino is powered
5. **Ask for Help:** Don't struggle alone!

### Documentation
- Take photos of working circuits
- Comment your code
- Write down what works
- Note any issues and solutions

---

## Assessment Criteria

### Beginner Projects (1-2)
- Circuit wired correctly
- Code runs without errors
- Basic functionality works
- Can explain how it works

### Intermediate Projects (3-6)
- Multiple components work together
- Code uses conditions effectively
- Project demonstrates understanding
- Can troubleshoot issues

### Advanced Projects (7-8)
- Complex system works correctly
- Multiple sensors and actuators
- Creative problem-solving
- Can help others

---

## Next Steps

After completing projects:
1. Modify and experiment
2. Combine ideas from different projects
3. Design your own project
4. Prepare for Day 3 (cloud integration)
5. Think about classroom applications

Remember: The best way to learn is by doing. Don't be afraid to experiment and make mistakes!

