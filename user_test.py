import unittest
from folder.credential import Credentials
from folder.user import User




class UserTest(unittest.TestCase):
    '''
    Test class that defines test cases for the User 
    '''
    def setUp(self):
        '''
        method that runs before the test
        '''
        self.user = User('moses', 'password')

    def test_create_user(self):
        self.assertEqual(self.user.user_name, 'moses')
        self.assertEqual(self.user.password, 'password')

    def test_save_user(self):
        '''
        Test case to check if the new instance of the user object has been recreated
        '''
        User.user_list = []
        self.user.save_user()
        self.assertEqual(len(User.user_list), 1)

    def  test_save_multiple_users(self):
        '''
        test to check if we can save multiple user object
        '''
        User.user_list = []
        self.user.save_user()
        test_user = User('mugo', 'mugo')
        test_user.save_user()
        self.assertEqual(len(User.user_list), 2)

    def test_delete_user(self):
        '''
        test method to remove user from user list
        '''
        self.user.save_user()
        test_user = User('mugo', 'mugo')
        test_user.save_user()
        self.user.delete_user(test_user.user_name)
        self.assertEqual(len(User.user_list), 2)

    def tearDown(self):
        '''
        method that does clean up after test has run
        '''
        User.user_list = []
    
class CredentialsTest(unittest.TestCase):

    def setUp(self):
            '''
            method that runs before the test
            '''
            self.credential_list = Credentials('twitter', 'moses', 'password')

    def test_create_credentials(self):
    
        self.assertEqual(self.credential_list.account, 'twitter')
        self.assertEqual(self.credential_list.user_name, 'mose')
        self.assertEqual(self.credential_list.password, 'password')

    def test_save_credentials(self):
        '''
        test to check if saved credentials object are in our credential list
        '''
        Credentials.credential_list = []
        self.credential_list.save_credentials()
        self.assertEqual(len(Credentials.credential_list), 1)
    
    def test_save_multiple_credentials(self):
        Credentials.credential_list = []
        self.credential_list.save_credentials()
        test_credentials = Credentials('test', 'test', 'test')
        test_credentials.save_credentials()
        self.assertEqual(len(Credentials.credential_list), 2)