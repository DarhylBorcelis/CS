"""
# 🏪 MODEL/DATABASE — Detailed Manual

After **starting the program**, you will see this menu:

******** Store Products Menu ********

1. Add Product
2. Search Product
3. Clear (Show Menu Again)
4. Exit Program

Below is a detailed explanation of **what each menu option does**, what the program asks you, and example interactions.

---

## 1. Add Product
**What it does**
- Lets you add a new product to the program's in-memory list.
- Automatically assigns a unique Product ID.

**User steps**
1. Type `1` and press Enter.
2. When prompted, type the **Product Name** (any case allowed). The program will store it in UPPERCASE.
3. When prompted, type the **Category**. Allowed values (case-insensitive): `Gadget`, `Clothing`, `Food`.

**Validation**
- If you enter anything other than the three allowed categories, the program will print:
  Invalid category. Please enter 'Gadget', 'Clothing', or 'Food'.
  and return to the main menu without adding the product.

**How ID is generated**
- ID = len(data) + 20250000
- Example: first product → 20250000, second → 20250001, etc.

**Example session**
-Enter your choice (1-4): 1
-Product Name: Laptop
-Category (Gadget, Clothing, or Food): Gadget
-Product added! ID: 20250000, Name: LAPTOP, Category: GADGET

---

## 2. Search Product
**What it does**
- Lets you either list *all* products or search for a single product by **Name** or **ID**.

**User steps**
1. Type `2` and press Enter.
2. When asked `Show all Products? y/n:`, enter:
   - `y` to list everything, or
   - `n` to search for a specific product.
3. If you chose `n`, you'll be prompted:
   Enter the Product Name or ID to search:
   Type a product name (any case) or the numeric ID.

**Matching rules**
- Names are compared in uppercase (the program converts your search to uppercase).
- IDs are compared as strings, so you can enter `20250000` as text.

**Outputs**
- If found:
  ID: [20250000] Name: [LAPTOP] Category: [GADGET]
- If not found:
  No matching product found.

**Example — show all**
Enter your choice (1-4): 2
Show all Products? y/n: y
***All Products***
1 ID: [20250000] Name: [LAPTOP] Category: [GADGET]
2 ID: [20250001] Name: [SHIRT]  Category: [CLOTHING]

**Example — search by name**
Enter your choice (1-4): 2
Show all Products? y/n: n
Enter the Product Name or ID to search: laptop
ID: [20250000] Name: [LAPTOP] Category: [GADGET]

---

## 3. Clear (Show Menu Again)
**What it does**
- Clears the console window and redisplays the menu to keep the screen tidy.

**Platform note**
- The program uses:
  os.system('cls')
  which works on **Windows**.
- If you're on **macOS** or **Linux**, replace 'cls' with 'clear' in the code:
  os.system('clear')

**Example**
Enter your choice (1-4): 3
# console clears and menu reappears

---

## 4. Exit Program
**What it does**
- Stops the program and prints a goodbye message.

**Example**
Enter your choice (1-4): 4
Exiting program. Goodbye!

---

## Other Important Details

### Invalid menu input
- If you type anything other than 1, 2, 3, or 4, the program will respond:
  Invalid choice. Please select 1, 2, 3, or 4.
  and show the menu again.

### Data persistence
- **All data is stored in memory only** (the `data` list). When you close the program, all products are lost.
- If you need permanent storage, consider adding file saving (CSV/JSON) or a database.

### Tips & Troubleshooting
- If `Clear` does nothing on macOS/Linux: change `'cls'` → `'clear'` as shown above.
- If search returns nothing, check the exact spelling or ID — names are matched in uppercase.
- To stop the program instantly, you can press `Ctrl + C` in the terminal (KeyboardInterrupt).

---

## Quick Full Example Session
******** Store Products Menu ********
1. Add Product
2. Search Product
3. Clear (Show Menu Again)
4. Exit Program

Enter your choice (1-4): 1
Product Name: Phone
Category (Gadget, Clothing, or Food): Gadget
Product added! ID: 20250000, Name: PHONE, Category: GADGET

Enter your choice (1-4): 2
Show all Products? y/n: y
***All Products***
1 ID: [20250000] Name: [PHONE] Category: [GADGET]

Enter your choice (1-4): 4
Exiting program. Goodbye!
"""

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
    show = input('Show all Products? y/n: ').lower()
    num = 0
    if show == 'y':
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
    print("4. Exit Program")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        add_data()
    elif choice == '2':
        search_data()
    elif choice == '3':
        os.system('cls')  # Change to 'clear' for macOS/Linux
        continue
    elif choice == '4':
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice. Please select 1, 2, 3, or 4.")

