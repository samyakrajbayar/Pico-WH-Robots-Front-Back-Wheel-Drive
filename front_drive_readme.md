# Front-Wheel Drive Robot Car - Raspberry Pi Pico W

A Python program to control a 2-wheel front-drive robot car using a Raspberry Pi Pico W. This configuration features 2 powered wheels at the front and 2 static caster wheels at the rear, providing excellent forward pushing power and natural steering.

## Features

- 🚗 **Front-Wheel Drive** - Powered wheels lead the direction
- 🎮 **Differential Steering** - Control turns by varying wheel speeds
- 🔧 **PWM Motor Control** - Smooth speed control
- 🎯 **Multiple Movement Modes** - Forward, backward, turns, spins, and arcs
- 📊 **Demo Programs** - Including figure-8 and obstacle avoidance patterns
- ⚡ **Efficient Design** - Only 2 motors, simple wiring

## Hardware Configuration

```
        FRONT (Powered Wheels)
    ┌─────────────────────────┐
    │    ⚙️           ⚙️      │
    │   LEFT       RIGHT      │
    │  MOTOR      MOTOR       │
    │                         │
    │      ROBOT BODY         │
    │                         │
    │    🔘           🔘      │
    │  CASTER     CASTER      │
    └─────────────────────────┘
        REAR (Static Wheels)
```

### Components Required

- 1x Raspberry Pi Pico W
- 2x DC motors with wheels
- 2x Caster wheels (ball casters or swivel casters)
- 1x Motor driver board (L298N, TB6612FNG, or DRV8833)
- 1x Battery pack (5-12V depending on motors)
- 1x Robot chassis
- Jumper wires
- Mounting hardware

### Wiring Diagram

```
Pico W GPIO    →    Motor Driver    →    Motor
─────────────────────────────────────────────────
GPIO 0         →    IN1 (Left)      →    Front Left Motor (+)
GPIO 1         →    IN2 (Left)      →    Front Left Motor (-)
GPIO 2         →    IN3 (Right)     →    Front Right Motor (+)
GPIO 3         →    IN4 (Right)     →    Front Right Motor (-)

Pico W VBUS    →    Motor Driver VCC (if 5V logic)
Pico W GND     →    Motor Driver GND
Battery +      →    Motor Driver Motor Power (+)
Battery -      →    Motor Driver Motor Power (-)
```

## Software Requirements

- MicroPython firmware for Raspberry Pi Pico W
- Thonny IDE or compatible MicroPython IDE
- USB cable for programming

## Installation

### 1. Install MicroPython

