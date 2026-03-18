balance = 0

while True:
    print("\n1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        amount = int(input("Enter amount to deposit: "))
        balance = balance + amount
        print("Amount deposited")

    elif choice == 2:
        amount = int(input("Enter amount to withdraw: "))
        if amount > balance:
            print("Insufficient balance")
        else:
            balance = balance - amount
            print("Amount withdrawn")

    elif choice == 3:
        print("Current balance is:", balance)

    elif choice == 4:
        print("Thank you for using banking system")
        break

    else:
        print("Invalid choice")