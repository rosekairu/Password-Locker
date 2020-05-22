class Credential:
    """
    a class that generates new Credentials for Users
    """

    pass
    credential_array = []

    def __init__(self, user_name, password):
        self.user_name = user_name
        self.password = password

    def save_credential(self):
        """
        save_contact method saves credentials objects into credintial_array
        """
        Credential.credential_array.append(self)

    @classmethod
    def display_credential(cls):
        """
        method that returns the credential array
        """

        return cls.credential_array
