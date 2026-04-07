def show_inventory(inventory):
    print("\nCurrent Inventory:")
    for fruit, stock in inventory.items():  
        print(f"{fruit}: {stock}")
    print()

def add_fruit(inventory):
    fruit = input("Enter the name of the new fruit: ").strip()
    if fruit in inventory:
        print(f"{fruit} already exists!\n")
    else:
        stock = input(f"Enter stock for {fruit}: ")
        inventory[fruit] = int(stock)  
        print(f"{fruit} added with stock {stock}.\n")

def update_stock(inventory):
    fruit = input("Enter the name of the fruit to update: ").strip()
    if fruit in inventory: 
        amount = input(f"Enter amount to add to {fruit}'s stock: ")
        inventory[fruit] += int(amount) 
        print(f"{fruit} stock increased by {amount}.\n")
    else:
        print(f"{fruit} is not in inventory. Use option 2 to add it.\n")

def menu():
    print("Options:")
    print("1 - View inventory")
    print("2 - Add new fruit")
    print("3 - Update existing fruit stock")
    print("4 - Exit")

def run_program():
    inventory = {
        "apples": 10,
        "bananas": 20,
        "oranges": 15
    }

    print("Welcome to the Fruit Shop!\n")

    while True:
        menu()
        choice = input("Enter option number: ")

        if choice == "1":
            show_inventory(inventory)
        elif choice == "2":
            add_fruit(inventory)
        elif choice == "3":
            update_stock(inventory)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose 1, 2, 3, or 4.\n")

if _name_ == "_main_":
    run_program()
[3:21 p. m., 7/4/2026] +57 323 8201509: def show_inventory(inventory):
    print("\nCurrent Inventory:")
    for fruit, stock in inventory.items():  
        print(f"{fruit}: {stock}")
    print()

def add_fruit(inventory):
    fruit = input("Enter the name of the new fruit: ").strip()
    if fruit in inventory:
        print(f"{fruit} already exists!\n")
    else:
        stock = input(f"Enter stock for {fruit}: ")
        inventory[fruit] = int(stock)  
        print(f"{fruit} added with stock {stock}.\n")

def update_stock(inventory):
    fruit = input("Enter the name of the fruit to update: ").strip()
    if fruit in inventory: 
        amount = input(f"Enter amount to add to {fruit}'s stock: ")
        inventory[fruit] += int(amount) 
        print(f"{fruit} stock increased by {amount}.\n")
 
debugging
[3:21 p. m., 7/4/2026] +57 323 8201509: from grades_manager import *

def main():
    print("Welcome to the Student Grades Manager!\n")

    my_grades = {}

    while True:
        print("Select an option:")
        print("1. Add a student")
        print("2. Print student grade averages")
        print("3. Exit")

        choice = input()

        if choice == "1":
            my_grades = add_student(my_grades)

        elif choice == "2":
            print("Select an option:")
            print("a. Display all students")
            print("b. Display selected students")

            sub_choice = input()

            if sub_choice == "a":
                avg_by_student(my_grades)

            elif sub_choice == "b":
                names = input("Enter student names (comma-separated):")
                keys = [n.strip() for n in names.split(",")]
                avg_by_student(my_grades, keys)

            else:
                print("Invalid option selected!")

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid option selected!")


if _name_ == "_main_":
    main()