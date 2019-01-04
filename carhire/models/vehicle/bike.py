from carhire.models.vehicle.vehicle import Vehicle


class Bike(Vehicle):

    def __init__(self, vehicle_id, make, model, wheels, colour, doors, passengers, user_id, storage):
        super().__init__(vehicle_id, make, model, wheels, colour, doors, passengers, user_id)
        self.storage = storage
