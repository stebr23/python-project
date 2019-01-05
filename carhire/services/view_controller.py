"""
This service is utilised to control the views

Method calls to other services will be made available for the Root Frame to call

Likewise all services will be collated into this class
"""
import carhire.constants as consts
import carhire.services as services
import tkinter as tk
from carhire.views.main_menu import MainMenu
from carhire.views.vehicle.vehicle_view import VehicleFrame


class ViewController:

    _root_frame = None
    current_frame = ''

    def add_root_frame(self, root_frame):
        """
        Adds the root frame to the View Controller so its methods can be called
        :param root_frame: A TKinter Frame that is the root frame
        """
        services.log_service.trace("ViewController", "Adding root frame")
        self._root_frame = root_frame

    def set_frame(self, frame_name=consts.FRAME_MAIN, vehicle_type=''):
        """
        Change the current frame of the root window by
        providing the name of the frame and an optional
        variable that outlines which vehicle the user wishes
        to view when selecting the Vehicle frame

        :param frame_name: String of the name of the frame being set
        :param vehicle_type: String of the type of vehicle to be shown
        """
        services.log_service.trace("ViewController", "Setting frame in root to %s" % frame_name)
        if self._root_frame.current_frame:
            self._root_frame.current_frame.grid_forget()

        if frame_name == consts.FRAME_MAIN:
            self._root_frame.frame_name = consts.FRAME_MAIN
            self._root_frame.current_frame = MainMenu(self._root_frame)
        if frame_name == consts.FRAME_VEHICLE:
            self._root_frame.frame_name = consts.FRAME_VEHICLE
            self._root_frame.current_frame = VehicleFrame(self._root_frame, vehicle_type)
        if frame_name == consts.FRAME_RENTED:
            self._root_frame.frame_name = consts.FRAME_RENTED
            self._root_frame.current_frame = VehicleFrame(self._root_frame, vehicle_type)

        self._root_frame.current_frame.grid(sticky=(tk.E + tk.W + tk.N + tk.S))

    @staticmethod
    def get_available_vehicles_catalogue(vehicle_type):
        """
        Retrieves Catalogue of vehicles available to rent from the Catalogue Service
        :param vehicle_type: String of the type of vehicle to return
        :return: Catalogue including the list of vehicles
        """
        services.log_service.trace("ViewController", "Getting available %s catalogue" % vehicle_type)
        return services.catalogue_service.get_catalogue_available(vehicle_type)

    @staticmethod
    def get_rented_vehicles_catalogue(vehicle_type):
        """
        Retrieves Catalogue of vehicles currently rented from the Catalogue Service
        :param vehicle_type: String of the type of vehicle to return
        :return: Catalogue including the list of vehicles
        """
        services.log_service.trace("ViewController", "Getting available %s catalogue" % vehicle_type)
        return services.catalogue_service.get_catalogue_rented(vehicle_type)
