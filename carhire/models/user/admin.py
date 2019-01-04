import carhire.constants as vc
from carhire.models.user.user import User


class Admin(User):
    """
    This class is used to create the Admin object
    to use for Administrator Users
    """
    def __init__(self, user_id, username, password, forename, surname):
        super().__init__(user_id, username, password, forename, surname)
        self.type = vc.USER_TYPE_ADMIN
