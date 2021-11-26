# ATMController
This is a simple bank ATM controller in a world of 1 dollar bills (no cents).

## Structure Overview
<img width="618" alt="Screen Shot 2021-11-26 at 7 09 59 PM" src="https://user-images.githubusercontent.com/77218372/143564097-cbd81dca-9bfa-4bd2-80f9-b4e02e4ffa6c.png">

There are total 5 classes in this ATMController : **Controller, Bank, Card, Account and CashBin.** 
- **Card and Account** : Holds information about each card and account. These are stored inside the Bank.
- **Bank** : Holds the card and account objects in the bank. 
- **Controller** : The controller only holds the card number and account number that it's dealing at each operation. Each time the controller needs more information about the card or account (username, balance, etc.), it needs to send request to the bank module. To check whether the pin number (for card) or password (for account) is correct, it needs to send a request to the bank module and get the answer not in the 'pin' or 'password' format, but only in 'True' or 'False' format.
- **Cashbin** : This class holds information about how much cash is in cashbin right now.

## Features

### Start

The ATM starts with following.
```
BR ATM Says Hi! Insert Your Card.
> Insert Card / Enter Account Number
```

### Option 1 : Insert Card / Enter Account Number
The user should then choose one of these 2 actions to proceed.

**1) Insert a Card**

After inserting a card (typing the card number), the user needs to type in the correct PIN number to proceed. If not, the ATM will terminate. The user then must select the account among the accounts connected to this card. The connected account list will be shown. This number must be valid, or else the ATM will terminate.

```
Card Inserted. Enter Your PIN Number.
Verification Success! Select Your Account!
> 123123
```

**2) Enter an Account Number**

After entering an account number, the user needs to type in the correct password to proceed. If not, the ATM will terminate.
```
Account Number Typed In. Enter Your Password.
Verification Success!
```

### Option 2 : See Balance / Deposit / Withdraw / Transfer
Then we move on to 'option2'. This ATM supports balance check, deposit, withdraw and transfer.

```
Choose Your Option Number
> 1. Check Balance
> 2. Deposit
> 3. Withdraw
> 4. Transfer
```

**1) See Balance**

Result will be shown as below.

```
***Your account balance : 940
```
**2) Deposit**

After typing in the amount you wish to deposit, result will be shown.

```
DEPOSIT : How much do you wish to deposit?
***DEPOSIT COMPLETE***
Before: 940   Deposit Amount: 50   After: 990
```

**3) Withdraw**

After typing in the amount you wish to withdraw, result will be shown. 

```
WITHDRAW : How much do you wish to withdraw?
***WITHDRAW COMPLETE***
Before: 990   Deposit Amount: 50   After: 940
```
If you type in more than the account limit or the amount of cash the cashbin holds, the ATM will terminate with some error message.

```
// Exceed Limit
WITHDRAW : How much do you wish to withdraw?
WITHDRAW FAILED. Account Limit Exceeded.

// Cashbin Doesn't Have Enough
WITHDRAW : How much do you wish to withdraw?
WITHDRAW FAILED. Not Enough Cash Here.
```

**4) Transfer**

After typing in the amount and the account you wish to transfer to, result will be shown. 

```
TRANSFER : Enter Account Number and Amount
***TRANSFER COMPLETE***
Transfered 60 to robot.
Your account balance now is 880.
```

If you type in more than the account limit or the account number doesn't exist, the ATM will terminate with some error message.

```
// Exceed Limit
TRANSFER : Enter Account Number and Amount
TRANSFER FAILED. Account Limit Exceeded.

// Account Number Doesn't Exist
TRANSFER : Enter Account Number and Amount
111111 is not a Valid Account Number.
```

### Finish
After you've successfully finished your operation, the ATM will terminate with following message.
```
Bye Bye! See You Again!
```

## How To Run Tests

Simply run the Test.py file with python. 
```
python Test.py
```
Test will start like this
```
------------------------TEST STARTS---------------------------

---------TEST#1. CARD SEE BALANCE SUCCESS---------
BR ATM Says Hi! Insert Your Card.
> Insert Card / Enter Account Number
...
```
and end like this.

```
> 3. Withdraw
> 4. Transfer
Invalid Option
------------------------TEST END---------------------------
```

There are total 14 test cases.
- TEST 1 : [SUCCESS] Insert a Card > See Balance
- TEST 2 : [SUCCESS] Insert a Card > Deposit
- TEST 3-1 : [SUCCESS] Insert a Card > Withdraw
- TEST 3-2 : [FAIL] Insert a Card > Withdraw > Exceed account limit
- TEST 3-3 : [FAIL] Insert a Card > Withdraw > Not enough cash in cashbin
- TEST 4-1 : [SUCCESS] Insert a Card > Transfer
- TEST 4-2 : [FAIL] Insert a Card > Transfer > Exceed account limit
- TEST 4-3 : [FAIL] Insert a Card > Transfer > Transfer account doesn't exist
- TEST 5 : [SUCCESS] Enter Account Number > See Balance
- TEST 6 : [SUCCESS] Enter Account Number > Deposit
- TEST 7-1 : [SUCCESS] Enter Account Number > Withdraw
- TEST 7-2 : [FAIL] Enter Account Number > Withdraw > Exceed account limit
- TEST 7-3 : [FAIL] Enter Account Number > Withdraw > Not enough cash in cashbin
- TEST 8-1 : [SUCCESS] Enter Account Number > Transfer
- TEST 8-2 : [FAIL] Enter Account Number > Transfer > Exceed account limit
- TEST 8-3 : [FAIL] Enter Account Number > Transfer > Transfer account doesn't exist
- TEST 9 : [FAIL] Insert a Card > Card number doesn't exist
- TEST 10 : [FAIL] Enter Account Number > Account number doesn't exist
- TEST 11-1 : [FAIL] Insert a Card > Wrong PIN number
- TEST 11-2 : [FAIL] Enter Account Number > Wrong account password
- TEST 12 : [FAIL] Insert a Card > Account number doesn't exist
- TEST 13 : [FAIL] Invalid option1
- TEST 14 : [FAIL] Invalid option2


## Files and Directories

| File  | Description |
| ------------- |:-------------|
| README.md      | This file.     |
| Controller.py      | Contains Controller class.     |
| Bank.py      | Contains Bank class.     |
| Account.py   | Contains Account class.     |
| Card.py      | Contains Card class.     |
| CashBin.py   | Contains CashBin class.     |
| Test.py      | Contains main function that tests this ATMController.      |
