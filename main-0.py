#!/usr/bin/python3
from programming_paradigm.bank_account import BankAccount

if __name__ == "__main__":
    # Create an account
    account = BankAccount("123456", "Isaac Abakah", 1000)

    # Deposit money
    account.deposit(500)

    # Withdraw money
    account.withdraw(200)

    # Print final balance
    print("Account holder:", account.account_holder)
    print("Account number:", account.account_number)
    print("Balance:", account.get_balance())
