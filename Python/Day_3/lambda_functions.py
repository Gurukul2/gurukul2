# lambda_functions.py

from typing import List, Dict

# Simple lambda function
square = lambda x: x ** 2

# Lambda function with multiple arguments
multiply = lambda x, y: x * y

# Using lambda with built-in functions
numbers: List[int] = [1, 2, 3, 4, 5]
squared_numbers: List[int] = list(map(lambda x: x**2, numbers))

# Using lambda with sorting
people: List[Dict[str, any]] = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35}
]
sorted_people: List[Dict[str, any]] = sorted(people, key=lambda x: x["age"])

# Example usage
if __name__ == "__main__":
    print(f"Square of 5: {square(5)}")
    print(f"4 * 6 = {multiply(4, 6)}")
    print(f"Squared numbers: {squared_numbers}")
    print("Sorted people by age:")
    for person in sorted_people:
        print(f"{person['name']}: {person['age']}")