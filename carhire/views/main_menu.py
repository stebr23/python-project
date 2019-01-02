import tkinter as tk
import carhire.views.view_constants as vc

from tkinter import ttk
from carhire.static import *


class MainMenu(tk.Frame):

    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent
        self.configure(background=vc.BG)
        self.set_title()
        self.create_view()

    def create_view(self):
        self.parent.title("Car Hire - Main Menu")
        self.configure_grid()
        self.create_vehicle_buttons()

    def configure_grid(self):
        self.columnconfigure(0, weight=2)
        self.columnconfigure(1, weight=3)
        self.columnconfigure(2, weight=2)
        self.rowconfigure(2, minsize=100, weight=1)
        self.rowconfigure(3, minsize=100, weight=1)
        self.rowconfigure(4, minsize=100, weight=1)

    def create_vehicle_buttons(self):
        self.create_car_button()
        self.create_bike_button()
        self.create_van_button()

    def create_van_button(self):
        van_image = tk.PhotoImage(file=VAN_IMG)
        van_button = tk.Button(self, text=("  %s" % vc.VANS), font=("TkDefaultFont", 24), command=self.view_van_page,
                               image=van_image, compound="left", cursor="hand2", bg=vc.FG, fg=vc.BG)
        van_button.image = van_image
        van_button.grid(row=4, column=1, sticky=(tk.N + tk.E + tk.S + tk.W), pady=(20, 20))

    def create_bike_button(self):
        bike_image = tk.PhotoImage(file=BIKER_IMG)
        bike_button = tk.Button(self, text=("  %s" % vc.BIKES), font=("TkDefaultFont", 24), command=self.view_bike_page,
                                image=bike_image, compound="left", cursor="hand2", bg=vc.FG, fg=vc.BG)
        bike_button.image = bike_image
        bike_button.grid(row=3, column=1, sticky=(tk.N + tk.E + tk.S + tk.W), pady=(20, 20))

    def create_car_button(self):
        car_image = tk.PhotoImage(file=CAR_IMG)
        car_button = tk.Button(self, text=("  %s" % vc.CARS), font=("TkDefaultFont", 24), command=self.view_car_page,
                               image=car_image, compound="left", cursor="hand2", bg=vc.FG, fg=vc.BG)
        car_button.image = car_image
        car_button.grid(row=2, column=1, sticky=(tk.N + tk.E + tk.S + tk.W), pady=(20, 20))

    def set_title(self):
        self.name = tk.StringVar()
        self.title_string = tk.StringVar()
        self.title_string.set("My Car Hire")
        title_label = ttk.Label(self, textvariable=self.title_string, font=("TkDefaultFont", 64), wraplength=600,
                                foreground=vc.WHITE)
        title_label.configure(background=vc.BG, anchor="center")
        title_label.grid(row=0, column=1, sticky=(tk.E + tk.W), pady=(80, 80))

    def view_car_page(self):
        self.parent.set_frame(vc.FRAME_VEHICLE, vc.CARS)

    def view_bike_page(self):
        self.parent.set_frame(vc.FRAME_VEHICLE, vc.BIKES)

    def view_van_page(self):
        self.parent.set_frame(vc.FRAME_VEHICLE, vc.VANS)
