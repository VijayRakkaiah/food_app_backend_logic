from FoodManager import FoodManager

class MainMenu:

    __options = {1:"Show Restaurant", 2:"Show Food Items", 3:"Search Restaurant", 4:"Search Food Items", 5:"Logout"}

    def __init__(self):
        self.__FoodManager = FoodManager()

    def ShowRestaurant(self):
        for res in self.__FoodManager.Restaurants:
            print(f">> {res.Name} => Rating: {res.Rating}")

        choice = int(input("Please select the Restaurants: "))
        res = self.__FoodManager.Restaurants[choice]
        self.ShowFoodMenus(res.FoodMenus)


    def ShowFoodItems(self, foot_items = None):
        if foot_items is not None:
            pass
        else:
            pass

    def SearchRestaurant(self):
        res_name = input("Enter Restaurant Name: ")
        res = self.__FoodManager.FindRestaurant(res_name)

        if res is not None:
            print("Restaurants Found...")
            print(f"Name: {res.Name}, Rating: {res.Rating}")
            self.ShowFoodMenus(res.FoodMenus)
        else:
            print(f"No restaurants found on the name {res_name}")

    def SearchFoodItems(self):
        pass

    def Logout(self):
        pass

    def ShowFoodMenus(self, menus):
        pass

    def start(self):

        while True:
            for option in MainMenu.__options:
                print(f"{option}. {MainMenu.__options[option]}", end="   ")
                print()

            try:
                choice = int(input("Enter Your Choice: "))
                value = MainMenu.__options[choice].replace(" ", "")
                getattr(self, value)()

            except (ValueError, KeyError):
                print("Invalid Input... Please enter the valid choice")