# Scratch for Arduino (S4A) Setup Instructions
## Complete Installation and Configuration Guide

## What is S4A?

**Scratch for Arduino (S4A)** is a modified version of Scratch that allows you to control Arduino hardware using visual programming blocks. It's perfect for beginners who want to do physical computing without learning text-based programming.

**Key Features:**
- Visual, block-based programming (like Scratch)
- Direct Arduino control
- Real-time sensor reading
- Easy to learn, powerful to use

---

## System Requirements

### Windows
- Windows 7 or later
- USB port
- Internet connection (for download)

### Mac
- macOS 10.9 or later
- USB port
- Internet connection (for download)

### Linux
- Most distributions supported
- USB port
- Internet connection (for download)

---

## Step-by-Step Installation

### Step 1: Download S4A

1. **Go to:** http://s4a.cat
2. **Click:** "Download" button
3. **Select:** Your operating system
4. **Download:** The installer file
5. **Save:** To your Downloads folder

**Alternative Download:**
- Direct link: http://s4a.cat/downloads/S4A16.zip (Windows)
- Check website for latest version

### Step 2: Install Arduino Drivers

**Why:** Your computer needs to recognize the Arduino board.

#### Windows

**Automatic Installation (Recommended):**
1. Connect Arduino to computer via USB
2. Windows should automatically detect and install drivers
3. Wait for "Device ready" notification

**Manual Installation (If Needed):**
1. Download Arduino IDE from: https://www.arduino.cc/en/software
2. Install Arduino IDE (includes drivers)
3. Or download drivers separately from Arduino website

**Verify Installation:**
1. Open Device Manager (Windows Key + X, then select Device Manager)
2. Look for "Arduino Uno" under "Ports (COM & LPT)"
3. Note the COM port number (e.g., COM3, COM4)

#### Mac

**Automatic Installation:**
1. Connect Arduino to computer via USB
2. Mac should automatically recognize device
3. No additional drivers needed for most Macs

**Verify Installation:**
1. Open System Information
2. Go to USB section
3. Look for "Arduino Uno"

#### Linux

**Installation:**
```bash
# Ubuntu/Debian
sudo apt-get install arduino

# Or add user to dialout group
sudo usermod -a -G dialout $USER
# Log out and back in
```

**Verify Installation:**
```bash
ls /dev/ttyACM*  # or /dev/ttyUSB*
```

### Step 3: Install S4A

#### Windows

1. **Extract ZIP file:**
   - Right-click downloaded file
   - Select "Extract All"
   - Choose extraction location

2. **Run S4A:**
   - Navigate to extracted folder
   - Double-click "S4A.exe"
   - No installation needed (portable version)

3. **Create Shortcut (Optional):**
   - Right-click S4A.exe
   - Select "Create Shortcut"
   - Move shortcut to Desktop

#### Mac

1. **Extract ZIP file:**
   - Double-click downloaded .zip file
   - It will extract automatically

2. **Move to Applications:**
   - Drag S4A folder to Applications folder

3. **Run S4A:**
   - Open Applications folder
   - Double-click S4A application
   - If security warning appears:
     - Go to System Preferences → Security & Privacy
     - Click "Open Anyway"

#### Linux

1. **Extract:**
   ```bash
   unzip S4A16.zip
   cd S4A16
   ```

2. **Make Executable:**
   ```bash
   chmod +x S4A
   ```

3. **Run:**
   ```bash
   ./S4A
   ```

---

## Step 4: Upload Firmware to Arduino

**Important:** This step is required once per Arduino board.

### Why Firmware?
- S4A needs special firmware on Arduino to communicate
- Firmware allows Scratch blocks to control Arduino
- Must be uploaded before first use

### Upload Process

1. **Connect Arduino:**
   - Connect Arduino to computer via USB
   - Wait for computer to recognize it
   - Note the COM port (Windows) or device name (Mac/Linux)

2. **Open S4A:**
   - Launch S4A application
   - Wait for interface to load

3. **Upload Firmware:**
   - In S4A, go to **"Board"** menu
   - Select **"Upload Firmware"**
   - Wait for upload process
   - Look for "Firmware uploaded successfully" message

4. **Verify Connection:**
   - In S4A, you should see "Arduino found on [port]"
   - Green indicator shows connection status

### Troubleshooting Firmware Upload

**Problem: "Arduino not found"**
- **Solution:** Check USB connection, try different USB port
- **Solution:** Verify drivers are installed
- **Solution:** Close other programs using Arduino (Arduino IDE)

**Problem: "Upload failed"**
- **Solution:** Disconnect and reconnect Arduino
- **Solution:** Try different USB cable
- **Solution:** Restart S4A

**Problem: "Permission denied" (Linux)**
- **Solution:** Add user to dialout group:
  ```bash
  sudo usermod -a -G dialout $USER
  ```
- **Solution:** Log out and back in

---

## Step 5: Test Your Setup

### Simple Test: Blink Built-in LED

1. **Open S4A**

2. **Create Simple Script:**
   - From **Events**, drag `when green flag clicked`
   - From **Control**, drag `forever` block
   - From **S4A** category (special blocks), drag:
     - `digital pin 13 on`
     - `wait 1 secs`
     - `digital pin 13 off`
     - `wait 1 secs`

