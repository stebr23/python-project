import sqlite3
import tkinter as tk
import carhire.constants as vc
import carhire.database as db_consts

from tkinter import ttk
from carhire.models.catalogue.catalogue import Catalogue
from carhire.models.user.customer import Customer, Address, BankDetails
from carhire.models.vehicle.bike import Bike
from carhire.models.vehicle.car import Car
from carhire.models.vehicle.van import Van
from carhire.static import HOME_ICON


class VehicleFrame(tk.Frame):
    """
    Creates the frame holding the information of the Vehicles in
    a catalogue

    The user can select from a list of vehicles and rent them by
    assigning them a user id
    """
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
        self.vehicle_list = []
        self.catalogue = ''
        self.vehicle = ''
        self.user = ''

        self.create_main_display()
        self.create_vehicle_list_display()

        print("VehicleView:  READY")

    def create_main_display(self):
        """
        Contains the functions that create the widgets for the frame
        """
        print("VehicleView:  Creating main vehicle view display")
        self.configure_root_frame()
        self.set_title()
        self.set_main_menu_button()

    def configure_root_frame(self):
        """
        Configures the root frame
        """
        print("VehicleView:  Configuring root frame")
        self.parent.title("Car Hire - %s" % self.vehicle_type)
        self.configure(background=vc.BG)
        self.columnconfigure(1, weight=1)

    def set_main_menu_button(self):
        """
        Creates a button widget for the user to navigate back to the
        main menu
        """
        print("VehicleView:  Setting main menu button")
        main_menu_image = tk.PhotoImage(file=HOME_ICON)
        main_menu_button = tk.Button(self, text="   ", bd=0, cursor="hand2", command=self.change_to_main_menu,
                                     image=main_menu_image, compound="right", background=vc.BG, fg=vc.FG)
        main_menu_button.image = main_menu_image
        main_menu_button.grid(row=0, column=0, sticky=(tk.E + tk.W))

    def set_title(self):
        """
        Sets the title of the frame so the user knows which frame they are viewing
        """
        print("VehicleView:  Setting title")
        title_label = ttk.Label(self, textvariable=self.title_string, font=("TkDefaultFont", 64), wraplength=600,
                                foreground=vc.WHITE)
        title_label.configure(background=vc.BG, anchor="center")
        title_label.grid(row=0, column=1, sticky=(tk.E + tk.W), pady=(30, 80))

    def create_vehicle_list_display(self):
        """
        Contains the functions used to create the list of vehicles
        for the user to interact with
        """
        print("VehicleView:  Creating vehicle list display")
        self.populate_catalogue()
        self.create_vehicle_list_frame()

    def populate_catalogue(self):
        """
        Populates the Catalogue object with vehicles from the database

        The types of vehicles (Car, Bike or Van) are determined by the
        option the user chose form the main menu
        """
        print("VehicleView:  Populating catalogue")
        db_table_name = self.set_db_table_name()
        conn = sqlite3.connect(db_consts.DB_NAME)
        c = conn.cursor()

        select_query = self.get_select_query(db_table_name)
        print("VehicleView:  Select query: %s " % select_query)

        for row in c.execute(select_query):
            self.vehicle_list.append(row)

        c.close()
        conn.close()
        self.catalogue = Catalogue(self.vehicle_list)

    def get_select_query(self, db_table_name):
        """
        Returns a relevant SELECT query depending on whether the user
        is viewing the vehicles that are available to rent or those
        are currently being rented

        :param db_table_name: String of the name of the db table to query
        :return: String of the whole SQL statement to retrieve the vehiclesfrom the db
        """
        if self.parent.frame_name == vc.FRAME_VEHICLE:
            return 'SELECT * FROM %s WHERE user_id IS NULL' % db_table_name
        elif self.parent.frame_name == vc.FRAME_RENTED:
            return 'SELECT * FROM %s WHERE user_id IS NOT NULL' % db_table_name
        return ''

    def create_vehicle_list_frame(self):
        """
        Contains the functions executed to produce the frame containing the list of vehicles and associated
        buttons
        """
        print("VehicleView:  Creating vehicle list frame")
        self.set_up_list_widgets()
        self.add_vehicles_from_catalogue_to_listbox()
        self.pack_list_widgets()
        if self.parent.frame_name == vc.FRAME_VEHICLE:
            self.create_rent_button_and_customer_input()
        self.set_change_view_button()

    def pack_list_widgets(self):
        """
        Packs the widgets to the vehicle list frame
        """
        print("VehicleView:  Packing widgets")
        self.list_listbox.pack()
        self.scrollbar.config(command=self.list_listbox.yview)
        self.list_frame.grid(row=1, column=1)

    def set_up_list_widgets(self):
        """
        Instantiates the widgets for the vehicle list frame and packs them to the frame
        """
        print("VehicleView:  Setting up list widgets")
        self.list_frame = tk.Frame(self, bd=2, relief=tk.SUNKEN, width=800, height=300)
        self.list_frame.pack_propagate(False)
        self.scrollbar = tk.Scrollbar(self.list_frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.list_listbox = tk.Listbox(self.list_frame, bd=0, font="consolas", yscrollcommand=self.scrollbar.set,
                                       width=800, height=300)
        self.list_listbox.pack_propagate(False)

    def create_rent_button_and_customer_input(self):
        """
        Creates the widgets to insert a customer id and rent a vehicle out to them
        """
        print("VehicleView:  Creating rent buttons and customer input field")
        customer_id_field_label = tk.Label(self, text="Enter a customer id:", fg=vc.FG, bg=vc.BG)
        customer_id_field_label.grid(row=2, column=1, pady=(10, 0))
        customer_id_field = tk.Entry(self, textvariable=self.customer_id, width=10)
        customer_id_field.grid(row=3, column=1, pady=(10, 0))
        rent_button = tk.Button(self, text="Rent Selected %s" % self.vehicle_type[0:len(self.vehicle_type) - 1],
                                command=self.rent_selected)
        rent_button.grid(row=4, column=1, pady=(10, 0))

    def set_change_view_button(self):
        """
        Create the button to reload the frame showing the vehicles that are
        currently available or that are rented out and place it in the frame
        """
        print("VehicleView:  current frame_name is: %s" % self.parent.frame_name)
        if self.parent.frame_name == vc.FRAME_VEHICLE:
            currently_rented_button = tk.Button(self, text="View Currently Rented %s" % self.vehicle_type,
                                                command=self.show_rented)
            currently_rented_button.grid(row=5, column=1, pady=(10, 0))
        elif self.parent.frame_name == vc.FRAME_RENTED:
            currently_rented_button = tk.Button(self, text="View Available %s" % self.vehicle_type,
                                                command=self.show_available)
            currently_rented_button.grid(row=5, column=1, pady=(10, 0))

    def add_vehicles_from_catalogue_to_listbox(self):
        """
        Creates relevant Vehicle objects (Car || Bike || Van) from the data in the database tables
        and displays the data in the listbox widget.

        The function calls the Vehicle's generate details function to populate the listbox
        """
        print("VehicleView:  Adding vehicles from catalogue to listbox")
        print("VehicleView:  Setting Vehicle object to specific vehicle type (Car||Van||Bike)")
        for vehicle in self.catalogue.get_entries():
            if self.vehicle_type == vc.CARS:
                self.vehicle = self.set_vehicle_as_car(vehicle)
            elif self.vehicle_type == vc.BIKES:
                self.vehicle = self.set_vehicle_as_bike(vehicle)
            elif self.vehicle_type == vc.VANS:
                self.vehicle = self.set_vehicle_as_van(vehicle)

            vehicle_details = self.vehicle.generate_vehicle_details_string()
            self.list_listbox.insert(tk.END, vehicle_details)

    @staticmethod
    def set_vehicle_as_van(vehicle):
        """
        Takes data from the database table and returns a Van object

        :param vehicle: Tuple containing an individual vehicle's data
        :return: Van object with the stored data
        """
        return Van(vehicle_id=vehicle[0], make=vehicle[1], model=vehicle[2], wheels=vehicle[3], colour=vehicle[4],
                   doors=vehicle[5], passengers=vehicle[6], user_id=vehicle[7], storage_space=vehicle[8])

    @staticmethod
    def set_vehicle_as_bike(vehicle):
        """
        Takes data from the database table and returns a Bike object

        :param vehicle: Tuple containing an individual vehicle's data
        :return: Bike object with the stored data
        """
        return Bike(vehicle_id=vehicle[0], make=vehicle[1], model=vehicle[2], wheels=vehicle[3], colour=vehicle[4],
                    doors=vehicle[5], passengers=vehicle[6], user_id=vehicle[7], storage=vehicle[8])

    @staticmethod
    def set_vehicle_as_car(vehicle):
        """
        Takes data from the database table and returns a Car object

        :param vehicle: Tuple containing an individual vehicle's data
        :return: Car object with the stored data
        """
        return Car(vehicle_id=vehicle[0], make=vehicle[1], model=vehicle[2], wheels=vehicle[3], colour=vehicle[4],
                   doors=vehicle[5], passengers=vehicle[6], user_id=vehicle[7], bags=vehicle[8], car_type=vehicle[9])

    def set_db_table_name(self):
        """
        Sets the database table name to use as part of the SQL query

        It is determined by the vehicle type provided when the frame initially loads
        :return: String of the database table for the selected vehicle type
        """
        print("VehicleView:  Setting db table name depending on vehicle type")
        if self.vehicle_type == vc.CARS:
            return db_consts.CARS_TABLE
        elif self.vehicle_type == vc.BIKES:
            return db_consts.BIKES_TABLE
        elif self.vehicle_type == vc.VANS:
            return db_consts.VANS_TABLE

    def rent_selected(self):
        """
        Takes the selected vehicle and assigns a user_id to it

        The vehicle is removed from the catalogue and the listbox

        The database is updated to include the user id on the specific vehicle
        table for the selected vehicle
        """
        print("VehicleView:  Renting selected vehicle...")
        if self.list_listbox.curselection():
            vehicle_index = self.list_listbox.curselection()[0]
            vehicle_to_rent = self.catalogue.get_vehicle(vehicle_index)
            customer_id = self.customer_id.get()

            if customer_id != '':
                customer = self.get_customer(customer_id)
                self.update_db_vehicle_table(vehicle_to_rent.vehicle_id, customer.user_id)
                self.list_listbox.delete(vehicle_index)
                self.catalogue.rent_vehicle(vehicle_to_rent, customer)
                self.vehicle_list.pop(vehicle_index)
                self.customer_id.set('')

    def update_db_vehicle_table(self, vehicle_id, customer_id):
        """
        Updates the database table to include the customer id on the vehicle record

        :param vehicle_id: String of the vehicle record id
        :param customer_id: String of the customer record id
        """
        print("VehicleView:  Updating db vehicle table with vehicle id: %s and customer_id: %s" % (
            vehicle_id, customer_id))
        db_table_name = self.set_db_table_name()
        conn = sqlite3.connect(db_consts.DB_NAME)
        c = conn.cursor()
        c.execute('UPDATE %s SET user_id = \'%s\' WHERE vehicle_id = %s' % (db_table_name, customer_id, vehicle_id))
        c.close()
        conn.commit()
        conn.close()

    @staticmethod
    def get_customer(customer_id):
        """
        Returns a customer object to be used by the catalogue object when assigning a vehicle to rent

        TODO:
          - Retrieve Customer from the DB table once this is set up

        :param customer_id: String of the customer_id of the customer to return
        :return: Customer object
        """
        print("VehicleView:  Getting customer")
        # TODO Update with Customer from db
        addr = Address(customer_id, "My Address 1", "My Address 2", "My City", "My County", "My Post Code")
        bank = BankDetails(customer_id, "My Bank", "00-00-00", "12345678")
        cust = Customer(customer_id, "usr", "pass", "Forename", "Surname", addr, bank, '')
        return cust

    def change_to_main_menu(self):
        """
        Change the frame back to the main menu
        """
        print("VehicleView:  Navigating to Main Menu")
        self.parent.set_frame(vc.FRAME_MAIN)

    def show_rented(self):
        """
        Change the frame to display the vehicles currently being rented
        """
        print("Showing Rented")
        self.vehicle_list = []
        self.parent.set_frame(vc.FRAME_RENTED, self.vehicle_type)

    def show_available(self):
        """
        Change the frame to display the vehicles available to rent
        """
        print("Showing Available")
        self.vehicle_list = []
        self.parent.set_frame(vc.FRAME_VEHICLE, self.vehicle_type)
