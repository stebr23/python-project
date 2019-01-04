from carhire.models.vehicle.vehicle import Vehicle


class Car(Vehicle):
    """
    This class is used to create the Car object
    """
    def __init__(self, vehicle_id, make, model, wheels, colour, doors, passengers, user_id, bags, car_type):
        super().__init__(vehicle_id, make, model, wheels, colour, doors, passengers, user_id)
        self.bags = bags
        self.car_type = car_type

    def __str__(self):
        return ("CAR: vehicle_id: %s, make: %s, model: %s, wheels: %s, colour: %s, doors: %s, passengers: %s, "
                "user_id: %s, bags: %s, car_type: %s" %
                (self.vehicle_id, self.make, self.model, self.wheels, self.colour, self.doors, self.passengers,
                 self.user_id, self.bags, self.car_type))
