class Cart:
    def __init__(self, items, choices):
        self.Choices = choices
        self.FoodItems = self.__AddtoCart(items)

    def __AddtoCart(self, items):
        food_dict = {}
        for choice in self.Choices:
            if choice > len(items):
                raise KeyError

            if choice in food_dict:
                food_dict[choice] += 1
            else:
                food_dict[choice] = 1

        return food_dict

    def ProcessOrder(self, food_items):

        total = 0

        for item in self.FoodItems:
            price = self.FoodItems[item] * food_items[item-1].Price
            total += price
            print(f"{food_items[item - 1].Name} x {self.FoodItems[item]} = {price}")

        print(f"Total: {total}")

        self.ProcessPayment(total)

    def ProcessPayment(self, amount):
        print("\nSelect Payment Method")
        print("1. Cash on Delivery")
        print("2. UPI / Card")

        choice = int(input("Enter choice: "))

        if choice in [1, 2]:
            print(f"Payment of ₹{amount} successful ✅")
            print("Order placed successfully...")
        else:
            print("Invalid payment option")


