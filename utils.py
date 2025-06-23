import re


class Utils:
    @staticmethod
    def parse_raw_moves(raw_moves):
        # 映射 Uw → u, Rw → r 等
        raw_moves = raw_moves.replace("Uw", "u").replace("Dw", "d").replace("Rw", "r")
        raw_moves = raw_moves.replace("Lw", "l").replace("Fw", "f").replace("Bw", "b")
        # 匹配：一个字母 + 可选的 ' 或 2
        move_list = re.findall(r"[rufdlbRUFDLBMESxyz][2']?", raw_moves)
        return move_list
        # example:
        # raw_moves = "R2 U R U R' U' R' U' R' U R'"
        # move_list = ['R2', 'U', 'R', 'U', "R'", "U'", "R'", "U'", "R'", 'U', "R'"]

    @staticmethod
    def rotate_clockwise(matrix):
        """顺时针旋转90度"""
        # 新索引位置 [6,3,0,7,4,1,8,5,2] 对应原位置索引
        return [
            matrix[6], matrix[3], matrix[0],
            matrix[7], matrix[4], matrix[1],
            matrix[8], matrix[5], matrix[2]
        ]