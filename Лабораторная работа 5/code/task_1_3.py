def fibonacci_generator(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

def add_ten_generator(fib_gen):
    for number in fib_gen:
        yield number + 10

def main():
    count = 10

    fib_gen = fibonacci_generator(count)

    fib_with_ten_gen = add_ten_generator(fib_gen)

    for num in fib_with_ten_gen:
        print(num)

if __name__ == "__main__":
    main()