from carhire.models.vehicle.vehicle import Vehicle


class Van(Vehicle):

    def __init__(self, vehicle_id, make, model, wheels, colour, doors, passengers, storage_space, user_id=''):
        super().__init__(self, vehicle_id, make, model, wheels, colour, doors, passengers, user_id)
        self.wheels = 4
        self.storage_space = storage_space
