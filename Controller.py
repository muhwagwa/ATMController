class Controller:
    def __init__(self, bank, cashbin):
        self.cashBin = cashbin
        self.bank = bank
        # The card ATM is processing right now
        self.cardNumber = 0
        # The account ATM is processing right now
        self.accountNumber = 0

    def insertCard(self, cardNumber):
        # Card Doesn't Exist
        if self.bank.checkCard(cardNumber) == False:
            print("This card is not registered.")
            return False
        # Card Exists
        else:
            self.cardNumber = cardNumber
            print("Card Inserted. Enter Your PIN Number.")
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
            self.accountNumber = accountNumber
            return True
        # Account Doesn't Exist
        else:
            print(str(accountNumber) + " is not a Valid Account Number.")
            return False

    def enterAccount(self, accountNumber):
        # Account Exists
        if self.bank.checkAccount(accountNumber):
            self.accountNumber = accountNumber
            print("Account Number Typed In. Enter Your Password.")
            return True
        # Account Doesn't Exist
        else:
            print(str(accountNumber) + " is not a Valid Account Number.")
            return False

    def checkAccountPwd(self, password):
        # Password match
        if self.bank.checkPassword(self.accountNumber, password):
            print("Verification Success!")
            return True
        # Password doesn't match
        else:
            print("Verification Failed. Please check your account password again.")
            return False

    def seeBalance(self):
        print("***Your account balance : " + str(self.bank.getAccount(self.accountNumber).getBalance()))

    def deposit(self, amount):
        balanceBefore = self.bank.getAccount(self.accountNumber).getBalance()
        self.bank.getAccount(self.accountNumber).deposit(amount)
        print("***DEPOSIT COMPLETE***\nBefore: " + str(balanceBefore) + "   Deposit Amount: " + str(amount) + "   After: " + str(self.bank.getAccount(self.accountNumber).getBalance()))

    def withdraw(self, amount):
        balanceBefore = self.bank.getAccount(self.accountNumber).getBalance()
        # Check if there's enough cash in the CashBin
        if self.cashBin.cashCheck(amount) == False:
            print("WITHDRAW FAILED. Not Enough Cash Here.")
            return False
        # Account limit exceeded
        if self.bank.getAccount(self.accountNumber).withdraw(amount) == False:
            print("WITHDRAW FAILED. Account Limit Exceeded.")
            return False
        # Withdraw SUCCESS
        else:
            print("***WITHDRAW COMPLETE***\nBefore: " + str(balanceBefore) + "   Deposit Amount: " + str(amount) + "   After: " + str(self.bank.getAccount(self.accountNumber).getBalance()))
            return True

    def transfer(self, accountNumber, amount):
        # Account Doesn't Exist
        if self.bank.checkAccount(accountNumber) == False:
            print(str(accountNumber) + " is not a Valid Account Number.")
            return False
        # Exceeds limit
        if amount > self.bank.getAccount(self.accountNumber).getLimit():
            print("TRANSFER FAILED. Account Limit Exceeded.")
            return False
        # Transfer SUCCESS
        self.bank.getAccount(self.accountNumber).withdraw(amount)
        self.bank.getAccount(accountNumber).deposit(amount)
        print("***TRANSFER COMPLETE***\nTransfered " + str(amount) + " to " + self.bank.getAccount(accountNumber).getUserName() +".")
        print("Your account balance now is " + str(self.bank.getAccount(self.accountNumber).getBalance()) + ".")
        return True
            
    def runATM(self, option1, cardNumber, PIN, accountNumber, password, option2, amount, transferAccount):
        print("BR ATM Says Hi! Insert Your Card.")

        # Operate Option1
        print("> Insert Card / Enter Account Number")
        if option1 == 1:
            if self.insertCard(cardNumber) == False:
                return False
            if self.checkPIN(PIN) == False:
                return False
            if self.selectAccount(accountNumber) == False:
                return False
        elif option1 == 2:
            if self.enterAccount(accountNumber) == False:
                return False
            if self.checkAccountPwd(password) == False:
                return False
        else:
            print("Invalid Option")
            return False

        # Operate Option2
        print("Choose Your Option Number\n> 1. Check Balance\n> 2. Deposit\n> 3. Withdraw\n> 4. Transfer")
        if option2 == 1:
            self.seeBalance()
        elif option2 == 2:
            print("DEPOSIT : How much do you wish to deposit?")
            self.deposit(amount)
        elif option2 == 3:
            print("WITHDRAW : How much do you wish to withdraw?")
            if self.withdraw(amount) == False:
                return False
        elif option2 == 4:
            print("TRANSFER : Enter Account Number and Amount")
            if self.transfer(transferAccount, amount) == False:
                return False
        else:
            print("Invalid Option")
            return False
        print("\nBye Bye! See You Again!")