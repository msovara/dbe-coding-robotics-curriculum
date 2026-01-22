# Day 2: Physical Computing with Scratch for Arduino
## Detailed Lesson Plan

**Duration:** 6-8 hours (Full Day)
**Target Audience:** DBE Teachers (Mixed Experience Levels)
**Prerequisites:** Day 1 completion (basic Scratch knowledge)
**Learning Objectives:**
- Understand Arduino hardware components
- Set up Scratch for Arduino (S4A)
- Create physical computing projects
- Manage hardware in classroom settings

---

## Morning Session (3-4 hours)

### Session 1: Introduction to Arduino Hardware (1 hour)
**Time:** 08:00 - 09:00

#### Learning Objectives
- Identify Arduino board components
- Understand basic electronics concepts
- Recognize safety considerations
- Connect components on breadboard

#### Activities

**Opening (10 minutes)**
- Review Day 1: What did we learn?
- Introduction: "Today we connect code to the physical world!"
- Pre-assessment: "What do you know about electronics?"

**Arduino Board Tour (20 minutes)**
- **Arduino Uno Components:**
  - USB port (power and communication)
  - Power jack (external power)
  - Digital pins (0-13): On/off signals
  - Analog pins (A0-A5): Variable signals
  - Reset button
  - LED indicators (power, TX, RX)
  - Microcontroller (the "brain")

**Hands-On: Component Identification (15 minutes)**
- **Activity:** "Arduino Component Scavenger Hunt"
  - Teachers identify components on their boards
  - Label components on diagram
  - Discuss function of each component

**Basic Electronics Concepts (10 minutes)**
- **Voltage, Current, Resistance:** Simple analogy (water in pipes)
- **Circuits:** Need complete path (power → component → ground)
- **Digital vs. Analog:**
  - Digital: On (1) or Off (0)
  - Analog: Range of values (0-1023)

**Safety Considerations (5 minutes)**
- **Important Rules:**
  - Never connect Arduino directly to wall outlet
  - Use USB or proper power supply only
  - Check connections before powering on
  - Disconnect power when making changes
  - Handle components carefully (static electricity)

**Reflection (5 minutes)**
- Quick write: "What surprised you about Arduino hardware?"
- Share one observation

---

### Session 2: Scratch for Arduino Setup (1 hour)
**Time:** 09:00 - 10:00

#### Learning Objectives
- Install S4A software
- Connect Arduino to computer
- Upload firmware to Arduino
- Troubleshoot common setup issues

#### Activities

**S4A Introduction (10 minutes)**
- **What is S4A?**
  - Scratch for Arduino
  - Extension of Scratch that controls Arduino
  - Visual programming for physical computing
  - Free and open-source

**Software Installation (20 minutes)**
- **Step 1: Download S4A**
  - Go to: http://s4a.cat
  - Download for your operating system
  - Extract files

- **Step 2: Install Arduino Drivers**
  - Windows: Usually automatic, may need manual install
  - Mac: Usually automatic
  - Linux: May need permissions setup

- **Step 3: Install S4A**
  - Follow installation guide (see resources)
  - Create desktop shortcut

**Connecting Arduino (15 minutes)**
- **Step 1: Connect USB Cable**
  - Connect Arduino to computer via USB
  - Wait for computer to recognize device
  - Check device manager (Windows) or system info (Mac)

- **Step 2: Upload Firmware**
  - Open S4A
  - Go to "Board" → "Upload Firmware"
  - Wait for "Firmware uploaded successfully"
  - **Important:** Firmware must be uploaded once per Arduino

**Testing Connection (10 minutes)**
- **Activity:** "Blink Test"
  - Open S4A
  - Use "digital pin 13 on" block
  - LED on board should light up
  - Use "digital pin 13 off" block
  - LED should turn off

**Troubleshooting (5 minutes)**
- **Common Issues:**
  - Arduino not recognized: Check USB cable, drivers
  - Firmware upload fails: Try different USB port
  - S4A won't connect: Restart S4A, re-upload firmware
  - See troubleshooting guide for more solutions

**Break (15 minutes)**

---

### Session 3: First Physical Projects (1-2 hours)
**Time:** 10:15 - 12:00

#### Learning Objectives
- Control LEDs using digital output
- Read button input
- Combine input and output
- Create interactive physical projects

#### Activities

**Project 1: Blinking LED (30 minutes)**
- **Components Needed:**
  - Arduino Uno
  - LED (any color)
  - 220Ω resistor
  - Breadboard
  - Jumper wires

- **Wiring:**
  - Connect LED to digital pin 13
  - Add resistor (220Ω) in series
  - Connect to ground

