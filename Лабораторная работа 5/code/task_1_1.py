import random

class RandomNumberIterator:
    def __init__(self,lst):
        self.min, self.max, self.size = lst
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter < self.size:
            self.counter += 1
            return random.randint(self.min, self.max)
        else:
            raise StopIteration
    
def main():
    generator = RandomNumberIterator([2,4,5])
    for number in generator:
        print(number)

main()