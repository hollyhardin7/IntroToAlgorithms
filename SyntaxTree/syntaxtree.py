import sys

class STNode:
    def __init__(self, x: str):
        self.key = x
        self.left = None
        self.right = None

class SyntaxTree:
    def init_helper(self, i: int, l: 'list of strings') -> STNode:
        if i >= len(l):
            return None
        node = STNode(l[i])
        node.left = self.init_helper(2 * i, l)
        node.right = self.init_helper(2 * i + 1, l)
        return node

    def __init__(self, l:'list of strings') -> 'complete syntax tree':
        self.root = self.init_helper(1, l)

    def evaluate_syntax_tree(self):
        if self.root == None:
            return
        print(self.evaluate_expression(self.root))

    def evaluate_expression(self, x):
        if x == None:
            return
        if x.left == None and x.right == None:
            return int(x.key)
        left_sum = self.evaluate_expression(x.left)
        right_sum = self.evaluate_expression(x.right)
        if x.key == "+":
            return left_sum + right_sum
        elif x.key == "-":
            return left_sum - right_sum
        elif x.key == "*":
            return left_sum * right_sum
        else:
            return None

    def inprint(self):
        array = []
        self.to_list_inorder(self.root, array)
        print(''.join(array))

    def to_list_inorder(self, x, a):
        if x != None:
            if x.left != None:
                a.append(str("("))
                self.to_list_inorder(x.left, a)
            a.append(str(x.key))
            if x.right != None:
                self.to_list_inorder(x.right, a)
                a.append(str(")"))
        return a

# this function runs the program according to the problem specification
def driver():
    with open(sys.argv[1]) as f:
        n = int(f.readline().strip())
        in_data = [None] + f.readline().strip().split()
        st = SyntaxTree(in_data)
        st.inprint()
        st.evaluate_syntax_tree()

if __name__ == "__main__":
    driver()
