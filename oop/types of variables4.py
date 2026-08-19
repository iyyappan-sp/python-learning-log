class Customer:
    bankname = "DS Bank"

    def __init__(self,name,balance=0.0):
        self.name = name
        self.balance = balance

    def deposite(self,amt):
        self.balance = self.balance+amt
        print("Balance After Deposite:",self.balance)
    def withdraw(self,amt):
        if amt > self.balance:
            print("Insufficent Fund!!! cann't perform this operation")
            exit()
        else:
            self.balance = self.balance-amt
            print("Balance After Withdraw:",self.balance)
print("Welcome to",Customer.bankname)
name = input("Enter Your Nmae:")
c = Customer(name)
while True:
    print("d - Deposite \n w - Withdraw \n e - Exit")
    option = input("Enter Your Option:")
    if option == 'd' or option == 'D':
        amt = float(input("Enter Your Amount for Deposite"))
        c.deposite(amt)
    elif option == 'w' or option == 'D':
        amt = float(input("Enter Your Amount for Withdraw"))
        c.withdraw(amt)
    elif option == 'e' or option == 'E':
        exit()
    else:
        print("Invalid Operation... Please Try Again")
