# return_statements.py

from typing import Tuple, Dict

def calculate_rectangle_properties(length: float, width: float) -> Tuple[float, float]:
    """
    Calculate the area and perimeter of a rectangle.
    
    Args:
    length (float): The length of the rectangle.
    width (float): The width of the rectangle.
    
    Returns:
    tuple: A tuple containing the area and perimeter.
    """
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter

def get_user_status(user_id: int) -> Dict[str, any]:
    """
    Get the status of a user.
    
    Args:
    user_id (int): The ID of the user.
    
    Returns:
    dict: A dictionary containing user status information.
    """
    # This is a mock function. In a real application, you'd fetch this from a database.
    return {
        "user_id": user_id,
        "is_active": True,
        "last_login": "2023-09-15 14:30:00"
    }

# Example usage
if __name__ == "__main__":
    rect_area, rect_perimeter = calculate_rectangle_properties(5, 3)
    print(f"Rectangle - Area: {rect_area}, Perimeter: {rect_perimeter}")
    
    user_status = get_user_status(12345)
    print("User Status:", user_status)