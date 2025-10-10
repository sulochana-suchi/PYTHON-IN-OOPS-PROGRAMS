# To create the BankAccount class
class bank:
    def __init__(self):
        self.bal = 0 # Initialize balance to 0
        print("Welcome to the SBI")

    def deposit(self):
        amt = float(input("Enter amount to be Deposited: "))
        self.bal += amt
        print("\n deposited amount :",amt) 

    def withdraw(self):
        amt = float(input("Enter amount to be withdraw:"))
        if self.bal >= amt:
            self.bal -= amt
            print("\nYou withdraw:",amt)
        else:
            print("\nInsufficient balance")

    def display(self):
        print("\nNet Available Balance =",self.bal)

                                                                       
s = bank()     # Create an object of Bank
s.deposit()   # Deposit money
s.withdraw()  # Withdraw money
s.display()   # Display balance