- **Code in S4A:**
  ```
  when green flag clicked
  forever
      digital pin 13 on
      wait 1 secs
      digital pin 13 off
      wait 1 secs
  end
  ```

- **Activity:** Teachers build and test
- **Extension:** Change blink speed, use different pin

**Project 2: Button Control (30 minutes)**
- **Components Needed:**
  - Button/switch
  - 10kΩ resistor (pull-down)
  - Additional jumper wires

- **Wiring:**
  - Connect button to digital pin 2
  - Add pull-down resistor
  - Connect to 5V and ground

- **Code in S4A:**
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

- **Activity:** Teachers build and test
- **Discussion:** How does this work? (Input → Process → Output)

**Project 3: Interactive Light Show (30 minutes)**
- **Challenge:** Create a light show with multiple LEDs
- **Requirements:**
  - At least 3 LEDs
  - Button to start/stop
  - Creative pattern

- **Planning:**
  - Sketch your design
  - Plan the sequence
  - Wire components
  - Write code

- **Sharing:** Teachers present their light shows

**Lunch Break (12:00 - 13:00)**

---

## Afternoon Session (3-4 hours)

### Session 4: Sensors and Actuators (2 hours)
**Time:** 13:00 - 15:00

#### Learning Objectives
- Use analog sensors (light, temperature, potentiometer)
- Control servo motors
- Use buzzer/speaker for audio output
- Create projects with multiple components

#### Activities

**Analog Sensors Introduction (20 minutes)**
- **What are Analog Sensors?**
  - Measure continuous values (not just on/off)
  - Examples: light, temperature, sound, distance
  - Values range from 0-1023 in Arduino

- **Reading Analog Values:**
  - Use "analog pin" blocks in S4A
  - Values are 0-1023
  - Need to interpret values for your sensor

**Project 4: Light Sensor (30 minutes)**
- **Components:**
  - Photoresistor (light sensor)
  - 10kΩ resistor
  - LED (for output)

- **Wiring:**
  - Connect photoresistor to analog pin A0
  - Add voltage divider with resistor
  - Connect LED to digital pin 13

- **Code:**
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

- **Activity:** Test in different lighting conditions
- **Extension:** Use value to control LED brightness (PWM)

**Project 5: Temperature Monitor (30 minutes)**
- **Components:**
  - Temperature sensor (TMP36 or LM35)
  - LED or buzzer
  - Optional: LCD display

- **Wiring:**
  - Connect sensor to analog pin A0
  - Power and ground connections

- **Code:**
  ```
  when green flag clicked
  forever
      set [temperature] to (analog pin A0 * 0.488) - 50
      if [temperature] > 25 then
          digital pin 13 on
          play note 60 for 0.5 beats
      else
          digital pin 13 off
      end
      wait 1 secs
  end
  ```

- **Activity:** Monitor room temperature
- **Discussion:** Real-world applications

**Servo Motors (20 minutes)**
- **What are Servos?**
  - Motors that can rotate to specific angles
  - Range: 0-180 degrees
  - Used in robotics, automation

- **Controlling Servos:**
  - Connect to digital pin (usually 9)
  - Use "servo pin 9 to angle" block
  - Angles: 0-180 degrees

- **Quick Demo:**
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

**Project 6: Temperature Monitor with Visual/Audio Feedback (20 minutes)**
- **Combine Previous Concepts:**
  - Temperature sensor
  - LED indicators (different colors for different ranges)
  - Buzzer for alerts
  - Servo for visual indicator

- **Requirements:**
  - Green LED: Normal temperature (20-25°C)
  - Yellow LED: Warm (25-30°C)
  - Red LED: Hot (>30°C)
  - Buzzer: Alert when too hot
  - Servo: Points to temperature range

- **Activity:** Teachers design and build
- **Sharing:** Present projects

**Break (15 minutes)**

---

### Session 5: Advanced S4A Projects (1-2 hours)
**Time:** 15:15 - 16:30

#### Learning Objectives
- Combine multiple sensors and actuators
- Implement data logging basics
- Design projects for specific subject areas
- Manage complex hardware setups

#### Activities

**Multiple Components (30 minutes)**
- **Challenge:** Use at least 3 sensors and 2 actuators
- **Planning:**
  - What problem are you solving?
  - Which sensors do you need?
  - What outputs will you use?
  - How will components interact?

- **Example Ideas:**
  - Security system (motion + light + sound)
  - Plant monitor (moisture + light + temperature)
  - Weather station (multiple sensors)

