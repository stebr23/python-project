"""Common variables and functions for unit tests"""

from carhire.models.vehicle.vehicle import Vehicle
from carhire.models.user.user import User
from carhire.models.user.customer import Customer, Address, BankDetails
from carhire.models.catalogue.catalogue import Catalogue

'''
Vehicle Variables
'''
vehicle_id = 456
make = "Ford"
model = "Focus"
wheels = 4
colour = "Blue"
doors = 4
passengers = 4


def get_vehicle(_customer_id=''):
    """

    :param _customer_id:
    :return:
    """
    return Vehicle(
        vehicle_id,
        make,
        model,
        wheels,
        colour,
        doors,
        passengers,
        _customer_id
    )


'''
User Variables
'''
user_id = 123
username = "my_username"
password = "my_password"
forename = "Emily"
surname = "Brayson"


def get_user():
    """

    :return:
    """
    return User(
        user_id,
        username,
        password,
        forename,
        surname
    )


def get_customer(_vehicle_id=''):
    """

    :param _vehicle_id:
    :return:
    """
    addr = get_address(user_id)
    bank = get_bank_details(user_id)
    cust = Customer(user_id, username, password, forename, surname, addr, bank, _vehicle_id)
    return cust


def get_address(_user_id):
    """

    :param _user_id:
    :return:
    """
    return Address(
        _user_id,
        "My Address 1",
        "My Address 2",
        "My City",
        "My County",
        "My Post Code"
    )


def get_bank_details(_user_id):
    """

    :param _user_id:
    :return:
    """
    return BankDetails(
        _user_id,
        "My Bank",
        "00-00-00",
        "12345678"
    )


'''
Catalogue Variables
'''
empty_catalogue = []


def get_populated_catalogue(size=5):
    """

    :param size:
    :return:
    """
    catalogue = get_list_of_vehicles(size)
    return Catalogue(catalogue)


def get_list_of_vehicles(size):
    """

    :param size:
    :return:
    """
    catalogue = []
    for i in range(size):
        catalogue.append(get_vehicle())
    return catalogue
