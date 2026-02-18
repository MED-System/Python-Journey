class DCMotor:
    # Set the initial state
    def __init__(self, name, max_speed):
        self.name = name           # The ID of the motor
        self.max_speed = max_speed # The safety limit
        self.current_speed = 0     # All motors start at 0
        self.is_running = False    # All motors start "OFF"

    # Logic to safely change the speed
    def set_speed(self, speed):
        if speed <= self.max_speed:
            self.current_speed = speed
            print(f"{self.name} speed set to {speed} RPM.")
            return True
        else:
            print("ERROR: Speed too high!")
            return False