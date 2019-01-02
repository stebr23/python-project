from carhire.models.vehicle.vehicle import Vehicle


class Car(Vehicle):

    def __init__(self, vehicle_id, make, model, colour, doors, passengers, bags, car_type, wheels='4', user_id=''):
        super().__init__(self, vehicle_id, make, model, wheels, colour, doors, passengers, user_id)
        self.bags = bags
        self.car_type = car_type
