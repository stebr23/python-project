import sqlite3
import tkinter as tk
import carhire.views.view_constants as vc
import carhire.database as db_consts

from tkinter import ttk
from carhire.static import HOME_ICON


class VehicleFrame(tk.Frame):

    _vehicle_list = []

    def __init__(self, parent, vehicle_type, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self.customer_id = tk.StringVar()
        self.parent = parent
        self.vehicle_type = vehicle_type
        self.name = self.vehicle_type
        self.title_string = tk.StringVar()
        self.title_string.set(vehicle_type)
        self.list_frame = tk.Frame()
        self.list_listbox = tk.Listbox()
        self.scrollbar = tk.Scrollbar()

        self.create_main_display()
        self.create_vehicle_list_display()

    def create_main_display(self):
        self.configure_root_frame()
        self.set_title()
        self.set_main_menu_button()

    def configure_root_frame(self):
        self.parent.title("Car Hire - %s" % self.vehicle_type)
        self.configure(background=vc.BG)
        self.columnconfigure(1, weight=1)

    def set_main_menu_button(self):
        main_menu_image = tk.PhotoImage(file=HOME_ICON)
        main_menu_button = tk.Button(self, text="   ", bd=0, cursor="hand2", command=self.change_to_main_menu, image=main_menu_image, compound="right", background=vc.BG, fg=vc.FG)
        main_menu_button.image = main_menu_image
        main_menu_button.grid(row=0, column=0, sticky=(tk.E + tk.W))

    def set_title(self):
        title_label = ttk.Label(self, textvariable=self.title_string, font=("TkDefaultFont", 64), wraplength=600, foreground=vc.WHITE)
        title_label.configure(background=vc.BG, anchor="center")
        title_label.grid(row=0, column=1, sticky=(tk.E + tk.W), pady=(30, 80))

    def create_vehicle_list_display(self):
        self.populate_vehicle_list()
        self.create_vehicle_list_frame()

    def populate_vehicle_list(self):
        db_table_name = self.set_db_table_name()
        conn = sqlite3.connect(db_consts.DB_NAME)
        c = conn.cursor()

        for row in c.execute('SELECT * FROM %s WHERE user_id IS NULL' % db_table_name):
            self._vehicle_list.append(row)

        c.close()
        conn.close()

    def create_vehicle_list_frame(self):
        self.set_up_list_widgets()
        self.add_vehicles_from_db_to_list()
        self.pack_list_widgets()
        self.create_rent_button_and_customer_input()

    def pack_list_widgets(self):
        self.list_listbox.pack()
        self.scrollbar.config(command=self.list_listbox.yview)
        self.list_frame.grid(row=1, column=1)

    def set_up_list_widgets(self):
        self.list_frame = tk.Frame(self, bd=2, relief=tk.SUNKEN, width=800, height=300)
        self.list_frame.pack_propagate(False)
        self.scrollbar = tk.Scrollbar(self.list_frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.list_listbox = tk.Listbox(self.list_frame, bd=0, font="consolas", yscrollcommand=self.scrollbar.set, width=800, height=300)
        self.list_listbox.pack_propagate(False)

    def create_rent_button_and_customer_input(self):
        customer_id_field_label = tk.Label(self, text="Enter a customer id:", fg=vc.FG, bg=vc.BG)
        customer_id_field_label.grid(row=2, column=1, pady=(10,0))
        customer_id_field = tk.Entry(self, textvariable=self.customer_id, width=10)
        customer_id_field.grid(row=3, column=1, pady=(10, 0))
        rent_button = tk.Button(self, text="Rent Selected %s" % self.vehicle_type[0:len(self.vehicle_type) - 1], command=self.rent_selected)
        rent_button.grid(row=4, column=1, pady=(10, 0))
        currently_rented_button = tk.Button(self, text="View Currently Rented %s" % self.vehicle_type)
        currently_rented_button.grid(row=5, column=1, pady=(10, 0))

    def add_vehicles_from_db_to_list(self):
        for vehicle in self._vehicle_list:
            vehicle_details = self.generate_vehicle_details_string(vehicle)
            self.list_listbox.insert(tk.END, vehicle_details)

    def set_db_table_name(self):
        if self.vehicle_type == vc.CARS:
            return db_consts.CARS_TABLE
        elif self.vehicle_type == vc.BIKES:
            return db_consts.BIKES_TABLE
        elif self.vehicle_type == vc.VANS:
            return db_consts.VANS_TABLE

    def generate_vehicle_details_string(self, vehicle):
        spaces_to_add = [20 - len(vehicle[1]), 15 - len(vehicle[2]), 10 - len(vehicle[4]), 10 - len(vehicle[-2])]
        vehicle_details_string = "%s:  " % vehicle[0]
        vehicle_details_string += vehicle[1] + self.add_number_of_spaces(spaces_to_add[0])
        vehicle_details_string += vehicle[2] + self.add_number_of_spaces(spaces_to_add[1])
        vehicle_details_string += vehicle[4] + self.add_number_of_spaces(spaces_to_add[2])
        vehicle_details_string += vehicle[-2]
        return vehicle_details_string

    def add_number_of_spaces(self, spaces_to_add):
        return ' ' * spaces_to_add

    def rent_selected(self):
        if self.list_listbox.curselection():
            vehicle_index = self.list_listbox.curselection()[0]
            vehicle_details = self.list_listbox.get(vehicle_index)
            vehicle_id = vehicle_details.split(":")[0]
            customer_id = self.customer_id.get()

            if customer_id != '':
                self.update_db_vehicle_table(vehicle_id, customer_id)
                self.list_listbox.delete(vehicle_index)
                self._vehicle_list.pop(vehicle_index)
                self.customer_id.set('')

    def update_db_vehicle_table(self, vehicle_id, customer_id):
        db_table_name = self.set_db_table_name()
        conn = sqlite3.connect(db_consts.DB_NAME)
        c = conn.cursor()
        c.execute('UPDATE %s SET user_id = \'%s\' WHERE vehicle_id = %s' % (db_table_name, customer_id, vehicle_id))
        c.close()
        conn.close()

    def change_to_main_menu(self):
        self.parent.set_frame(vc.FRAME_MAIN)
