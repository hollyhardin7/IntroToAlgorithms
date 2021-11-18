import sys

class Node():
    def __init__(self, c = None, loc1 = None, v1 = None, loc2 = None, v2 = None, k = None, l = None, r = None, p = None):
        self.color = c
        self.key = k
        self.loc_one = loc1
        self.val_one = v1
        self.loc_two = loc2
        self.val_two = v2
        self.left = l
        self.right = r
        self.parent = p

class RedBlackTree():
    def __init__(self):
        self.nil = Node(None)
        self.nil.color = "Black"
        self.root = self.nil
        self.count = 0

    def insert(self, key, loc):
        found = self.search(key)
        if found == False:
             new_node = Node()
             new_node.key = key
             if loc == "magazine":
                 new_node.loc_one = "magazine"
                 new_node.val_one = 1
             elif loc == "note":
                 new_node.loc_two = "note"
                 new_node.val_two = 1
             new_node.left = self.nil
             new_node.right = self.nil
             new_node.parent = self.nil
             self.rb_insert(new_node)
             self.count += 1
        else:
             if loc == "magazine":
                 if found.val_one == None:
                     found.loc_one = loc
                     found.val_one = 1
                 else:
                     found.val_one += 1
             elif loc == "note":
                 if found.val_two == None:
                     found.loc_two = loc
                     found.val_two = 1
                 else:
                     found.val_two += 1

    def rb_insert(self, z):
        y = self.nil
        x = self.root
        while x != self.nil:
            y = x
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
       found = self.rb_search(self.root, key)
       if found == self.nil:
           return False
       else:
           return found

    def rb_search(self, x, k):
        if x == self.nil or str(k) == str(x.key):
            return x
        if str(k) < str(x.key):
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
            if x.loc_one != None:
                a.append(str(x.loc_one))
                a.append(str(x.val_one))
            if x.loc_two != None:
                a.append(str(x.loc_two))
                a.append(str(x.val_two))
            self.to_list_inorder(x.right, a)
        return a

    def solve(self):
        a = []
        valid = True
        self.to_list_inorder(self.root, a)
        #for i in range(0, len(a), 2):
        #    print(a[i], a[i+1])
        for i in range(0, len(a), 2):
            if a[i] == None and a[i+1] != None:
                valid = False
            elif a[i] != None and a[i+1] == None:
                continue
            elif a[i] < a[i+1]:
                valid = False
        if valid == False:
            print("NO")
        else:
            print("YES")

    def to_list_inorder(self, x, a):
        if x != self.nil:
            self.to_list_inorder(x.left, a)
            a.append(x.val_one)
            a.append(x.val_two)
            self.to_list_inorder(x.right, a)
        return a

# this function runs the program according to the problem specification
def driver():
    rbt = RedBlackTree()
    with open(sys.argv[1]) as f:
        first_line = f.readline().split()
        n_mag = int(first_line[0])
        n_note = int(first_line[1])
        second_line = f.readline().split()
        third_line = f.readline().split()
    for i in range(n_mag):
        rbt.insert(second_line[i].lower(), "magazine")
    for i in range(n_note):
        rbt.insert(third_line[i].lower(), "note")
    rbt.solve()

if __name__ == "__main__":
    driver()
