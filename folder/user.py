class User:
    '''
    Class that generates new instace of User
    '''
    user_list = []

    def __init__ (self, user_name, password):
        self.user_name = user_name
        self.password = password

    def save_ser(self):
        '''
        method that returns the user_list
        '''
        User.user_list.append(self)

    def save_user(self):
        '''
        '''
        User.user_list.append()