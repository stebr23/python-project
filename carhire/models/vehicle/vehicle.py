class Vehicle:
    """
    This class is used to create the Bike object
    """
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
        """
        Assigns a user id to the vehicle effectively linking
        the Vehicle and User objects

        :param user_id: String containing the id of the user object
        """
        if self.user_id == '':
            self.user_id = user_id

    def remove_user_id(self):
        """
        Removes the user_id value from the Vehicle, effectively
        removing the link between a Vehicle and a User
        """
        self.user_id = ''

    def generate_vehicle_details_string(self):
        """
        Creates a string containing details about the vehicle

        This string is used in a ListBox widget on the vehicle view
        frame to outline information about the vehicle, specifically:
         - Vehicle Make
         - Vehicle Model
         - Vehicle Colour
         - Vehicle User Id

        :return: String of details of the vehicle
        """
        spaces_to_add = [20 - len(self.make), 15 - len(self.model), 10 - len(self.colour)]
        vehicle_details_string = "%s:  " % self.vehicle_id
        vehicle_details_string += self.make + self.add_number_of_spaces(spaces_to_add[0])
        vehicle_details_string += self.model + self.add_number_of_spaces(spaces_to_add[1])
        vehicle_details_string += self.colour + self.add_number_of_spaces(spaces_to_add[2])
        vehicle_details_string += self.user_id if self.user_id else ''
        return vehicle_details_string

    @staticmethod
    def add_number_of_spaces(spaces):
        """
        Returns a string containing N number of spaces

        It is used to format the vehicle details string that is
        inserted into the ListBox widget on the Vehicle View frame
        :param spaces: Integer of the number of spaces wishing to be generated
        :return: String containing N number of spaces
        """
        return ' ' * spaces

    def get_vehicle_id(self):
        """
        Get the vehicle id
        :return: String of the vehicle ID
        """
        return self.vehicle_id

    def get_make(self):
        """
        Get the vehicle make
        :return: String of the vehicle make
        """
        return self.make

    def get_model(self):
        """
        Get the vehicle model
        :return: String of the vehicle's model
        """
        return self.model

    def get_wheels(self):
        """
        Get the number of wheels the vehicle has
        :return: Integer of the number of wheels
        """
        return self.wheels

    def get_colour(self):
        """
        Get the colour of the vehicle
        :return: String of the colour of the vehicle
        """
        return self.colour

    def get_doors(self):
        """
        Get the number of doors the vehicle had
        :return: Integer of the number of doors
        """
        return self.doors

    def get_passengers(self):
        """
        Get the number of passengers the vehicle can hold
        :return: Integer of the number of passengers the vehicle holds
        """
        return self.passengers

    def get_user_id(self):
        """
        Get the user_id associated with the vehicle
        :return: String of the user id associated with the vehicle
        """
        return self.user_id
