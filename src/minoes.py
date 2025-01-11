from copy import deepcopy

F = 0
I = 1
L = 2
N = 3
P = 4
T = 5
U = 6
V = 7
W = 8
X = 9
Y = 10
Z = 11


class Mino:
    def __init__(self, width, height, type, coords):
        """
        Initialize a Mino object with given width, height, type and coordinates.

        :param width: The width of the Mino.
        :type width: int
        :param height: The height of the Mino.
        :type height: int
        :param type: The type of the Mino.
        :type type: int
        :param coords: The coordinates of the Mino.
        :type coords: list[list[int]]
        """
        self.width = width
        self.height = height
        self.type = type
        self.coords = coords

    def can_place(self, board, x, y):
        """
        Check if the Mino can be placed on the board at the specified position.

        This method verifies whether the Mino, represented by its coordinates, can be placed
        on the board at position (x, y) without overlapping any existing pieces or going
        out of bounds.

        :param board: The current state of the board.
        :type board: list[list[int]]
        :param x: The x-coordinate on the board where the Mino is to be placed.
        :type x: int
        :param y: The y-coordinate on the board where the Mino is to be placed.
        :type y: int
        :return: True if the Mino can be placed at the specified position, False otherwise.
        :rtype: bool
        """
        if x + self.width >= len(board[0]) or y + self.height - self.coords[0][1] >= len(board) or y - self.coords[0][1] < 0:
            return False

        for i in range(5):
            nx = x + self.coords[i][0] - self.coords[0][0]
            ny = y + self.coords[i][1] - self.coords[0][1]
            if board[ny][nx] != -1:
                return False

        return True

    def place(self, board, x, y):
        """
        Place the Mino on the board at the specified position.

        This method places the Mino, represented by its coordinates, on the board at position (x, y).

        :param board: The current state of the board.
        :type board: list[list[int]]
        :param x: The x-coordinate on the board where the Mino is to be placed.
        :type x: int
        :param y: The y-coordinate on the board where the Mino is to be placed.
        :type y: int
        """
        for i in range(5):
            nx = x + self.coords[i][0] - self.coords[0][0]
            ny = y + self.coords[i][1] - self.coords[0][1]
            board[ny][nx] = self.type


def rot(shape):
    for s in shape:
        s[0], s[1] = s[1], -s[0]

    x = 100
    y = 100
    for s in shape:
        x = min(x, s[0])
        y = min(y, s[1])

    for s in shape:
        s[0] -= x
        s[1] -= y


def flip(shape):
    for s in shape:
        s[0] = -s[0]

    x = 100
    y = 100
    for s in shape:
        x = min(x, s[0])
        y = min(y, s[1])

    for s in shape:
        s[0] -= x
        s[1] -= y


MINOES = [[] for _ in range(12)]


def f(shape, pos, t):
    if pos[0]:
        MINOES[t].append(Mino(
            max(s[0] for s in shape),
            max(s[1] for s in shape),
            t,
            sorted(deepcopy(shape)),
        ))

    for i in range(1, 4):
        rot(shape)
        if pos[i]:
            MINOES[t].append(Mino(
                max(s[0] for s in shape),
                max(s[1] for s in shape),
                t,
                sorted(deepcopy(shape)),

            ))

    flip(shape)
    for i in range(4, 8):
        if pos[i]:
            MINOES[t].append(Mino(
                max(s[0] for s in shape),
                max(s[1] for s in shape),
                t,
                sorted(deepcopy(shape)),
            ))
        rot(shape)


mino_f = [
    [0, 2], [1, 0], [1, 1], [1, 2], [2, 1],
]
f(mino_f, [True]*8, F)


mino_i = [
    [0, 0], [0, 1], [0, 2], [0, 3], [0, 4],
]
f(mino_i, [True]*2 + [False]*6, I)

mino_l = [
    [0, 0], [0, 1], [0, 2], [0, 3], [1, 0]
]
f(mino_l, [True]*8, L)

mino_n = [
    [0, 0], [0, 1], [0, 2], [1, 2], [1, 3]
]
f(mino_n, [True]*8, N)

mino_p = [
    [0, 0], [0, 1], [0, 2], [1, 1], [1, 2]
]
f(mino_p, [True]*8, P)

mino_t = [
    [0, 2], [1, 1], [1, 2], [1, 0], [2, 2]
]
f(mino_t, [True]*4 + [False]*4, T)

mino_u = [
    [0, 0], [0, 1], [1, 0], [2, 0], [2, 1]
]
f(mino_u, [True]*4 + [False]*4, U)

mino_v = [
    [0, 0], [0, 1], [0, 2], [1, 0], [2, 0]
]
f(mino_v, [True]*4 + [False]*4, V)

mino_x = [
    [0, 1], [1, 0], [1, 1], [1, 2], [2, 1]
]
f(mino_x, [True] + [False]*7, X)

mino_w = [
    [0, 1], [0, 2], [1, 0], [1, 1], [2, 0]
]
f(mino_w, [True]*4 + [False]*4, W)

mino_y = [
    [0, 2], [1, 0], [1, 1], [1, 2], [1, 3]
]
f(mino_y, [True]*8, Y)

mino_z = [
    [0, 2], [1, 0], [1, 1], [1, 2], [2, 0]
]
f(mino_z, [True, True, False, False] * 2, Z)

if __name__ == "__main__":
    print(MINOES[I][0].width, MINOES[I][0].height, MINOES[I][0].coords)
    print(MINOES[I][1].width, MINOES[I][1].height, MINOES[I][1].coords)
