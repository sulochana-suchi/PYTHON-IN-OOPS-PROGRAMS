class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self,item_name,qty):
        item = (item_name,qty)
        self.items.append(item)

    def remove_item(self,item_name):

      for item in self.items:
        if item[0] == item_name:
            self.items.remove(item)
            break

    def calculate_toal(self):
        total = 0
        for item in self.items:
            total +=item[1]
        return total

#driver code
cart = ShoppingCart()
#Add items to the shopping cart
cart.add_item("Papaya",100)
cart.add_item("Guava",200)
cart.add_item("Orange",150)

print("Current Items in Cart:")
for item in cart.items:
   print(item[0],"_",item[1])

total_qty = cart.calculate_total()
print("Total Quantity:",total_qty)

cart.remove_item("Guava")
print("\nUpdated Items in cart after removing orange:")
for item in cart.items:
    print(item[0],"_",item[1])
total_qty = cart.calculate_total()
print("Total Quantity:",total_qty)
    
