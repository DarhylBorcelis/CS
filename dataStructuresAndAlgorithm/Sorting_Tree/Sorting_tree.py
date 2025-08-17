class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BST:
    def __init__(self, root_key):
        self.root = Node(root_key)

    def insert(self, key):
        self._insert(self.root, key)

    def _insert(self, current, key):
        if key < current.key:
            if current.left is None:
                current.left = Node(key)
            else:
                self._insert(current.left, key)
        elif key > current.key:
            if current.right is None:
                current.right = Node(key)
            else:
                self._insert(current.right, key)

    def inorder(self):
        self._inorder(self.root)
        print()

    def _inorder(self, current):
        if current is not None:
            self._inorder(current.left)
            print(current.key, end=" ")
            self._inorder(current.right)


root_value = int(input("Enter the root of the tree: "))
tree = BST(root_value)

n = int(input("How many other nodes do you want to insert? "))

for i in range(n):
    num = int(input(f"Enter node {i+1}: "))
    tree.insert(num)

print("\nInorder Traversal (sorted order):")
tree.inorder()
