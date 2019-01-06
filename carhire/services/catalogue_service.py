"""
The Catalogue Service is involved with serving up catalogues to the application

The catalogue service communicates with the DB Service to retrieve vehicle records
"""
import carhire.services as services
from carhire.models.catalogue.catalogue import Catalogue


class CatalogueService:
    """
    This class populates two Catalogues, a rented and available vehicle catalogue
    from the database using the DB Service
    """

    @staticmethod
    def get_catalogue_available(vehicle_type):
        """
        Populates available vehicle (where user_id is null)
        catalogue from the db table provided by the param vehicle type
        TODO:
          - Refactor

        :param vehicle_type: String of the vehicle type that matches a db table (cars, bikes or vans)
        """
        services.log_service.trace("Catalogue Service", "Populating catalogues from db with vehicle_type: %s" % vehicle_type)
        records_list = services.db_service.execute_select(vehicle_type, "user_id IS NULL")
        return Catalogue(vehicle_type, records_list)

    @staticmethod
    def get_catalogue_rented(vehicle_type):
        """
        Populates rented vehicle catalogue (where user_id is nor null)
        from the db table provided by the param vehicle type
        TODO:
          - Refactor

        :param vehicle_type: String of the vehicle type that matches a db table (cars, bikes or vans)
        """
        services.log_service.trace("Catalogue Service", "Populating catalogues from db with vehicle_type: %s" % vehicle_type)
        records_list = services.db_service.execute_select(vehicle_type, "user_id IS NOT NULL")
        return Catalogue(vehicle_type, records_list)
