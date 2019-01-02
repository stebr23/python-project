import tkinter as tk
import carhire.views.view_constants as vc

from carhire.views.main_menu import MainMenu
from carhire.views.vehicle.vehicle_view import VehicleFrame


class RootView(tk.Tk):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Car Hire")
        self.resizable(width=False, height=False)
        self.state('zoomed')
        self.configure(background=vc.BG)
        self.currentFrame = MainMenu(self)
        self.set_frame(self.currentFrame)
        self.columnconfigure(0, weight=1)

    def set_frame(self, frame_name, vehicle_type=''):
        self.currentFrame.grid_forget()

        if frame_name == vc.FRAME_MAIN:
            self.currentFrame = MainMenu(self)
        if frame_name == vc.FRAME_VEHICLE:
            self.currentFrame = VehicleFrame(self, vehicle_type)

        self.currentFrame.grid(sticky=(tk.E + tk.W + tk.N + tk.S))

    def get_frame(self):
        return self.currentFrame
