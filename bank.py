class Bank_Account:
    def __init__(self):
       self.balance=0
       print("Hello!!! welcome to the deposit & withdraw machine")
    def deposit(self):
        amount=float(input("Enter amount to be Deposited: "))
        self.balance += amount
        print("\n Amount Deposited:" ,amount)
    def Withdraw(self):
        amount = float(input("Enter amount to be Withdraw: "))
        if self.balance>=amount:
            self.balance-=amount
            print("\n you Withdraw:",amount)
        else:
            print("\n Insufficient balance  ")
    def display(self):
        print("\n Net Available Balance=",self.balance)

s=Bank_Account()

s.deposit()
s.Withdraw()
s.display()
