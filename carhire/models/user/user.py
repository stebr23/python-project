class User:
    """
    This class is used to create the base User object
    """
    def __init__(self, user_id, username, password, forename, surname):
        self.user_id = user_id
        self.username = username
        self.password = password
        self.forename = forename
        self.surname = surname
