# Referenced from Sventeks' Notes
import sys

class Node:
    def __init__(self, key = None, left = None, right = None, parent = None):
        self.key = key
        self.left = left
        self.right = right
        self.parent = parent

class SplayTree():
    class Underflow(Exception):
        def __init__(self, data = None):
            super().__init__(data)

    def __init__(self):
        self.root = None
        self.count = 0
        self.height = 0

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
        self.splay(z)

    def splay(self, x):
        while x != self.root:
            if x.parent == self.root:
                if x == x.parent.left:
                    self.right_rotate(x)
                else:
                    self.left_rotate(x)
            else:
                if x == x.parent.left:
                    if x.parent == x.parent.parent.left:
                        self.right_rotate(x)
                        self.right_rotate(x)
                    else:
                        self.right_rotate(x)
                        self.left_rotate(x)
                else:
                    if x.parent == x.parent.parent.right:
                        self.left_rotate(x)
                        self.left_rotate(x)
                    else:
                        self.left_rotate(x)
                        self.right_rotate(x)

    def left_rotate(self, x):
        p = x.parent
        x.parent = p.parent
        if p == self.root:
            self.root = x
        elif p == p.parent.left:
            p.parent.left = x
        else:
            p.parent.right = x
        p.right = x.left
        if p.right != None:
            p.right.parent = p
        x.left = p
        p.parent = x

    def right_rotate(self, x):
        p = x.parent
        x.parent = p.parent
        if p == self.root:
            self.root = x
        elif p == p.parent.left:
            p.parent.left = x
        else:
            p.parent.right = x
        p.left = x.right
        if p.left != None:
            p.left.parent = p
        x.right = p
        p.parent = x

    def search(self, key):
        if self.count == 0:
            print("NotFound")
            return
        else:
            found = self.bst_search(self.root, key)
            if found == None:
                print("NotFound")
            else:
                self.splay(found)
                print("Found")

    def bst_search(self, x, k):
        if x == None or int(k) == int(x.key):
            return x
        if int(k) < int(x.key):
            return self.bst_search(x.left, k)
        else:
            return self.bst_search(x.right, k)

    def inprint(self):
        if self.count == 0:
            print("Empty")
            return
        else:
            array = []
            self.to_list_inorder(self.root, array)
            print(" ".join(array))

    def to_list_inorder(self, x, a):
        if x != None:
            self.to_list_inorder(x.left, a)
            a.append(str(x.key))
            self.to_list_inorder(x.right, a)
        return a

    def get_root(self):
        if self.count == 0:
            print("Empty")
        else:
            print(self.root.key)

    def get_height(self):
        print(self.max_depth(self.root))

    def max_depth(self, x):
        if x == None:
            return 0
        else:
            l_depth = self.max_depth(x.left)
            r_depth = self.max_depth(x.right)
        
        if l_depth > r_depth:
            return l_depth + 1
        else:
            return r_depth + 1

# this function runs the program according to the problem specification
def driver():
    st = SplayTree()
    with open(sys.argv[1]) as f:
        n = int(f.readline().strip())
        for _ in range(n):
            in_data = f.readline().strip().split()
            action, value_option = in_data[0], in_data[1:]
            if action == "insert":
                st.insert(int(in_data[1]))
            elif action == "search":
                st.search(int(in_data[1]))
            elif action == "inprint":
                st.inprint()
            elif action == "root":
                st.get_root()
            elif action == "height":
                st.get_height()

if __name__ == "__main__":
    driver()
