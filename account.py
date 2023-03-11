"""
Account class
"""
from password import Password

class Account():
    def __init__(self, name, balance, password) -> None:
        self.name = name
        self.balance = int(balance)
        self.password = Password(password)

    def deposit(self, amountToDeposit, password):
        if password != self.password.getPassword():
            print("Sorry, incorrect password")
            return None
        
        if amountToDeposit < 0:
            print("You cannot deposit a negative amount")
            return None
        
        self.balance = self.balance + amountToDeposit
        return self.balance
        
    def withdraw(self, amountToWithdraw, password):
        if password != self.password.getPassword():
            print("Incorrect password for this account")
            return None
        
        if amountToWithdraw < 0:
            print("You cannot withdraw a negative amount")
            return None
        
        if amountToWithdraw > self.balance:
            print("You cannot withdraw more then you have in your account")
            return None
        
        self.balance = self.balance - amountToWithdraw
        return self.balance

    def getBalance(self, password):
        if password != self.password.getPassword():
            print("Sorry, incorrect password")
            return None
        return self.balance
    
    def show(self):
        print("        Name:", self.name)
        print("        Balance:", self.balance)
        print("        Password:", self.password)
        print()
    