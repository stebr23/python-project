"""
The Rental Service is involved with handling renting and returning vehicles
"""
import carhire.services as services

class RentalService:
    """
    This class will provide the rent and return functionality for the vehicles
    and customers in the database
    """

    def __init__(self):
        pass

    @staticmethod
    def rent_vehicle(vehicle_type, vehicle_id, user_id):
        """
        Assigns the vehicle a user_id and assigns a customer a vehicle_id,
        updating the values in the database via the DB Service
        :param vehicle_type: vehicle_type: String of the type of vehicle to return
        :param vehicle_id: String of the vehicle's ID
        :param user_id: String of the customer's ID
        """
        services.log_service.trace("RentalService",
                                   "Updating db vehicle table with type: %s, vehicle id: %s and customer_id: %s" % (vehicle_type, vehicle_id, user_id))
        values = "user_id='%s'" % user_id
        condition = "vehicle_id='%s'" % vehicle_id
        services.db_service.execute_update(vehicle_type, values, condition)

    @staticmethod
    def return_vehicle(vehicle_type, vehicle_id, user_id):
        """
        Assigns the vehicle a user_id and assigns a customer a vehicle_id,
        updating the values in the database via the DB Service
        :param user_id: String of the users's id to remove
        :param vehicle_type: vehicle_type: String of the type of vehicle to return
        :param vehicle_id: String of the vehicle's ID
        """
        services.log_service.trace("RentalService",
                                   "Updating db vehicle table with type: %s, vehicle id: %s and customer_id: %s" % (
                                    vehicle_type, vehicle_id, user_id))
        values = "user_id=NULL"
        condition = "vehicle_id='%s'" % vehicle_id
        services.db_service.execute_update(vehicle_type, values, condition)

