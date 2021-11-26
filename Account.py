class Account:
    def __init__(self, username, accountNumber, password, cardNumber, balance, limit):
        self.username = username
        self.accountNumber = accountNumber
        self.password = password
        self.cardNumber = cardNumber
        self.balance = balance
        self.limit = limit

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount < self.limit:
            self.balance -= amount
            return True
        # exceeded account limit
        else:
            return False

    def checkPassword(self, inputPassword):
        if self.password == inputPassword:
            return True
        else:
            return False

    def getUserName(self):
        return self.username

    def getAccountNumber(self):
        return self.accountNumber

    def getPassword(self):
        return self.password
    
    def getCardNumber(self):
        return self.cardNumber

    def getBalance(self):
        return self.balance

    def getLimit(self):
        return self.limit