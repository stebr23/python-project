import unittest

from carhire.models.catalogue.catalogue import Catalogue
from carhire.models.vehicle.car import Car


class TestCatalogue(unittest.TestCase):
    """
    Testing the Catalogue class
    """

    def test_create_catalogue_class(self):
        """
        Test the Catalogue class exists and an object can be instantiated
        """
        vehicle_type = 'CAR'
        c1 = Catalogue(vehicle_type)

        self.assertEqual(c1.__class__, Catalogue)

    def test_get_vehicle_list(self):
        vehicle_type = 'CAR'
        vehicle_list = ["Car1", "Car2"]
        catalogue = Catalogue(vehicle_type, vehicle_list)

        self.assertEqual(catalogue.get_list(), vehicle_list)

    def test_get_vehicle_by_id(self):
        vehicle_type = 'Cars'
        car1 = Car("123", "Ford", "Focus", 4, "Blue", 3, 5, "abc", 4, "Sedan")
        car2 = Car("456", "Ford", "Focus", 4, "Blue", 3, 5, "abc", 4, "Sedan")
        car3 = Car("789", "Ford", "Focus", 4, "Blue", 3, 5, "abc", 4, "Sedan")
        car_list = [car1, car2, car3]
        catalogue = Catalogue(vehicle_type, car_list)

        car4 = catalogue.get_vehicle_by_id("123")
        car5 = catalogue.get_vehicle_by_id("456")
        car6 = catalogue.get_vehicle_by_id("789")

        self.assertEqual(car1.vehicle_id, car4.vehicle_id)
        self.assertEqual(car2.vehicle_id, car5.vehicle_id)
        self.assertEqual(car3.vehicle_id, car6.vehicle_id)
