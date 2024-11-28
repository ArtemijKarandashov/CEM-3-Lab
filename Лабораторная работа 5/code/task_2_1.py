from time import perf_counter

def fib_gen(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

class Timer:
    def __init__(self):
        self.start = None
        self.end = None

    def __enter__(self):
        self.start = perf_counter()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.end = perf_counter()
        self.total = self.end - self.start
        print(f"Estimated time: {self.total} seconds")

def main():
    with Timer():
        fib = fib_gen(1000000)

if __name__ == "__main__":
    main()
