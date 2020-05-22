import unittest  # Importing the unittest module
from credential import Credential  # Importing the credential class


class TestUser(unittest.TestCase):

    def setUp(self):
        """
        Set up method to run before each test cases
        """
        self.new_credential = Credential(
            "user_name", "password",)  # creates credential object

    def tearDown(self):
        """
        tearDown method does clean up after each test case has run
        """
        Credential.credential_array = []

    def test_init(self):
        """
        test_init test case to test if the object is initialized propery
        """
        self.assertEqual(self.new_credential.user_name, "user_name")
        self.assertEqual(self.new_credential.password, "password")
        #self.assertEqual(self.new_credential.email, "email@ms.com")

    def test_save_multiple_credential(self):
        """
        test_save_multiple_credential to check if we can save multiple credential object into the credentials array
        """
        self.new_credential.save_credential()  # saving the new credentials
        self.assertEqual(len(Credential.credential_array), 1)

    def test_display_credential(self):
        """
        test_display_credentials method returns a list of saved credentials
        """
        self.assertEqual(Credential.display_credential(),
                         Credential.credential_array)

    def delete_credential(self):
        """
        delete_credential method deletes a saved credential from our credeital array
        """
        Credential.credential_array.remove(self)


if __name__ == '__main__':
    unittest.main()
