import random
import dashboard
from device import SmartLight, Thermostat, SecurityCamera

class AutomationSystem:
    def __init__(self):
        self.devices = []
        self.dashboard = dashboard

    def discover_device(self, device):
        self.devices.append(device)

    def randomize_device_status(self):
        for device in self.devices:
            device.status = random.choice([True, False])

    def get_device_by_id(self, device_id):
        for device in self.devices:
            if device.device_id == device_id:
                return device
        return None

    def randomize_device_values(self):
        for device in self.devices:
            if isinstance(device, SmartLight):
                device.change_brightness(random.randint(0, 100))
            elif isinstance(device, Thermostat):
                device.set_temperature(random.randint(0, 40))
            elif isinstance(device, SecurityCamera):
                device.toggle_security_status() if random.choice([True, False]) else None
