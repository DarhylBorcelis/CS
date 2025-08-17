while True:
    num = int(input("Bubble Sort how many numbers? "))
    bubble = []

    for x in range(1, num + 1):
        now = int(input(f"Enter number {x}: "))
        bubble.append(now)

    ans = input(
        "Enter ('asc') for Ascending or ('des') for Descending: ").lower()

    if ans == 'asc':
        bubble.sort()
        print("Sorted list:", bubble)
    elif ans == 'des':
        bubble.sort(reverse=True)
        print("Sorted list:", bubble)
    else:
        print("Invalid choice. Please type 'asc' or 'des'.")

    con = input("Repeat? (1/0): ").lower()
    if con == "0":
        break

