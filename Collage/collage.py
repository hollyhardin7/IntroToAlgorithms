# Referenced class notes and book to complete project
import sys

class HashTable:
    def __init__(self):
        self.magazine_words = {}
        self.size = 0
        self.count = 0
        self.valid = True

    def insert_mag_word(self, word):
        if word in self.magazine_words:
            self.magazine_words[word] += 1
        else:
            self.magazine_words[word] = 1
            self.count += 1

    def find_mag_word(self, word):
        if word in self.magazine_words:
            if self.magazine_words[word] > 0:
                self.valid = True
                self.magazine_words[word] -= 1
            else:
                self.valid = False
        else:
            self.valid = False

# this function runs the program according to the problem specification
def driver():
    with open(sys.argv[1]) as f:
        first_line = f.readline()
        n_mag = int(first_line[0])
        n_note = int(first_line[2])
        second_line = f.readline().split()
        third_line = f.readline().split()
        h = HashTable()
        for i in range(n_mag):
            h.insert_mag_word(second_line[i])
        for i in range(n_note):
            h.find_mag_word(third_line[i])
            if h.valid is False:
                print("NO")
                return -1
        if h.valid is True:
            print("YES")


if __name__ == "__main__":
    driver()
