# IMPORT: Bringing in the classes from your other files
from motor_systems import DCMotor
from sensor_modules import Sensor


class Robot:
    # Taking two objects and putting them inside a "Robot"
    def __init__(self, robot_name, motor_obj, sensor_obj):
        self.name = robot_name
        self.motor = motor_obj
        self.sensor = sensor_obj

    #  Using the motor and sensor methods together
    def run_check(self, sensor_value):
        print(f"Running {self.name} ")
        # The robot asks the sensor to format the value
        report = self.sensor.read(sensor_value)
        print(report)

        # The robot checks its own motor status
        if self.motor.current_speed > 0:
            print("System Status: MOVING")
        else:
            print("System Status: STATIONARY")


# Create the component objects
my_motor = DCMotor("Primary_Drive", 1500)
my_sensor = Sensor("Infrared", "meters")

# Build the robot using those components
my_bot = Robot("Mecha_Unit_01", my_motor, my_sensor)

#  Test the system
my_bot.run_check(0.5)  # Perform check while stationary
my_motor.set_speed(500)  # Start the motor
my_bot.run_check(0.8)  # Perform check while moving