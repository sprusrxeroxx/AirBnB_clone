#!/usr/bin/python3
import unittest
from models.user import User


class TestUserClass(unittest.TestCase):
    """
    Test case class for the User class in the models.user module.
    """
    def setUp(self):
        """ Set up a User object for testing."""
        self.user = User()

    def test_user_id(self):
        userId = self.user.id

    def test_user_first_name(self):
        """ Test setting and getting the first_name attribute of User.
        """
        self.user.first_name = "Jack"
        self.assertEqual(self.user.first_name, "Jack")

    def test_user_last_name(self):
        """ Test setting and getting the last_name attribute of User.
        """
        self.user.last_name = "Sparrow"
        self.assertEqual(self.user.last_name, "Sparrow")

    def test_user_email(self):
        """ Test setting and getting the email attribute of User.
        """
        self.user.email = "hello@world.com"
        self.assertEqual(self.user.email, "hello@world.com")

    def test_user_password(self):
        """
        Test setting and getting the password attr of User.
        """
        self.user.password = "helloworld12345"
        self.assertEqual(self.user.password, "helloworld12345")

    def test_inherited_attributes(self):
        """ Validate that all supperclass default attributes were
        inherited
        """
        self.assertTrue('id' in self.user.__dict__)
        self.assertTrue('created_at' in self.user.__dict__)
        self.assertTrue('updated_at' in self.user.__dict__)

    def test_user_default_attributes(self):
        """ Test if User has the expected default attributes.
        """
        self.assertEqual(self.user.first_name, "")
        self.assertEqual(self.user.last_name, "")
        self.assertEqual(self.user.email, "")
        self.assertEqual(self.user.password, "")


if __name__ == '__main__':
    unittest.main()