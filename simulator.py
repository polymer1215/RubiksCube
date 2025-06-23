from console_renderer import ConsoleRenderer
from rubikscube import RubiksCube
from utils import Utils

class Simulator:
    def __init__(self):
        self.cube = RubiksCube()

    def console_render_cube(self):
        ConsoleRenderer.render_to_console(ConsoleRenderer.get_str_render(self.cube.state))

    def console_render_test(self):
        ConsoleRenderer.render_to_console(ConsoleRenderer.get_str_test_render(self.cube.state))

    def carry_move(self, move_list):
        # example: move_list = ['R2', 'U', 'R', 'U', "R'", "U'", "R'", "U'", "R'", 'U', "R'"]
        for move in move_list:
            self.cube.rotate(move)
            self.console_render_cube()

    def carry_raw(self, raw_moves):
        move_list = Utils.parse_raw_moves(raw_moves)
        moves = ""
        for move in move_list:
            moves += str(move) + " "
        print(f"enter to carry moves: {moves}")
        input()
        self.carry_move(move_list)
