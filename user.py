class User:
    """
    Class that generates new instance of User
    """
    user_list = []

    def __init__(self, user_name, password):

        self.user_name = user_name
        self.password = password
    def save_user(self):

        '''
        save_contact method saves contact objects into contact_list
        '''

        User.user_list.append(self)

    @classmethod
    def display_user(cls):
        '''
        method that returns the user list
        '''
        return cls.user_list
class  Credential:
    