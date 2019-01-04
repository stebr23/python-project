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

    def generate_vehicle_details_string(self):
        print(self.make + " | " + self.model + " | " + str(self.colour))
        spaces_to_add = [20 - len(self.make), 15 - len(self.model), 10 - len(self.colour)]
        vehicle_details_string = "%s:  " % self.vehicle_id
        vehicle_details_string += self.make + self.add_number_of_spaces(spaces_to_add[0])
        vehicle_details_string += self.model + self.add_number_of_spaces(spaces_to_add[1])
        vehicle_details_string += self.colour + self.add_number_of_spaces(spaces_to_add[2])
        return vehicle_details_string

    def add_number_of_spaces(self, spaces_to_add):
        return ' ' * spaces_to_add
