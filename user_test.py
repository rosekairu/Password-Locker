import unittest  # Importing the unittest module
from user import User  # Importing the user class


class TestUser(unittest.TestCase):
    '''
    Test class that defines test cases for the user class behaviours.

    Args:
    unittest.TestCase: TestCase class that helps in creating test cases
    '''

    def setUp(self):
        """
        Set up method to run before each test cases
        """
        self.new_user = User("Rose", "Kairu",)  # create user object

    def tearDown(self):
        """
        tearDown method does clean up after each test case has run
        """
        User.users_list = []

    def test_init(self):
        """
        test_init test case to test if the object is initialized propery
        """
        self.assertEqual(self.new_user.first_name, "Rose")
        self.assertEqual(self.new_user.last_name, "Kairu")

    def test_save_user(self):
        """
        test_save_user test case to check if we can save a user object into the users list
        """
        self.new_user.save_user()  # saving the new user
        self.assertEqual(len(User.users_list), 1)

    def test_save_multiple_users(self):
        """
        test_save_multiple_users to check if we can save multiple user object into the users list
        """
        self.new_user.save_user()
        test_user = User("Test", "user",)  # new user
        test_user.save_user()
        self.assertEqual(len(User.users_list), 2)

    def test_display_all_users(self):
        """
        method that returns a list of all users saved
        """
        self.assertEqual(User.display_users(), User.users_list)

    def test_user_exists(self):
        """
        test_user_exists to check if the user exists in the users list
        """

    def delete_user(self):
        """
        delete_user method deletes a saved user from our users list
        """
        User.users_list.remove(self)


if __name__ == '__main__':
    unittest.main()
