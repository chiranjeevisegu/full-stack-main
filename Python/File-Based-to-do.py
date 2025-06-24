# FILE-BASED TO-DO LIST APPLICATION

TODO_FILE = "todos.txt"

def add_todo():
    """
    Prompts the user to input a to-do item,
    adds it to the file and confirms the action.
    """
    todo = input("Enter a new to-do item: ").strip()

    if not todo:
        print("❌ To-do item cannot be empty.")
        return

    try:
        with open(TODO_FILE, "a", encoding="utf-8") as file:
            file.write(todo + "\n")
        print(f"✅ Added to-do: '{todo}'")
    except Exception as e:
        print(f"❌ Error saving to-do: {e}")

def view_todos():
    """
    Reads all to-do items from the file and prints them as a numbered list.
    Handles the case when the file doesn't exist.
    """
    print("\n📋 Your To-Do List:")
    try:
        with open(TODO_FILE, "r", encoding="utf-8") as file:
            todos = file.readlines()
            if not todos:
                print("🗒️ No to-do items found.")
                return

            print("-" * 30)
            for idx, item in enumerate(todos, start=1):
                print(f"{idx}. {item.strip()}")
            print("-" * 30)
    except FileNotFoundError:
        print("⚠️ No to-do list found. Start adding some tasks!")
    except Exception as e:
        print(f"❌ Error reading to-do list: {e}")

def todo_menu():
    """
    Displays a menu and handles user input until 'exit' is chosen.
    """
    print("📌 Welcome to the File-Based To-Do List App!")

    while True:
        print("\n====== 📝 MENU ======")
        print("1. Add a To-Do Item")
        print("2. View To-Do List")
        print("3. Exit")
        print("======================")

        choice = input("Choose an option (1-3): ").strip()

        if choice == "1":
            add_todo()
        elif choice == "2":
            view_todos()
        elif choice == "3":
            print("👋 Goodbye! Your to-dos are saved.")
            break
        else:
            print("❌ Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    todo_menu()
