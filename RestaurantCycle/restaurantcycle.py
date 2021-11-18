import sys

class Node:
    def __init__(self, num = None, energy = None, energy_loss = None, next = None):
       self.num = num
       self.energy = energy
       self.next = next

class LinkedList:
    def __init__(self, head = None, tail = None):
       self.head = head
       self.tail = tail

class Queue:
    def __init__(self):
         self.list = LinkedList()
         self.count = 0

    def enqueue(self, i, e, l):
        new_node = Node()
        new_node.num = i
        new_node.energy = e
        new_node.energy_loss = l
        if self.count == 0:
            self.list.head = new_node
            self.list.tail = new_node
        else:
             if self.count == 1:
                 self.list.tail.next = new_node
             self.list.head.next = new_node
             self.list.head = new_node
             self.list.head.next = self.list.tail
        self.count = self.count + 1
        #print("head num is ", self.list.head.num, " and tail num is ", self.list.tail.num)

    def dequeue(self):
        if self.count == 0:
            return -1
        else:
            num = self.list.tail.num
            energy = self.list.tail.energy
            energy_loss = self.list.tail.energy_loss
            self.list.tail = self.list.tail.next
            self.list.head.next = self.list.tail
            self.count = self.count - 1
            self.enqueue(num, energy, energy_loss)
        #print("head num is ", self.list.head.num, " and tail num is ", self.list.tail.num)

    def is_empty(self):
        if self.count == 0:
           return True
        else:
           return False

def find_restuarant(q, n):
    acc_energy = 0
    first_restaurant = 0
    count = 0
    total_restaurants = n
    while (count != total_restaurants):
        num_restaurant = int(q.list.tail.num)
        energy = int(q.list.tail.energy)
        energy_loss = int(q.list.tail.energy_loss)
        acc_energy += energy
        acc_energy -= energy_loss
        q.dequeue()
        if acc_energy <= 0:
            acc_energy = 0
            count = 0
            first_restaurant = q.list.tail.num
        else:
            count += 1
    print(first_restaurant)

def driver():
    q = Queue()
    with open(sys.argv[1]) as f:
        n = int(f.readline().strip())
        for i in range(n):
            restaurant = f.readline().strip().split()
            energy, energy_loss = restaurant[0], restaurant[1]
            q.enqueue(i, energy, energy_loss)
        find_restuarant(q, n)

if __name__ == "__main__":
    driver()
