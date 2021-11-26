class CashBin:
    def __init__(self, cash):
        self.cash = cash

    def cashIn(self, amount):
        self.cash += amount

    def cashCheck(self, amount):
        # Enough cash in cashbin
        if self.cash >= amount:
            return True
        # Not Enough cash in cashbin
        else:
            return False

    def cashOut(self, amount):
        self.cash -= amount