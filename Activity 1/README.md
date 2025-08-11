# 🛒 Model/Database — User Manual

When you **start the program**, you will see:

```
******** Store Products ********
1. Add Product
2. Search Product
3. Clear (Show Menu Again)
4. Exit Program
```

---

## 1. What the Program Does
- Allows you to **store products** with an auto-generated ID.
- Lets you **search products** by ID or name.
- Supports **three categories**:  
  - `Gadget`  
  - `Clothing`  
  - `Food`

---

## 2. Menu Options

### **Option 1 — Add Product**
- Prompts for:
  1. **Product Name** → converted to uppercase automatically.
  2. **Category** → must be `"Gadget"`, `"Clothing"`, or `"Food"`.
- Automatically generates a **unique Product ID** starting from `20250000`.
- Example:
  ```
  Product Name: Laptop
  Category (Gadget, Clothing, or Food): Gadget
  Product added! ID: 20250000, Name: LAPTOP, Category: GADGET
  ```

---

### **Option 2 — Search Product**
- First asks:
  ```
  Show all Products? y/n:
  ```
  - `y` → Displays **all stored products** in a numbered list:
    ```
    ***All Products***
    1 ID: [20250000] Name: [LAPTOP] Category: [GADGET]
    ```
  - `n` → Lets you search by **Product Name** or **Product ID**:
    ```
    Enter the Product Name or ID to search: LAPTOP
    ID: [20250000] Name: [LAPTOP] Category: [GADGET]
    ```
  - If no match is found:
    ```
    No matching product found.
    ```

---

### **Option 3 — Clear (Show Menu Again)**
- Clears the screen and **re-displays the menu**.

---

### **Option 4 — Exit Program**
- Exits the program:
  ```
  Exiting program. Goodbye!
  ```

---

## 3. Example Session

```
******** Store Products ********
1. Add Product
2. Search Product
3. Clear (Show Menu Again)
4. Exit Program
Enter your choice (1-4): 1
Product Name: Laptop
Category (Gadget, Clothing, or Food): Gadget
Product added! ID: 20250000, Name: LAPTOP, Category: GADGET

******** Store Products ********
Enter your choice (1-4): 2
Show all Products? y/n: y
***All Products***
1 ID: [20250000] Name: [LAPTOP] Category: [GADGET]
```

---
