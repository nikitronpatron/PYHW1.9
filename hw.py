import csv
import math
import json
import random

def generate_random_number():
    return random.randint(1, 10)

def generate_csv_file(file_name, num_rows):
    with open(file_name, mode='w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        for _ in range(num_rows):
            row = [generate_random_number() for _ in range(3)]
            csv_writer.writerow(row)

def solve_quadratic_equation(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return root1, root2
    elif discriminant == 0:
        root = -b / (2*a)
        return root
    else:
        return None

def save_to_json(json_file_name):
    def decorator(func):
        def wrapper(*args, **kwargs):
            results = {}
            params = {"args": args, "kwargs": kwargs}
            try:
                result = func(*args, **kwargs)
                results["result"] = result
                print(f"Результат для коэффициентов {args}: {result}")
            except Exception as e:
                results["error"] = str(e)
            results.update(params)

            with open(json_file_name, 'a') as json_file:
                json.dump(results, json_file, indent=4)

        return wrapper
    return decorator

def find_roots_from_csv(csv_file_name):
    def decorator(func):
        def wrapper(*args, **kwargs):
            with open(csv_file_name, mode='r') as csv_file:
                csv_reader = csv.reader(csv_file)
                for row in csv_reader:
                    if len(row) != 3:
                        print("Ошибка: строка в файле CSV должна содержать три числа.")
                        continue
                    a, b, c = map(int, row)
                    func(a, b, c)
        return wrapper
    return decorator

csv_file_name = 'random_numbers.csv'
num_rows = random.randint(100, 1000)

@find_roots_from_csv(csv_file_name)
@save_to_json('results.json')
def find_roots(a, b, c):
    return solve_quadratic_equation(a, b, c)

if __name__ == "__main__":
    generate_csv_file(csv_file_name, num_rows)
    find_roots()
