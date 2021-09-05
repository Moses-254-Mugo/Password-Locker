class User:
    '''
    Class that generates new instace of User
    '''
    user_list = []

    def __init__ (self, user_name, password):
        self.user_name = user_name
        self.password = password
        