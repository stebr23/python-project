from carhire.models.vehicle.bike import Bike
from carhire.models.vehicle.car import Car
from carhire.models.vehicle.van import Van
import carhire.constants as vc


class Catalogue:
    """
    This class is used to create the Catalogue object
    """

    vehicle_list = []
    _vehicle_type = ''

    def __init__(self, vehicle_type, vehicles_list=[]):
        self._vehicle_type = vehicle_type
        self.vehicle_list = vehicles_list

    def get_list(self):
        """
        Returns vehicle list
        :return: vehicle list
        """
        return self.vehicle_list

    def get_vehicle_by_id(self, vehicle_id):
        """
        Returns a vehicle from the catalogue when provided with a vehicle id
        :param vehicle_id: String of the id relating to the vehicle
        :return: Specific Vehicle object (Car, Bike, or Van) depending on the vehicle type set on initialising
        """
        for vehicle in self.vehicle_list:
            if vehicle.vehicle_id == vehicle_id:
                return self.return_vehicle(vehicle)

    def return_vehicle(self, vehicle):
        """
        Returns a vehicle which has matched the initial vehicle id
        :param vehicle: Tuple containing details of a vehicle
        :return: Specific Vehicle object (Car, Bike, or Van) depending on the vehicle type set on initialising
        """
        if self._vehicle_type == vc.CARS:
            return self.return_car(vehicle)
        elif self._vehicle_type == vc.BIKES:
            return self.return_bike(vehicle)
        elif self._vehicle_type == vc.VANS:
            return self.return_van(vehicle)

    @staticmethod
    def return_van(vehicle):
        """
        Returns a Van object from the details of the tuple found in the catalogue
        :param vehicle: Tuple containing details of the van vehicle
        :return: Van object instantiated with the details from the catalogue
        """
        van = Van(vehicle.vehicle_id, vehicle.make, vehicle.model, vehicle.wheels, vehicle.colour, vehicle.doors,
                  vehicle.passengers, vehicle.user_id, vehicle.storage_space)
        return van

    @staticmethod
    def return_bike(vehicle):
        """
        Returns a Bike object from the details of the tuple found in the catalogue
        :param vehicle: Tuple containing details of the bike vehicle
        :return: Bike object instantiated with the details from the catalogue
        """
        bike = Bike(vehicle.vehicle_id, vehicle.make, vehicle.model, vehicle.wheels, vehicle.colour, vehicle.doors,
                    vehicle.passengers, vehicle.user_id, vehicle.storage)
        return bike

    @staticmethod
    def return_car(vehicle):
        """
        Returns a Car object from the details of the tuple found in the catalogue
        :param vehicle: Tuple containing details of the car vehicle
        :return: Car object instantiated with the details from the catalogue
        """
        # car = Car(vehicle[0], vehicle[1], vehicle[2], vehicle[3], vehicle[4], vehicle[5], vehicle[6],
        #           vehicle[7], vehicle[8], vehicle[9])
        car = Car(vehicle.vehicle_id, vehicle.make, vehicle.model, vehicle.wheels, vehicle.colour, vehicle.doors,
                  vehicle.passengers, vehicle.user_id, vehicle.bags, vehicle.car_type)
        return car
