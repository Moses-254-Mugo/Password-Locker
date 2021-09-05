import unittest
from folder.credential import Credentials
from folder.user import User




class UserTest(unittest.TestCase):
    '''
    Test class that defines test cases for the User 
    '''
    def setUp(self):
        self.user = User('moses', 'password')

    def test_create_user(self):
        self.assertEqual(self.user.user_name, 'moses')
        self.assertEqual(self.user.password, 'password')

    def test_save_user(self):
        User.user_list = []
        self.user.save_user()
        self.assertEqual(len(User.user_list), 1)

    def  test_save_multiple_users(self):
        User.user_list = []
        self.user.save_user()
        test_user = User('mugo', 'mugo')
        test_user.save_user()
        self.assertEqual(len(User.user_list), 2)