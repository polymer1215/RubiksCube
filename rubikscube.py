from utils import Utils


class RubiksCube:
    """Rubik's Cube simulator class that manages cube state and rotations."""
    
    # Rotation configuration: (face_letters, position_indices) for each move
    ROTATION_CONFIGS = {
        'R': (['U', 'B', 'D', 'F'], [8, 5, 2, 0, 3, 6, 8, 5, 2, 8, 5, 2]),
        'U': (['F', 'L', 'B', 'R'], [2, 1, 0, 2, 1, 0, 2, 1, 0, 2, 1, 0]),
        'F': (['U', 'R', 'D', 'L'], [6, 7, 8, 0, 3, 6, 2, 1, 0, 5, 8, 2]),
        'L': (['U', 'F', 'D', 'B'], [0, 3, 6, 0, 3, 6, 0, 3, 6, 8, 5, 2]),
        'B': (['U', 'L', 'D', 'R'], [2, 1, 0, 0, 3, 6, 6, 7, 8, 8, 5, 2]),
        'D': (['F', 'R', 'B', 'L'], [6, 7, 8, 6, 7, 8, 6, 7, 8, 6, 7, 8]),
        'E': (['F', 'R', 'B', 'L'], [3, 4, 5, 3, 4, 5, 3, 4, 5, 3, 4, 5]),
        'M': (['U', 'F', 'D', 'B'], [1, 4, 7, 1, 4, 7, 1, 4, 7, 7, 4, 1]),
        'S': (['U', 'R', 'D', 'L'], [3, 4, 5, 1, 4, 7, 5, 4, 3, 7, 4, 1]),
    }
    
    def __init__(self):
        """Initialize a solved Rubik's Cube."""
        # 每个面一个 9 元素列表，顺序为：上(U)、左(L)、前(F)、右(R)、后(B)、下(D)
        self.state = {
            'U': ['W'] * 9,  # White - Up
            'L': ['O'] * 9,  # Orange - Left
            'F': ['G'] * 9,  # Green - Front
            'R': ['R'] * 9,  # Red - Right
            'B': ['B'] * 9,  # Blue - Back
            'D': ['Y'] * 9,  # Yellow - Down
        }

    def rotate(self, move):
        """Parse and execute rotation instruction.
        
        Args:
            move: Rotation notation (e.g., 'R', "R'", 'R2', 'U', etc.)
        """
        times = 1  # 默认旋转一次

        # 检查是否包含单引号
        if "'" in move:
            times = 3  # Counter-clockwise = 3x clockwise
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
        """Rotate a single face 90 degrees clockwise."""
        new_face = Utils.rotate_clockwise(self.state[face])
        self.state[face] = new_face

    def rotate_single_ring(self, indice_letter_list, indice_number_list):
        """Rotate the ring of colors around the cube edges.
        
        Args:
            indice_letter_list: List of 4 face letters (e.g., ['U', 'B', 'D', 'F'])
            indice_number_list: List of 12 position indices for the ring
            
        Example:
            indice_letter_list = ['U', 'B', 'D', 'F']
            indice_number_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
            new_indice_number_list = [9, 10, 11, 0, 1, 2, 3, 4, 5, 6, 7, 8]
        """
        # Rotate indices and letters by one position
        new_indice_number_list = indice_number_list[3:] + indice_number_list[:3]
        new_indice_letter_list = indice_letter_list[1:] + indice_letter_list[:1]

        # Extract current colors from the ring
        color_list = []
        count = 0
        for i in range(4):
            indice_letter = indice_letter_list[i]
            for j in range(3):
                color_list.append(self.state[indice_letter][indice_number_list[count]])
                count += 1

        # Place colors in new positions
        count = 0
        for i in range(4):
            new_indice_letter = new_indice_letter_list[i]
            new_colors = self.state[new_indice_letter]
            for j in range(3):
                new_colors[new_indice_number_list[count]] = color_list[count]
                count += 1
            self.state[new_indice_letter] = new_colors

    def rotate_R(self):
        """Rotate right face clockwise."""
        self.rotate_single_face('R')
        faces, indices = self.ROTATION_CONFIGS['R']
        self.rotate_single_ring(faces, indices)

    def rotate_U(self):
        """Rotate upper face clockwise."""
        self.rotate_single_face('U')
        faces, indices = self.ROTATION_CONFIGS['U']
        self.rotate_single_ring(faces, indices)

    def rotate_F(self):
        """Rotate front face clockwise."""
        self.rotate_single_face('F')
        faces, indices = self.ROTATION_CONFIGS['F']
        self.rotate_single_ring(faces, indices)

    def rotate_L(self):
        """Rotate left face clockwise."""
        self.rotate_single_face('L')
        faces, indices = self.ROTATION_CONFIGS['L']
        self.rotate_single_ring(faces, indices)

    def rotate_B(self):
        """Rotate back face clockwise."""
        self.rotate_single_face('B')
        faces, indices = self.ROTATION_CONFIGS['B']
        self.rotate_single_ring(faces, indices)

    def rotate_D(self):
        """Rotate down face clockwise."""
        self.rotate_single_face('D')
        faces, indices = self.ROTATION_CONFIGS['D']
        self.rotate_single_ring(faces, indices)

    def rotate_E(self):
        """Rotate middle layer (horizontal, between U and D) like D."""
        faces, indices = self.ROTATION_CONFIGS['E']
        self.rotate_single_ring(faces, indices)

    def rotate_M(self):
        """Rotate middle layer (vertical, between L and R) like L."""
        faces, indices = self.ROTATION_CONFIGS['M']
        self.rotate_single_ring(faces, indices)

    def rotate_S(self):
        """Rotate middle layer (between F and B) like F."""
        faces, indices = self.ROTATION_CONFIGS['S']
        self.rotate_single_ring(faces, indices)

    def rotate_r(self):
        """Rotate right face and middle layer (wide move)."""
        self.rotate_R()
        for i in range(3):
            self.rotate_M()

    def rotate_u(self):
        """Rotate upper face and middle layer (wide move)."""
        self.rotate_U()
        for i in range(3):
            self.rotate_E()

    def rotate_f(self):
        """Rotate front face and middle layer (wide move)."""
        self.rotate_F()
        self.rotate_S()

    def rotate_l(self):
        """Rotate left face and middle layer (wide move)."""
        self.rotate_L()
        self.rotate_M()

    def rotate_b(self):
        """Rotate back face and middle layer (wide move)."""
        self.rotate_B()
        for i in range(3):
            self.rotate_S()

    def rotate_d(self):
        """Rotate down face and middle layer (wide move)."""
        self.rotate_D()
        self.rotate_E()

    def rotate_x(self):
        """Rotate entire cube on R axis."""
        self.rotate_r()
        for i in range(3):
            self.rotate_L()

    def rotate_y(self):
        """Rotate entire cube on U axis."""
        self.rotate_u()
        for i in range(3):
            self.rotate_D()

    def rotate_z(self):
        """Rotate entire cube on F axis."""
        self.rotate_f()
        for i in range(3):
            self.rotate_B()