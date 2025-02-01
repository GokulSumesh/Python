class products():
    def products(self,name,price):
        self.name=name
        self.price=price
        print(f"Product Name: {self.name}, Price: {self.price}")

class mobile_shop(products):
    def _init_(self):
        print("This is mobile shop")

class slipper_shop(products):
    def slipper_shop(self):
        pass

class grocery_shop(products):
    def grocery_shop(self):
        pass

class fruit_shop(products):
    def fruit_shop(self):
        pass


a=mobile_shop()
a.products("Samsung",500)
a=slipper_shop()
a.products("Nike Slippers", 20)
a=grocery_shop()
a.products("Apple", 2)
a=fruit_shop()
a.products("Banana", 1)

