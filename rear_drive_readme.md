# Rear-Wheel Drive Robot Car - Raspberry Pi Pico W

A Python program to control a 2-wheel rear-drive robot car using a Raspberry Pi Pico W. This configuration features 2 powered wheels at the rear and 2 static caster wheels at the front, providing exceptional reverse maneuverability similar to a shopping cart!

## Features

- 🛒 **Rear-Wheel Drive** - Superior reverse turning ability
- 🔄 **Shopping Cart Dynamics** - Front casters provide natural steering
- 🎮 **Differential Steering** - Control turns by varying wheel speeds
- 🔧 **PWM Motor Control** - Smooth speed control
- 🎯 **Enhanced Reverse Control** - Separate forward and reverse arc functions
- 🚗 **Real-World Maneuvers** - Parallel parking and three-point turn demos
- ⚡ **Efficient Design** - Only 2 motors, simple wiring

## Hardware Configuration

```
        FRONT (Static Wheels)
    ┌─────────────────────────┐
    │    🔘           🔘      │
    │  CASTER     CASTER      │
    │                         │
    │      ROBOT BODY         │
    │                         │
    │    ⚙️           ⚙️      │
    │   LEFT       RIGHT      │
    │  MOTOR      MOTOR       │
    └─────────────────────────┘
        REAR (Powered Wheels)
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
GPIO 0         →    IN1 (Left)      →    Rear Left Motor (+)
GPIO 1         →    IN2 (Left)      →    Rear Left Motor (-)
GPIO 2         →    IN3 (Right)     →    Rear Right Motor (+)
GPIO 3         →    IN4 (Right)     →    Rear Right Motor (-)

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
4. Save as `main.py` (auto-run on boot) or `rear_drive.py`

## Usage

### Basic Demo

Run the comprehensive movement demo:

```python
from rear_drive import demo
demo()
```

### Custom Control

```python
from rear_drive import RearDriveRobot

robot = RearDriveRobot()

# Basic movements
robot.forward(speed=60)
robot.backward(speed=60)
robot.stop()

# Turning while moving forward
robot.turn_left_forward(speed=60)
robot.turn_right_forward(speed=60)

# Turning while moving backward (very agile!)
robot.turn_left_reverse(speed=60)
robot.turn_right_reverse(speed=60)

# Spinning in place
robot.spin_left(speed=50)
robot.spin_right(speed=50)

# Arc turns - forward
robot.arc_left(speed=60, turn_ratio=0.5)
robot.arc_right(speed=60, turn_ratio=0.3)

# Arc turns - reverse (special advantage!)
robot.arc_left_reverse(speed=60, turn_ratio=0.3)
robot.arc_right_reverse(speed=60, turn_ratio=0.3)
```

### Special Maneuver Demos

```python
from rear_drive import parallel_parking_demo, three_point_turn, navigation_pattern

# Demonstrate parking skills
parallel_parking_demo()

# Execute a three-point turn
three_point_turn()

# Navigate using reverse turns
navigation_pattern()
```

## API Reference

### RearDriveRobot Class

#### Core Methods

- **`move(left_speed, right_speed)`** - Direct motor control (-100 to 100)
- **`forward(speed=50)`** - Move forward
- **`backward(speed=50)`** - Move backward (excellent control!)
- **`stop()`** - Stop all motors

#### Forward Turning Methods

- **`turn_left_forward(speed=50)`** - Turn left while moving forward
- **`turn_right_forward(speed=50)`** - Turn right while moving forward
- **`arc_left(speed=50, turn_ratio=0.5)`** - Smooth left arc (forward)
- **`arc_right(speed=50, turn_ratio=0.5)`** - Smooth right arc (forward)

#### Reverse Turning Methods (Special Feature!)

- **`turn_left_reverse(speed=50)`** - Turn left while reversing (very tight!)
- **`turn_right_reverse(speed=50)`** - Turn right while reversing (very tight!)
- **`arc_left_reverse(speed=50, turn_ratio=0.5)`** - Smooth left arc (reverse)
- **`arc_right_reverse(speed=50, turn_ratio=0.5)`** - Smooth right arc (reverse)

#### Rotation Methods

- **`spin_left(speed=50)`** - Spin counter-clockwise in place
- **`spin_right(speed=50)`** - Spin clockwise in place

### Speed Parameters

- All speed values range from 0 to 100
- Negative values in `move()` reverse motor direction
- `turn_ratio`: 0.0 (sharp turn) to 1.0 (gentle turn)

## Movement Characteristics

### Advantages of Rear-Wheel Drive

✅ **Exceptional reverse control** - Like a shopping cart, turns easily backwards  
✅ **Tight reverse turns** - Front casters pivot freely  
✅ **Natural steering** - Front casters lead the direction  
✅ **Excellent for parking** - Superior backing maneuvers  
✅ **Versatile maneuvering** - Great for tight spaces  

### Unique Capabilities

🌟 **Shopping Cart Effect** - The robot behaves like a shopping cart, making it intuitive to control in reverse  
🌟 **Zero-Radius Reverse Turns** - Can pivot around a point when reversing  
🌟 **Parallel Parking** - Excellent for backing into tight spots  

### Limitations

❌ **Forward turning radius** - Slightly wider than front-drive  
⚠️ **Less predictable forward** - Casters can wander slightly  

### Best Use Cases

- 🚗 Parking and docking applications
- 📦 Precise positioning tasks
- 🏭 Warehouse navigation (backing into loading zones)
- 🎯 Tight space maneuvering
- 🔄 Situations requiring frequent direction changes

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

### Robot wanders when moving forward

**Cause:** Normal for rear-drive - front casters can drift  
**Solution:** 
- Use quality casters with minimal play
- Ensure floor is smooth and level
- Adjust speed to maintain control
- Add weight to front for stability

### Excellent reverse control but tricky forward

**Cause:** This is expected! Rear-drive excels in reverse  
**Solution:** 
- Embrace the reverse turning advantage
- Use forward movement for straight paths
- Use reverse for precision maneuvering

### Casters don't pivot smoothly in reverse

**Cause:** Caster quality or debris  
**Solution:**
- Use high-quality ball casters
- Clean caster wheels regularly
- Lubricate swivel mechanism if applicable
- Test on smooth surfaces

### Motors don't respond

**Cause:** Wiring or power issue  
**Solution:**
- Check all connections
- Verify battery voltage
- Test motors directly with motor driver
- Check GPIO pin assignments in code

## Demo Programs

### 1. Basic Movement Demo

Tests all movement functions including forward and reverse turns:
```python
demo()
```

### 2. Parallel Parking

Demonstrates the rear-drive advantage for parking maneuvers:
```python
parallel_parking_demo()
```

### 3. Three-Point Turn

Shows how to execute a U-turn using forward and reverse:
```python
three_point_turn()
```

### 4. Navigation Pattern

Uses reverse turning for navigation (rear-drive advantage):
```python
navigation_pattern()
```

## Safety Guidelines

⚠️ **Important Safety Notes:**

- Start with low speed values (30-40) for testing
- Ensure adequate space for robot movement
- Keep fingers away from wheels during operation
- Use appropriate voltage for your motors
- Add emergency stop button for safety
- Supervise robot operation at all times
- Test reverse movements in open space first

## Performance Tips

### Optimal Performance

1. **Caster Placement** - Position front casters for balanced weight distribution
2. **Weight Distribution** - Center of gravity should be slightly forward
3. **Caster Quality** - Use ball casters for smoother operation
4. **Battery Placement** - Mount over rear wheels for traction

### Maximizing Reverse Turning

```python
# Very tight reverse turn
robot.turn_left_reverse(70)
time.sleep(1.0)

