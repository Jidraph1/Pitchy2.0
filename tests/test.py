import unittest
from .models import User, Pitch

class UserTest(unittest.TestCase):
    """
    Test class to test the behaviour of the User class
    """
    def setUp(self):
        """
        SetUp method that will run before every test
        """
        self.new_user = User(password = 'banana')

    def test_password_setter(self):
        self.assertTrue(self.new_user.pass_secure is not None)

    def test_no_access_password(self):
        with self.assertRaises(AttributeError):
            self.new_user.password

    def test_password_verification(self):
        self.assertTrue(self.new_user.verify_password('banana'))

class PitchModelTest(unittest.TestCase):
    """
    Test class to test the behaviour of the User class
    """
    def setUp(self):
        """
        SetUp method that will run before every test
        """

if __name__ == '__main__':
    unittest.main()