import unittest
import test.variables as tv

from carhire.models.catalogue.catalogue import Catalogue


class TestCatalogue(unittest.TestCase):

    def test_create_catalogue_class(self):
        catalogue_size = 5
        list_of_vehicles = tv.get_list_of_vehicles(catalogue_size)
        c1 = Catalogue(list_of_vehicles)

        self.assertEqual(len(c1.vehicles), catalogue_size)

    def test_rent_from_catalogue_removes_vehicle(self):
        vehicle = tv.get_vehicle()
        customer = tv.get_customer(tv.vehicle_id)
        catalogue = Catalogue([vehicle])

        self.assertEqual(1, catalogue.get_size())

        catalogue.rent_vehicle(vehicle, customer)
        self.assertEqual(0, catalogue.get_size())

    def test_rent_from_catalogue_adds_user_id_to_vehicle(self):
        vehicle = tv.get_vehicle()
        customer = tv.get_customer()
        catalogue = Catalogue([vehicle])

        catalogue.rent_vehicle(vehicle, customer)

        self.assertEqual(vehicle.user_id, customer.user_id)

    def test_rent_from_catalogue_adds_vehicle_id_to_customer(self):
        vehicle = tv.get_vehicle()
        customer = tv.get_customer()
        catalogue = Catalogue([vehicle])

        catalogue.rent_vehicle(vehicle, customer)

        self.assertEqual(customer.vehicle_id, vehicle.vehicle_id)

    def test_return_to_catalogue_adds_vehicle(self):
        vehicle = tv.get_vehicle()
        customer = tv.get_customer()
        catalogue = Catalogue([])

        catalogue.return_vehicle(vehicle, customer)

        self.assertEqual(1, catalogue.get_size())
        self.assertEqual(vehicle, catalogue.vehicles[0])
