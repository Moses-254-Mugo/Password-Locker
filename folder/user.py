class User:
    '''
    Class that generates new instace of User
    '''
    user_list = []

    def __init__ (self, user_name, password):
        self.user_name = user_name
        self.password = password

    def save_user(self):
        '''
        Method that saves a user
        '''
        User.user_list.append(self)

    @classmethod
    def display_user(cls):
        '''
        function that return user_list
        '''
        return cls.user_list

    def find_user_name(cls, user_name):
        '''
        Find uses by user name
        '''
        for user in cls.user_list:
            if user.user_name == user_name:
                return user

    def find_user(cls):
        return cls.user_list


    
    def delete_user(cls, user_name):
        for user in cls.user_list:
            if user.user_name == user_name:
                cls.user_list.remove(user)
                return True
            return False

    def del_user(self):
        '''
        Function to delete user
        '''
        User.user_list.remove(self)
        return True