class Vehicle:

    def __init__(self, vehicle_id, make, model, wheels, colour, doors, passengers, user_id=''):
        self.vehicle_id = vehicle_id
        self.make = make
        self.model = model
        self.wheels = wheels
        self.colour = colour
        self.doors = doors
        self.passengers = passengers
        self.user_id = user_id

    def get_vehicle_id(self):
        return self.vehicle_id

    def assign_user_id(self, user_id):
        if self.user_id == '':
            self.user_id = user_id

    def remove_user_id(self):
        self.user_id = ''
