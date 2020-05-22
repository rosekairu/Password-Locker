class User:
    """
    a class that generates new instances of users
    """
    pass

    users_array = []

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def save_user_details(self):
        """
        save_contact method saves contact objects into user_array
        """
        User.users_array.append(self)

    @classmethod
    def display_users(cls):
        """
        method that returns the class array
        """
        return cls.users_array
