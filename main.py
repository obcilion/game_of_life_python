from game_board import GameBoard
from cell import Cell
from renderer import Renderer

def main():
    game_board = GameBoard(get_blinker())
    renderer = Renderer()

    renderer.render(game_board.live_cells)
    game_board.game_step()
    renderer.render(game_board.live_cells)
    game_board.game_step()
    renderer.render(game_board.live_cells)
    game_board.game_step()
    renderer.render(game_board.live_cells)
    game_board.game_step()
   
    

def get_blinker() -> set[Cell]:
    return{
        Cell(-1, 0),
        Cell(0, 0),
        Cell(1, 0)
    }

if __name__ == '__main__':
    main()