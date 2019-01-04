from carhire.models.vehicle.vehicle import Vehicle


class Car(Vehicle):

    def __init__(self, vehicle_id, make, model, wheels, colour, doors, passengers, user_id, bags, car_type):
        super().__init__(vehicle_id, make, model, wheels, colour, doors, passengers, user_id)
        self.bags = bags
        self.car_type = car_type
