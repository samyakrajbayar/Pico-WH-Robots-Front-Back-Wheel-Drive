from machine import Pin, PWM
import time

class FrontDriveRobot:
    """
    Robot with 2 powered wheels at the FRONT and 2 static caster wheels at the REAR
    This configuration provides good forward pushing power and easy turning
    """
    def __init__(self):
        # Motor pins - adjust GPIO numbers based on your wiring
        # Front Left Motor (powered)
        self.left_fwd = PWM(Pin(0))
        self.left_rev = PWM(Pin(1))
        
        # Front Right Motor (powered)
        self.right_fwd = PWM(Pin(2))
        self.right_rev = PWM(Pin(3))
        
        # Set PWM frequency (1kHz is typical for DC motors)
        self.motors = [
            self.left_fwd, self.left_rev,
            self.right_fwd, self.right_rev
        ]
        
        for motor in self.motors:
            motor.freq(1000)
        
        self.max_speed = 65535  # 16-bit PWM resolution
        self.stop()
    
    def set_motor(self, fwd_pin, rev_pin, speed):
        """Set individual motor speed (-100 to 100)"""
        speed = max(-100, min(100, speed))  # Clamp speed
        duty = int(abs(speed) * self.max_speed / 100)
        
        if speed > 0:
            fwd_pin.duty_u16(duty)
            rev_pin.duty_u16(0)
        elif speed < 0:
            fwd_pin.duty_u16(0)
            rev_pin.duty_u16(duty)
        else:
            fwd_pin.duty_u16(0)
            rev_pin.duty_u16(0)
    
    def move(self, left_speed, right_speed):
        """
        Move robot with differential drive control
        left_speed: left front motor speed (-100 to 100)
        right_speed: right front motor speed (-100 to 100)
        """
        self.set_motor(self.left_fwd, self.left_rev, left_speed)
        self.set_motor(self.right_fwd, self.right_rev, right_speed)
    
    def forward(self, speed=50):
        """Move forward - front wheels push, rear casters follow"""
        self.move(speed, speed)
    
    def backward(self, speed=50):
        """Move backward - front wheels pull, rear casters pivot"""
        self.move(-speed, -speed)
    
    def turn_left(self, speed=50):
        """Turn left while moving forward"""
        self.move(0, speed)
    
    def turn_right(self, speed=50):
        """Turn right while moving forward"""
        self.move(speed, 0)
    
    def spin_left(self, speed=50):
        """Spin left in place - tight turn around center"""
        self.move(-speed, speed)
    
    def spin_right(self, speed=50):
        """Spin right in place - tight turn around center"""
        self.move(speed, -speed)
    
    def arc_left(self, speed=50, turn_ratio=0.5):
        """
        Smooth arc turn to the left
        turn_ratio: 0 (sharp) to 1 (gentle)
        """
        right_speed = speed
        left_speed = int(speed * turn_ratio)
        self.move(left_speed, right_speed)
    
    def arc_right(self, speed=50, turn_ratio=0.5):
        """
        Smooth arc turn to the right
        turn_ratio: 0 (sharp) to 1 (gentle)
        """
        left_speed = speed
        right_speed = int(speed * turn_ratio)
        self.move(left_speed, right_speed)
    
    def pivot_left(self, speed=50):
        """Pivot around left wheel (left wheel stopped, right wheel moves)"""
        self.move(0, speed)
    
    def pivot_right(self, speed=50):
        """Pivot around right wheel (right wheel stopped, left wheel moves)"""
        self.move(speed, 0)
    
    def stop(self):
        """Stop all motors"""
        for motor in self.motors:
            motor.duty_u16(0)

# Demo program
def demo():
    robot = FrontDriveRobot()
    
    print("Front-Wheel Drive Robot Demo")
    print("2 powered wheels at FRONT, 2 static casters at REAR")
    print("="*50)
    
    try:
        # Forward movement
        print("Moving forward...")
        robot.forward(60)
        time.sleep(2)
        robot.stop()
        time.sleep(1)
        
        # Backward movement (casters will pivot)
        print("Moving backward...")
        robot.backward(60)
        time.sleep(2)
        robot.stop()
        time.sleep(1)
        
        # Turn left while moving
        print("Turning left (forward)...")
        robot.turn_left(60)
        time.sleep(1.5)
        robot.stop()
        time.sleep(1)
        
        # Turn right while moving
        print("Turning right (forward)...")
        robot.turn_right(60)
        time.sleep(1.5)
        robot.stop()
        time.sleep(1)
        
        # Spin in place (left)
        print("Spinning left in place...")
        robot.spin_left(50)
        time.sleep(1.5)
        robot.stop()
        time.sleep(1)
        
        # Spin in place (right)
        print("Spinning right in place...")
        robot.spin_right(50)
        time.sleep(1.5)
        robot.stop()
        time.sleep(1)
        
        # Smooth arc turns
        print("Arc left (gentle curve)...")
        robot.arc_left(60, turn_ratio=0.6)
        time.sleep(2)
        robot.stop()
        time.sleep(1)
        
        print("Arc right (sharp curve)...")
        robot.arc_right(60, turn_ratio=0.3)
        time.sleep(2)
        robot.stop()
        time.sleep(1)
        
        print("\nDemo complete!")
        
    except KeyboardInterrupt:
        print("\nStopping robot...")
        robot.stop()

# Figure-8 pattern demo
def figure_eight():
    robot = FrontDriveRobot()
    
    print("Figure-8 Pattern Demo")
    
    try:
        # First loop
        print("First circle (right)...")
        robot.arc_right(60, turn_ratio=0.4)
        time.sleep(4)
        
        # Second loop
        print("Second circle (left)...")
        robot.arc_left(60, turn_ratio=0.4)
        time.sleep(4)
        
        robot.stop()
        print("Figure-8 complete!")
        
    except KeyboardInterrupt:
        print("\nStopping robot...")
        robot.stop()

# Obstacle avoidance simulation
def obstacle_avoidance_demo():
    """
    Simulates obstacle avoidance behavior
    In real application, use ultrasonic or IR sensors
    """
    robot = FrontDriveRobot()
    
    print("Obstacle Avoidance Demo (simulated)")
    print("Robot will move forward and make turns as if avoiding obstacles")
    
    try:
        for i in range(3):
            # Move forward
            print(f"Moving forward {i+1}...")
            robot.forward(60)
            time.sleep(2)
            
            # "Detect obstacle" - turn
            robot.stop()
            time.sleep(0.3)
            
            print("Avoiding obstacle (turning)...")
            robot.spin_right(50)
            time.sleep(1)
            
            robot.stop()
            time.sleep(0.3)
        
        robot.stop()
        print("Avoidance demo complete!")
        
    except KeyboardInterrupt:
        print("\nStopping robot...")
        robot.stop()

# Run the demos
if __name__ == "__main__":
    print("\n" + "="*50)
    print("FRONT-WHEEL DRIVE ROBOT")
    print("Powered wheels: FRONT | Static wheels: REAR")
    print("="*50 + "\n")
    
    demo()
    
    # Uncomment to run other demos:
    # figure_eight()
    # obstacle_avoidance_demo()
