import sys

class Node:
    def __init__(self, key = None, left = None, right = None, parent = None):
        self.key = key
        self.left = left
        self.right = right
        self.parent = parent

class BinarySeachTree():
    class Underflow(Exception):
        def __init__(self, data = None):
            super().__init__(data)

    def __init__(self):
        self.root = None
        self.count = 0

    def insert(self, key):
        new_node = Node(key)
        self.bst_insert(new_node)
        self.count += 1

    def bst_insert(self, z):
        y = None
        x = self.root
        while x != None:
            y = x
            if int(z.key) < int(x.key):
                x = x.left
            else:
                x = x.right
        z.parent = y
        if y == None:
            self.root = z
        elif int(z.key) < int(y.key):
            y.left = z
        else:
            y.right = z

    def search(self, key):
        if self.count == 0:
            print("NotFound")
            return
        else:
            found = self.bst_search(self.root, key)
            if found == None:
                print("NotFound")
            else:
                print("Found")

    def bst_search(self, x, k):
        if x == None or int(k) == int(x.key):
            return x
        if int(k) < int(x.key):
            return self.bst_search(x.left, k)
        else:
            return self.bst_search(x.right, k)

    def remove(self, key):
        if self.count == 0:
            print("TreeError")
            return
        else:
            found = self.bst_search(self.root, key)
            if found == None:
                print("TreeError")
            else:
                self.bst_remove(found)
                self.count -= 1
                return

    def bst_remove(self, z):
        if z.left == None:
            self.transplant(z, z.right)
        elif node.right == None:
            self.transplant(z, z.left)
        else:
            y = self.successor(z.right)
            if y.parent != z:
                self.transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            self.transplant(z, y)
            y.left = z.left
            y.left.parent = y

    def transplant(self, u, v):
        if u.parent == None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        if v != None:
            v.parent = u.parent

    def successor(self, x):
        if x.right != None:
            return self.min(x.right)
        y = x.parent
        while y != None and x == y.right:
            x = y
            y = y.p
        return y

    def min(self):
        if self.count == 0:
            print("Empty")
            return
        else:
            minimum = self.bst_min(self.root)
            print(minimum)

    def bst_min(self, x):
        while x.left != None:
            x = x.left
        return x.key

    def max(self):
        if self.count == 0:
            print("Empty")
            return
        else:
            maximum = self.bst_max(self.root)
            print(maximum)

    def bst_max(self, x):
        while x.right != None:
            x = x.right
        return x.key

    def inprint(self):
        if self.count == 0:
            print("Empty")
            return
        else:
            array = []
            self.to_list_inorder(self.root, array)
            print(" ".join(array))

    def preprint(self):
        if self.count == 0:
            print("Empty")
            return
        else:
            array = []
            self.to_list_preorder(self.root, array)
            print(" ".join(array))

    def postprint(self):
        if self.count == 0:
            print("Empty")
            return
        else:
            array = []
            self.to_list_postorder(self.root, array)
            print(" ".join(array))

    def to_list_inorder(self, x, a):
        if x != None:
            self.to_list_inorder(x.left, a)
            a.append(x.key)
            self.to_list_inorder(x.right, a)
        return a

    def to_list_preorder(self, x, a):
        if x != None:
            a.append(x.key)
            self.to_list_preorder(x.left, a)
            self.to_list_preorder(x.right, a)
        return a

    def to_list_postorder(self, x, a):
        if x != None:
            self.to_list_postorder(x.left, a)
            self.to_list_postorder(x.right, a)
            a.append(x.key)
        return a

# this function runs the program according to the problem specification
def driver():
    bst = BinarySeachTree()
    with open(sys.argv[1]) as f:
        n = int(f.readline().strip())
        for _ in range(n):
            in_data = f.readline().strip().split()
            action, value_option = in_data[0], in_data[1:]
            if action == "insert":
                bst.insert(in_data[1])
            elif action == "search":
                bst.search(in_data[1])
            elif action == "remove":
                bst.remove(in_data[1])
            elif action == "min":
                bst.min()
            elif action == "max":
                bst.max()
            elif action == "inprint":
                bst.inprint()
            elif action == "preprint":
                bst.preprint()
            elif action == "postprint":
                bst.postprint()

if __name__ == "__main__":
    driver()