**Data Logging Basics (20 minutes)**
- **Concept:** Recording sensor values over time
- **Simple Method:** Use variables and lists in S4A
- **Advanced Method:** Export to file or cloud (Day 3)

- **Example:**
  ```
  when green flag clicked
  set [reading count] to 0
  forever
      add (analog pin A0) to [sensor readings]
      change [reading count] by 1
      wait 1 secs
  end
  ```

**Project 7: Smart Plant Monitor (30 minutes)**
- **Components:**
  - Moisture sensor (or make simple one)
  - Light sensor
  - Temperature sensor
  - LED indicators
  - Buzzer

- **Functionality:**
  - Monitor plant conditions
  - Alert when water needed
  - Show light levels
  - Display temperature

- **Activity:** Teachers build and test
- **Extension:** Add data logging

**Project 8: Security System (30 minutes)**
- **Components:**
  - Motion sensor (PIR) or button (simulated)
  - Light sensor
  - Buzzer
  - LED indicators
  - Servo (for camera simulation)

- **Functionality:**
  - Detect motion
  - Check if dark (night mode)
  - Sound alarm
  - Visual indicators

- **Activity:** Teachers design and build

**Subject-Specific Project Design (20 minutes)**
- **Activity:** Design a project for your subject area
  - **Mathematics:** Data collection and graphing
  - **Science:** Experiment monitoring
  - **Technology:** Automation systems
  - **Languages:** Interactive storytelling device

- **Planning Template:**
  - Subject: _________________
  - Topic: _________________
  - Sensors needed: _________________
  - Actuators needed: _________________
  - Learning objectives: _________________

- **Sharing:** Present project ideas

**Wrap-up and Reflection (10 minutes)**
- **Daily Reflection Journal**
- **Key Takeaways:**
  - What did you learn?
  - What was challenging?
  - How will you use this in your classroom?

---

## Materials Needed

### Hardware (per 2-3 teachers)
- Arduino Uno board with USB cable
- Breadboard
- LEDs (assorted colors, 5-10)
- Resistors (220Ω, 10kΩ, assortment)
- Buttons/switches (2-3)
- Photoresistor (light sensor)
- Temperature sensor (TMP36 or LM35)
- Servo motor (1)
- Buzzer/speaker (1)
- Jumper wires (assorted, 20+)
- Optional: LCD display, motion sensor, moisture sensor

### Software
- S4A (Scratch for Arduino)
- Arduino IDE (for reference)
- USB drivers for Arduino

### Handouts
- Arduino component guide
- S4A setup instructions
- Wiring diagrams
- Project templates
- Troubleshooting guide
- Safety guidelines

---

## Differentiation Strategies

### For Beginners
- Provide step-by-step wiring diagrams
- Use simpler projects (single LED, single sensor)
- Pair with more experienced teacher
- Extra time for setup and troubleshooting

### For Advanced Learners
- Challenge with complex projects
- Multiple sensors and actuators
- Data logging and analysis
- Help others troubleshoot

---

## Assessment

### Formative (Throughout Day)
- Observation during building
- Quick check-ins
- Project completion
- Troubleshooting ability

### Summative (End of Day)
- Completed physical project
- Wiring diagram
- Code explanation
- Reflection journal
- Self-assessment using rubric

---

## Safety Reminders

1. **Always disconnect power** when making wiring changes
2. **Check connections** before powering on
3. **Use proper resistors** to protect components
4. **Never short circuit** (connect power directly to ground)
5. **Handle components carefully** (avoid static electricity)
6. **Supervise students** closely when working with hardware

---

## Troubleshooting Tips

### Arduino Not Recognized
- Try different USB cable
- Check device manager
- Reinstall drivers
- Try different USB port

### Components Not Working
- Check wiring connections
- Verify power and ground
- Test components individually
- Check resistor values

### S4A Connection Issues
- Re-upload firmware
- Restart S4A
- Check Arduino is connected
- Verify correct COM port

---

## Homework/Preparation for Day 3

1. Complete reflection journal
2. Finish project design for your subject
3. Review cloud computing basics (handout provided)
4. Think about: How can sensors connect to the internet?

---

## Notes for Facilitators

- **Safety First:** Always emphasize safety
- **Hands-On Support:** Be available for troubleshooting
- **Celebrate Success:** Every working circuit is an achievement
- **Encourage Experimentation:** Mistakes are learning opportunities
- **Manage Resources:** Rotate hardware if limited
- **Documentation:** Take photos of working projects

---

## Next Day Preview

Tomorrow we'll explore cloud computing and connect our Arduino projects to the internet! We'll learn about IoT (Internet of Things) and data visualization.

