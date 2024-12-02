
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
        self.width = width
        self.height = height
        self.type = type
        self.coords = coords

    def can_place(self, board, x, y):
        if x + self.width >= len(board[0]) or y + self.height - self.coords[0][1] >= len(board) or y - self.coords[0][1] < 0:
            return False

        for i in range(5):
            nx = x + self.coords[i][0] - self.coords[0][0]
            ny = y + self.coords[i][1] - self.coords[0][1]
            if board[ny][nx] != -1:
                return False

        return True

    def place(self, board, x, y):
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


MINOS = [[] for _ in range(12)]


def f(shape, pos, t):
    if pos[0]:
        MINOS[t].append(Mino(
            max(s[0] for s in shape),
            max(s[1] for s in shape),
            t,
            sorted(deepcopy(shape)),
        ))

    for i in range(1, 4):
        rot(shape)
        if pos[i]:
            MINOS[t].append(Mino(
                max(s[0] for s in shape),
                max(s[1] for s in shape),
                t,
                sorted(deepcopy(shape)),

            ))

    flip(shape)
    for i in range(4, 8):
        if pos[i]:
            MINOS[t].append(Mino(
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
    print(MINOS[I][0].width, MINOS[I][0].height, MINOS[I][0].coords)
    print(MINOS[I][1].width, MINOS[I][1].height, MINOS[I][1].coords)
