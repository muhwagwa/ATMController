class CashBin:
    def __init__(self, cash):
        self.cash = cash

    def cashIn(self, amount):
        self.cash += amount

    def cashOut(self, amount):
        # Enough cash in cashbin
        if self.cash >= amount:
            self.cash -= amount
            return True
        # Not Enough cash in cashbin
        else:
            return False