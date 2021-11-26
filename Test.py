from Bank import Bank
from Account import Account
from Card import Card
from CashBin import CashBin
from Controller import Controller

if __name__ == '__main__':

    # 0. Create Some Dummy Data
    # 0-1. Create 2 cards (username, cardNumber, PIN, accountNumber)
    bearCard = Card("bear", 123456789, 1234, 123123)
    robotCard = Card("robot", 135792468, 1357, 135248)

    # 0-2. Create 2 accounts (username, accountNumber, password, cardNumber, balance, limit)
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
    # 1. CARD 'See Balance' SUCCESS
    # runATM input: option1, cardNumber, PIN, accountNumber, password, option2, amount, transferAccount
    print("\n---------TEST#1. CARD SEE BALANCE SUCCESS---------")
    ATM.runATM(1, 123456789, 1234, 123123, 1234, 1, 0 ,0)

    # 2. CARD 'Deposit' SUCCESS
    print("\n---------TEST#2. CARD DEPOSIT SUCCESS---------")
    ATM.runATM(1, 123456789, 1234, 123123, 1234, 2, 50, 0)

    # 3-1. CARD 'Withdraw' SUCCESS
    print("\n---------TEST#3-1. CARD WITHDRAW SUCCESS---------")
    ATM.runATM(1, 123456789, 1234, 123123, 1234, 3, 50, 0)

    # 3-2. CARD 'Withdraw' FAIL
    print("\n------TEST#3-2. CARD WITHDRAW FAIL - EXCEEDED LIMIT-------")
    ATM.runATM(1, 123456789, 1234, 123123, 1234, 3, 600, 0)

    # 3-3. CARD 'Withdraw' FAIL
    print("\n-----TEST#3-3. CARD WITHDRAW FAIL - EXCEEDED CASHBIN-----")
    ATM.runATM(1, 135792468, 1357, 135248, 1234, 3, 15000, 0)

    # 4-1. CARD 'Transfer' SUCCESS
    print("\n---------TEST#4-1. CARD TRANSFER SUCCESS---------")
    ATM.runATM(1, 123456789, 1234, 123123, 1234, 4, 60, 135248)

    # 4-2. CARD 'Transfer' FAIL
    print("\n----TEST#4-2. CARD TRANSFER FAIL - EXCEEDED LIMIT----")
    ATM.runATM(1, 123456789, 1234, 123123, 1234, 4, 600, 135248)

    # 4-3. CARD 'Transfer' FAIL
    print("\n---TEST#4-3. CARD TRANSFER FAIL - ACCOUNT DOESN'T EXIST---")
    ATM.runATM(1, 123456789, 1234, 123123, 1234, 4, 600, 111111)

    # 5. ACCOUNT 'See Balance' SUCCESS
    print("\n---------TEST#5. ACCOUNT SEE BALANCE SUCCESS---------")
    ATM.runATM(2, 0, 0, 123123, 1234, 1, 0, 0)

    # 6. ACCOUNT 'Deposit' SUCCESS
    print("\n---------TEST#6. ACCOUNT DEPOSIT SUCCESS---------")
    ATM.runATM(2, 0, 0, 123123, 1234, 2, 50, 0)

    # 7-1. ACCOUNT 'Withdraw' SUCCESS
    print("\n---------TEST#7-1. ACCOUNT WITHDRAW SUCCESS---------")
    ATM.runATM(2, 0, 0, 123123, 1234, 3, 50, 0)

    # 7-2. ACCOUNT 'Withdraw' FAIL
    print("\n------TEST#7-2. ACCOUNT WITHDRAW FAIL - EXCEEDED LIMIT-------")
    ATM.runATM(2, 0, 0, 123123, 1234, 3, 600, 0)

    # 7-3. ACCOUNT 'Withdraw' FAIL
    print("\n-----TEST#7-3. ACCOUNT WITHDRAW FAIL - EXCEEDED CASHBIN-----")
    ATM.runATM(2, 135792468, 1357, 135248, 1234, 3, 15000, 0)

    # 8-1. ACCOUNT 'Transfer' SUCCESS
    print("\n---------TEST#8-1. ACCOUNT TRANSFER SUCCESS---------")
    ATM.runATM(2, 123456789, 1234, 123123, 1234, 4, 60, 135248)

    # 8-2. ACCOUNT 'Transfer' FAIL
    print("\n----TEST#8-2. ACCOUNT TRANSFER FAIL - EXCEEDED LIMIT----")
    ATM.runATM(2, 123456789, 1234, 123123, 1234, 4, 600, 135248)

    # 8-3. ACCOUNT 'Transfer' FAIL
    print("\n---TEST#8-3. ACCOUNT TRANSFER FAIL - ACCOUNT DOESN'T EXIST---")
    ATM.runATM(2, 123456789, 1234, 123123, 1234, 4, 600, 111111)

    # 9. Not registered Card
    print("\n------TEST#9. FAIL - CARD NOT REGISTERED------")
    ATM.runATM(1, 111111111, 1234, 123123, 1234, 1, 50, 0)

    # 10. Not registered Account
    print("\n------TEST#10. FAIL - ACCOUNT NOT REGISTERED------")
    ATM.runATM(2, 123456789, 1234, 111111, 1234, 1, 50, 0)

    # 11-1. Verification FAIL
    print("\n--------TEST#9-1. FAIL - WRONG PIN--------")
    ATM.runATM(1, 123456789, 1111, 123123, 1234, 1, 0, 0)

    # 11-2. Verification FAIL
    print("\n-------TEST#11-2. FAIL - WRONG PASSWORD-------")
    ATM.runATM(2, 123456789, 12345, 123123, 1111, 1, 0, 0)

    # 12. Wrong Account Number
    print("\n-----TEST#12. FAIL - WRONG ACCOUNT NUMBER-----")
    ATM.runATM(1, 123456789, 1234, 123456, 1234, 1, 0, 0)

    # 13. Invalid Option1 FAIL
    print("\n---------TEST#13. FAIL - INVALID OPTION1---------")
    ATM.runATM(3, 123456789, 1234, 123123, 1234, 1, 50, 0)

    # 14. Invalid Option2 FAIL
    print("\n---------TEST#14. FAIL - INVALID OPTION2---------")
    ATM.runATM(1, 123456789, 1234, 123123, 1234, 5, 50, 0)

    print("------------------------TEST END---------------------------")