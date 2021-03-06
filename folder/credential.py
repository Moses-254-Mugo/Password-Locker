from .user import User
import string
import random

class Credentials: 
    '''
    Test class the defines test cases for the  class behaviour.
    '''

    credential_list = []

    def __init__(self, account, user_name, password):
        self.account = account
        self.user_name = user_name
        self.password = password

    @classmethod
    def verify_user(cls, user_name, password):
        verify_user = ''
        for user in User.user_list:
            if user.user_name == user_name and user.password == password:
                verify_user = user.user_name
            return verify_user

    def save_credentials(self):
        Credentials.credential_list.append(self)

    @classmethod
    def search_user_credentials(cls, account):
        for credential_list in cls.credentials_list:
            if credential_list.account == account:
                return credential_list.__repr__()

    @classmethod
    def display_credentials(cls):
        # Add somethings here..
        return cls.credential_list

    @classmethod
    def check_if_credentials_exist(cls, account):
        for credential_list in cls.credential_list:
            if credential_list.account == account:
                return True
            return False

        
    @classmethod
    def delete_credentials(cls, account):
        for credential_list in cls.credential_list:
            if credential_list.account == account:
                cls.credential_list.remove(credential_list)
                return cls.credential_list

    def generate_credentials(length=8):
        password = string.ascii_lowercase + string.digits + string.ascii_uppercase + "':@!#$%^&*"
        return ''.join(random.choice(password) for _ in range(length))