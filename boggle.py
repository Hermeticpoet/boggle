from string import ascii_uppercase
from random import choice

def make_grid(width, height):
    """
    Creates a grid that will hold all of the tiles for a 
    boggle game
    """
    return {(row, col): choice(ascii_uppercase) 
        for row in range(height)
        for col in range(width)}

def neighbours_of_position(coords):
    """
    Get neighbours of a given position
    """
    row = coords[0]
    col = coords[1]
    
    # Assign each of the neighbours
    
    # Top-Left to Top-Right
    top_left = (row - 1, col - 1)
    top_center = (row - 1, col)
    top_right = (row - 1, col + 1)
    
    # Left to Right
    left = (row, col - 1)
    right = (row, col + 1)
    
    # Bottom-Left to Bottom-Right
    bottom_left = (row + 1, col - 1)
    bottom_center = (row + 1, col)
    bottom_right = (row + 1, col + 1)
    
    return [top_left, top_center, top_right,
            left, right,
            bottom_left, bottom_center, bottom_right]
    
    
    