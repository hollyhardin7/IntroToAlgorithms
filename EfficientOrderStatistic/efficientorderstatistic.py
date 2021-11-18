import sys

class Node():
    def __init__(self, c = None, k = None, s = None, l = None, r = None, p = None):
        self.color = c
        self.key = k
        self.size = s
        self.left = l
        self.right = r
        self.parent = p

class RedBlackTree():
    def __init__(self):
        self.nil = Node(None)
        self.nil.color = "Black"
        self.nil.size = 0
        self.nil.left = self.nil
        self.nil.right = self.nil
        self.nil.parent = self.nil
        self.root = self.nil
        self.count = 0

    def insert(self, key):
        new_node = Node(None)
        new_node.key = key
        new_node.size = 1
        self.rb_insert(new_node)
        self.count += 1

    def rb_insert(self, z):
        y = self.nil
        x = self.root
        while x != self.nil:
            y = x
            x.size += 1
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        z.parent = y
        if y == self.nil:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z
        z.left = self.nil
        z.right = self.nil
        z.color = "Red"
        self.rb_insert_fixup(z)

    def rb_insert_fixup(self, z):
        while z.parent.color == "Red":
            if z.parent == z.parent.parent.left:
                y = z.parent.parent.right
                if y.color == "Red":
                    z.parent.color = "Black"
                    y.color = "Black"
                    z.parent.parent.color = "Red"
                    z = z.parent.parent
                else:
                    if z == z.parent.right:
                        z = z.parent
                        self.left_rotate(z)
                    z.parent.color = "Black"
                    z.parent.parent.color = "Red"
                    self.right_rotate(z.parent.parent)
            else:
                y = z.parent.parent.left
                if y.color == "Red":
                    z.parent.color = "Black"
                    y.color = "Black"
                    z.parent.parent.color = "Red"
                    z = z.parent.parent
                else:
                    if z == z.parent.left:
                        z = z.parent
                        self.right_rotate(z)
                    z.parent.color = "Black"
                    z.parent.parent.color = "Red"
                    self.left_rotate(z.parent.parent)
        self.root.color = "Black"

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.nil:
            y.left.parent = x
        y.parent = x.parent
        if x.parent == self.nil:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y
        y.size = x.size
        x.size = x.left.size + x.right.size + 1

    def right_rotate(self, y):
        x = y.left
        y.left = x.right
        if x.right != self.nil:
            x.right.parent = y
        x.parent = y.parent
        if y.parent == self.nil:
            self.root = x
        elif y == y.parent.right:
            y.parent.right = x
        else:
            y.parent.left = x
        x.right = y
        y.parent = x
        x.size = y.size
        y.size = y.right.size + y.left.size + 1

    def remove(self, key):
        if self.count == 0:
            print("TreeError")
            return
        else:
            found = self.rb_search(self.root, key)
            if found == self.nil:
                print("TreeError")
            else:
                self.rb_remove(found)
                self.count -= 1

    def rb_remove(self, z):
        y = z
        y_original_color = y.color
        if z.left == self.nil:
            x = z.right
            self.rb_transplant(z, z.right)
        elif z.right == self.nil:
            x = z.left
            self.rb_transplant(z, z.left)
        else:
            y = self.rb_min(z.right)
            y_original_color = y.color
            x = y.right
            if y.parent == z:
                x.parent = y
            else:
                self.rb_transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            self.rb_transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color
        if y_original_color == "Black":
            self.rb_delete_fixup(x)

    def rb_delete_fixup(self, x):
        while x != self.root and x.color == "Black" and x != self.nil:
            if x == x.parent.left:
                w = x.parent.right
                if w.color == "Red":
                    w.color = "Black"
                    x.parent.color = "Red"
                    self.left_rotate(x.parent)
                    w = x.parent.right
                if w.left.color == "Black" and w.right.color == "Black":
                    w.color = "Red"
                    x = x.parent
                else:
                    if w.right.color == "Black":
                        w.left.color = "Black"
                        w.color = "Red"
                        self.right_rotate(w)
                        w = x.parent.right
                    w.color = x.parent.color
                    x.parent.color = "Black"
                    w.right.color = "Black"
                    self.left_rotate(x.parent)
                    x = self.root
            else:
                if x == x.parent.right:
                    w = x.parent.left
                    if w.color == "Red":
                        w.color = "Black"
                        x.parent.color = "Red"
                        self.right_rotate(x.parent)
                        w = x.parent.right
                    if w.right.color == "Black" and w.left.color == "Black":
                        w.color = "Red"
                        x = x.parent
                    else:
                        if w.left.color == "Black":
                            w.right.color = "Black"
                            w.color = "Red"
                            self.left_rotate(w)
                            w = x.parent.right
                        w.color = x.parent.color
                        x.parent.color = "Black"
                        w.right.color = "Black"
                        self.right_rotate(x.parent)
                        x = self.root
        x.color = "Black"

    def rb_transplant(self, u, v):
        if u.parent == self.nil:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def search(self, key):
        if self.count == 0:
            print("NotFound")
            return
        else:
            found = self.rb_search(self.root, key)
            if found == self.nil:
                print("NotFound")
            else:
                print("Found")

    def rb_search(self, x, k):
        if x == self.nil or int(k) == int(x.key):
            return x
        if int(k) < int(x.key):
            return self.rb_search(x.left, k)
        else:
            return self.rb_search(x.right, k)

    def min(self):
        if self.count == 0:
            print("Empty")
            return
        else:
            minimum = self.rb_min(self.root)
            print(minimum.key)

    def rb_min(self, x):
        while x.left != self.nil:
            x = x.left
        return x

    def max(self):
        if self.count == 0:
            print("Empty")
            return
        else:
            maximum = self.rb_max(self.root)
            print(maximum.key)

    def rb_max(self, x):
        while x.right != self.nil:
            x = x.right
        return x

    def inprint(self):
        if self.count == 0:
            print("Empty")
            return
        else:
            array = []
            self.to_list_inorder(self.root, array)
            print(" ".join(array))

    def to_list_inorder(self, x, a):
        if x != self.nil:
            self.to_list_inorder(x.left, a)
            a.append(str(x.key))
            a.append(str(x.size))
            self.to_list_inorder(x.right, a)
        return a

    def get_subtree_sizes(self):
        print("Getting subtree sizes")

    def order(self, x):
        node = self.os_select(self.root, x)
        if node.key == None:
            print("TreeError")
        else:
            print(node.key)

    def os_select(self, x, i):
        r = x.left.size + 1
        if i == r:
            return x
        elif i < r:
            return self.os_select(x.left, i)
        else:
            return self.os_select(x.right, i-r)

# this function runs the program according to the problem specification
def driver():
    rbt = RedBlackTree()
    with open(sys.argv[1]) as f:
        n = int(f.readline().strip())
        for _ in range(n):
            in_data = f.readline().strip().split()
            action, value_option = in_data[0], in_data[1:]
            if action == "insert":
                rbt.insert(int(in_data[1]))
            #elif action == "get_subtree_sizes":
            #    rbt.get_subtree_sizes()
            elif action == "order":
                rbt.order(int(in_data[1]))

if __name__ == "__main__":
    driver()
