class Sensor:
    # find what type of sensor this is
    def __init__(self, sensor_type, unit):
        self.sensor_type = sensor_type # e.g., "Ultrasonic"
        self.unit = unit               # e.g., "cm"

    # make a raw number into a readable string
    def read(self, value):
        # This returns the text so another class can use it
        return f"[{self.sensor_type}] Reading: {value} {self.unit}"