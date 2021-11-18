import sys

class Node:
    def __init__(self, key = None, left = None, right = None, parent = None):
        self.key = key
        self.left = left
        self.right = right
        self.parent = parent

class BinarySeachTree():
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
        elif z.right == None:
            self.transplant(z, z.left)
        else:
            y = self.bst_min(z.right)
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

    def bst_min(self, x):
        while x.left != None:
            x = x.left
        return x

    def best_path_value(self):
        if self.count == 0:
            print("TreeError")
            return
        d = {}
        a = list()
        max = 0
        self.find_paths(self.root, a, d)
        for i in d.items():
            if i[1] > max:
                max = i[1]
        print(max)

    def find_paths(self, node, a, d):
        if node == None:
            return
        a += [node.key]
        a1 = list(a)
        a2 = list(a)
        if node.left == None and node.right == None:
            self.save_in_dictionary(a, d)
        else:
            self.find_paths(node.left, a1, d)
            self.find_paths(node.right, a2, d)

    def save_in_dictionary(self, a, d):
        num = int(str(a).count('5'))
        d[str(a)] = num

# this function runs the program according to the problem specification
def driver():
    bst = BinarySeachTree()
    with open(sys.argv[1]) as f:
        n = int(f.readline().strip())
        for _ in range(n):
            in_data = f.readline().strip().split()
            action, value_option = in_data[0], in_data[1:]
            if action == "insert":
                bst.insert(int(in_data[1]))
            elif action == "remove":
                bst.remove(int(in_data[1]))
            elif action == "bpv":
                bst.best_path_value()

if __name__ == "__main__":
    driver()
