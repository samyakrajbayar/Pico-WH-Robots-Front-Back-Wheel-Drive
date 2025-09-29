from machine import Pin, PWM
import time

class RearDriveRobot:
    """
    Robot with 2 powered wheels at the REAR and 2 static caster wheels at the FRONT
    This configuration is similar to a shopping cart - rear wheels push, front casters steer
    """
    def __init__(self):
        # Motor pins - adjust GPIO numbers based on your wiring
        # Rear Left Motor (powered)
        self.left_fwd = PWM(Pin(0))
        self.left_rev = PWM(Pin(1))
        
        # Rear Right Motor (powered)
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
        left_speed: left rear motor speed (-100 to 100)
        right_speed: right rear motor speed (-100 to 100)
        """
        self.set_motor(self.left_fwd, self.left_rev, left_speed)
        self.set_motor(self.right_fwd, self.right_rev, right_speed)
    
    def forward(self, speed=50):
        """Move forward - rear wheels push, front casters lead"""
        self.move(speed, speed)
    
    def backward(self, speed=50):
        """
        Move backward - rear wheels pull, front casters trail
        Note: Rear-drive robots turn MORE easily in reverse!
        """
        self.move(-speed, -speed)
    
    def turn_left_forward(self, speed=50):
        """Turn left while moving forward"""
        self.move(0, speed)
    
    def turn_right_forward(self, speed=50):
        """Turn right while moving forward"""
        self.move(speed, 0)
    
    def turn_left_reverse(self, speed=50):
        """Turn left while moving backward (very tight turns possible)"""
        self.move(0, -speed)
    
    def turn_right_reverse(self, speed=50):
        """Turn right while moving backward (very tight turns possible)"""
        self.move(-speed, 0)
    
    def spin_left(self, speed=50):
        """Spin left in place"""
        self.move(-speed, speed)
    
    def spin_right(self, speed=50):
        """Spin right in place"""
        self.move(speed, -speed)
    
    def arc_left(self, speed=50, turn_ratio=0.5):
        """
        Smooth arc turn to the left (forward)
        turn_ratio: 0 (sharp) to 1 (gentle)
        """
        right_speed = speed
        left_speed = int(speed * turn_ratio)
        self.move(left_speed, right_speed)
    
    def arc_right(self, speed=50, turn_ratio=0.5):
        """
        Smooth arc turn to the right (forward)
        turn_ratio: 0 (sharp) to 1 (gentle)
        """
        left_speed = speed
        right_speed = int(speed * turn_ratio)
        self.move(left_speed, right_speed)
    
    def arc_left_reverse(self, speed=50, turn_ratio=0.5):
        """
        Smooth arc turn to the left (backward)
        Rear-drive robots turn very well in reverse!
        """
        right_speed = -speed
        left_speed = int(-speed * turn_ratio)
        self.move(left_speed, right_speed)
    
    def arc_right_reverse(self, speed=50, turn_ratio=0.5):
        """
        Smooth arc turn to the right (backward)
        Rear-drive robots turn very well in reverse!
        """
        left_speed = -speed
        right_speed = int(-speed * turn_ratio)
        self.move(left_speed, right_speed)
    
    def stop(self):
        """Stop all motors"""
        for motor in self.motors:
            motor.duty_u16(0)

# Demo program
def demo():
    robot = RearDriveRobot()
    
    print("Rear-Wheel Drive Robot Demo")
    print("2 powered wheels at REAR, 2 static casters at FRONT")
    print("="*50)
    
    try:
        # Forward movement
        print("Moving forward...")
        robot.forward(60)
        time.sleep(2)
        robot.stop()
        time.sleep(1)
        
        # Backward movement (rear-drive excels at this!)
        print("Moving backward...")
        robot.backward(60)
        time.sleep(2)
        robot.stop()
        time.sleep(1)
        
        # Turn left (forward)
        print("Turning left (forward)...")
        robot.turn_left_forward(60)
        time.sleep(1.5)
        robot.stop()
        time.sleep(1)
        
        # Turn right (forward)
        print("Turning right (forward)...")
        robot.turn_right_forward(60)
        time.sleep(1.5)
        robot.stop()
        time.sleep(1)
        
        # Turn left (reverse) - very tight!
        print("Turning left (reverse - tight turn)...")
        robot.turn_left_reverse(60)
        time.sleep(1.5)
        robot.stop()
        time.sleep(1)
        
        # Turn right (reverse) - very tight!
        print("Turning right (reverse - tight turn)...")
        robot.turn_right_reverse(60)
        time.sleep(1.5)
        robot.stop()
        time.sleep(1)
        
        # Spin in place
        print("Spinning left...")
        robot.spin_left(50)
        time.sleep(1.5)
        robot.stop()
        time.sleep(1)
        
        print("Spinning right...")
        robot.spin_right(50)
        time.sleep(1.5)
        robot.stop()
        time.sleep(1)
        
        # Arc movements forward
        print("Arc left (forward)...")
        robot.arc_left(60, turn_ratio=0.4)
        time.sleep(2)
        robot.stop()
        time.sleep(1)
        
        # Arc movements in reverse (special advantage of rear-drive!)
        print("Arc left (reverse - very agile)...")
        robot.arc_left_reverse(60, turn_ratio=0.3)
        time.sleep(2)
        robot.stop()
        time.sleep(1)
        
        print("\nDemo complete!")
        
    except KeyboardInterrupt:
        print("\nStopping robot...")
        robot.stop()

# Parallel parking demo (rear-drive advantage!)
def parallel_parking_demo():
    robot = RearDriveRobot()
    
    print("Parallel Parking Demo")
    print("Demonstrating rear-drive agility in reverse!")
    
    try:
        # Pull forward
        print("Step 1: Moving forward...")
        robot.forward(50)
        time.sleep(1.5)
        robot.stop()
        time.sleep(0.5)
        
        # Back up and turn right
        print("Step 2: Backing up and turning right...")
        robot.turn_right_reverse(50)
        time.sleep(1.5)
        robot.stop()
        time.sleep(0.5)
        
        # Back up and turn left to straighten
        print("Step 3: Backing up and turning left to straighten...")
        robot.turn_left_reverse(50)
        time.sleep(1)
        robot.stop()
        time.sleep(0.5)
        
        # Back up straight
        print("Step 4: Backing straight...")
        robot.backward(50)
        time.sleep(1)
        robot.stop()
        
        print("Parking complete!")
        
    except KeyboardInterrupt:
        print("\nStopping robot...")
        robot.stop()

# Three-point turn demo
def three_point_turn():
    robot = RearDriveRobot()
    
    print("Three-Point Turn Demo")
    
    try:
        # Turn 1: Forward and turn right
        print("Point 1: Forward right turn...")
        robot.arc_right(50, turn_ratio=0.2)
        time.sleep(2)
        robot.stop()
        time.sleep(0.5)
        
        # Turn 2: Reverse and turn left (rear-drive shines here!)
        print("Point 2: Reverse left turn...")
        robot.arc_left_reverse(50, turn_ratio=0.2)
        time.sleep(2)
        robot.stop()
        time.sleep(0.5)
        
        # Turn 3: Forward and straighten
        print("Point 3: Forward to complete turn...")
        robot.forward(50)
        time.sleep(1.5)
        robot.stop()
        
        print("Three-point turn complete!")
        
    except KeyboardInterrupt:
        print("\nStopping robot...")
        robot.stop()

# Navigation pattern
def navigation_pattern():
    robot = RearDriveRobot()
    
    print("Navigation Pattern: Exploring with reverse turning")
    
    try:
        for i in range(3):
            # Move forward
            print(f"Segment {i+1}: Moving forward...")
            robot.forward(60)
            time.sleep(2)
            
            robot.stop()
            time.sleep(0.3)
            
            # Turn using reverse (rear-drive advantage)
            print(f"Segment {i+1}: Turning in reverse...")
            robot.turn_right_reverse(55)
            time.sleep(1.2)
            
            robot.stop()
            time.sleep(0.3)
        
        robot.stop()
        print("Navigation pattern complete!")
        
    except KeyboardInterrupt:
        print("\nStopping robot...")
        robot.stop()

# Run the demos
if __name__ == "__main__":
    print("\n" + "="*50)
    print("REAR-WHEEL DRIVE ROBOT")
    print("Powered wheels: REAR | Static wheels: FRONT")
    print("Special advantage: Superior reverse turning!")
    print("="*50 + "\n")
    
    demo()
    
    # Uncomment to run other demos:
    # parallel_parking_demo()
    # three_point_turn()
    # navigation_pattern()
