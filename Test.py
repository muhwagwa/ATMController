from Bank import Bank
from Account import Account
from Card import Card
from CashBin import CashBin
from Controller import Controller

if __name__ == '__main__':

    # 0. Create Some Dummy Data
    # 0-1. Create 3 cards (username, cardNumber, PIN, accountNumber)
    bearCard = Card("bear", 123456789, 1234, 123123)
    robotCard = Card("robot", 135792468, 1357, 135248)

    # 0-2. Create 3 accounts (username, accountNumber, password, cardNumber, balance, limit)
    bearAccount = Account("bear", 123123, 1234, 123456789, 1000, 500)
    robotAccount = Account("robot", 135248, 1357, 135792468, 48000, 20000)

    # 0-3. Create a Bank & add some card and account info
    BRbank = Bank()
    BRbank.addCard(bearCard)
    BRbank.addCard(robotCard)
    BRbank.addAccount(bearAccount)
    BRbank.addAccount(robotAccount)

    # 0-4. Create a CashBin with 10000 dollar cash
    BRcashbin = CashBin(10000)

    # 0-5. Create an ATM
    ATM = Controller(BRbank, BRcashbin)

    print("------------------------TEST STARTS---------------------------")
    # 1. 'See Balance' SUCCESS
    # runATM Input : cardNumber / PIN / accountNumber / option / amount
    print("\n---------TEST#1. SEE BALANCE SUCCESS---------")
    ATM.runATM(123456789, 1234, 123123, 1, 0)

    # 2. 'Deposit' SUCCESS
    print("\n---------TEST#2. DEPOSIT SUCCESS---------")
    ATM.runATM(123456789, 1234, 123123, 2, 50)

    # 3-1. 'Withdraw' SUCCESS
    print("\n---------TEST#3-1. WITHDRAW SUCCESS---------")
    ATM.runATM(123456789, 1234, 123123, 3, 50)

    # 3-2. 'Withdraw' FAIL
    print("\n------TEST#3-2. WITHDRAW FAIL - EXCEEDED LIMIT-------")
    ATM.runATM(123456789, 1234, 123123, 3, 600)

    # 3-3. 'Withdraw' FAIL
    print("\n-----TEST#3-3. WITHDRAW FAIL - EXCEEDED CASHBIN-----")
    ATM.runATM(135792468, 1357, 135248, 3, 15000)

    # 4. Not registered Card
    print("\n------TEST#4. FAIL - CARD NOT REGISTERED------")
    ATM.runATM(111111111, 1234, 123123, 4, 50)

    # 5. 'See Balance' FAIL
    print("\n--------TEST#5. FAIL - WRONG PASSWORD--------")
    ATM.runATM(123456789, 1111, 123123, 1, 0)

    # 6. Wrong Account Number
    print("\n-----TEST#6. FAIL - WRONG ACCOUNT NUMBER-----")
    ATM.runATM(123456789, 1234, 123456, 1, 0)

    # 7. Invalid Option FAIL
    print("\n---------TEST#7. FAIL - INVALID OPTION---------")
    ATM.runATM(123456789, 1234, 123123, 4, 50)

    print("------------------------TEST END---------------------------")