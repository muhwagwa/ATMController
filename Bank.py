class Bank:
    def __init__(self):
        self.card = []
        self.account = []

    def addCard(self, card):
        self.card.append(card)

    def addAccount(self, account):
        self.account.append(account)

    # Check Card Existence with Card Number
    def checkCard(self, cardNumber):
        for card in self.card:
            if cardNumber == card.getCardNumber():
                return True
        return False

    # Find Card with Card Number
    def getCard(self, cardNumber):
        for card in self.card:
            if cardNumber == card.getCardNumber():
                return card

    def checkPin(self, cardNumber, inputPin):
        card = self.getCard(cardNumber)
        if card.checkPin(inputPin):
            return True
        else:
            return False

    # Check Account Existence with Account Number
    def checkAccount(self, accountNumber):
        for account in self.account:
            if accountNumber == account.getAccountNumber():
                return True
        return False

    # Find Account with Account Number
    def getAccount(self, accountNumber):
        for account in self.account:
            if accountNumber == account.getAccountNumber():
                return account

    def checkPassword(self, accountNumber, inputPassword):
        account = self.getAccount(accountNumber)
        if account.checkPassword(inputPassword):
            return True
        else:
            return False

    