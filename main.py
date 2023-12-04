from tkinter import Tk
from dashboard import Dashboard
from automation_system import AutomationSystem
from device import SmartLight, Thermostat, SecurityCamera, MotionCamera

if __name__ == "__main__":
    root = Tk()

    automation_system = AutomationSystem()

    smart_light = SmartLight(device_id="Living Room Light")
    thermostat = Thermostat(device_id="Living Room Thermostat")
    security_camera = SecurityCamera(device_id="Front Door Camera")
    motion_camera = MotionCamera(device_id="Motion Camera")

    automation_system.discover_device(smart_light)
    automation_system.discover_device(thermostat)
    automation_system.discover_device(security_camera)
    automation_system.discover_device(motion_camera)

    automation_system.dashboard = Dashboard(root, automation_system)

    root.mainloop()