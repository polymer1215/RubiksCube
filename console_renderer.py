class ConsoleRenderer:
    """Renderer for displaying Rubik's Cube state in console with colors."""
    
    COLOR_MAP = {
        'W': '\033[97m',   # White
        'O': '\033[38;5;214m',  # Orange
        'G': '\033[92m',   # Green
        'R': '\033[91m',   # Red
        'B': '\033[94m',   # Blue
        'Y': '\033[93m',   # Yellow
        'T': '\033[90m',   # Test color
    }
    RESET = '\033[0m'
    FACE_SEPARATOR = ' '  # Placeholder for spacing between faces
    FACE_SPACING = '  '   # Actual double space between faces
    FACE_INDENT = "       "  # Indentation for U and D faces
    MIDDLE_FACES = ['L', 'F', 'R', 'B']  # Faces displayed in middle row
    
    @staticmethod
    def colorize(color_code):
        """Return ANSI color code for given color."""
        return ConsoleRenderer.COLOR_MAP.get(color_code, ConsoleRenderer.RESET)
    
    @staticmethod
    def format_cell(color_code):
        """Format a single cell with color."""
        return f"{ConsoleRenderer.colorize(color_code)}{color_code}{ConsoleRenderer.RESET}"
    
    @staticmethod
    def format_row(cells, indent=""):
        """Format a row of cells with optional indentation."""
        formatted_cells = [ConsoleRenderer.format_cell(cell) for cell in cells]
        return f"{indent}{' '.join(formatted_cells)}\n"
    
    @staticmethod
    def format_face(face, indent=""):
        """Format a 3x3 face with optional indentation."""
        result = ""
        for i in range(3):
            row_start = i * 3
            result += ConsoleRenderer.format_row(face[row_start:row_start + 3], indent)
        return result

    @staticmethod
    def get_str_render(state):
        """Generate colored string representation of the cube.
        
        Args:
            state: Dictionary with cube state for faces U, L, F, R, B, D
            
        Returns:
            String representation of the cube with ANSI colors
        """
        result = ""
        
        # Upper face (U) - indented
        result += ConsoleRenderer.format_face(state['U'], ConsoleRenderer.FACE_INDENT)
        
        # Middle section - L, F, R, B side by side
        for i in range(3):
            row_cells = []
            for idx, face in enumerate(ConsoleRenderer.MIDDLE_FACES):
                row_start = i * 3
                row_cells.extend(state[face][row_start:row_start + 3])
                # Add spacing between faces except after last
                if idx < len(ConsoleRenderer.MIDDLE_FACES) - 1:
                    row_cells.append(ConsoleRenderer.FACE_SEPARATOR)
            
            # Format with proper spacing
            formatted = []
            for cell in row_cells:
                if cell == ConsoleRenderer.FACE_SEPARATOR:
                    formatted.append(ConsoleRenderer.FACE_SPACING)
                else:
                    formatted.append(ConsoleRenderer.format_cell(cell))
            result += f"{''.join(formatted)}\n"
        
        # Lower face (D) - indented
        result += ConsoleRenderer.format_face(state['D'], ConsoleRenderer.FACE_INDENT)
        
        return result

    @staticmethod
    def get_str_test_render(state):
        """Generate labeled string representation of the cube for testing.
        
        Args:
            state: Dictionary with cube state for faces U, L, F, R, B, D
            
        Returns:
            String representation with position labels (e.g., U0, U1, ...)
        """
        # Create labeled faces
        labeled_state = {}
        for face_name in ['U', 'L', 'F', 'R', 'B', 'D']:
            labeled_state[face_name] = [f"{face_name}{i}" for i in range(9)]

        result = ""

        # Upper face (U) - indented
        for i in range(3):
            row_start = i * 3
            row = labeled_state['U'][row_start:row_start + 3]
            result += f"       {' '.join(row)}\n"

        # Middle section - L, F, R, B side by side
        for i in range(3):
            row_parts = []
            for face in ['L', 'F', 'R', 'B']:
                row_start = i * 3
                row = labeled_state[face][row_start:row_start + 3]
                row_parts.append(' '.join(row))
            result += f"{row_parts[0]}   {row_parts[1]}   {row_parts[2]}   {row_parts[3]}\n"

        # Lower face (D) - indented
        for i in range(3):
            row_start = i * 3
            row = labeled_state['D'][row_start:row_start + 3]
            result += f"       {' '.join(row)}\n"

        return result

    @staticmethod
    def render_to_console(content):
        """Print content to console."""
        print(f"{content}\n")