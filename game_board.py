from cell import Cell

class GameBoard:
    """
    Keep and update the game state
    """

    def __init__(self, cells: set[Cell]) -> None:
        self.live_cells = cells

    def game_step(self) -> None:
        cells_to_kill = self.get_cells_to_kill()
        cells_to_ressurect = self.get_cells_to_ressurect()
        
        self.live_cells.difference_update(cells_to_kill)
        self.live_cells.update(cells_to_ressurect)

    def get_cells_to_kill(self) -> set[Cell]:
        return {
            live_cell for live_cell in self.live_cells 
            if self.live_neighbours_count(live_cell) < 2
            or  self.live_neighbours_count(live_cell) > 3
        }
    
    def get_cells_to_ressurect(self) -> set[Cell]:
        all_neighbors = set()
        for live_cell in self.live_cells:
            all_neighbors.update(live_cell.get_neighbours())
        dead_neighbors = all_neighbors - self.live_cells

        return {
            dead_neighbor for dead_neighbor in dead_neighbors
            if self.live_neighbours_count(dead_neighbor) == 3
        }

    def live_neighbours_count(self, cell: Cell) -> int:
        result = sum(1 for neighbor in cell.get_neighbours() if self.cell_is_alive(neighbor))
        return result
    
    def cell_is_alive(self, cell: Cell) -> bool:
        is_alive = cell in self.live_cells
        return is_alive
