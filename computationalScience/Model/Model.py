import os
data = []


def add_data():
    ID = len(data) + 20250000
    name = input("Product Name: ").upper()
    category = input("Category (Gadget, Clothing, or Food): ").upper()

    if category not in ['GADGET', 'CLOTHING', 'FOOD']:
        print("Invalid category. Please enter 'Gadget', 'Clothing', or 'Food'.")
        return

    data.append([ID, name, category])
    print(f"Product added! ID: {ID}, Name: {name}, Category: {category}")


def search_data():
    show = input('Show all Products? (1/0): ')
    num = 0
    if show == '1':
        print("***All Products***")
        for x in data:
            num += 1
            print(f"{num} ID: [{x[0]}] Name: [{x[1]}] Category: [{x[2]}]")
    else:
        con = input("Enter the Product Name or ID to search: ").upper()
        found = False
        for x in data:
            if con == str(x[0]) or con == x[1]:
                print(f"ID: [{x[0]}] Name: [{x[1]}] Category: [{x[2]}]")
                found = True
        if not found:
            print("No matching product found.")


while True:
    print("\n******** Store Products Menu ********")
    print("1. Add Product")
    print("2. Search Product")
    print("3. Clear (Show Menu Again)")
    print("0. Exit Program")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        add_data()
    elif choice == '2':
        search_data()
    elif choice == '3':
        os.system('cls')
        continue
    elif choice == '0':
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice. Please select 1, 2, 3, or 0.")


