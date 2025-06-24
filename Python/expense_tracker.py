# Expense Tracker Application

expenses = []
def add_expense():
    """
    Prompts the user to enter a description and an amount.
    Validates the amount to ensure it's a positive number.
    Adds the expense as a tuple to the global expenses list.
    """
    print("\n📝 Add a New Expense")
    description = input("Enter the description of the expense (e.g., Lunch, Bus Fare): ").strip()

    try:
        amount_input = input("Enter the amount (positive number): ").strip()
        amount = float(amount_input)  

        if amount <= 0:
            raise ValueError("Amount must be greater than 0.")
        
        expenses.append((description, amount))
        print(f"✅ Expense added: {description} - ${amount:.2f}")

    except ValueError as e:
        print(f"❌ Invalid input: {e}")

def view_expenses():
    """
    Prints all the expenses stored in the expenses list.
    Shows each description and amount neatly formatted.
    """
    print("\n📋 List of All Expenses")

    if not expenses:
        print("No expenses recorded yet.")
        return

    print("-" * 40)
    print("{:<5} {:<20} {:>10}".format("No.", "Description", "Amount ($)"))
    print("-" * 40)

    for i, (desc, amt) in enumerate(expenses, start=1):
        print("{:<5} {:<20} {:>10.2f}".format(i, desc, amt))

    print("-" * 40)

def total_expenses():
    """
    Calculates the sum of all expenses' amounts.
    Displays the total value in a formatted string.
    """
    print("\n💵 Total Amount Spent")
    
    total = sum(amount for _, amount in expenses)

    print(f"📊 You have spent a total of: ${total:.2f}")

def show_menu():
    """
    Displays the main menu with options.
    Keeps running in a loop until the user chooses to exit.
    """
    while True:
        print("\n========== 🧾 EXPENSE TRACKER MENU ==========")
        print("1. ➕ Add Expense")
        print("2. 📄 View All Expenses")
        print("3. 💰 View Total Spent")
        print("4. 🚪 Exit")
        print("==============================================")

        choice = input("Choose an option (1-4): ").strip()

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            total_expenses()
        elif choice == '4':
            print("👋 Exiting Expense Tracker. Stay budget-smart!")
            break
        else:
            print("❌ Invalid choice. Please enter 1, 2, 3, or 4.")

if __name__ == "__main__":
    print("💼 Welcome to the Python Expense Tracker!")
    show_menu()
