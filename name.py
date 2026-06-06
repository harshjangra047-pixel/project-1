# Expense Tracker

expenses = [] # list of all expenses in form of dictionary

print("Welcome to the Expense Tracker!")
while True:
    print("\n====== Menu ======")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. Calculate Total Spending")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        date = input("Enter the date (YYYY-MM-DD): ")
        catagory = input("Enter category (eg: food, transport, entertainment): ")
        amount = float(input("Enter the amount: "))
        description = input("Enter a description: ")

        expense = {
            "date": date,
            "catagory": catagory,
            "amount": amount,
            "description": description
        }
        expenses.append(expense)
        print("\nExpense added successfully!")

    # 2. View all expenses
    elif choice == '2':
        if len(expenses) == 0:
            print("No expenses found.")
        else:
            print("====== All Expenses ======")
            count = 1
            for eachexpense in expenses:
               # Fixed the f-string quotes
               print(f"Expense number {count} -> {eachexpense['date']}, {eachexpense['catagory']}, {eachexpense['description']}, {eachexpense['amount']}")
               count = count + 1

    # 3. View total spending
    elif choice == '3':
        total = 0
        for eachexpense in expenses:
            total = total + eachexpense["amount"]
        print(f"\nTotal expenses = {total}")

    # 4. Exit
    elif choice == '4':
        print("Thank you for using this system!")
        break
 
    else:
        print("Invalid choice! Try Again.")