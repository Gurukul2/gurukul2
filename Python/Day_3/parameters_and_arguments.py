# parameters_and_arguments.py

# No additional imports needed for this example

def greet(name, greeting="Hello"):
    """
    Greet a person with a custom or default greeting.
    
    Args:
    name (str): The name of the person to greet.
    greeting (str, optional): The greeting to use. Defaults to "Hello".
    
    Returns:
    str: A greeting message.
    """
    return f"{greeting}, {name}!"

def create_profile(name, age, job):
    """
    Create a user profile with the given information.
    
    Args:
    name (str): The user's name.
    age (int): The user's age.
    job (str): The user's job.
    
    Returns:
    dict: A dictionary containing the user's profile information.
    """
    return {"name": name, "age": age, "job": job}

# Example usage
if __name__ == "__main__":
    print(greet("Bob"))
    print(greet("Alice", "Good morning"))
    
    profile = create_profile(name="Charlie", age=30, job="Developer")
    print("User Profile:", profile)