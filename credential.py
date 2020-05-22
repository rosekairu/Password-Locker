import clipboard


class Credential:
    """
    a class that generates new Credentials for Users
    """

    credential_list = []

    @classmethod
    def __init__(self, user_name, password):
        """
        Method that defines user credentials
        """

        self.user_name = user_name
        self.password = password

    def save_credential(self):
        """
        save_contact method saves credentials objects into credintial list
        """
        Credential.credential_list.append(self)

    def delete_credential(self):
        """
        Method that deletes user credentials
        """
        Credential.credential_list.remove(self)

    @classmethod
    def display_credential(cls):
        """
        Method that returns the credential list
        """
        return Credential.credential_list

    @classmethod
    def find_by_name(cls, user_name):
        '''
        method that takes in a username and returns the user credentials that matches the username.

        Args:
            name: user_name to search for credential
        Return :
            Credential of person that matches the username.    
        '''
        for credential in Credential.credential_list:
            if credential.user_name == user_name:
                return credential

    @classmethod
    def find_by_password(cls, password):
        '''
        Method that takes in a password and returns a user that matches that password.
        Args:
            password: password to search for
        Returns :
            credentials of person that matches the password.
        '''

        for credential in Credential.credential_list:
            if credential.password == password:
                return credential

    @classmethod
    def copy_password(cls, user_name):
        found_credential = Credential.find_by_name(user_name)
        clipboard.copy(found_credential.password)
        #text = clipboard.paste()

    @classmethod
    def credential_exist(cls, name):
        '''
        A method to check if credentials exists in the credentials list
        Args:
           account-name: name to search if credentials exist
        Returns:
            Boolean : True / False if the credential exists or not
            '''
        for credential in Credential.credential_list:
            if credential.user_name == name:
                return True

        return False
