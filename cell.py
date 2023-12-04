
class Cell:
    """
    Represents a single cell, with position only.
    """
    def __init__(self, x, y) -> None:
        self.pos_x = x
        self.pos_y = y
    
    def __repr__(self) -> str:
        return f"Cell({self.pos_x},{self.pos_y})"

    def __eq__(self, other: object) -> bool:
        return self.pos_x == other.pos_x and self.pos_y == other.pos_y
    
    def __hash__(self):
        return hash((self.pos_x, self.pos_y))

    def get_neighbours(self) -> set:
        neighbours = {
            Cell(self.pos_x + x, self.pos_y + y) 
            for x in range(-1, 2) 
            for y in range(-1, 2)
            if (x, y) != (0, 0)  # Exclude the current cell itself
        }
        return neighbours