import sys

class MaxHeap:
    class Underflow(Exception):
        def __init__(self, data = None):
            super().__init__(data)

    def __init__(self, array = None):
        if array == None:
            self.bhsize = 0
            self.length = 1025
            self.array = [None] * self.length
        else:
            self.length = len(array) + 1
            self.array = [None] * self.length
            for i in range(len(array)):
                self.array[i+1] = array[i]
            self.bhsize = self.length - 1
            i = self.length // 2
            while i > 0:
                self.sift_down(i)
                i -= 1

    def sift_down(self, i):
        left = 2 * i
        right = left + 1
        largest = i
        if left <= self.bhsize and self.array[left] > self.array[largest]:
            largest = left
        if right <= self.bhsize and self.array[right] > self.array[largest]:
            largest = right
        if largest != i:
            x = self.array[i]
            self.array[i] = self.array[largest]
            self.array[largest] = x
            self.sift_down(largest)

    def sift_up(self, i):
        parent = i // 2
        while i > 1 and self.array[parent] < self.array[i]:
            x = self.array[parent]
            self.array[parent] = self.array[i]
            self.array[i] = x
            i = parent
            parent = i // 2

    def insert(self, x):
        if self.bhsize >= self.length: # need to resize
            nlength = 2 * self.length
            narray = [None] * nlength
            for i in range(1, self.bhsize+1):
                narray[i] = self.array[i]
            self.length = nlength
            self.array = narray
        self.bhsize += 1
        self.array[self.bhsize] = x
        self.sift_up(self.bhsize)

    def remove(self):
        if self.bhsize == 0:
            raise BinaryHeap.Underflow("remove() called on empty heap")
        maximum = self.array[1]
        self.array[1] = self.array[self.bhsize]
        self.bhsize -= 1
        self.sift_down(1)
        return maximum

    def look(self):
        if self.bhsize == 0:
            raise BinaryHeap.Underflow("look() called on empty heap")
        return self.array[1]

    def size(self):
        return self.bhsize

    def is_empty(self):
        if self.bhsize == 0:
            return True
        else:
            return False

    def to_string(self):
        if self.bhsize == 0:
            result = 'Empty'
        else:
            l = []
            for i in range(1, self.bhsize+1):
                l.append(str(self.array[i]))
            result = ' '.join(l)
        return result

        def __len__(self):
            return self.size()

        def __str__(self):
            return self.to_string()

        def __iter__(self):
            i = 1
            while i <= self.bhsize:
                yield self.array[i]
                i += 1

class MinHeap:
    class Underflow(Exception):
        def __init__(self, data = None):
            super().__init__(data)

    def __init__(self, array = None):
        if array == None:
            self.bhsize = 0
            self.length = 1025
            self.array = [None] * self.length
        else:
            self.length = len(array) + 1
            self.array = [None] * self.length
            for i in range(len(array)):
                self.array[i+1] = array[i]
            self.bhsize = self.length - 1
            i = self.length // 2
            while i > 0:
                self.sift_down(i)
                i -= 1

    def sift_down(self, i):
        left = 2 * i
        right = left + 1
        smallest = i
        if left <= self.bhsize and self.array[left] < self.array[smallest]:
            smallest = left
        if right <= self.bhsize and self.array[right] < self.array[smallest]:
            smallest = right
        if smallest != i:
            x = self.array[i]
            self.array[i] = self.array[smallest]
            self.array[smallest] = x
            self.sift_down(smallest)

    def sift_up(self, i):
        parent = i // 2
        while i > 1 and self.array[parent] > self.array[i]:
            x = self.array[parent]
            self.array[parent] = self.array[i]
            self.array[i] = x
            i = parent
            parent = i // 2

    def insert(self, x):
        if self.bhsize >= self.length: # need to resize
            nlength = 2 * self.length
            narray = [None] * nlength
            for i in range(1, self.bhsize+1):
                narray[i] = self.array[i]
            self.length = nlength
            self.array = narray
        self.bhsize += 1
        self.array[self.bhsize] = x
        self.sift_up(self.bhsize)

    def remove(self):
        if self.bhsize == 0:
            raise BinaryHeap.Underflow("remove() called on empty heap")
        minimum = self.array[1]
        self.array[1] = self.array[self.bhsize]
        self.bhsize -= 1
        self.sift_down(1)
        return minimum

    def look(self):
        if self.bhsize == 0:
            raise BinaryHeap.Underflow("look() called on empty heap")
        return self.array[1]

    def size(self):
        return self.bhsize

    def is_empty(self):
        if self.bhsize == 0:
            return True
        else:
            return False

    def to_string(self):
        if self.bhsize == 0:
            result = 'Empty'
        else:
            l = []
            for i in range(1, self.bhsize+1):
                l.append(str(self.array[i]))
            result = ' '.join(l)
        return result

        def __len__(self):
            return self.size()

        def __str__(self):
            return self.to_string()

        def __iter__(self):
            i = 1
            while i <= self.bhsize:
                yield self.array[i]
                i += 1

class Iterator:
    def __init__(self, itlist):
        self.list = itlist
        self.index = 0
        self.size = len(itlist)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < self.size:
            val = self.list[self.index]
            self.index += 1
            return val
        else:
            raise StopIteration

    def __iter__(self):
        itlist = []
        for i in range(1, self.bhsize + 1):
            itlist.append(self.array[i])
        return BinaryHeap.Iterator(itlist)

def median(heap1, heap2):
    if heap1.size() == heap2.size():
        v = (heap1.look() + heap2.look()) / 2
        if (v).is_integer():
            v = int(v)
        else:
            v = round(v, 1)
        return v
    elif heap1.size() > heap2.size():
        value = heap1.look()
        return value
    elif heap2.size() > heap1.size():
        value = heap2.look()
        return value

# this function runs the program according to the problem specification
def driver():
    min_heap = MinHeap()
    max_heap = MaxHeap()
    with open(sys.argv[1]) as f:
        n = int(f.readline().strip())
        # Determine smaller or larger element
        v1 = int(f.readline().strip())
        v2 = int(f.readline().strip())
        n -= 2
        # Insert elements into binary heap
        if v1 < v2:
            smallest = v1
            largest = v2
            max_heap.insert(smallest)
            print(median(min_heap, max_heap))
            min_heap.insert(largest)
            print(median(min_heap, max_heap))
        else:
            smallest = v2
            largest = v1
            min_heap.insert(largest)
            print(median(min_heap, max_heap))
            max_heap.insert(smallest)
            print(median(min_heap, max_heap))
        # Insert the rest of the items
        for i in range(n):
            v = int(f.readline().strip())
            # Decide what heap to insert value into
            if v < max_heap.look():
                max_heap.insert(v)
            elif v <= min_heap.look():
                min_heap.insert(v)
            # If one heap has more elements than the other heap, insert root into other heap
            if min_heap.size == max_heap.size():
                print(median(min_heap, max_heap))
                return
            elif min_heap.size() > max_heap.size():
                removed_node = min_heap.remove()
                max_heap.insert(removed_node)
                print(median(min_heap, max_heap))
            elif max_heap.size() > min_heap.size():
                removed_node = max_heap.remove()
                min_heap.insert(removed_node)
                print(median(min_heap, max_heap))

if __name__ == "__main__":
    driver()
