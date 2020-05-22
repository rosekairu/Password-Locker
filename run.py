
from user import User
from credential import Credential
import random


def login_user(user_name, password):
    """
    function that checks whether a user exist and then login them in.
    """

    log_in = User.log_in(user_name, password)
    if log_in != False:
        return User.log_in(user_name, password)


def create_user(first_name, last_name):
    """
    Function to create a new user
    """
    new_user = User(first_name, last_name)
    return new_user


def create_credential(user_name, password):
    """
    Function to create new user credentials
    """
    new_credential = Credential(user_name, password)
    return new_credential


def save_user(user):
    """
    Function to to save a user
    """
    user.save_user()


def save_credential(credential):
    """
    Function to save credentials
    """
    credential.save_credential()


def del_user(user):
    """
    Function to to delete a user
    """
    user.delete_user()


def del_credential(credential):
    """
    Function to to delete a user credentials
    """
    credential.delete_credential()


def verify__user(name):
    """
    Fuction to check if user already exists in the users list
    """
    current_user = Credential.find_by_name(name)
    return current_user


def display_user():
    """
    Function that returns a saved user
    """
    return User.display_users()


def display_credential():
    """
    Function that returns a saved user credentials
    """
    return Credential.display_credential()


def find_credential(user_name):
    """
    function that finds credentials by account name
    """
    return Credential.find_by_name(user_name)


def check_existing_credential(name):
    '''
    Function to check if an inputed credential name exists
     '''
    return Credential.find_by_name(name)


# def generate_password(user_name):
 #   '''
  #      This is a function to generate random password
   #     '''
    #gen_pass = Credential.generate_password()
    # return gen_pass


def main():
    print("Welcome to your password locker, Enter a short code from the list of allowed short code actions")

    while True:
        print("Allowed Short Code Actions\n nu - create a new user account with a user-defined password\n ag -create a new user account with an auto-generated password\n da -display all user accounts\n fc -Find user credential\n dc -Delete user credetials\n ex -exit the App\n ")

        short_code = input().lower()

        if short_code == 'nu':
            print("New User")
            print("-"*10)
            print("Hi,What site do you want to create the account for?")
            site = input()
            print(f"Creating a Account with {site}?")

            print(" First name...")
            first_name = input()

            print(" Last name...")
            last_name = input()

            print("Enter username...")
            user_name = input()

            print("Enter password...")
            password = input()
            # create and save new user account.
            save_user(create_user(first_name, last_name))
            # create and save a credential listing for the above user
            save_credential(create_credential(user_name, password))
            print('\n')
            print(
                f" A new {site} account by {first_name} {last_name} has successfully been created")
            print(
                f" The username is {user_name} and the password is {password}")
            print('\n')

        elif short_code == 'ag':
            print("New User")
            print("-" * 10)
            print("Hey There!!! What site do you want to create an account for?")
            site = input()
            print(f"Creating an Account for {site}?")

            print("First name ....")
            first_name = input()

            print("Last name ...", )
            last_name = input()

            print(
                "Enter username ... Hint: a secure password will be generated for you...")
            user_name = input()

            s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
            password = "".join(random.sample(s, 8))

            # create and save new user account.
            save_user(create_user(first_name, last_name))
            # create and save a credential listing for the above user
            save_credential(create_credential(user_name, password))
            print('\n')
            print(
                f" A new {site} account by {first_name} {last_name} has successfully been created")
            print(
                f" The username is {user_name} and the password is {password}")
            print('\n')

        elif short_code == 'da':

            if display_user():
                print("Here is a list of all your user accounts")
                # print('\n')
                print('*' * 10)
                print('_' * 10)

                for user in display_user():
                    print(
                        f"{user.first_name} {user.last_name} {user.user_name}  {user.password} has an account for {site}")

                print('*' * 10)
                print('_' * 10)

                print('\n')
            else:
                print('\n')
                print(
                    "You don't seem to have any existing account with password locker yet")
                print('\n')

        elif short_code == 'fc':
            print("Enter the Account name you want to search...")
            search_name = input().lower()
            if find_credential(search_name):
                search_credetial = find_credential(search_name)
                print(f"Account name : {search_credetial.account}")
                print(
                    f"User Name : {search_credetial.user_name} passwod : {search_credetial.password} ")

            else:
                print("That Account does not exist")
                print('\n')

        elif short_code == "dc":
            print("Enter Account to Delete Credentials")
            search_name = input().lower()
            if find_credential(search_name):
                search_credetial = find_credential(search_name)
                search_credetial.delete_credential()
                print('\n')
                print(
                    f"Your credentials for : {search_credetial.account} was successfully deleted ")
                print('\n')

            else:
                print(
                    "The Account you want to delete does not yet exist on password locker")

        elif short_code == "ex":
            print(":/ You are Logged Out. See you soon...")
            break
        else:
            print(" :( Only key in the allowed actions !!")


if __name__ == '__main__':
    main()
