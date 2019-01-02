from carhire.models.vehicle.vehicle import Vehicle


class Bike(Vehicle):

    def __init__(self, vehicle_id, make, model, colour, doors, passengers, storage, wheels='2', user_id=''):
        super().__init__(self, vehicle_id, make, model, wheels, colour, doors, passengers, user_id)
        self.storage = storage
