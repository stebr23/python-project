"""Unit Tests for the View"""

import unittest
from carhire.views.root_view import RootView
from carhire.views.vehicle.vehicle_view import VehicleFrame


class TestView(unittest.TestCase):

    def test_create_view(self):
        root_view = RootView()

        self.assertIsInstance(root_view, RootView)

    def test_create_vehicle_frame(self):
        vehicle_frame = VehicleFrame()

        self.assertIsInstance(vehicle_frame, VehicleFrame)
