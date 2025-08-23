balance = 1000  # initial balance

while True:   # loop continues until user chooses to exit
    x = input("Do you want to Deposit or Withdraw or CheckBalance or Exit: ")
    x = x.lower()   # make input case-insensitive

    if x == "deposit":
        deposit = int(input("Deposit amount: "))
        balance += deposit
        print(f"Deposited: {deposit}, Balance available: {balance}")

    elif x == "withdraw":
        withdraw = int(input("Amount to withdraw: "))
        if withdraw <= balance:
            balance -= withdraw
            print(f"Withdrawn: {withdraw}, Balance Available: {balance}")
        else:
            print("Insufficient Balance!")

    elif x == "checkbalance":
        print(f"Balance Available: {balance}")

    elif x == "exit":
        print("👋 Thank you! Exiting...")
        break   # this now works correctly (inside loop)

    else:
        print("Invalid choice! Please type Deposit / Withdraw / CheckBalance / Exit")
