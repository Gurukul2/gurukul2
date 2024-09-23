# advanced_function_concepts.py

import time
from typing import Callable, Any

def print_args(*args: Any, **kwargs: Any) -> None:
    """
    Demonstrate the usage of *args and **kwargs.
    
    Args:
    *args: Variable number of positional arguments.
    **kwargs: Variable number of keyword arguments.
    """
    print("Positional arguments:")
    for arg in args:
        print(f"- {arg}")
    
    print("\nKeyword arguments:")
    for key, value in kwargs.items():
        print(f"- {key}: {value}")

def timer_decorator(func: Callable) -> Callable:
    """
    A decorator that measures the execution time of a function.
    
    Args:
    func (callable): The function to be decorated.
    
    Returns:
    callable: The wrapped function.
    """
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} executed in {end_time - start_time:.4f} seconds")
        return result
    return wrapper

@timer_decorator
def slow_function() -> None:
    """A function that simulates a time-consuming operation."""
    time.sleep(2)
    print("Slow operation completed")

# Example usage
if __name__ == "__main__":
    print_args(1, 2, 3, name="Alice", age=30, job="Developer")
    
    print("\nExecuting slow_function with timer decorator:")
    slow_function()