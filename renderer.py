from cell import Cell

class Renderer:
    """
    Render the live cells to terminal.
    Currently has a very simple rendering using print().
    The next step would be to use curses to render the cells in-place instead of scrolling.
    """

    def __init__(self) -> None:
        self.x_max = 0
        self.x_min = 0

        self.y_max = 0
        self.y_min = 0

    def render(self, live_cells: set[Cell]) -> None:
        x_max = max(cell.pos_x for cell in live_cells)
        x_min = min(cell.pos_x for cell in live_cells)
        y_max = max(cell.pos_y for cell in live_cells)
        y_min = min(cell.pos_y for cell in live_cells)

        self.x_max = max(self.x_max, x_max)
        self.x_min = min(self.x_min, x_min)
        self.y_max = max(self.y_max, y_max)
        self.y_min = min(self.y_min, y_min)
      

        for y in range(self.y_min - 1, self.y_max + 1):
            for x in range(self.x_min - 1, self.x_max +1):
                if Cell(x, y) in live_cells:
                    print('*', end=' ')
                else:
                    print(' ', end=' ')
            print()  # Print a newline to move to the next line after each row
