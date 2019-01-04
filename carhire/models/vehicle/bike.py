from carhire.models.vehicle.vehicle import Vehicle


class Bike(Vehicle):
    """
    This class is used to create the Bike object
    """
    def __init__(self, vehicle_id, make, model, wheels, colour, doors, passengers, user_id, storage):
        super().__init__(vehicle_id, make, model, wheels, colour, doors, passengers, user_id)
        self.storage = storage
