"""
# 🌳 Binary Search Tree (BST) — Detailed Manual

After **starting the program**, you will see:

    Enter the root of the tree:

---

## 1. What the Program Does
- Lets you create a **Binary Search Tree** by first defining the root.
- Allows you to insert additional nodes one by one.
- Displays the tree using **Inorder Traversal** (which shows the numbers in sorted order).

---

## 2. User Steps

### Step 1 — Enter the root of the tree
Example:
    Enter the root of the tree: 50

---

### Step 2 — Decide how many nodes to insert
Example:
    How many other nodes do you want to insert? 4

---

### Step 3 — Insert nodes one by one
Example:
    Enter node 1: 30
    Enter node 2: 70
    Enter node 3: 20
    Enter node 4: 40

---

### Step 4 — Display the tree (Inorder Traversal)
Example output:
    Inorder Traversal (sorted order):
    20 30 40 50 70

---

## 3. How Insertion Works
- If the new value is **less** than the current node → goes to the **left**.
- If the new value is **greater** than the current node → goes to the **right**.
- Duplicate values are ignored.

Example Tree (from input above):

        50
       /  \
     30    70
    /  \
  20    40

---

## 4. Example Session

    Enter the root of the tree: 50
    How many other nodes do you want to insert? 4
    Enter node 1: 30
    Enter node 2: 70
    Enter node 3: 20
    Enter node 4: 40

    Inorder Traversal (sorted order):
    20 30 40 50 70

---

## 5. Notes & Tips
- Works only with integers (decimal input will cause an error unless modified).
- Inorder traversal **always prints the tree in ascending order**.
- You can expand the program to include:
  - Preorder and Postorder traversals
  - Node search
  - Deletion of nodes
