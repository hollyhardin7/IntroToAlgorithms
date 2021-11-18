import sys

class PriorityQueueRequest:
    def __init__(self, ip_address, estimate, index):
       self.ip_address = ip_address
       self.estimate = estimate
       self.index = index

class Queue:
    def __init__(self):
         self.list = list()
         self.count = 0

    def __len__(self):
        return len(self.list)

    def enqueue(self, ip, e, i):
        self.list.append([ip, e, i])
        self.count += 1

    def dequeue(self):
        highest_ip = self.list[0][0]
        highest_estimate = self.list[0][1]
        highest_index = self.list[0][2]
        for i in range(self.__len__()):
            if self.list[i][1] < highest_estimate:
                highest_ip = self.list[i][0]
                highest_estimate = self.list[i][1]
                highest_index = self.list[i][2]
            elif self.list[i][1] == highest_estimate:
                if self.list[i][2] < highest_index:
                    highest_ip = self.list[i][0]
                    highest_estimate = self.list[i][1]
                    highest_index = self.list[i][2]
        self.count -= 1
        for i in range(self.__len__()):
            if self.list[i][0] == highest_ip and self.list[i][1] == highest_estimate and self.list[i][2] == highest_index:
                request = self.list.pop(i)
                request_ip = request[0]
                return request_ip

    def is_empty(self):
        return len(self) == 0

def print_queue(q):
     if q.is_empty() is True:
        print("Empty")
     else:
        dequeued = []
        n = q.count
        for i in range(n):
           dequeued.append(str(q.dequeue()))
        print("\n".join(dequeued))

# this function runs the program according to the problem specification
def driver():
    tierA = Queue()
    tierB = Queue()
    with open(sys.argv[1]) as f:
        n = int(f.readline().strip())
        for i in range(n):
            in_data = f.readline().strip().split()
            IP_ADDR, TIER, ESTIMATE = str(in_data[0]), str(in_data[1]), int(in_data[2])
            if TIER is 'A':
                tierA.enqueue(IP_ADDR, ESTIMATE, int(i))
            elif TIER is 'B':
                tierB.enqueue(IP_ADDR, ESTIMATE, int(i))
        print_queue(tierA)
        print_queue(tierB)

if __name__ == "__main__":
    driver()
