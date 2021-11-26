class Bank:
    def __init__(self):
        self.card = []
        self.account = []

    def addCard(self, card):
        self.card.append(card)

    def addAccount(self, account):
        self.account.append(account)

    # Find Card with Card Number / Return False if doesn't exist
    def getCard(self, cardNumber):
        for card in self.card:
            if cardNumber == card.getCardNumber():
                return card
        return False

    # Find Account with Account Number / Return False if doesn't exist
    def getAccount(self, accountNumber):
        for account in self.account:
            if accountNumber == account.getAccountNumber():
                return account
        return False
