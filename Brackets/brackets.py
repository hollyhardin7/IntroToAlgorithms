# Referenced class notes and book to complete project
import sys
import copy

class Node:
    def __init__(self, data = None, next = None):
       self.data = data
       self.next = next

class LinkedList:
    def __init__(self, head = None, tail = None):
       self.head = head
       self.tail = tail

class Stack:
    def __init__(self):
         self.list = LinkedList()
         self.count = 0

    def push(self, x):
        new_node = Node()
        new_node.data = x
        if self.count == 0:
            self.list.head = new_node
            self.list.tail = new_node
        else:
             new_node.next = self.list.tail
             self.list.tail = new_node
        self.count = self.count + 1

    def pop(self):
        if self.count == 0:
            return -1
        else:
            if self.count == 1:
                self.count = self.count - 1
                return self.list.head.data
            else:
                popped = self.list.tail.data
                self.list.tail = self.list.tail.next
                self.count = self.count - 1
                return popped

    def is_empty(self):
        if self.count == 0:
           return True
        else:
           return False

def print_stack(s):
     if s.is_empty() is True:
        print("Empty")
     else:
        temp = copy.deepcopy(s)
        popped = []
        n = temp.count
        for i in range(n):
           popped.append(str(temp.pop()))
        print (" ".join(popped))

def opening_bracket(x):
    if x is "(" or x is "[" or x is "{":
        return True
    else:
        return False

def closing_bracket(x):
    if x is ")" or x is "]" or x is "}":
        return True
    else:
        return False

def balanced(x, y):
    if y is "(" and x is ")":
        return True
    elif y is "[" and x is "]":
        return True
    elif y is "{" and x is "}":
        return True
    else:
        return False

# this function runs the program according to the problem specification
def driver():
    with open(sys.argv[1]) as f:
        n = int(f.readline().strip())
        s = Stack()
        for _ in range(n):
            brackets = f.readline().strip()
            length = len(brackets)
            well_formed = False
            for i in range(length):
                if opening_bracket(brackets[i]) is True:
                    s.push(brackets[i])
                elif closing_bracket(brackets[i]) is True:
                    popped = s.pop()
                    if balanced(brackets[i], popped) is True:
                        well_formed = True
                    else:
                        well_formed = False
                if s.is_empty() is False:
                    well_formed = False
            if well_formed is True:
                print("YES")
            else:
                print("NO")

if __name__ == "__main__":
    driver()
