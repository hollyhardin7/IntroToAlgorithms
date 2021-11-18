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

class Queue:
    def __init__(self):
         self.list = LinkedList()
         self.count = 0

    def enqueue(self, x):
        new_node = Node()
        new_node.data = x
        if self.count == 0:
            self.list.head = new_node
            self.list.tail = new_node
        else:
             if self.count == 1:
                 self.list.tail.next = new_node
             self.list.head.next = new_node
             self.list.head = new_node
        self.count = self.count + 1

    def dequeue(self):
        if self.count == 0:
            return -1
        else:
            if self.count == 1:
                self.count = self.count - 1
                return self.list.tail.data
            else:
                dequeued = self.list.tail.data
                self.list.tail = self.list.tail.next
                self.count = self.count - 1
                return dequeued

    def is_empty(self):
        if self.count == 0:
           return True
        else:
           return False

def print_queue(q):
     if q.is_empty() is True:
        print("Empty")
     else:
        dequeued = []
        n = q.count
        for i in range(n):
           dequeued.append(str(q.dequeue()))
        print(" ".join(dequeued))
        for i in range(n):
            q.enqueue(dequeued[i])

# this function runs the program according to the problem specification
def driver():
    q = Queue()
    with open(sys.argv[1]) as f:
        n = int(f.readline().strip())
        for _ in range(n):
            in_data = f.readline().strip().split()
            action, value_option = in_data[0], in_data[1:]
            if action == "enqueue":
                value = int(value_option[0])
                q.enqueue(value)
            elif action == "dequeue":
                val = q.dequeue()
                if val == -1:
                       print("QueueError")
                else:
                       print (val)
            elif action == "print":
                print_queue(q)

if __name__ == "__main__":
    driver()
