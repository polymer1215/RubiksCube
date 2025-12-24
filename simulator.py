from console_renderer import ConsoleRenderer
from rubikscube import RubiksCube
from utils import Utils


class Simulator:
    """Simulator for Rubik's Cube operations with console rendering."""
    
    def __init__(self):
        """Initialize simulator with a new solved cube."""
        self.cube = RubiksCube()

    def console_render_cube(self):
        """Render the cube state to console with colors."""
        ConsoleRenderer.render_to_console(ConsoleRenderer.get_str_render(self.cube.state))

    def console_render_test(self):
        """Render the cube state to console with position labels (for testing)."""
        ConsoleRenderer.render_to_console(ConsoleRenderer.get_str_test_render(self.cube.state))

    def carry_move(self, move_list):
        """Execute a list of moves and render after each move.
        
        Args:
            move_list: List of move strings (e.g., ['R2', 'U', 'R', "R'", ...])
        """
        for move in move_list:
            self.cube.rotate(move)
            self.console_render_cube()

    def carry_raw(self, raw_moves):
        """Parse and execute raw move string.
        
        Args:
            raw_moves: String of moves (e.g., "R2 U R U R' U' R' U' R' U R'")
        """
        move_list = Utils.parse_raw_moves(raw_moves)
        moves = " ".join(move_list)
        print(f"enter to carry moves: {moves}")
        input()
        self.carry_move(move_list)
