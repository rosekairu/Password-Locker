from user import User
from credential import Credential
import random


def create_user(first_name, last_name):
    """
    Function to crreate a new user
    """
    new_user = User(first_name, last_name)
    return new_user


def create_credential(user_name, password, ):
    """
    Function to create new user credentials
    """
    new_credential = Credential(user_name, password, )
    return new_credential


def save_user(user):
    """
    Function to to save a user
    """
    user.save_user_details()


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


def main():
    print("Welcome to your password locker, Enter a short code from the list of allowed short code actions")

    while True:
        print("Allowed Short Code Actions\n ud - create a new user account with a user-defined password\n ag -create a new user account with an auto-generated password\n da -display all user accounts\n ex -exit the list\n ")

        short_code = input().lower()

        if short_code == 'ud':
            print("New User")
            print("-"*10)
            print("Hi,What site do you want to create the account for?")
            site = input()
            print(f"Aah, so you like {site}?")

            print(" First name...")
            f_name = input()

            print(" Last name...")
            l_name = input()

            #print(" Phone number...")
            #p_number = input()

            #print(" Email address...")
            #e_address = input()

            print("Enter username...")
            user_name = input()

            print("Enter password...")
            password = input()
            # create and save new user account.
            save_user(create_user(f_name, l_name))
            # create and save a credential listing for the above user
            save_credential(create_credential(user_name, password))
            print('\n')
            print(
                f" A new {site} account by {f_name} {l_name} has successfully been created")
            print(
                f" The username is {user_name} and the password is {password}")
            print('\n')

        elif short_code == 'ag':
            print("New User")
            print("-" * 10)
            print("Hey There!!! What site do you want to create an account for?")
            site = input()
            print(f"Aah!! So you love {site}?")

            print("First name ....")
            f_name = input()

            print("Last name ...", )
            l_name = input()

            #print("Phone number ...")
            #p_number = input()

            #print("Email address ...")
            #e_address = input()

            print(
                "Enter username ... Hint: a secure password will be generated for you...")
            user_name = input()

            s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
            pword = "".join(random.sample(s, 8))

            # create and save new user account.
            save_user(create_user(f_name, l_name))
            # create and save a credential listing for the above user
            save_credential(create_credential(user_name, pword))
            print('\n')
            print(
                f" A new {site} account by {f_name} {l_name} has successfully been created")
            print(f" The username is {user_name} and the password is {pword}")
            print('\n')

        elif short_code == 'da':

            if display_user():
                print("Here is a list of all your user accounts")
                print('\n')

                for user in display_user():
                    print(
                        f"{user.first_name} {user.last_name} has an account for {site}")

                print('\n')
            else:
                print('\n')
                print("You don't seem to have any existing accounts")
                print('\n')

        elif short_code == "ex":
            print(":/ See you soon then...")
            break
        else:
            print(" :( Only key in the allowed actions !!")


if __name__ == '__main__':
    main()
