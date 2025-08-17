# 🔢 Bubble Sort — Detailed Manual

After **starting the program**, you will see:

```
Bubble Sort how many numbers?
```

---

## 1. What the Program Does
- Lets you input a list of numbers.
- Sorts the list in **ascending** or **descending** order based on your choice.
- Repeats until you decide to exit.

---

## 2. User Steps

### Step 1 — Enter number of items
- Type the number of elements you want to sort.
- Example:
  ```
  Bubble Sort how many numbers? 5
  ```

---

### Step 2 — Input numbers
- The program will ask for each number in sequence.
- Example:
  ```
  Enter number 1: 42
  Enter number 2: 5
  Enter number 3: 17
  Enter number 4: 8
  Enter number 5: 99
  ```

---

### Step 3 — Choose sort order
- Type:
  - `asc` for ascending order (small → large)
  - `des` for descending order (large → small)

Example:
```
Enter ('asc') for Ascending or ('des') for Descending: asc
Sorted list: [5, 8, 17, 42, 99]
```

---

## 3. Validation
- If you type anything other than `asc` or `des`, the program will display:
  ```
  Invalid choice. Please type 'asc' or 'des'.
  ```
  and will go back to asking if you want to repeat.

---

## 4. Repeat or Exit
- After sorting, the program asks:
  ```
  Repeat? y/n:
  ```
- Type:
  - `y` to run again.
  - `n` to quit the program.

---

## 5. Example Session

```
Bubble Sort how many numbers? 4
Enter number 1: 10
Enter number 2: 3
Enter number 3: 7
Enter number 4: 1
Enter ('asc') for Ascending or ('des') for Descending: des
Sorted list: [10, 7, 3, 1]
Repeat? y/n: n
```

---

## 6. Notes & Tips
- Works only with integers (decimal input will cause an error unless code is modified).
