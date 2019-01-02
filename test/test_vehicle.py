"""Unit Tests for the Vehicle class"""

import unittest
import test.variables as tv

from carhire.models.vehicle.vehicle import Vehicle


class TestVehicle(unittest.TestCase):

    def test_create_vehicle_class(self):
        make = "Ford"
        model = "Focus"
        wheels = 4
        colour = "Blue"
        doors = 4
        passengers = 4
        user_id = 123
        vehicle = tv.get_vehicle(user_id)

        self.assertEqual(vehicle.make, make)
        self.assertEqual(vehicle.model, model)
        self.assertEqual(vehicle.wheels, wheels)
        self.assertEqual(vehicle.colour, colour)
        self.assertEqual(vehicle.doors, doors)
        self.assertEqual(vehicle.passengers, passengers)
        self.assertEqual(vehicle.user_id, user_id)

    def test_create_vehicle_class_sans_user_id(self):
        vehicle_id = tv.vehicle_id
        make = tv.make
        model = tv.model
        wheels = tv.wheels
        colour = tv.colour
        doors = tv.doors
        passengers = tv.passengers

        vehicle = Vehicle(
            vehicle_id,
            make,
            model,
            wheels,
            colour,
            doors,
            passengers
        )

        self.assertEqual(vehicle.make, make)
        self.assertEqual(vehicle.model, model)
        self.assertEqual(vehicle.wheels, wheels)
        self.assertEqual(vehicle.colour, colour)
        self.assertEqual(vehicle.doors, doors)
        self.assertEqual(vehicle.passengers, passengers)
        self.assertEqual(vehicle.user_id, '')

    def test_assign_user_id_to_vehicle(self):
        vehicle = tv.get_vehicle()
        customer = tv.get_customer()

        vehicle.assign_user_id(customer.user_id)

        self.assertEqual(123, vehicle.user_id)
