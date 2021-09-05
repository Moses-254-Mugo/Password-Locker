from folder.user import User
from folder.credential import Credentials

def create_our_user(user_name, password):
    """
    Function to create a new user
    """
    new_user = User(user_name, password)
    return new_user

def save_our_user(user):
    user.save_user()

def show_user(user):
    '''
    Function to display user
    '''
    user.display_user()
    
def login(user_name, password):
    """
    Function to login
    """
    verified_user = Credentials.verify_user(user_name, password)
    return verified_user

def create_credentials(account, user_name, password):
    """
    Function to create a new credentials
    """
    new_credentials = Credentials(account, user_name, password)
    return new_credentials

def save_credentials(credential_list):

    Credentials.save_credentials(credential_list)

def delete_credentials(credential_list):
    Credentials.delete_credentials(credential_list)

def search_credentials(account):
    return Credentials.search_user_credentials(account)

def show_all_credentials():
    return Credentials.display_credentials()

def generate_credentials():
    auto_generated_password = Credentials.generate_credentials()
    # print(auto_generated_password)
    return auto_generated_password



def password_locker():
    message = '''
    Hello and Welcome to password locker.\n
    What would you like to do?\n

    1. Create a new account\n
    2. Have a account already?\n
    '''

    user_output  = input(message).lower(). strip()

    print(user_output)

    if user_output == "1":
        print ("Nice! let'create a new account")
        user_name =input("Enter use your username: ")
        while True:
            pass_massage = """
            1. Create a password for the account\n
            2. Use a generated password\n
            """
            pass_response = input(pass_massage).lower().strip()
            if pass_response == "1":
                password = input("Enter your password: ")
            elif pass_response == "2":
                password = generate_credentials()
                break
            else:
                print("Invalid password!!")

        save_our_user(create_our_user(user_name, password))

        print(f'Hello {user_name} your account has been created and your password is {password}')

    elif user_output == "2":
        print("Nice! let's login now")
        user_name = input("Enter your username: ")
        password = input("Enter your password: ")
    
        verified_user = login(user_name, password)
        
        if verified_user == login(user_name, password):
            print(f'Hello {user_name} your account is verified')
        else:
            print("Invalid username or password !!")
    while True:
        logged_in_message = """
        1. Create credentials \n
        2. Search credentials \n
        3. Display credentials \n
        4. Delete credentials \n
        """
        logged_in_response = input(logged_in_message).lower().strip()
        if logged_in_response == "1":
            print("Great! Let's create a new credentials")
            account = input("Enter your account name: ")
            user_name = input("Enter your username: ")
            my_pass_message = """
            1. Create a password for the account\n
            2. Use a generated password\n
            """
            response = input(my_pass_message).lower().strip()
            if response == "1":
                password = input("Enter your password: ")
                print(f'Your credentials for {account} has been created')
            elif response == "2":
                password = generate_credentials()
            save_credentials(create_credentials(account, user_name, password))
            print(f'Credentials for {account} created')

        elif logged_in_response == "2":
            print("Nice! let's search credentials")
            account = input("Enter your account name: ")
            search_credentials(account)
        elif logged_in_response == "3":
            if show_all_credentials():
                print("Nice! Let's display credentials\n")
                print("Here's a list of all your credentials\n")
                for credential_list in show_all_credentials():
                    print(f'Account: {credential_list.account}\nUsername: {credential_list.user_name}\nPassword: {credential_list.password} \n')
            else:
                print("You don't have any credentials saved yet")
        elif logged_in_response == "4":
            print("Great! Let's delete credentials")
            account = input("Enter your account name: ")
            delete_credentials(account)


if __name__ == '__main__':
    password_locker()
