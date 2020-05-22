import unittest  # Importing the unittest module
from user import User  # Importing the user class


class TestUser(unittest.TestCase):

    def setUp(self):
        """
        Set up method to run before each test cases
        """
        self.new_user = User("James", "Muriuki",)  # create user object

    def tearDown(self):
        """
        tearDown method does clean up after each test case has run
        """
        User.users_array = []

    def test_init(self):
        """
        test_init test case to test if the object is initialized propery
        """
        self.assertEqual(self.new_user.first_name, "James")
        self.assertEqual(self.new_user.last_name, "Muriuki")
        #self.assertEqual(self.new_user.phone_number, "0712345678")
        #self.assertEqual(self.new_user.email, "james@ms.com")

    def test_save_multiple_user(self):
        """
        test_save_multiple_user test case to check if we can save multiple user object into the users array
        """
        self.new_user.save_user_details()  # saving the new user
        self.assertEqual(len(User.users_array), 1)

    def test_save_multiple_users(self):
        """
        test_save_multiple_users to check if we can save multiple user object into the users array
        """
        self.new_user.save_user_details()
        test_user = User("Test", "user",)  # new user
        test_user.save_user_details()
        self.assertEqual(len(User.users_array), 2)

    def test_display_all_users(self):
        """
        method that returns a list of all users saved
        """
        self.assertEqual(User.display_users(), User.users_array)

    def delete_user(self):
        """
        delete_user method deletes a saved user from our users array
        """
        User.users_array.remove(self)


if __name__ == '__main__':
    unittest.main()
