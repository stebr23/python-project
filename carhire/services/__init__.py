from carhire.app import LOG_LEVEL
from carhire.services.db_service import DBService
from carhire.services.logging_service import LoggingService

log_service = LoggingService(LOG_LEVEL)
db_service = DBService()
# rental_service = RentalService()
# catalogue_service = CatalogueService()
# user_service = UserService()
