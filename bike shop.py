class BikeShop:

    def __init__(self,stock):
        self.stock = stock

    def ShowBike(self):
        printf("Total Bikes:",self.stocks)

    def rentBike(self,quantity):

        if quantity <= 0:
            print("Please Enter the positive value or greater tan zero")
        elif quantity > self.stock:
            print("Enter te value(less than stock)")
        else:
           self.stock = self.stock - quantity
           print("Total Price :",quantity * 100)
           print("Total Bikes",self.stock)

while True:
    obj = Bikeshop(100)
    user_input = int(input('''
    1-> Display Stock
    2-> Rent a Bike
    3- Exit
                         '''))


    if user_input == 1:
      obj.ShowBike()
    elif user_input == 2:
       n = int(input("Enter The Rent Bike :->"))
       obj.rentBike(n)
    else:
       break
   
