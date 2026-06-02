# Ask user for withdrawal amount.
# Cases:
#
# amount <= 0 → Invalid amount
# amount > balance → Insufficient funds
# otherwise deduct and show remaining balance

balance = 10000

withdraw_amount = int(input("Enter withdraw amount: "))

if withdraw_amount <= 0:
    print("Invalid amount")
elif withdraw_amount > balance:
    print("Insufficient funds")
else:
    print(f"Remaining balance: {balance - withdraw_amount}")