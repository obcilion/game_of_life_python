from game_board import GameBoard
from cell import Cell
from renderer import Renderer
import typer
import time

def main(start_state_name: str):
    game_board = GameBoard(get_start_state(start_state_name))
    renderer = Renderer()

    while(True):
        renderer.render(game_board.live_cells)
        game_board.game_step()
        time.sleep(0.25)
    
   
def get_start_state(start_state_name: str) -> set[Cell]:
    match start_state_name:
        case "blinker":
            return blinker_start_state()
        case "penta-decathlon":
            return penta_decathlon_start_state()
        case "acorn":
            return acorn_start_state()
        case "diehard":
            return diehard_start_state()
        case _:
            raise ValueError(f"start state {start_state_name} not found")

def blinker_start_state() -> set[Cell]:
    return{
        Cell(-1, 0),
        Cell(0, 0),
        Cell(1, 0)
    }

def acorn_start_state() -> set[Cell]:
    return {
        Cell(0, 0),
        Cell(1, 0),
        Cell(1, 2),
        Cell(3, 1),
        Cell(4, 0),
        Cell(5, 0),
        Cell(6, 0),
    }

def diehard_start_state() -> set[Cell]:
    return {
        Cell(6, 0),
        Cell(0, 1),
        Cell(1, 1),
        Cell(1, 2),
        Cell(5, 2),
        Cell(6, 2),
        Cell(7, 2),
    }

def penta_decathlon_start_state() -> set[Cell]:
    return {
        # - Top row -
        Cell(2, 0),
        Cell(7, 0),

        # - Middle row -
        Cell(0, 1),
        Cell(1, 1),
        # 2 is blank
        Cell(3, 1),
        Cell(4, 1),
        Cell(5, 1),
        Cell(6, 1),
        # 7 is blank
        Cell(8, 1),
        Cell(9, 1),

        # - Bottom row -
        Cell(2, 2),
        Cell(7, 2),
    }

if __name__ == '__main__':
    typer.run(main)