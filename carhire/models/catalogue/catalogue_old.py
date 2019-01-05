from carhire.models.vehicle.vehicle import Vehicle


class Catalogue:
    """
    This class is used to create the Catalogue object
    """
    def __init__(self, vehicles=None):
        if vehicles is None:
            vehicles = []
        self.vehicles = vehicles

    def rent_vehicle(self, vehicle, customer):
        """

        :param vehicle:
        :param customer:
        """
        if vehicle in self.vehicles:
            vehicle.user_id = customer.user_id
            customer.vehicle_id = vehicle.vehicle_id
            self.vehicles.remove(vehicle)
            # Move vehicle to db currently rented table

    def return_vehicle(self, vehicle, customer):
        """

        :param vehicle:
        :param customer:
        """
        vehicle.remove_user_id()
        customer.remove_vehicle_id()
        self.vehicles.append(vehicle)
        # Move vehicle to available table

    def get_entries(self):
        """

        :return:
        """
        return self.vehicles

    def get_size(self):
        """

        :return:
        """
        return len(self.vehicles)

    def get_vehicle(self, index):
        """

        :param index:
        :return:
        """
        return Vehicle(self.vehicles[index][0],
                       self.vehicles[index][1],
                       self.vehicles[index][2],
                       self.vehicles[index][3],
                       self.vehicles[index][4],
                       self.vehicles[index][5],
                       self.vehicles[index][6],
                       self.vehicles[index][7])
