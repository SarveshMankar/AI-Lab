# Class Node of Tree
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self): # __str__
        return f"Node({self.data})"

# Class Tree
class Tree:
    def __init__(self):
        self.root = None

    # Method to insert data in tree
    def insert(self, data):
        if self.root == None:
            self.root = Node(data)
        else:
            self._insert(data, self.root)

    # Method to insert data in tree
    def _insert(self, data, cur_node):
        if data < cur_node.data:
            if cur_node.left == None:
                cur_node.left = Node(data)
            else:
                self._insert(data, cur_node.left)
        elif data > cur_node.data:
            if cur_node.right == None:
                cur_node.right = Node(data)
            else:
                self._insert(data, cur_node.right)
        else:
            print("Value already present in tree.")

    # Method to find data in tree
    def find(self, data):
        if self.root:
            is_found = self._find(data, self.root)
            if is_found:
                return True
            return False
        else:
            return None

    # Method to find data in tree
    def _find(self, data, cur_node):
        if data > cur_node.data and cur_node.right:
            return self._find(data, cur_node.right)
        elif data < cur_node.data and cur_node.left:
            return self._find(data, cur_node.left)
        if data == cur_node.data:
            return True

    # Method to print tree
    def print_tree(self):
        if self.root != None:
            self._print_tree(self.root)



    # Method to print tree
    def _print_tree(self, cur_node):
        if cur_node != None:
            self._print_tree(cur_node.left)
            print(str(cur_node.data), str(cur_node.left), str(cur_node.right))
            self._print_tree(cur_node.right)


# Path: tree.py
# Main method

tree = Tree()
tree.insert(5)
tree.insert(4)
tree.insert(6)
tree.insert(7)
tree.insert(8)

tree.print_tree()

#      2    3
#   (0)--(1)--(2)
#    |   / \   |
#   6| 8/   \5 |7
#    | /     \ |
#   (3)-------(4)
#       9