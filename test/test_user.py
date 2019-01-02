"""Unit Tests for the User class"""

import unittest
import test.variables as tv


class TestUser(unittest.TestCase):

    def test_create_user_class(self):
        user_id = 123
        username = "my_username"
        password = "my_password"
        forename = "Emily"
        surname = "Brayson"

        u = tv.get_user()

        self.assertEqual(u.user_id, user_id)
        self.assertEqual(u.username, username)
        self.assertEqual(u.password, password)
        self.assertEqual(u.forename, forename)
        self.assertEqual(u.surname, surname)

    def test_assign_vehicle_id_to_customer(self):
        vehicle = tv.get_vehicle()
        customer = tv.get_customer()

        customer.add_vehicle_id(vehicle.get_vehicle_id())

        self.assertEqual(vehicle.vehicle_id, customer.vehicle_id)

    def test_assign_vehicle_id_to_already_assigned(self):
        vehicle = tv.get_vehicle()
        customer = tv.get_customer(vehicle.get_vehicle_id())
        new_vehicle_id = 789

        customer.add_vehicle_id(new_vehicle_id)

        self.assertNotEqual(new_vehicle_id, customer.vehicle_id)

    def test_remove_vehicle_id_from_customer(self):
        customer = tv.get_customer(tv.vehicle_id)

        customer.remove_vehicle_id()

        self.assertEqual('', customer.vehicle_id)
