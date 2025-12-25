from Models.User import User

class UserManager:
    __Users = []

    @classmethod
    def add_users(cls, user_obj):
        if isinstance(user_obj, User):
            cls.__Users.append(user_obj)
            print("You have been successfully registered")
        else:
            print("Invalid User")

    @classmethod
    def find_user(cls, mail, pwd):
        for user in cls.__Users:
            if user.MailId == mail and user.Password == pwd:
                return user