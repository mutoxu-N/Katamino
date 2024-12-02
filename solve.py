from pprint import pprint
from minos import MINOS, F, I, L, N, P, T, U, V, W, X, Y, Z, Mino
from copy import deepcopy


def solve(
        width: int,
        height: int,
        uses: list[bool],
) -> list:
    # check board size
    if width * height % 5 != 0:
        return (False, None)

    cnt = 0
    for use in uses:
        if use:
            cnt += 1

    if width*height > cnt*5:
        return (False, None)

    board = [[-1]*width for _ in [None]*height]
    remains = deepcopy(MINOS)

    for use in range(len(uses)):
        if not uses[use]:
            remains[use].clear()

    # solve
    board = put(board, remains, 0, 0, 0, width*height//5)

    return (board is not None, board)


def print_board(board):
    m = {
        -1: "_",
        F: "F",
        I: "I",
        L: "L",
        N: "N",
        P: "P",
        T: "T",
        U: "U",
        V: "V",
        W: "W",
        X: "X",
        Y: "Y",
        Z: "Z",
    }
    for bs in board:
        for b in bs:
            print(m[b], end=" ")
        print()

    print()


def put(board, remains, start_x, start_y, depth, max_depth):

    if depth == max_depth:
        return board

    empty_x, empty_y = [-1]*2

    for y in range(start_y, len(board)):
        if board[y][start_x] != -1:
            continue

        empty_x, empty_y = start_x, y
        break

    if empty_x == -1:
        for x in range(start_x+1, len(board[0])):
            f = False
            for y in range(len(board)):
                if board[y][x] != -1:
                    continue

                empty_x, empty_y = x, y
                f = True
                break

            if f:
                break

    if empty_x == -1 or empty_y == -1:
        print("Empty cell not found!")
        return None

    for i in range(len(remains)):
        remain = remains[i]

        for mino in remain:
            new_board = deepcopy(board)

            if mino.can_place(new_board, empty_x, empty_y):
                mino.place(new_board, empty_x, empty_y)

                new_remains = deepcopy(remains)
                new_remains[i].clear()

                res = put(new_board, new_remains, empty_x,
                          empty_y, depth+1, max_depth)
                if res is not None:
                    return res
    return None


if __name__ == "__main__":
    ans = solve(10, 6)
    if ans[0]:
        print_board(ans[1])
    else:
        print("No solution")
