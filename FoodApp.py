from Models.User import User
from Models.UserManager import UserManager

class LoginSystem:

    def login(self):
        mail = input("Email Id: ")
        password = input("Password: ")

        user = UserManager.find_user(mail, password)

        if user is not None:
            print("Login Successful...")
        else:
            print("please retry")

    def register(self):
        name = input("Name: ")
        mobile = int(input("Mobile Number: "))
        mail_id = input("Email Id: ")
        password = input("Password: ")

        user = User(name, mobile, mail_id, password)
        UserManager.add_users(user)

    def guest_login(self):
        pass

    def validate_option(self, option):
        if option == 1:
            self.login()
        elif option == 2:
            self.register()
        elif option == 3:
            self.guest_login()
        elif option == 4:
            print("Thank you for using our Food App... 🥰")
            exit()
        else:
            print("Invalid Choice.... Please Retry")

class FoodApp:
    login_options = {1:"Login", 2:"Register", 3:"Guest", 4:"Exit"}

    @staticmethod
    def initialize():
        print("<< Welcome to online food ordering >>")

        login_system = LoginSystem()

        while True:
            for options in FoodApp.login_options:
                print(f"{options}. {FoodApp.login_options[options]}", end="   ")
            print()

            try:
                choice = int(input("Please Enter Your Choice: "))
                login_system.validate_option(choice)
            except ValueError:
                print("Invalid Choice... Please retry")

FoodApp.initialize()