import random




def generator(lst):
    min,max,size = lst 
    for i in range(size):
        yield random.randint(min,max)

def main():
    gen = generator([1,10,5])
    print(next(gen))
    print(next(gen))
    print(next(gen))
    print(next(gen))
    print(next(gen))

main()