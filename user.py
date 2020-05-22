from credential import Credential


class User:
    """
    a class that generates new instances of users
    """
    pass

    users_list = []

    def __init__(self, first_name, last_name):
        '''
        __init__ method that helps us define properties for our users.
        '''

        self.first_name = first_name
        self.last_name = last_name

    def save_user(self):
        """
        save_contact method saves contact objects into user_list
        """
        User.users_list.append(self)

    def delete_users(self):
        """
        method that deletes a user from the list
        """
        User.users_list.remove(self)

    @classmethod
    def log_in(cls, user_name, password):
        '''
        Method that allows a user to log into their credential
        Args:
            name : user_name of the user
            password : password for the user
        Returns:
            Credential list for the user that matches the name and password
            False: if the name or password is incorrect
        '''

        # Search for the user in the user list
        for user in User.users_list:
            if user.user_name == user_name and user.user_password == password:
                return Credential.credential_list

        return False

    @classmethod
    def display_users(cls):
        """
        method that returns the list
        """
        return User.users_list

    @classmethod
    def users_exist(cls, name):
        '''
        method that checks if a user exists from the user_list

        Args:
            name: username to search if the person exists
        Returns:
        Boolean: true or false depending if the user exists
        '''
        for user in User.users_list:
            if user.user_name == name:
                return True

        return False
