#  SIMPLE CALCULATOR CLASS 

class Calculator:
    """
    A basic calculator class that performs four operations:
    addition, subtraction, multiplication, and division.
    Each method accepts two numbers as arguments and returns the result.
    """
    
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        try:
            result = a / b
            return result
        except ZeroDivisionError:
            print("❌ Error: Cannot divide by zero.")
            return None

def get_numbers():
    """
    Prompts the user for two numeric values.
    Returns them as floats.
    """
    try:
        num1 = float(input("Enter the first number: ").strip())
        num2 = float(input("Enter the second number: ").strip())
        return num1, num2
    except ValueError:
        print("❌ Invalid input. Please enter numeric values.")
        return None, None

def calculator_menu():
    """
    Displays a menu for calculator operations.
    Handles user interaction and loops until the user exits.
    """
    calc = Calculator()  

    print("🧮 Welcome to the Python Simple Calculator!")

    while True:
        print("\n====== CALCULATOR MENU ======")
        print("1. ➕ Add")
        print("2. ➖ Subtract")
        print("3. ✖ Multiply")
        print("4. ➗ Divide")
        print("5. 🚪 Exit")
        print("=============================")

        choice = input("Choose an operation (1-5): ").strip()

        if choice == "5":
            print("👋 Exiting Calculator. Goodbye!")
            break

        num1, num2 = get_numbers()
        if num1 is None or num2 is None:
            continue  
        if choice == "1":
            result = calc.add(num1, num2)
            print(f"✅ Result: {num1} + {num2} = {result}")
        elif choice == "2":
            result = calc.subtract(num1, num2)
            print(f"✅ Result: {num1} - {num2} = {result}")
        elif choice == "3":
            result = calc.multiply(num1, num2)
            print(f"✅ Result: {num1} × {num2} = {result}")
        elif choice == "4":
            result = calc.divide(num1, num2)
            if result is not None:
                print(f"✅ Result: {num1} ÷ {num2} = {result}")
        else:
            print("❌ Invalid choice. Please enter a number from 1 to 5.")

if __name__ == "__main__":
    calculator_menu()
