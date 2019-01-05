import tkinter as tk
import carhire.constants as vc


class RootView(tk.Tk):
    """
    This is the Root Window and Frame of the GUI of the application

    It is called once on app startup and referred to by the
    nested frames when they initialise, which occurs as the user
    changes between frames
    """
    _view_controller = None
    current_frame = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Car Hire")
        self.resizable(width=False, height=False)
        self.state('zoomed')
        self.configure(background=vc.BG)
        self.frame_name = vc.FRAME_MAIN
        self.columnconfigure(0, weight=1)

    def add_view_controller(self, view_controller):
        """
        Add the View Controller to the root frame to access its methods
        :param view_controller: The View Controller service
        """
        self._view_controller = view_controller

    def get_frame(self):
        """
        Returns a string of the name of the currently selected frame
        :return: String of the name of the frame
        """
        return self.current_frame
