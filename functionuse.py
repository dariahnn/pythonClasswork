"""
PROGRAM 2:
YOBUILD IN A BANKING APPLICATION WHERE USERS CAN WITHDRAW AND CHECK BALANCES
"""
amount= 0
balance = int(input("Enter Balance: "))
#deposit function
def deposit(balance, amount):
    result = balance + amount
    return result


#WITHDRAWAL
def withdraw():
    withdrawal_amount = int(input("Enter withdrawal amount: "))
    current_balance = deposit(balance,amount)
    if current_balance< withdrawal_amount:
        return "Insufficient funds"
    else :
        available_balance = current_balance - withdrawal_amount
        return (f"Withdrawal success {withdrawal_amount} balance was at"
                f"{current_balance} new balance {available_balance}")
print(withdraw())