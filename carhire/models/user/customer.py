import carhire.constants as vc
from carhire.models.user.user import User


class Customer(User):
    """
    This class is used to create the Customer object
    """
    def __init__(self, user_id, username, password, forename, surname, address, bank_details, vehicle_id=''):
        User.__init__(self, user_id, username, password, forename, surname)
        self.type = vc.USER_TYPE_CUSTOMER
        self.address = address
        self.bank_details = bank_details
        self.vehicle_id = vehicle_id

    def add_vehicle_id(self, vehicle_id):
        """
        Add a vehicle_id to the Customer object,
        effectively linking a vehicle to a customer

        :param vehicle_id: id of the vehicle to link to the customer
        """
        if self.vehicle_id == '':
            self.vehicle_id = vehicle_id

    def remove_vehicle_id(self):
        """
        Remove the vehicle_id from the Customer object,
        effectively removing the link between vehicle and customer
        """
        self.vehicle_id = ''


class Address:
    """
    This class is used to create the Address object

    The Address is a requirement for any Customer object
    and includes address details of the customer
    """
    def __init__(self, user_id, address_line_1, address_line_2, town_city, county, post_code):
        self.user_id = user_id
        self.address_line_1 = address_line_1
        self.address_line_2 = address_line_2
        self.town_city = town_city
        self.county = county
        self.post_code = post_code


class BankDetails:
    """
    This class is used to create the BankDetails object

    The BankDetails is a requirement for any Customer object
    and includes banking details of the customer
    """
    def __init__(self, user_id, bank_name, sort_code, account_number):
        self.user_id = user_id
        self.bank_name = bank_name,
        self.sort_code = sort_code,
        self.account_number = account_number
