class Controller:
    def __init__(self, bank, cashbin):
        self.cashBin = cashbin
        self.bank = bank
        # The card ATM is processing right now
        self.cardNumber = 0
        # The account ATM is processing right now
        self.account = 0

    def insertCard(self, cardNumber):
        # Card Doesn't Exist
        if self.bank.checkCard(cardNumber) == False:
            print("This card is not registered.")
            return False
        # Card Exists
        else:
            self.cardNumber = cardNumber
            print("Enter Your PIN Number")
            return True
            
    def checkPIN(self, pin):
        # PIN match
        if self.bank.checkPin(self.cardNumber, pin):
            print("Verification Success! Select Your Account!")
            # print account options
            for account in self.bank.getCard(self.cardNumber).getAccountList():
                print("> " + str(account))
            return True
        # PIN doesn't match
        else:
            print("Verification Failed. Please check your PIN number again.")
            return False

    def selectAccount(self, accountNumber):
        # Account Exists
        if accountNumber in self.bank.getCard(self.cardNumber).getAccountList():
            self.account = self.bank.getAccount(accountNumber)
            print("Choose Your Option Number\n>1. Check Balance\n>2. Deposit\n>3. Withdraw")
            return True
        # Account Doesn't Exist
        else:
            print(str(accountNumber) + " is not a Valid Account Number.")
            return False

    def seeBalance(self):
        print("***Your account balance : " + str(self.account.getBalance()))

    def deposit(self, amount):
        balanceBefore = self.account.getBalance()
        self.account.deposit(amount)
        print("***DEPOSIT COMPLETE***\nBefore: " + str(balanceBefore) + "   Deposit Amount: " + str(amount) + "   After: " + str(self.account.getBalance()))

    def withdraw(self, amount):
        balanceBefore = self.account.getBalance()
        # Check if there's enough cash in the CashBin
        if self.cashBin.cashCheck(amount) == False:
            print("WITHDRAW FAILED. Not Enough Cash Here.")
            return False
        # Account limit exceeded
        if self.account.withdraw(amount) == False:
            print("WITHDRAW FAILED. Account Limit Exceeded.")
            return False
        # Withdraw SUCCESS
        else:
            print("***WITHDRAW COMPLETE***\nBefore: " + str(balanceBefore) + "   Deposit Amount: " + str(amount) + "   After: " + str(self.account.getBalance()))
            return True

    def runATM(self, cardNumber, PIN, accountNumber, option, amount):
        print("BR ATM Says Hi! Insert Your Card.")
        if self.insertCard(cardNumber) == False:
            return False
        if self.checkPIN(PIN) == False:
            return False
        if self.selectAccount(accountNumber) == False:
            return False
        # Operate Option
        if option == 1:
            self.seeBalance()
        elif option == 2:
            print("DEPOSIT : How much do you wish to deposit?")
            self.deposit(amount)
        elif option == 3:
            print("WITHDRAW : How much do you wish to withdraw?")
            if self.withdraw(amount) == False:
                return False
        else:
            print("Invalid Option")
            return False
        print("\nBye Bye! See You Again!")