from Models.User import User
from Models.UserManager import UserManager
from Controllers.MainMenu import MainMenu

class LoginSystem:

    def Login(self):
        mail = input("Email Id: ")
        password = input("Password: ")

        user = UserManager.find_user(mail, password)

        if user is not None:
            print("Login Successful...")
            menu = MainMenu()
            menu.start()
        else:
            print("please retry")

    def Register(self):
        name = input("Name: ")
        mobile = int(input("Mobile Number: "))
        mail_id = input("Email Id: ")
        password = input("Password: ")

        user = User(name, mobile, mail_id, password)
        UserManager.add_users(user)

    def Guest(self):
        pass

    def Exit(self):
        print("Thank you for using our Food App... 🥰")
        exit()

    def validate_option(self, option):
        getattr(self, option)()

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
                login_system.validate_option(FoodApp.login_options[choice])
            except (ValueError, KeyError):
                print("Invalid Choice... Please retry")

FoodApp.initialize()