"""Unit Tests for the View"""

import unittest
from carhire.views.root_view import RootView


class TestView(unittest.TestCase):

    def test_create_view(self):
        root_view = RootView()

        self.assertIsInstance(root_view, RootView)
