from carhire.app import LOG_LEVEL
from carhire.services.catalogue_service import CatalogueService
from carhire.services.db_service import DBService
from carhire.services.logging_service import LoggingService
from carhire.services.rental_service import RentalService
from carhire.services.view_controller import ViewController

log_service = LoggingService(LOG_LEVEL)
db_service = DBService()
catalogue_service = CatalogueService()
view_controller = ViewController()
rental_service = RentalService()
# user_service = UserService()
