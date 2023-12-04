class Device:
    def __init__(self, device_id):
        self.device_id = device_id
        self.status = False

    def turn_on(self):
        self.status = True

    def turn_off(self):
        self.status = False

class SmartLight(Device):
    def __init__(self, device_id):
        super().__init__(device_id)
        self.brightness = 0

    def change_brightness(self, value):
        self.brightness = value

class Thermostat(Device):
    def __init__(self, device_id):
        super().__init__(device_id)
        self.temperature = 20

    def set_temperature(self, value):
        self.temperature = value

class SecurityCamera(Device):
    def __init__(self, device_id):
        super().__init__(device_id)
        self.security_status = False

    def arm(self):
        self.security_status = True

    def disarm(self):
        self.security_status = False

    def toggle_security_status(self):
        self.security_status = not self.security_status

class MotionCamera(Device):
    def __init__(self, device_id):
        super().__init__(device_id)