1. Download MicroPython firmware from [micropython.org](https://micropython.org/download/rp2-pico-w/)
2. Hold BOOTSEL button while connecting Pico W to computer
3. Drag and drop the `.uf2` file to RPI-RP2 drive
4. Pico W will reboot with MicroPython installed

### 2. Upload the Program

1. Open Thonny IDE
2. Connect to your Pico W
3. Copy the program code
4. Save as `main.py` (auto-run on boot) or `front_drive.py`

## Usage

### Basic Demo

Run the comprehensive movement demo:

```python
from front_drive import demo
demo()
```

### Custom Control

```python
from front_drive import FrontDriveRobot

robot = FrontDriveRobot()

# Basic movements
robot.forward(speed=60)
robot.backward(speed=60)
robot.stop()

# Turning while moving
robot.turn_left(speed=60)
robot.turn_right(speed=60)

# Spinning in place
robot.spin_left(speed=50)
robot.spin_right(speed=50)

# Smooth arc turns
robot.arc_left(speed=60, turn_ratio=0.5)  # 0=sharp, 1=gentle
robot.arc_right(speed=60, turn_ratio=0.3)

# Pivot around one wheel
robot.pivot_left(speed=50)
robot.pivot_right(speed=50)
```

### Pattern Demos

```python
from front_drive import figure_eight, obstacle_avoidance_demo

# Drive in a figure-8 pattern
figure_eight()

# Simulate obstacle avoidance
obstacle_avoidance_demo()
```

## API Reference

### FrontDriveRobot Class

#### Core Methods

- **`move(left_speed, right_speed)`** - Direct motor control (-100 to 100)
- **`forward(speed=50)`** - Move forward
- **`backward(speed=50)`** - Move backward
- **`stop()`** - Stop all motors

#### Turning Methods

- **`turn_left(speed=50)`** - Turn left (right wheel only)
- **`turn_right(speed=50)`** - Turn right (left wheel only)
- **`spin_left(speed=50)`** - Spin counter-clockwise in place
- **`spin_right(speed=50)`** - Spin clockwise in place

#### Advanced Movement

- **`arc_left(speed=50, turn_ratio=0.5)`** - Smooth left arc
- **`arc_right(speed=50, turn_ratio=0.5)`** - Smooth right arc
- **`pivot_left(speed=50)`** - Pivot around left wheel
- **`pivot_right(speed=50)`** - Pivot around right wheel

### Speed Parameters

- All speed values range from 0 to 100
- Negative values in `move()` reverse motor direction
- `turn_ratio`: 0.0 (sharp turn) to 1.0 (gentle turn)

## Movement Characteristics

### Advantages of Front-Wheel Drive

✅ **Excellent forward control** - Powered wheels lead the direction  
✅ **Good traction when pushing** - Weight helps grip  
✅ **Predictable forward turning** - Front wheels steer naturally  
✅ **Simple design** - Rear casters follow automatically  

### Limitations

❌ **Less agile in reverse** - Casters need to pivot 180°  
❌ **Wider reverse turns** - Not ideal for backing into tight spaces  
⚠️ **Backward movement slower** - May need to pause for caster alignment  

### Best Use Cases

- 🎯 Forward-focused navigation
- 🏃 Racing and speed applications
- 📦 Pushing objects
- 🎪 Line following robots
- 🎮 General purpose robotics

## Configuration

### Adjusting GPIO Pins

```python
def __init__(self):
    self.left_fwd = PWM(Pin(0))   # Change pin numbers here
    self.left_rev = PWM(Pin(1))
    self.right_fwd = PWM(Pin(2))
    self.right_rev = PWM(Pin(3))
```

### Adjusting PWM Frequency

```python
for motor in self.motors:
    motor.freq(1000)  # Change frequency (Hz)
```

### Motor Direction Correction

If motors run in wrong direction, swap the pin assignments:

```python
# Swap these two lines for left motor
self.left_fwd = PWM(Pin(0))
self.left_rev = PWM(Pin(1))
```

## Troubleshooting

### Robot veers to one side

**Cause:** Motors have different speeds or wheel sizes differ  
**Solution:** 
- Calibrate motor speeds by adjusting individual speed values
- Check wheel alignment and mounting
- Ensure wheels are same diameter

### Difficulty turning backward

**Cause:** Normal for front-wheel drive - casters need to pivot  
**Solution:** 
- Reduce speed when reversing
- Add small pause after direction change
- Consider rear-wheel drive for reverse-heavy applications

### Caster wheels wobble or stick

**Cause:** Poor quality casters or debris  
**Solution:**
- Use quality ball casters or swivel casters
- Clean caster wheels regularly
- Ensure smooth floor surface

### Motors don't respond

**Cause:** Wiring or power issue  
**Solution:**
- Check all connections
- Verify battery voltage
- Test motors directly with motor driver
- Check GPIO pin assignments in code

## Demo Programs

### 1. Basic Movement Demo

Tests all movement functions in sequence:
```python
demo()
```

### 2. Figure-8 Pattern

Demonstrates smooth curved turning:
```python
figure_eight()
```

### 3. Obstacle Avoidance

Simulates navigation around obstacles:
```python
obstacle_avoidance_demo()
```

## Safety Guidelines

⚠️ **Important Safety Notes:**

- Start with low speed values (30-40) for testing
- Ensure adequate space for robot movement
- Keep fingers away from wheels during operation
- Use appropriate voltage for your motors
- Add emergency stop button for safety
- Supervise robot operation at all times

## Performance Tips

### Optimal Performance

1. **Caster Selection** - Use high-quality ball casters for smooth operation
2. **Weight Distribution** - Place battery over front wheels for better traction
3. **Wheel Size** - Larger front wheels provide better obstacle clearance
4. **Speed Calibration** - Fine-tune individual motor speeds for straight movement

### Improving Turn Accuracy

```python
# Adjust timing for 90-degree turn
robot.spin_right(50)
time.sleep(0.65)  # Tune this value
robot.stop()
```

## Extensions and Upgrades

### Add Sensors

- 🔊 Ultrasonic sensor for obstacle detection
- 📡 IR sensors for line following
- 🧭 IMU for orientation tracking

### Remote Control

- 📱 WiFi control via web interface
- 🎮 Bluetooth gamepad support
- 📻 RF remote control

### Autonomous Features

- 🗺️ Path planning algorithms
- 🤖 Wall following behavior
- 🎯 Target tracking

## Example Projects

### Line Following Robot

```python
# Pseudocode - add IR sensors
while True:
    if left_sensor_dark and right_sensor_light:
        robot.arc_right(50, 0.3)
    elif left_sensor_light and right_sensor_dark:
        robot.arc_left(50, 0.3)
    else:
        robot.forward(50)
```

### Room Explorer

```python
# Pseudocode - add ultrasonic sensor
while True:
    if distance < 20:  # Obstacle ahead
        robot.stop()
        robot.spin_right(50)
        time.sleep(random.uniform(0.5, 1.5))
    else:
        robot.forward(60)
```

## Comparison with Other Configurations

| Feature | Front-Drive | Rear-Drive | 4-Wheel |
|---------|-------------|------------|---------|
| Forward agility | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ |
| Reverse agility | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ |
| Simplicity | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ |
| Cost | 💰💰 | 💰💰 | 💰💰💰 |

## License

This project is open source and available under the MIT License.

## Contributing

Contributions welcome! Feel free to submit issues or pull requests.

## Support

For questions or issues:
- Check the troubleshooting section
- Review MicroPython documentation
- Test with simplified demo code

---

**Happy Building! 🚗🤖**