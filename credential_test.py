import unittest  # Importing the unittest module
from credential import Credential  # Importing the credential class


class TestCredential(unittest.TestCase):
    '''
    Test class that defines test cases for the user class behaviours.

    Args:
    unittest.TestCase: TestCase class that helps in creating test cases
    '''

    def setUp(self):
        """
        Set up method to run before each test cases
        """
        self.new_credential = Credential(
            "user_name", "password")  # creates credential object

    def tearDown(self):
        """
        tearDown method does clean up after each test case has run
        """
        Credential.credential_list = []

    def test_init(self):
        """
        test_init test case to test if the object is initialized propery
        """
        self.assertEqual(self.new_credential.user_name, "user_name")
        self.assertEqual(self.new_credential.password, "password")

    def test_save_credential(self):
        '''
        test_save_credential test case to test if  credentials object are saved into
         the credential list
        '''
        self.new_credential.save_credential()
        self.assertEqual(len(Credential.credential_list), 1)

    def test_save_multiple_credential(self):
        """
        test_save_multiple_credential to check if we can save multiple credential object into the credentials list
        """
        self.new_credential.save_credential()  # saving the new credentials
        test_credential = Credential("user_name", "password")
        test_credential.save_credential()
        self.assertEqual(len(Credential.credential_list), 2)

    def test_display_credential(self):
        """
        test_display_credentials method returns a list of saved credentials
        """
        self.assertEqual(Credential.display_credential(),
                         Credential.credential_list)

    def test_delete_credential(self):
        """
         test_delete_credential tests if we can remove a saved credential from our credeital list
        """
        self.new_credential.save_credential()
        test_credential = Credential("user", "test2")
        test_credential.save_credential()

        self.new_credential.delete_credential()
        self.assertEqual(len(Credential.credential_list), 1)
        # Credential.credential_list.remove(self)

    def test_find_credential_by_name(self):
        """
        Test is to check if we can find credentials and display information
        """
        self.new_credential.save_credential()
        test_credential = Credential("Twitter", "test3")
        test_credential.save_credential()
        found_credential = Credential.find_by_name("Twitter")
        self.assertEqual(found_credential.user_name,
                         test_credential.user_name)

    def test_credential_exist(self):
        """
        test_credential_exist test to check if we can find the credentials or not by returning a true or false.
        """
        self.new_credential.save_credential()
        test_credential = Credential("Twitter", "password")
        test_credential.save_credential()
        credential_exist = Credential.find_by_name("Twitter")

        self.assertTrue(credential_exist)


if __name__ == '__main__':
    unittest.main()
