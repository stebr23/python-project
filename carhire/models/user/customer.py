from carhire.constants import *
from carhire.models.user.user import User


class Customer(User):

    def __init__(self, user_id, username, password, forename, surname, address, bank_details, vehicle_id=''):
        User.__init__(self, user_id, username, password, forename, surname)
        self.type = USER_TYPE_CUSTOMER
        self.address = address
        self.bank_details = bank_details
        self.vehicle_id = vehicle_id

    def add_vehicle_id(self, vehicle_id):
        if self.vehicle_id == '':
            self.vehicle_id = vehicle_id

    def remove_vehicle_id(self):
        self.vehicle_id = ''


class Address:

    def __init__(self, user_id, address_line_1, address_line_2, town_city, county, post_code):
        self.user_id = user_id
        self.address_line_1 = address_line_1
        self.address_line_2 = address_line_2
        self.town_city = town_city
        self.county = county
        self.post_code = post_code


class BankDetails:

    def __init__(self, user_id, bank_name, sort_code, account_number):
        self.user_id = user_id
        self.bank_name = bank_name,
        self.sort_code = sort_code,
        self.account_number = account_number
