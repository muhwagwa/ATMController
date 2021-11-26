# ATMController
This is a simple bank ATM controller in a world of 1 dollar bills (no cents).

## Structure Overview
<img width="618" alt="Screen Shot 2021-11-26 at 7 09 59 PM" src="https://user-images.githubusercontent.com/77218372/143564097-cbd81dca-9bfa-4bd2-80f9-b4e02e4ffa6c.png">

There are total 5 classes in this ATMController : Controller, Bank, Card, Account and CashBin. Card and Account objects are stored inside the bank and the controller only holds the card number and account number that it's dealing at each operation. Each time the controller needs more information about the card or account (username, balance, etc.), it needs to send request to the bank module. To check whether the pin number (for card) or password (for account) is correct, it needs to send a request to the bank module and get the answer not in the 'pin' or 'password' format, but only in 'True' or 'False' format.

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
Note that this ATMController was implemented with python 3.9.7.

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
