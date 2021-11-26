import CashBin
import Bank
import Card

class Controller:
    def __init__(self, bank, cashbin):
        self.cashBin = cashbin
        self.bank = bank
        self.card = 0
        self.account = 0

    def insertCard(self, cardNumber):
        card = self.bank.getCard(cardNumber)
        # Card Doesn't Exist
        if card == False:
            print("This card is not registered.")
            return False
        # Card Exists
        else:
            self.card = card
            print("Enter Your PIN Number")
            return True
            
    def checkPIN(self, pin):
        # PIN match
        if pin == self.card.getPin:
            print("WELCOME! Select Your Account!")
            # print account options
            for account in self.card.getAccountList:
                print("> " + account)
            return True
        # PIN doesn't match
        else:
            print("Verification Failed. Please check your PIN number again.")
            return False

    def selectAccount(self, accountNumber):
        # Account Exists
        if accountNumber in self.card.getAccountList:
            self.account = self.bank.getAccount(accountNumber)
            print("Choose Your Option Number\n1. Check Balance\n2.Deposit\n3.Withdraw")
        # Account Doesn't Exist
        else:
            print("Something Went Wrong...")

    def seeBalance(self):
        print("Your account balance : " + self.account.getBalance())

    def deposit(self, amount):
        balanceBefore = self.account.getBalance
        self.account.deposit(amount)
        print(">>DEPOSIT COMPLETED<<\n  Before: " + balanceBefore + "   Deposit Amount: " + amount + "   After: " + self.account.getBalance())

    def withdraw(self, amount):
        balanceBefore = self.account.getBalance
        # Check if there's enough cash in the CashBin
        if self.cashBin.cashCheck == False:
            print("WITHDRAW FAILED. Not Enough Cash Here.")
            return False
        # Account limit exceeded
        if self.account.withdraw(amount) == False:
            print("DEPOSIT FAILED. Account Limit Exceeded.")
            return False
        # Withdraw SUCCESS
        else:
            print(">>DEPOSIT COMPLETED<<\n  Before: " + balanceBefore + "   Deposit Amount: " + amount + "   After: " + self.account.getBalance())
            return True

    def runATM(self, cardNumber, PIN, accountNumber, option, amount):
        self.insertCard(cardNumber)
        self.checkPIN(PIN)
        self.selectAccount(accountNumber)
        if option == 1:
            self.seeBalance()
        elif option == 2:
            print("DEPOSIT\nHow much do you wish to deposit?")
            self.deposit(amount)
        elif option == 3:
            print("WITHDRAW\nHow much do you wish to withdraw?")
            self.withdraw(amount)
        else:
            print("Invalid Option")
        print("\nBye Bye! See You Again!")