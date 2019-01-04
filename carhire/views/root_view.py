import tkinter as tk
import carhire.constants as vc

from carhire.views.main_menu import MainMenu
from carhire.views.vehicle.vehicle_view import VehicleFrame


class RootView(tk.Tk):
    """
    This is the Root Window and Frame of the GUI of the application

    It is called once on app startup and referred to by the
    nested frames when they initialise, which occurs as the user
    changes between frames
    """
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
        """
        Change the current frame of the root window by
        providing the name of the frame and an optional
        variable that outlines which vehicle the user wishes
        to view when selecting the Vehicle frame

        :param frame_name: String of the name of the frame being set
        :param vehicle_type: String of the type of vehicle to be shown
        """
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
        """
        Returns a string of the name of the currently selected frame
        :return: String of the name of the frame
        """
        return self.current_frame
