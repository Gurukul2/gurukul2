# built_in_functions.py

from typing import List, Tuple

def demonstrate_built_in_functions():
    """
    Demonstrate the usage of various built-in Python functions.
    """
    numbers: List[int] = [4, 2, 7, 1, 8, 3]
    words: List[str] = ["apple", "banana", "cherry", "date"]

    print(f"Original list: {numbers}")
    print(f"Length of the list: {len(numbers)}")
    print(f"Maximum value: {max(numbers)}")
    print(f"Minimum value: {min(numbers)}")
    print(f"Sum of all numbers: {sum(numbers)}")
    print(f"Sorted list: {sorted(numbers)}")

    print(f"\nOriginal words: {words}")
    print(f"Sorted words: {sorted(words)}")

    # Using enumerate
    print("\nEnumerated words:")
    for index, word in enumerate(words, start=1):
        print(f"{index}. {word}")

    # Using zip
    prices: List[float] = [0.50, 0.75, 1.00, 1.25]
    print("\nFruit prices:")
    for word, price in zip(words, prices):
        print(f"{word}: ${price:.2f}")

    # Type conversion
    num_str: str = "42"
    num_int: int = int(num_str)
    num_float: float = float(num_str)
    print(f"\nString '42' converted to int: {num_int} (type: {type(num_int)})")
    print(f"String '42' converted to float: {num_float} (type: {type(num_float)})")

# Example usage
if __name__ == "__main__":
    demonstrate_built_in_functions()