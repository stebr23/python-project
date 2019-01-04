from carhire.constants import *
from carhire.models.user.user import User


class Admin(User):

    def __init__(self, user_id, username, password, forename, surname):
        super().__init__(user_id, username, password, forename, surname)
        self.type = USER_TYPE_ADMIN
