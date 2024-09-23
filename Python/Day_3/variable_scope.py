# variable_scope.py

# No additional imports needed for this example

global_var = "I'm a global variable"

def demonstrate_scope():
    """
    Demonstrate the difference between local and global scope.
    """
    local_var = "I'm a local variable"
    print("Inside the function:")
    print(f"Local variable: {local_var}")
    print(f"Global variable: {global_var}")

def modify_global():
    """
    Demonstrate how to modify a global variable from within a function.
    """
    global global_var
    global_var = "I've been modified"

# Example usage
if __name__ == "__main__":
    demonstrate_scope()
    print("\nOutside the function:")
    print(f"Global variable: {global_var}")
    # This would raise an error:
    # print(f"Local variable: {local_var}")
    
    modify_global()
    print("\nAfter modifying global variable:")
    print(f"Global variable: {global_var}")