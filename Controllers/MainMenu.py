from Controllers.FoodManager import FoodManager
from Models.Cart import Cart

class MainMenu:

    __options = {1:"Show Restaurant", 2:"Show Food Items", 3:"Search Restaurant", 4:"Search Food Items", 5:"Logout"}

    def __init__(self):
        self.__FoodManager = FoodManager()

    def ShowRestaurant(self):
        for i, res in enumerate(self.__FoodManager.Restaurants, 1):
            res.DisplayItem(i)

        choice = int(input("Please select the Restaurants: "))
        res = self.__FoodManager.Restaurants[choice-1]
        self.ShowFoodMenus(res.FoodMenus)


    def ShowFoodItems(self, food_items = None):
        if food_items is not None:
            for i, food_item in enumerate(food_items, 1):
                food_item.DisplayItem(i)

            choices = list(map(int, input("Enter your order (eg. 1, 1, 2): ").split(",")))
            cart = Cart(food_items, choices)
            cart.ProcessOrder(food_items)

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
        print("List of menus available")
        for i, menu in enumerate(menus, start=1):
            menu.DisplayItem(i)
        choice = int(input("Please choose menu: "))
        food_items = menus[choice-1].FoodItems
        self.ShowFoodItems(food_items)

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