from tkinter import Label, Button, Scale, StringVar
from tkinter.ttk import Checkbutton, LabelFrame
from device import SmartLight, Thermostat, SecurityCamera, MotionCamera

class Dashboard:
    def __init__(self, master, automation_system):
        self.master = master
        self.automation_system = automation_system
        self.brightness_scales = {}
        self.temperature_scales = {}
        master.title("Smart Home Dashboard")

        self.label = Label(master, text="Smart Home Dashboard")
        self.label.pack()

        self.randomize_button = Button(master, text="Randomize Values", command=self.rand)
        self.randomize_button.pack()

        self.run_simulation_button = Button(master, text="Run Simulation", command=self.run_simulation)
        self.run_simulation_button.pack()

        self.device_status_vars = []
        self.create_device_controls()

        self.button = Button(master, text="Quit", command=master.quit)
        self.button.pack()

    def create_device_controls(self):
        for device in self.automation_system.devices:
            device_frame = LabelFrame(self.master, text=device.device_id)
            device_frame.pack(padx=10, pady=10)

            status_var = StringVar()
            status_var.set("Status: OFF")
            self.device_status_vars.append(status_var)

            status_label = Label(device_frame, textvariable=status_var)
            status_label.pack()

            if isinstance(device, SmartLight):
                brightness_label = Label(device_frame, text="Brightness")
                brightness_label.pack()

                brightness_scale = Scale(device_frame, from_=0, to=100,
                                         orient="horizontal", command=lambda value,
                                                                             d=device: self.change_brightness(value, d))
                brightness_scale.pack()
                self.brightness_scales[device.device_id] = brightness_scale

            elif isinstance(device, Thermostat):
                temperature_label = Label(device_frame, text="Temperature")
                temperature_label.pack()

                temperature_scale = Scale(device_frame, from_=0, to=40,
                                          orient="horizontal", command=lambda value,
                                                                              d=device: self.set_temperature(value, d))
                temperature_scale.pack()
                self.temperature_scales[device.device_id] = temperature_scale

            elif isinstance(device, SecurityCamera):
                security_checkbutton = Checkbutton(device_frame,
                                                   text="Security Status",
                                                   command=lambda d=device: self.toggle_security_status(d))
                security_checkbutton.pack()

            if isinstance(device, MotionCamera):
                on_off_button = Button(device_frame, text="Toggle On/Off",
                                       command=lambda d=device: self.motion_camera(d))
                on_off_button.pack()
            else:
                on_off_button = Button(device_frame, text="Toggle On/Off",
                                       command=lambda d=device: self.toggle_device_status(d))
                on_off_button.pack()

    def motion_camera(self, d):
        self.toggle_device_status(d)
        smart_light_device = self.automation_system.get_device_by_id("Living Room Light")

        if (not smart_light_device.status) & d.status:
            self.toggle_device_status(smart_light_device)

    @staticmethod
    def change_brightness(value, device):
        device.change_brightness(int(value))

    @staticmethod
    def set_temperature(value, device):
        device.set_temperature(int(value))

    @staticmethod
    def toggle_security_status(device):
        device.toggle_security_status()

    def toggle_device_status(self, device):
        if device.status:
            device.turn_off()
        else:
            device.turn_on()
        self.update_device_status(device)

    def update_device_status(self, device):
        status_var = self.device_status_vars[self.automation_system.devices.index(device)]
        status_var.set(f"Status: {'ON' if device.status else 'OFF'}")

    def randomize_status(self):
        self.automation_system.randomize_device_status()
        self.update_device_values()

    def randomize_values(self):
        self.automation_system.randomize_device_values()
        self.update_device_values()
        self.update_slider_values()

    def update_slider_values(self):
        for device, status_var in zip(self.automation_system.devices, self.device_status_vars):
            if isinstance(device, SmartLight):
                self.brightness_scales[device.device_id].set(device.brightness)
            elif isinstance(device, Thermostat):
                self.temperature_scales[device.device_id].set(device.temperature)

    def rand(self):
        self.randomize_values()
        self.randomize_status()

    def update_device_values(self):
        for device, status_var in zip(self.automation_system.devices, self.device_status_vars):
            status_var.set(f"Status: {'ON' if device.status else 'OFF'}")

    def run_simulation(self, count=0):
        if count < 5:
            self.rand()
            self.master.after(2000, self.run_simulation, count + 1)