3. **Connect Blocks:**
   ```
   when green flag clicked
   forever
       digital pin 13 on
       wait 1 secs
       digital pin 13 off
       wait 1 secs
   end
   ```

4. **Click Green Flag:**
   - LED on Arduino board should blink
   - If it works, setup is successful!

### If Test Fails

**Check:**
- Arduino is connected via USB
- Firmware is uploaded
- Correct COM port selected (if multiple ports)
- S4A shows "Arduino found"

**Try:**
- Re-upload firmware
- Restart S4A
- Reconnect Arduino
- Check USB cable

---

## S4A Interface Overview

### Main Window

```
┌─────────────────────────────────────────┐
│  File  Edit  Share  [Menu Bar]        │
├──────────┬──────────────┬──────────────┤
│          │              │              │
│  Stage   │  Scripts    │  Blocks     │
│  Area    │  Area        │  Palette    │
│          │              │              │
│          │              │              │
│          ├──────────────┤              │
│          │  Sprite List │              │
│          └──────────────┘              │
└─────────────────────────────────────────┘
```

### S4A-Specific Blocks

**S4A Category (Special Blocks):**

**Digital Output:**
- `digital pin [X] on` - Turn pin HIGH
- `digital pin [X] off` - Turn pin LOW

**Analog Output (PWM):**
- `analog pin [X] to [value]` - Set PWM value (0-255)

**Digital Input:**
- `digital pin [X]` - Read digital value (0 or 1)

**Analog Input:**
- `analog pin [X]` - Read analog value (0-1023)

**Servo Control:**
- `servo pin [X] to [angle]` - Set servo angle (0-180)

**Special:**
- `board connected?` - Check if Arduino is connected
- `reset all digital pins` - Reset all pins to LOW

---

## Configuration Settings

### Selecting COM Port (Windows)

1. **In S4A:**
   - Go to **"Board"** menu
   - Select **"Select Serial Port"**
   - Choose correct COM port (e.g., COM3, COM4)

2. **Finding COM Port:**
   - Open Device Manager
   - Look under "Ports (COM & LPT)"
   - Find "Arduino Uno" and note COM number

### Selecting Device (Mac/Linux)

1. **In S4A:**
   - Go to **"Board"** menu
   - Select **"Select Serial Port"**
   - Choose device (e.g., /dev/tty.usbmodem...)

2. **Finding Device:**
   - Mac: System Information → USB
   - Linux: `ls /dev/ttyACM*` or `/dev/ttyUSB*`

---

## Common Issues and Solutions

### Issue 1: S4A Won't Start

**Windows:**
- Check if .NET Framework is installed
- Try running as Administrator
- Check antivirus isn't blocking it

**Mac:**
- Check security settings
- Allow in System Preferences → Security

**Linux:**
- Check permissions
- Install required libraries

### Issue 2: Arduino Not Found

**Solutions:**
- Verify USB connection
- Check COM port selection
- Re-upload firmware
- Try different USB port
- Restart S4A

### Issue 3: Blocks Don't Work

**Solutions:**
- Verify firmware is uploaded
- Check Arduino is connected
- Verify correct pin numbers
- Check wiring connections

### Issue 4: Connection Drops

**Solutions:**
- Check USB cable quality
- Try different USB port
- Avoid USB hubs (use direct connection)
- Check power supply

---

## Best Practices

1. **Always Upload Firmware First**
   - Required for each new Arduino
   - Re-upload if having connection issues

2. **Check Connection Status**
   - Look for "Arduino found" message
   - Green indicator shows connection

3. **Save Your Projects**
   - S4A projects save as .sb files
   - Save frequently
   - Use descriptive names

4. **Test Incrementally**
   - Test simple code first
   - Add complexity gradually
   - Verify each step works

5. **Keep S4A Updated**
   - Check website for updates
   - New versions may have bug fixes

---

## Alternative: Arduino IDE

**If S4A doesn't work, you can use Arduino IDE:**
- Download from: https://www.arduino.cc/en/software
- More complex but more powerful
- Text-based programming (C++)
- Can upload S4A firmware manually

**Uploading S4A Firmware via Arduino IDE:**
1. Download S4A firmware from S4A website
2. Open in Arduino IDE
3. Select correct board and port
4. Upload to Arduino

---

## Quick Reference

### Installation Checklist
- [ ] Downloaded S4A
- [ ] Installed Arduino drivers
- [ ] Extracted/installed S4A
- [ ] Connected Arduino via USB
- [ ] Uploaded firmware to Arduino
- [ ] Tested with simple blink program
- [ ] Verified connection status

### First Project Checklist
- [ ] Arduino connected and recognized
- [ ] Firmware uploaded
- [ ] Correct COM port selected
- [ ] Simple test program works
- [ ] Ready for Day 2 projects!

---

## Support Resources

### Official Resources
- **S4A Website:** http://s4a.cat
- **S4A Documentation:** http://s4a.cat/docs
- **S4A Forum:** Check website for community links

### Troubleshooting
- Check S4A website FAQ
- Search online forums
- Ask workshop facilitators
- Check Arduino official documentation

---

## Next Steps

After successful setup:
1. Practice with simple projects
2. Explore S4A blocks
3. Try Day 2 projects
4. Experiment with sensors
5. Design your own projects

**Remember:** If you encounter issues, don't hesitate to ask for help. Setup problems are common and usually easy to fix!

