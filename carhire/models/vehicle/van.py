from carhire.models.vehicle.vehicle import Vehicle


class Van(Vehicle):
    """
    This class is used to create the Van object from the base Vehicle
    """
    def __init__(self, vehicle_id, make, model, wheels, colour, doors, passengers, user_id, storage_space):
        super().__init__(vehicle_id, make, model, wheels, colour, doors, passengers, user_id)
        self.storage_space = storage_space
