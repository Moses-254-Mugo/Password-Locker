import unittest
from folder import user
from folder.user import User
from  folder.credential import Credentials

class UserTest(unittest.TestCase):
    def setUp(self):
        self.user_list = user('moses', 'password')