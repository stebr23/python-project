import tkinter as tk
import carhire.constants as vc
import carhire.database as db_consts
import carhire.services as services

from tkinter import ttk
from carhire.models.user.customer import Customer, Address, BankDetails
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
        self.view_controller = self.parent._view_controller
        self.vehicle_type = vehicle_type
        self.name = self.vehicle_type
        self.title_string = tk.StringVar()
        self.title_string.set(vehicle_type)
        self.list_frame = tk.Frame()
        self.list_listbox = tk.Listbox()
        self.scrollbar = tk.Scrollbar()
        self.vehicle_list = []
        self.catalogue = None
        self.vehicle = ''
        self.user = ''

        self.create_main_display()
        self.create_vehicle_list_display()

        services.log_service.trace("VehicleView", "READY")

    def create_main_display(self):
        """
        Contains the functions that create the widgets for the frame
        """
        services.log_service.trace("VehicleView", "Creating main vehicle view display")
        self.configure_root_frame()
        self.set_title()
        self.set_main_menu_button()

    def configure_root_frame(self):
        """
        Configures the root frame
        """
        services.log_service.trace("VehicleView", "Configuring root frame")
        self.parent.title("Car Hire - %s" % self.vehicle_type)
        self.configure(background=vc.BG)
        self.columnconfigure(1, weight=1)

    def set_title(self):
        """
        Sets the title of the frame so the user knows which frame they are viewing
        """
        services.log_service.trace("VehicleView", "Setting title")
        title_label = ttk.Label(self, textvariable=self.title_string, font=("TkDefaultFont", 64), wraplength=600,
                                foreground=vc.WHITE)
        title_label.configure(background=vc.BG, anchor="center")
        title_label.grid(row=0, column=1, sticky=(tk.E + tk.W), pady=(30, 80))

    def set_main_menu_button(self):
        """
        Creates a button widget for the user to navigate back to the
        main menu
        """
        services.log_service.trace("VehicleView", "Setting main menu button")
        main_menu_image = tk.PhotoImage(file=HOME_ICON)
        main_menu_button = tk.Button(self, text="   ", bd=0, cursor="hand2", command=self.change_to_main_menu,
                                     image=main_menu_image, compound="right", background=vc.BG, fg=vc.FG)
        main_menu_button.image = main_menu_image
        main_menu_button.grid(row=0, column=0, sticky=(tk.E + tk.W))

    def create_vehicle_list_display(self):
        """
        Contains the functions used to create the list of vehicles
        for the user to interact with
        """
        services.log_service.trace("VehicleView", "Creating vehicle list display")
        self.populate_catalogue()
        self.create_vehicle_list_frame()

    def populate_catalogue(self):
        """
        Populates the Catalogue object with vehicles from the database
        by retrieving the Catalogue from the View Controller

        The types of vehicles (Car, Bike or Van) are determined by the
        option the user chose form the main menu
        """
        services.log_service.trace("VehicleView", "Populating catalogue")

        if self.parent.frame_name == vc.FRAME_VEHICLE:
            self.catalogue = self.view_controller.get_available_vehicles_catalogue(self.vehicle_type)
            services.log_service.debug("VehicleView", "catalogue: %s" % self.catalogue)
        elif self.parent.frame_name == vc.FRAME_RENTED:
            self.catalogue = self.view_controller.get_rented_vehicles_catalogue(self.vehicle_type)
            services.log_service.debug("VehicleView", "catalogue: %s" % self.catalogue)

    def create_vehicle_list_frame(self):
        """
        Contains the functions executed to produce the frame containing the list of vehicles and associated
        buttons
        """
        services.log_service.trace("VehicleView", "Creating vehicle list frame")
        self.set_up_list_widgets()
        self.add_vehicles_from_catalogue_to_listbox()
        self.pack_list_widgets()
        if self.parent.frame_name == vc.FRAME_VEHICLE:
            self.create_rent_button_and_customer_input()
        self.set_change_view_button()

    def set_up_list_widgets(self):
        """
        Instantiates the widgets for the vehicle list frame and packs them to the frame
        """
        services.log_service.trace("VehicleView", "Setting up list widgets")
        self.list_frame = tk.Frame(self, bd=2, relief=tk.SUNKEN, width=800, height=300)
        self.list_frame.pack_propagate(False)
        self.scrollbar = tk.Scrollbar(self.list_frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.list_listbox = tk.Listbox(self.list_frame, bd=0, font="consolas", yscrollcommand=self.scrollbar.set,
                                       width=800, height=300)
        self.list_listbox.pack_propagate(False)

    def set_change_view_button(self):
        """
        Create the button to reload the frame showing the vehicles that are
        currently available or that are rented out and place it in the frame
        """
        services.log_service.trace("VehicleView", "current frame_name is: %s" % self.parent.frame_name)
        if self.parent.frame_name == vc.FRAME_VEHICLE:
            currently_rented_button = tk.Button(self, text="View Currently Rented %s" % self.vehicle_type,
                                                command=self.show_rented)
            currently_rented_button.grid(row=5, column=1, pady=(10, 0))
        elif self.parent.frame_name == vc.FRAME_RENTED:
            currently_rented_button = tk.Button(self, text="View Available %s" % self.vehicle_type,
                                                command=self.show_available)
            currently_rented_button.grid(row=5, column=1, pady=(10, 0))
            return_vehicle_button = tk.Button(self, text="Return Selected %s" % self.vehicle_type[0:-1],
                                              command=self.return_selected)
            return_vehicle_button.grid(row=6, column=1, pady=(10, 0))

    def add_vehicles_from_catalogue_to_listbox(self):
        """
        Creates relevant Vehicle objects (Car || Bike || Van) from the data in the database tables
        and displays the data in the listbox widget.

        The function calls the Vehicle's generate details function to populate the listbox
        """
        services.log_service.trace("VehicleView", "Adding vehicles from catalogue to listbox")
        services.log_service.trace("VehicleView", "Setting Vehicle object to specific vehicle type (Car||Van||Bike)")

        for vehicle in self.catalogue.get_list():
            services.log_service.debug("VehicleView", "Vehicle: %s" % vehicle[0])
            if self.vehicle_type == vc.CARS:
                self.vehicle = self.catalogue.return_car(vehicle)
            elif self.vehicle_type == vc.BIKES:
                self.vehicle = self.catalogue.return_bike(vehicle)
            elif self.vehicle_type == vc.VANS:
                self.vehicle = self.catalogue.return_van(vehicle)

            vehicle_details = self.vehicle.generate_vehicle_details_string()
            self.list_listbox.insert(tk.END, vehicle_details)

    def pack_list_widgets(self):
        """
        Packs the widgets to the vehicle list frame
        """
        services.log_service.trace("VehicleView", "Packing widgets")
        self.list_listbox.pack()
        self.scrollbar.config(command=self.list_listbox.yview)
        self.list_frame.grid(row=1, column=1)

    def create_rent_button_and_customer_input(self):
        """
        Creates the widgets to insert a customer id and rent a vehicle out to them
        """
        services.log_service.trace("VehicleView", "Creating rent buttons and customer input field")
        customer_id_field_label = tk.Label(self, text="Enter a customer id:", fg=vc.FG, bg=vc.BG)
        customer_id_field_label.grid(row=2, column=1, pady=(10, 0))
        customer_id_field = tk.Entry(self, textvariable=self.customer_id, width=10)
        customer_id_field.grid(row=3, column=1, pady=(10, 0))
        rent_button = tk.Button(self, text="Rent Selected %s" % self.vehicle_type[0:len(self.vehicle_type) - 1],
                                command=self.rent_selected)
        rent_button.grid(row=4, column=1, pady=(10, 0))

    def set_db_table_name(self):
        """
        Sets the database table name to use as part of the SQL query

        It is determined by the vehicle type provided when the frame initially loads
        :return: String of the database table for the selected vehicle type
        """
        services.log_service.trace("VehicleView", "Setting db table name depending on vehicle type")
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
        services.log_service.trace("VehicleView", "Renting selected vehicle...")

        if self.list_listbox.curselection():
            vehicle_index = self.list_listbox.curselection()[0]
            vehicle_to_rent = self.list_listbox.get(vehicle_index)
            vehicle_id = vehicle_to_rent[0:4]
            services.log_service.debug("VehicleView", "vehicle: %s" % vehicle_id)
            customer_id = self.customer_id.get()

            if customer_id != '':
                self.view_controller.rent_vehicle(self.vehicle_type, vehicle_id, self.customer_id.get())
                self.list_listbox.delete(vehicle_index)
                self.customer_id.set('')

    def return_selected(self):
        """
        Takes the selected vehicle and removes the user_id
        and removes the vehicle_id from the user

        The vehicle is removed from the catalogue and the listbox

        The database is updated to clear the user id on the specific vehicle
        table for the selected vehicle whilst removing the vehicle_id from
        the user
        """
        services.log_service.trace("VehicleView", "Returning selected vehicle...")
        if self.list_listbox.curselection():
            vehicle_index = self.list_listbox.curselection()[0]
            vehicle_to_rent = self.list_listbox.get(vehicle_index)
            vehicle_id = vehicle_to_rent[0:4]
            customer_id = vehicle_to_rent.split()[-1]

            services.log_service.debug("VehicleView", "vehicle: %s, customer_id: %s" % (vehicle_id, customer_id))
            self.view_controller.return_vehicle(self.vehicle_type, vehicle_id, customer_id)
            self.list_listbox.delete(vehicle_index)

    @staticmethod
    def get_customer(customer_id):
        """
        Returns a customer object to be used by the catalogue object when assigning a vehicle to rent

        TODO:
          - Retrieve Customer from the DB table with User Service once this is set up

        :param customer_id: String of the customer_id of the customer to return
        :return: Customer object
        """
        services.log_service.trace("VehicleView", "Getting customer")
        # TODO Update with Customer from view_controller
        addr = Address(customer_id, "My Address 1", "My Address 2", "My City", "My County", "My Post Code")
        bank = BankDetails(customer_id, "My Bank", "00-00-00", "12345678")
        cust = Customer(customer_id, "usr", "pass", "Forename", "Surname", addr, bank, '')
        return cust

    def change_to_main_menu(self):
        """
        Change the frame back to the main menu
        """
        services.log_service.trace("VehicleView", "Navigating to Main Menu")
        self.view_controller.set_frame(vc.FRAME_MAIN)

    def show_rented(self):
        """
        Change the frame to display the vehicles currently being rented
        """
        print("Showing Rented")
        self.vehicle_list = []
        self.view_controller.set_frame(vc.FRAME_RENTED, self.vehicle_type)

    def show_available(self):
        """
        Change the frame to display the vehicles available to rent
        """
        print("Showing Available")
        self.vehicle_list = []
        self.view_controller.set_frame(vc.FRAME_VEHICLE, self.vehicle_type)
