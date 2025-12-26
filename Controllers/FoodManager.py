from Models.FoodItem import FoodItem
from Models.FoodMenu import FoodMenu
from Models.Restaurant import Restaurant

class FoodManager:

    def __init__(self):
        self.Restaurants = self.__PrepareRestaurant()

    def __PrepareFoodItems(self):
        item_1 = FoodItem("Veg Biriyani", 4.0, 120, "Good")
        item_2 = FoodItem("Chicken Biryiani", 4.4, 160, "Tasty")
        item_3 = FoodItem("Parota", 4.5, 50, "Good")
        item_4 = FoodItem("Dosa", 3.8, 65, "Good")
        item_5 = FoodItem("Noodles", 4.1, 100, "Good")
        return [item_1, item_2, item_3, item_4, item_5]

    def __PrepareFoodMenus(self):
        FoodItems = self.__PrepareFoodItems()
        menu_1 = FoodMenu("Veg")
        menu_1.FoodItems = [FoodItems[0], FoodItems[3]]
        menu_2 = FoodMenu("Non Veg")
        menu_2.FoodItems = [FoodItems[1], FoodItems[2]]
        menu_3 = FoodMenu("Chinese")
        menu_3.FoodItems = [FoodItems[4]]
        return [menu_1, menu_2, menu_3]

    def __PrepareRestaurant(self):
        FoodMenus = self.__PrepareFoodMenus()
        res_1 = Restaurant("A2b", 4.6, "Chennai", 10)
        res_1.FoodMenus = [FoodMenus[0]]
        res_2 = Restaurant("Muniyandi Vilas", 4.2, "Madurai", 20)
        res_2.FoodMenus = [FoodMenus[0], FoodMenus[1]]
        res_3 = Restaurant("KFC", 4.0, "cbe", 6)
        res_3.FoodMenus = [FoodMenus[1], FoodMenus[2]]
        return [res_1, res_2, res_3]

    def FindRestaurant(self, name):
        for res in self.Restaurants:
            if res.Name == name:
                return res