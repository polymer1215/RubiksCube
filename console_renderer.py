class ConsoleRenderer:
    @staticmethod
    def colorize(color_code):
        color_map = {
            'W': '\033[97m',  # 白色
            'O': '\033[38;5;214m',  # 橙色
            'G': '\033[92m',  # 绿色
            'R': '\033[91m',  # 红色
            'B': '\033[94m',  # 蓝色
            'Y': '\033[93m',  # 黄色
            'T': '\033[90m',  # 测试
        }
        return color_map.get(color_code, '\033[0m')

    @staticmethod
    def get_str_render(state):
        U = state['U']
        L = state['L']
        F = state['F']
        R = state['R']
        B = state['B']
        D = state['D']

        result = ""

        # 上面 (使用实际颜色代码)
        result += "       {} {} {}\n".format(
            ConsoleRenderer.colorize(U[0]) + U[0] + '\033[0m',
            ConsoleRenderer.colorize(U[1]) + U[1] + '\033[0m',
            ConsoleRenderer.colorize(U[2]) + U[2] + '\033[0m'
        )
        result += "       {} {} {}\n".format(
            ConsoleRenderer.colorize(U[3]) + U[3] + '\033[0m',
            ConsoleRenderer.colorize(U[4]) + U[4] + '\033[0m',
            ConsoleRenderer.colorize(U[5]) + U[5] + '\033[0m'
        )
        result += "       {} {} {}\n".format(
            ConsoleRenderer.colorize(U[6]) + U[6] + '\033[0m',
            ConsoleRenderer.colorize(U[7]) + U[7] + '\033[0m',
            ConsoleRenderer.colorize(U[8]) + U[8] + '\033[0m'
        )

        # 中间部分（使用实际颜色代码）
        for i in range(3):
            result += "{} {} {}   {} {} {}   {} {} {}   {} {} {}\n".format(
                ConsoleRenderer.colorize(L[i*3])   + L[i*3]   + '\033[0m',
                ConsoleRenderer.colorize(L[i*3+1]) + L[i*3+1] + '\033[0m',
                ConsoleRenderer.colorize(L[i*3+2]) + L[i*3+2] + '\033[0m',
                ConsoleRenderer.colorize(F[i*3])   + F[i*3]   + '\033[0m',
                ConsoleRenderer.colorize(F[i*3+1]) + F[i*3+1] + '\033[0m',
                ConsoleRenderer.colorize(F[i*3+2]) + F[i*3+2] + '\033[0m',
                ConsoleRenderer.colorize(R[i*3])   + R[i*3]   + '\033[0m',
                ConsoleRenderer.colorize(R[i*3+1]) + R[i*3+1] + '\033[0m',
                ConsoleRenderer.colorize(R[i*3+2]) + R[i*3+2] + '\033[0m',
                ConsoleRenderer.colorize(B[i*3])   + B[i*3]   + '\033[0m',
                ConsoleRenderer.colorize(B[i*3+1]) + B[i*3+1] + '\033[0m',
                ConsoleRenderer.colorize(B[i*3+2]) + B[i*3+2] + '\033[0m'
            )

        # 底面 (使用实际颜色代码)
        result += "       {} {} {}\n".format(
            ConsoleRenderer.colorize(D[0]) + D[0] + '\033[0m',
            ConsoleRenderer.colorize(D[1]) + D[1] + '\033[0m',
            ConsoleRenderer.colorize(D[2]) + D[2] + '\033[0m'
        )
        result += "       {} {} {}\n".format(
            ConsoleRenderer.colorize(D[3]) + D[3] + '\033[0m',
            ConsoleRenderer.colorize(D[4]) + D[4] + '\033[0m',
            ConsoleRenderer.colorize(D[5]) + D[5] + '\033[0m'
        )
        result += "       {} {} {}\n".format(
            ConsoleRenderer.colorize(D[6]) + D[6] + '\033[0m',
            ConsoleRenderer.colorize(D[7]) + D[7] + '\033[0m',
            ConsoleRenderer.colorize(D[8]) + D[8] + '\033[0m'
        )

        return result

    @staticmethod
    def get_str_test_render(state):
        U = state['U']
        L = state['L']
        F = state['F']
        R = state['R']
        B = state['B']
        D = state['D']

        # 创建带标签的面数组
        def create_labeled_face(face_name, face):
            return [f"{face_name}{i}" for i in range(9)]

        UL = create_labeled_face("U", U)
        LL = create_labeled_face("L", L)
        FL = create_labeled_face("F", F)
        RL = create_labeled_face("R", R)
        BL = create_labeled_face("B", B)
        DL = create_labeled_face("D", D)

        result = ""

        # 上面（U面）
        result += "       {} {} {}\n".format(UL[0], UL[1], UL[2])
        result += "       {} {} {}\n".format(UL[3], UL[4], UL[5])
        result += "       {} {} {}\n".format(UL[6], UL[7], UL[8])

        # 中间部分：左(L)、前(F)、右(R)、后(B)面
        for i in range(3):
            result += "{} {} {}   {} {} {}   {} {} {}   {} {} {}\n".format(
                LL[i * 3], LL[i * 3 + 1], LL[i * 3 + 2],
                FL[i * 3], FL[i * 3 + 1], FL[i * 3 + 2],
                RL[i * 3], RL[i * 3 + 1], RL[i * 3 + 2],
                BL[i * 3], BL[i * 3 + 1], BL[i * 3 + 2]
            )

        # 底面（D面）
        result += "       {} {} {}\n".format(DL[0], DL[1], DL[2])
        result += "       {} {} {}\n".format(DL[3], DL[4], DL[5])
        result += "       {} {} {}\n".format(DL[6], DL[7], DL[8])

        return result

    @staticmethod
    def render_to_console(content):
        print(f"{content}\n")