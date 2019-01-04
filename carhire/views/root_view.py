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
        self.frame_name = vc.FRAME_MAIN
        self.current_frame = MainMenu(self)
        self.set_frame(self.frame_name)
        self.columnconfigure(0, weight=1)

    def set_frame(self, frame_name, vehicle_type=''):
        self.current_frame.grid_forget()

        if frame_name == vc.FRAME_MAIN:
            self.frame_name = vc.FRAME_MAIN
            self.current_frame = MainMenu(self)
        if frame_name == vc.FRAME_VEHICLE:
            self.frame_name = vc.FRAME_VEHICLE
            self.current_frame = VehicleFrame(self, vehicle_type)
        if frame_name == vc.FRAME_RENTED:
            self.frame_name = vc.FRAME_RENTED
            self.current_frame = VehicleFrame(self, vehicle_type)

        self.current_frame.grid(sticky=(tk.E + tk.W + tk.N + tk.S))

    def get_frame(self):
        return self.current_frame
