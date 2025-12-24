import re


class Utils:
    """Utility functions for Rubik's Cube operations."""
    
    @staticmethod
    def parse_raw_moves(raw_moves):
        """Parse raw move string into list of individual moves.
        
        Handles standard Rubik's Cube notation including:
        - Basic moves: R, U, F, D, L, B
        - Wide moves: r, u, f, d, l, b (or Rw, Uw, etc.)
        - Slice moves: M, E, S
        - Cube rotations: x, y, z
        - Modifiers: ' (prime/counter-clockwise), 2 (double turn)
        
        Args:
            raw_moves: String of moves (e.g., "R2 U R U R' U' R' U' R' U R'")
            
        Returns:
            List of individual move strings (e.g., ['R2', 'U', 'R', ...])
        """
        # 映射 Uw → u, Rw → r 等
        raw_moves = raw_moves.replace("Uw", "u").replace("Dw", "d").replace("Rw", "r")
        raw_moves = raw_moves.replace("Lw", "l").replace("Fw", "f").replace("Bw", "b")
        # 匹配：一个字母 + 可选的 ' 或 2
        move_list = re.findall(r"[rufdlbRUFDLBMESxyz][2']?", raw_moves)
        return move_list

    @staticmethod
    def rotate_clockwise(matrix):
        """Rotate a 3x3 matrix 90 degrees clockwise.
        
        Args:
            matrix: List of 9 elements representing a 3x3 grid (row-major order)
            
        Returns:
            Rotated list with elements in new positions
            
        Example:
            [0, 1, 2,    [6, 3, 0,
             3, 4, 5, →   7, 4, 1,
             6, 7, 8]     8, 5, 2]
        """
        # 新索引位置 [6,3,0,7,4,1,8,5,2] 对应原位置索引
        return [
            matrix[6], matrix[3], matrix[0],
            matrix[7], matrix[4], matrix[1],
            matrix[8], matrix[5], matrix[2]
        ]