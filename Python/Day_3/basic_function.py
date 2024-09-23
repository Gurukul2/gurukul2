# function_basics.py

# No additional imports needed for this example

def greet(name):
    """
    A simple function to greet a person.
    
    Args:
    name (str): The name of the person to greet.
    
    Returns:
    str: A greeting message.
    """
    return f"Hello, {name}! Welcome to Python functions."

def add_numbers(a, b):
    """
    Add two numbers and return the result.
    
    Args:
    a (int or float): The first number.
    b (int or float): The second number.
    
    Returns:
    int or float: The sum of a and b.
    """
    return a + b

# Example usage
if __name__ == "__main__":
    print(greet("Alice"))
    result = add_numbers(5, 3)
    print(f"5 + 3 = {result}")