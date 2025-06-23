from utils import Utils


class RubiksCube:
    def __init__(self):

        self.is_test = False
        # 每个面一个 9 元素列表，顺序为：上(U)、左(L)、前(F)、右(R)、后(B)、下(D)
        if not self.is_test:
            self.state = {
                'U': ['W'] * 9,
                'L': ['O'] * 9,
                'F': ['G'] * 9,
                'R': ['R'] * 9,
                'B': ['B'] * 9,
                'D': ['Y'] * 9,
            }
        else:
            self.state = {
                'U': ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'],
                'L': ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
                'F': ['G', 'T', 'G', 'G', 'T', 'G', 'G', 'G', 'T'],
                'R': ['R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R'],
                'B': ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'],
                'D': ['Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y'],
            }

    def rotate(self, move):
        """解析并执行旋转指令"""
        times = 1  # 默认旋转一次

        # 检查是否包含单引号
        if "'" in move:
            times = 3
        # 如果没有单引号，则检查数字（如 R2）
        elif len(move) > 1 and move[1].isdigit():
            times = int(move[1])

        # 获取旋转面字母
        sign = move[0]  # 旋转标记

        # 动态获取旋转方法并调用
        rotate_method_name = f"rotate_{sign}"  # 创建方法名称，如 "rotate_R"

        # 使用 getattr 动态调用方法
        rotate_method = getattr(self, rotate_method_name, None)  # 获取方法，如果没有找到则返回 None

        # 如果方法存在，执行该方法
        if rotate_method:
            for _ in range(times):
                rotate_method()  # 调用对应的旋转方法
        else:
            print(f"Invalid move: {move}")

    def rotate_single_face(self, face):
        new_face = Utils.rotate_clockwise(self.state[face])
        self.state[face] = new_face

    def rotate_single_ring(self, indice_letter_list, indice_number_list):
        # example:
        # indice_letter_list = ['U', 'B', 'D', 'F']
        # indice_number_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        # new_indice_number_list = [9, 10, 11, 0, 1, 2, 3, 4, 5, 6, 7]

        new_indice_number_list = indice_number_list[3:] + indice_number_list[:3]
        new_indice_letter_list = indice_letter_list[1:] + indice_letter_list[:1]

        color_list = []
        count = 0
        for i in range(4):
            indice_letter = indice_letter_list[i]
            for j in range(3):
                color_list.append(self.state[indice_letter][indice_number_list[count]])
                count += 1

        count = 0
        for i in range(4):
            new_indice_letter = new_indice_letter_list[i]
            new_colors = self.state[new_indice_letter]
            for j in range(3):
                new_colors[new_indice_number_list[count]] = color_list[count]
                count += 1
            self.state[new_indice_letter] = new_colors

    def rotate_R(self):
        self.rotate_single_face('R')
        indice_letter_list_R = ['U', 'B', 'D', 'F']
        indice_number_list_R = [8, 5, 2, 0, 3, 6, 8, 5, 2, 8, 5, 2]
        self.rotate_single_ring(indice_letter_list_R, indice_number_list_R)

    def rotate_U(self):
        self.rotate_single_face('U')
        indice_letter_list_U = ['F', 'L', 'B', 'R']
        indice_number_list_U = [2, 1, 0, 2, 1, 0, 2, 1, 0, 2, 1, 0]
        self.rotate_single_ring(indice_letter_list_U, indice_number_list_U)

    def rotate_F(self):
        self.rotate_single_face('F')
        indice_letter_list_F = ['U', 'R', 'D', 'L']
        indice_number_list_F = [6, 7, 8, 0, 3, 6, 2, 1, 0, 5, 8, 2]
        self.rotate_single_ring(indice_letter_list_F, indice_number_list_F)

    def rotate_L(self):
        self.rotate_single_face('L')
        indice_letter_list_L = ['U', 'F', 'D', 'B']
        indice_number_list_L = [0, 3, 6, 0, 3, 6, 0, 3, 6, 8, 5, 2]
        self.rotate_single_ring(indice_letter_list_L, indice_number_list_L)

    def rotate_B(self):
        self.rotate_single_face('B')
        indice_letter_list_B = ['U', 'L', 'D', 'R']
        indice_number_list_B = [2, 1, 0, 0, 3, 6, 6, 7, 8, 8, 5, 2]
        self.rotate_single_ring(indice_letter_list_B, indice_number_list_B)

    def rotate_D(self):
        self.rotate_single_face('D')
        indice_letter_list_D = ['F', 'R', 'B', 'L']
        indice_number_list_D = [6, 7, 8, 6, 7, 8, 6, 7, 8, 6, 7, 8]
        self.rotate_single_ring(indice_letter_list_D, indice_number_list_D)

    def rotate_E(self):
        indice_letter_list_E = ['F', 'R', 'B', 'L']
        indice_number_list_E = [3, 4, 5, 3, 4, 5, 3, 4, 5, 3, 4, 5]
        self.rotate_single_ring(indice_letter_list_E, indice_number_list_E)

    def rotate_M(self):
        indice_letter_list_M = ['U', 'F', 'D', 'B']
        indice_number_list_M = [1, 4, 7, 1, 4, 7, 1, 4, 7, 7, 4, 1]
        self.rotate_single_ring(indice_letter_list_M, indice_number_list_M)

    def rotate_S(self):
        indice_letter_list_S = ['U', 'R', 'D', 'L']
        indice_number_list_S = [3, 4, 5, 1, 4, 7, 5, 4, 3, 7, 4, 1]
        self.rotate_single_ring(indice_letter_list_S, indice_number_list_S)

    def rotate_r(self):
        self.rotate_R()
        for i in range (3):
            self.rotate_M()

    def rotate_u(self):
        self.rotate_U()
        for i in range (3):
            self.rotate_E()

    def rotate_f(self):
        self.rotate_F()
        self.rotate_S()

    def rotate_l(self):
        self.rotate_L()
        self.rotate_M()

    def rotate_b(self):
        self.rotate_B()
        for i in range (3):
            self.rotate_S()

    def rotate_d(self):
        self.rotate_D()
        self.rotate_E()

    def rotate_x(self):
        self.rotate_r()
        for i in range (3):
            self.rotate_L()

    def rotate_y(self):
        self.rotate_u()
        for i in range (3):
            self.rotate_D()

    def rotate_z(self):
        self.rotate_f()
        for i in range (3):
            self.rotate_B()