# Hardware Troubleshooting Guide
## Systematic Approach to Solving Hardware Problems

## Troubleshooting Philosophy

**Key Principles:**
1. Start simple, add complexity
2. Test one thing at a time
3. Verify before assuming
4. Document what works
5. Ask for help when stuck

---

## Systematic Troubleshooting Process

### Step 1: Verify Power

**Check Arduino Power:**
- [ ] USB cable connected
- [ ] Power LED on Arduino is lit
- [ ] Computer recognizes Arduino
- [ ] S4A shows "Arduino found"

**If No Power:**
- Try different USB cable
- Try different USB port
- Check USB cable quality
- Try different computer
- Check Arduino board (may be damaged)

**Check Component Power:**
- [ ] Components connected to correct voltage
- [ ] Ground connections made
- [ ] No short circuits
- [ ] Power supply adequate

---

### Step 2: Check Connections

**Wiring Verification:**
- [ ] Follow wiring diagram exactly
- [ ] Pin numbers match code
- [ ] All connections secure
- [ ] No loose wires
- [ ] Breadboard connections good

**Common Wiring Mistakes:**
- Wrong pin numbers
- Loose breadboard connections
- Missing ground connections
- Reversed polarity (LEDs, etc.)
- Wrong resistor values

**Testing Connections:**
- Gently wiggle wires (shouldn't come loose)
- Check with multimeter
- Verify continuity
- Re-seat all connections

---

### Step 3: Test Components Individually

**LED Test:**
- Connect LED directly: 5V → 220Ω → LED → GND
- Should light up
- If not: Check orientation, resistor, LED

**Button Test:**
- Connect button: 5V → Button → Pin 2
- Add pull-down: Pin 2 → 10kΩ → GND
- Read pin in code, should change when pressed

**Sensor Test:**
- Connect sensor properly
- Read value in serial monitor or S4A
- Verify value changes appropriately
- Compare to expected range

**Motor Test:**
- Connect motor with appropriate driver
- Use simple code to test
- Verify power supply adequate
- Check for mechanical issues

---

### Step 4: Check Code

**Code Verification:**
- [ ] Pin numbers match wiring
- [ ] Correct pin mode (input/output)
- [ ] Logic is correct
- [ ] No syntax errors
- [ ] Timing appropriate

**Common Code Mistakes:**
- Wrong pin numbers
- Missing delays
- Logic errors (if-then conditions)
- Wrong data types
- Missing initialization

**Testing Code:**
- Start with simplest code
- Add complexity gradually
- Test each addition
- Use serial monitor for debugging
- Add print statements to track execution

---

### Step 5: Use Tools

**Multimeter:**
- Test voltage at pins
- Check continuity
- Measure resistance
- Verify component values

**Serial Monitor:**
- Print sensor values
- Debug code execution
- Track variable values
- Identify where code fails

**LED Test Circuit:**
- Simple circuit to test components
- Quick verification tool
- Isolate problems

---

## Common Problems and Solutions

### Problem: Nothing Works

**Possible Causes:**
- No power
- Wrong connections
- Code not running
- Arduino not connected

**Solutions:**
1. Check power LED on Arduino
2. Verify USB connection
3. Check S4A connection status
4. Verify code is running (green flag clicked)
5. Check all wiring

---

### Problem: LED Doesn't Light

**Possible Causes:**
- Wrong polarity (LED backwards)
- Missing or wrong resistor
- Wrong pin number
- LED burned out
- No power

**Solutions:**
1. Check LED orientation (long leg = +)
2. Verify 220Ω resistor
3. Check pin number in code
4. Test LED with known-good circuit
5. Try different LED

---

### Problem: Button Doesn't Work

**Possible Causes:**
- Missing pull-up/pull-down resistor
- Wrong pin number
- Button not connected properly
- Code logic error

**Solutions:**
1. Add 10kΩ pull-down resistor
2. Verify pin number
3. Check button connections
4. Test with simple code
5. Verify button works (test with multimeter)

---

### Problem: Sensor Reads Wrong Values

**Possible Causes:**
- Wrong wiring
- Sensor damaged
- Need calibration
- Wrong pin
- Interference

**Solutions:**
1. Verify wiring diagram
2. Test sensor with multimeter
3. Calibrate sensor (adjust code)
4. Check for interference
5. Try different sensor

---

### Problem: Servo Doesn't Move

**Possible Causes:**
- Not enough power
- Wrong pin (not PWM)
- Servo damaged
- Code error
- Wiring issue

**Solutions:**
1. Use external power for servo
2. Verify PWM pin (9, 10, or 11)
3. Test with simple code
4. Check servo wiring
5. Try different servo

---

### Problem: Multiple Components Not Working

**Possible Causes:**
- Power supply inadequate
- Short circuit
- Wiring errors
- Code conflicts

**Solutions:**
1. Check total current draw
2. Use external power if needed
3. Check for short circuits
4. Test each component individually
5. Verify all wiring
6. Simplify code, add components one at a time

---

### Problem: Arduino Not Recognized

**Possible Causes:**
- USB driver not installed
- Faulty USB cable
- Wrong USB port
- Arduino board issue

**Solutions:**
1. Install Arduino drivers
2. Try different USB cable
3. Try different USB port
4. Test on different computer
5. Check device manager (Windows)

---

### Problem: S4A Won't Connect

**Possible Causes:**
- Firmware not uploaded
- Wrong COM port
- Another program using Arduino
- S4A issue

**Solutions:**
1. Re-upload firmware
2. Check COM port selection
3. Close other programs (Arduino IDE)
4. Restart S4A
5. Reconnect Arduino

---

## Component-Specific Troubleshooting

### LEDs

**Won't Light:**
- Check polarity
- Verify resistor (220Ω)
- Test with multimeter
- Try different LED

**Too Dim:**
- Resistor too large
- Not enough power
- LED aging

**Burns Out:**
- Missing resistor
- Too much current
- Wrong voltage

---

### Buttons

**Always Reads HIGH:**
- Missing pull-down resistor
- Button stuck
- Wiring issue

**Always Reads LOW:**
- Missing pull-up
- Button not connected
- Wiring issue

**Intermittent:**
- Loose connection
- Bad button
- Need debouncing (advanced)

---

### Sensors

**Reads Constant Value:**
- Sensor not connected properly
- Sensor damaged
- Wrong pin
- Need calibration

**Reads Wrong Range:**
- Need calibration
- Wrong formula
- Sensor type mismatch
- Interference

**No Response:**
- No power to sensor
- Wrong wiring
- Sensor damaged
- Code issue

---

### Motors

**Won't Move:**
- Not enough power
- Wrong wiring
- Motor damaged
- Code error

**Moves Wrong Direction:**
- Reverse motor wires
- Code logic error

**Jittery Movement:**
- Power supply issue
- Need smoothing (advanced)
- Mechanical issue

---

## Advanced Troubleshooting

### Using Multimeter

**Voltage Testing:**
- Set to DC voltage
- Red probe to test point
- Black probe to ground
- Read voltage

**Continuity Testing:**
- Set to continuity mode
- Test connections
- Should beep if connected
- No beep = broken connection

**Resistance Testing:**
- Set to resistance mode
- Test resistor values
- Compare to color code
- Verify component

---

### Code Debugging

**Serial Monitor:**
- Print variable values
- Track execution
- Identify errors
- Monitor sensor readings

**Step-by-Step:**
- Add print statements
- Test each section
- Isolate problem area
- Fix one issue at a time

**Simplified Code:**
- Start with minimal code
- Add features gradually
- Test each addition
- Identify where it breaks

---

## Prevention Strategies

### Before Building

1. **Plan:**
   - Draw circuit diagram
   - List components
   - Check power requirements
   - Verify pin assignments

2. **Prepare:**
   - Gather all components
   - Check component values
   - Verify components work
   - Organize workspace

3. **Review:**
   - Check wiring diagram
   - Verify code logic
   - Review safety guidelines
   - Have tools ready

### During Building

1. **Build Incrementally:**
   - Add one component at a time
   - Test after each addition
   - Verify before continuing

2. **Check Frequently:**
   - Verify connections
   - Test functionality
   - Check for errors
   - Document what works

3. **Stay Organized:**
   - Keep wiring neat
   - Label connections
   - Document changes
   - Take photos

### After Building

1. **Test Thoroughly:**
   - Test all functions
   - Verify under different conditions
   - Check for edge cases
   - Document results

2. **Document:**
   - Take photos
   - Write notes
   - Save code
   - Share solutions

---

## Troubleshooting Checklist

### Quick Check
- [ ] Power on?
- [ ] Arduino connected?
- [ ] Code running?
- [ ] Wiring correct?
- [ ] Components good?

### Detailed Check
- [ ] All connections secure?
- [ ] Pin numbers match?
- [ ] Resistor values correct?
- [ ] Component orientation correct?
- [ ] Power supply adequate?
- [ ] No short circuits?
- [ ] Code logic correct?
- [ ] Components tested individually?

---

## Getting Help

### When to Ask for Help
- After trying systematic approach
- When safety is concern
- When stuck for >15 minutes
- When component might be damaged

### What Information to Provide
- What you're trying to do
- What's not working
- What you've tried
- Photos of circuit
- Code you're using
- Error messages (if any)

### Resources
- Workshop facilitators
- Online forums
- Component datasheets
- Tutorial videos
- Documentation

---

## Remember

- **Patience:** Troubleshooting takes time
- **Systematic:** Follow the process
- **Documentation:** Write down what works
- **Learning:** Every problem teaches something
- **Help:** Don't hesitate to ask
- **Safety:** Always prioritize safety

Most problems have simple solutions. Stay calm, be systematic, and you'll solve it!

