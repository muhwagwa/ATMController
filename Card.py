class Card:
    def __init__(self, username, cardNumber, pin, accountNumber):
        self.username = username
        self.cardNumber = cardNumber
        self.pin = pin
        self.accountList = [accountNumber]

    def getUsername(self):
        return self.username
        
    def getCardNumber(self):
        return self.cardNumber

    def getPin(self):
        return self.pin
    
    def getAccountList(self):
        return self.accountList