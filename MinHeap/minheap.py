# Referenced class notes and book to complete project
import sys
import math

class Tree():
    def __init__(self):
        self.min_heap = [0]
        self.heap_size = 0

    def parent(self, i):
        return math.floor(self.heap_size / 2)

    def left_child(self, i):
        return (2 * i)

    def right_child(self, i):
        return ((2 * i) + 1)

    def insert(self, x):
        self.heap_size += 1
        self.min_heap += [x]
        self.heap_increase_key(self.heap_size, x)

    def heap_increase_key(self, i, key):
        self.min_heap[i] = key
        while i > 1 and self.min_heap[self.parent(i)] > self.min_heap[i]:
            self.exchange(i, self.parent(i))
            i = self.parent(i)

    def min_heapify(self, i):
        left = self.left_child(i)
        right = self.right_child(i)
        smallest = i
        if left <= self.heap_size and self.min_heap[left] < self.min_heap[i]:
            smallest = left
        if right <= self.heap_size and self.min_heap[right] < self.min_heap[smallest]:
            smallest = right
        if smallest != i:
            self.exchange(i, smallest)
            self.min_heapify(smallest)

    def heap_sort(self):
        self.build_min_heap()
        for i in range(len(self.min_heap), 2, -1):
            self.exchange(1, i)
            self.heap_size -= 1
            self.min_heapify(1)

    def exchange(self, a, b):
        var1 = self.min_heap[a]
        var2 = self.min_heap[b]
        self.min_heap[a] = var2
        self.min_heap[b] = var1

    def build_min_heap(self):
        self.heap_size = len(self.min_heap)
        for i in range(math.floor(len(self.min_heap) / 2), 1, -1):
            self.min_heapify(i)

    def remove(self):
        value = self.min_heap[1]
        self.min_heap[1] = self.min_heap[self.heap_size]
        self.heap_size -= 1
        self.min_heapify(1)
        return value

    def best(self):
        return self.min_heap[1]

    def is_empty(self):
        if self.heap_size == 0:
            return True
        else:
            return False

    def to_string(self):
        heap_string = []
        for i in range(1, self.heap_size + 1):
            heap_string.append(str(self.min_heap[i]))
        return heap_string

    def size(self):
        return self.heap_size

def driver():
    min_heap = Tree()
    with open(sys.argv[1]) as f:
        n = int(f.readline().strip())
        for _ in range(n):
            in_data = f.readline().strip().split()
            action, value_option = in_data[0], in_data[1:]
            if action == "insert":
               value = int(value_option[0])
               min_heap.insert(value)
            elif action == "remove":
                if min_heap.is_empty() is True:
                    print("HeapError")
                else:
                    print(min_heap.remove())
            elif action == "best":
                if min_heap.is_empty() is True:
                    print("HeapError")
                else:
                    print(min_heap.best())
            elif action == "print":
                if min_heap.is_empty() is True:
                    print("Empty")
                else:
                    print(" ".join(min_heap.to_string()))
            elif action == "size":
                print(min_heap.size())

if __name__ == "__main__":
    driver()