# Ultra-sharp reverse arc
robot.arc_right_reverse(60, turn_ratio=0.1)
```

### Calibrating Turn Angles

```python
# Adjust timing for specific turn angles
robot.spin_right(50)
time.sleep(0.65)  # Tune for 90° turn
robot.stop()
```

## Extensions and Upgrades

### Add Sensors

- 🔊 Rear ultrasonic sensor for backing assistance
- 📡 Front IR sensors for obstacle detection
- 🧭 IMU for precise angle control
- 📹 Camera for vision-guided parking

### Autonomous Features

- 🅿️ Automatic parallel parking
- 🎯 Precision docking
- 🗺️ Reverse path following
- 🔄 Automatic three-point turns

### Remote Control

- 📱 WiFi control with reverse camera view
- 🎮 Gamepad with trigger-based reverse
- 📻 RF remote with dedicated reverse controls

## Example Projects

### Automatic Parking Assistant

```python
# Pseudocode - add distance sensors
def auto_park():
    # Move forward past parking spot
    robot.forward(50)
    wait_for_opening()
    
    # Back into spot
    robot.turn_right_reverse(55)
    time.sleep(1.5)
    
    # Straighten
    robot.turn_left_reverse(55)
    time.sleep(1.0)
    
    # Final positioning
    robot.backward(40)
    time.sleep(0.5)
    robot.stop()
```

### Warehouse Dock Robot

```python
# Pseudocode - precision backing
def dock_at_station():
    # Approach station
    robot.forward(50)
    
    # Precise reverse docking
    while not at_dock():
        distance = get_rear_sensor()
        speed = map_distance_to_speed(distance)
        robot.backward(speed)
    
    robot.stop()
```

## Comparison with Other Configurations

| Feature | Rear-Drive | Front-Drive | 4-Wheel |
|---------|------------|-------------|---------|
| Forward agility | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ |
| Reverse agility | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ |
| Parking ability | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ |
| Simplicity | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ |
| Cost | 💰💰 | 💰💰 | 💰💰💰 |

## Real-World Analogy

**Think of it like a shopping cart:**
- Push forward → Steers somewhat predictably
- Pull backward → Turns on a dime!
- Rear wheels provide power, front casters follow

This is why forklifts and many warehouse vehicles use rear-wheel drive!

## Advanced Techniques

### Drift Turns (in reverse)

```python
# Sharp drift-like turn in reverse
robot.arc_right_reverse(80, turn_ratio=0.0)
time.sleep(0.8)
robot.stop()
```

### Precision Alignment

```python
# Use tiny reverse movements for alignment
def align_precisely():
    robot.backward(30)
    time.sleep(0.1)
    robot.stop()
    time.sleep(0.2)
```

## License

This project is open source and available under the MIT License.

## Contributing

Contributions welcome! Especially interested in:
- Parking algorithm improvements
- Sensor integration examples
- Path planning for reverse navigation

## Support

For questions or issues:
- Check the troubleshooting section
- Review MicroPython documentation
- Test reverse movements in open space first

---

**Happy Building! 🛒🤖**

*Remember: When in doubt, back it up! This robot loves reverse!*