class Catalogue:

    def __init__(self, vehicles=[]):
        self.vehicles = vehicles

    def rent_vehicle(self, vehicle, customer):
        if vehicle in self.vehicles:
            vehicle.user_id = customer.user_id
            customer.vehicle_id = vehicle.vehicle_id
            self.vehicles.remove(vehicle)
            # Move vehicle to db currently rented table

    def return_vehicle(self, vehicle, customer):
        vehicle.remove_user_id()
        customer.remove_vehicle_id()
        self.vehicles.append(vehicle)
        # Move vehicle to available table

    def get_size(self):
        return len(self.vehicles)
