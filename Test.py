import Bank
import Account
import Card
import CashBin
import Controller

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
    # 1-1. 'See Balance' SUCCESS
    # runATM Input : cardNumber / PIN / accountNumber / option / amount
    print("\nTEST#1-1. SEE BALANCE SUCCESS")
    ATM.runATM(123456789, 1234, 123123, 1, 0)

    # 1-2. 'See Balance' FAIL
    print("\nTEST#1-2. SEE BALANCE FAIL - WRONG ACCOUNT NUMBER")
    ATM.runATM(123456789, 1234, 123456, 1, 0)

    # 1-3. 'See Balance' FAIL
    print("\nTEST#1-3. SEE BALANCE FAIL - WRONG PASSWORD")
    ATM.runATM(123456789, 1111, 123456, 1, 0)

    # 2-1. 'Deposit' SUCCESS
    # runATM Input : cardNumber / PIN / accountNumber / option / amount
    print("\nTEST#2-1. SEE BALANCE SUCCESS")
    ATM.runATM(123456789, 1234, 123123, 2, 50)

    # 2-2. 'Deposit' FAIL
    print("\nTEST#2-2. SEE BALANCE FAIL - WRONG ACCOUNT NUMBER")
    ATM.runATM(123456789, 1234, 123456, 2, 50)

    # 2-3. 'Deposit' FAIL
    print("\nTEST#2-3. SEE BALANCE FAIL - WRONG PASSWORD")
    ATM.runATM(123456789, 1111, 123123, 2, 50)

    # 3-1. 'Deposit' SUCCESS
    # runATM Input : cardNumber / PIN / accountNumber / option / amount
    print("\nTEST#3-1. SEE BALANCE SUCCESS")
    ATM.runATM(123456789, 1234, 123123, 3, 50)

    # 3-2. 'Deposit' FAIL
    print("\nTEST#3-2. SEE BALANCE FAIL - WRONG ACCOUNT NUMBER")
    ATM.runATM(123456789, 1234, 123456, 3, 50)

    # 3-3. 'Deposit' FAIL
    print("\nTEST#3-3. SEE BALANCE FAIL - WRONG PASSWORD")
    ATM.runATM(123456789, 1111, 123123, 3, 50)

    # 3-4. 'Deposit' FAIL
    print("\nTEST#3-4. SEE BALANCE FAIL - EXCEEDED LIMIT")
    ATM.runATM(123456789, 1234, 123456, 3, 600)

    # 3-5. 'Deposit' FAIL
    print("\nTEST#3-5. SEE BALANCE FAIL - EXCEEDED CASHBIN")
    ATM.runATM(135792468, 1357, 135248, 3, 15000)