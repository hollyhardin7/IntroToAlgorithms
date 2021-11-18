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
        popped = []
        n = s.count
        for i in range(n):
           popped.append(str(s.pop()))
        print(" ".join(popped))
        for i in range(n - 1, -1, -1):
            s.push(popped[i])

# this function runs the program according to the problem specification
def driver():
    s = Stack()
    with open(sys.argv[1]) as f:
        n = int(f.readline().strip())
        for _ in range(n):
            in_data = f.readline().strip().split()
            action, value_option = in_data[0], in_data[1:]
            if action == "push":
               value = int(value_option[0])
               s.push(value)
            elif action == "pop":
               val = s.pop()
               if val == -1:
                   print("StackError")
               else:
                   print(val)
            elif action == "print":
               print_stack(s)

if __name__ == "__main__":
    driver()
