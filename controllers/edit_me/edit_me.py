"""Simple robot controller."""

from controller import Robot
import sys

# Define the target motor position in radians.
left_target = 12
right_target = 8

# Get pointer to the robot.
robot = Robot()

motor_max_speed = robot.getDevice("motor.left").getMaxVelocity()
robot.getDevice("motor.right").setVelocity(motor_max_speed*right_target/left_target)

# Set the target position of the left and right wheels motors.
robot.getDevice("motor.left").setPosition(left_target)
robot.getDevice("motor.right").setPosition(right_target)

# This is the most simple controller that works for this benchmark
# If you want to experiment with more complex functions, you can read the programming guide here:
#  https://www.cyberbotics.com/doc/guide/controller-programming?tab-language=python
# or the Robot() documentation here:
#  https://cyberbotics.com/doc/reference/robot?tab-language=python
