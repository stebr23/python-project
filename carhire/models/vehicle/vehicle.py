def add_number_of_spaces(spaces_to_add):
    return ' ' * spaces_to_add


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

    def assign_user_id(self, user_id):
        if self.user_id == '':
            self.user_id = user_id

    def remove_user_id(self):
        self.user_id = ''

    def generate_vehicle_details_string(self):
        spaces_to_add = [20 - len(self.make), 15 - len(self.model), 10 - len(self.colour)]
        vehicle_details_string = "%s:  " % self.vehicle_id
        vehicle_details_string += self.make + add_number_of_spaces(spaces_to_add[0])
        vehicle_details_string += self.model + add_number_of_spaces(spaces_to_add[1])
        vehicle_details_string += self.colour + add_number_of_spaces(spaces_to_add[2])
        vehicle_details_string += self.user_id if self.user_id else ''
        return vehicle_details_string

    def get_vehicle_id(self):
        return self.vehicle_id

    def get_make(self):
        return self.make

    def get_model(self):
        return self.model

    def get_wheels(self):
        return self.wheels

    def get_colour(self):
        return self.colour

    def get_doors(self):
        return self.doors

    def get_passengers(self):
        return self.passengers

    def get_user_id(self):
        return self.user_id
