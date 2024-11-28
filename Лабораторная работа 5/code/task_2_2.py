from calculator import calc
from time import perf_counter

class CalcManager:
    def __init__(self, filename, args, oper, tolerance):
        self.filename = filename
        self.data = args
        self.oper = oper
        self.tolerance = tolerance
        self.status = "FAILED"
    
    def __enter__(self):
        self.start = perf_counter()
        self.file = open(self.filename, 'a')

        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        self.end = perf_counter()
        self.total = self.end - self.start
        print(f"Status: {self.status} \nEstimated time: {self.total} seconds")
        self.file.write(f"\nInput: {self.data}, {self.oper}\nStatus: {self.status}\nEstimated time: {self.total} seconds\n")
        self.file.close()

def main():
    calc_args = [100, 2]
    calc_kwargs = {'oper': '/', 'tolerance': 0.1}

    calc_manager = CalcManager(
        filename='calc.log',
        args=calc_args,
        oper=calc_kwargs['oper'],
        tolerance=calc_kwargs['tolerance']
    )

    with calc_manager:    
        result = calc(*calc_manager.data, oper = calc_manager.oper, tolerance = calc_manager.tolerance)
        if result is not None:
            calc_manager.status = "SUCCESS"
            print(f"Result: {result}")

if __name__ == '__main__':
    main()