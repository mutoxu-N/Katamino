import flet as ft
import flet.canvas as cv
from minos import F, I, L, N, P, T, U, V, W, X, Y, Z
from solve import solve

COLORS = {
    F: "#8000ff",
    I: "#0000ff",
    L: "#ffc700",
    N: "#330066",

    P: "#f50fc3",
    T: "#006300",
    U: "#ffff00",
    V: "#33ccff",

    W: "#00ff00",
    X: "#ff0000",
    Y: "#996600",
    Z: "#006fc0",
}

NAMES = {
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

uses = [True]*12
calculating = False
failed = False
board = None


def mino_icon(mino_type: int, icon_width: int, enabled: bool = True, on_clicked=lambda e: None):
    data = None
    if mino_type == F:
        data = [[0, 1], [1, 0], [1, 1], [2, 1], [2, 2]]
    elif mino_type == I:
        data = [[0, 1], [1, 1], [2, 1], [3, 1], [4, 1]]
    elif mino_type == L:
        data = [[0, 0], [1, 0], [2, 0], [3, 0], [3, 1]]
    elif mino_type == N:
        data = [[0, 1], [1, 1], [2, 1], [2, 2], [3, 2]]
    elif mino_type == P:
        data = [[0, 1], [1, 0], [1, 1], [2, 0], [2, 1]]
    elif mino_type == T:
        data = [[0, 2], [1, 0], [1, 1], [1, 2], [2, 2]]
    elif mino_type == U:
        data = [[0, 0], [0, 1], [1, 0], [2, 0], [2, 1]]
    elif mino_type == V:
        data = [[0, 0], [0, 1], [0, 2], [1, 0], [2, 0]]
    elif mino_type == W:
        data = [[0, 1], [0, 2], [1, 0], [1, 1], [2, 0]]
    elif mino_type == X:
        data = [[0, 1], [1, 0], [1, 1], [1, 2], [2, 1]]
    elif mino_type == Y:
        data = [[0, 0], [1, 0], [2, 0], [2, 1], [3, 0]]
    elif mino_type == Z:
        data = [[0, 2], [1, 0], [1, 1], [1, 2], [2, 0]]

    WIDTH, HEIGHT = 5, 3

    mino_paint = ft.Paint(
        style=ft.PaintingStyle.FILL,
        color=COLORS[mino_type],
    )

    mion_cover_paint = ft.Paint(
        style=ft.PaintingStyle.FILL,
        color="#afffffff",
    )

    mino_border_paint = ft.Paint(
        style=ft.PaintingStyle.STROKE,
        color="#cccccc",
        stroke_width=2,
    )
    size = icon_width*0.8 // WIDTH

    shapes = []
    for h in range(HEIGHT):
        for w in range(WIDTH):
            if [w, h] in data:
                shapes.append(
                    cv.Rect(w*size, (HEIGHT-1-h)*size,
                            size, size, paint=mino_paint)
                )
                if not enabled:
                    shapes.append(
                        cv.Rect(w*size, (HEIGHT-1-h)*size,
                                size, size, paint=mion_cover_paint)
                    )
                shapes.append(
                    cv.Rect(w*size, (HEIGHT-1-h)*size,
                            size, size, paint=mino_border_paint),

                )

    def canvas_clicked(e):
        global calculating
        if not calculating:
            uses[mino_type] = not uses[mino_type]
            on_clicked(e)

    return ft.Container(
        ft.Row(
            [
                ft.Container(
                    ft.Text(
                        NAMES[mino_type],
                        text_align=ft.alignment.center,
                        size=20,
                        color="#000000" if enabled else "#aaaaaa",
                    ),
                    width=icon_width*0.2,
                    height=size*3,
                    alignment=ft.alignment.center,
                ),
                cv.Canvas(
                    shapes=shapes,
                    width=WIDTH*size,
                    height=HEIGHT*size,
                )
            ],
        ),
        on_click=canvas_clicked,
    )


def result_board(board, w, h, board_width, board_height):
    global failed

    margin = 5
    size = min(board_width / w, board_height / h)

    shapes = []
    shapes.append(
        cv.Rect(
            0, 0,
            w*size + margin*2, h*size + margin*2,
            paint=ft.Paint(
                style=ft.PaintingStyle.FILL,
                color="#000000" if not failed else "#FF0000",
            )
        )
    )
    shapes.append(
        cv.Rect(
            margin, margin,
            w*size, h*size,
            paint=ft.Paint(
                style=ft.PaintingStyle.FILL,
                color="#ffffff",
            )
        )
    )

    if board is not None:
        for hi in range(h):
            for wi in range(w):
                shapes.append(
                    cv.Rect(
                        margin+wi*size, margin+hi*size,
                        size, size,
                        paint=ft.Paint(
                            style=ft.PaintingStyle.FILL,
                            color=COLORS[board[hi][wi]],
                        )
                    )
                )
                shapes.append(
                    cv.Rect(
                        margin+wi*size, margin+hi*size,
                        size, size,
                        paint=ft.Paint(
                            style=ft.PaintingStyle.STROKE,
                            color="#cccccc",
                            stroke_width=3,
                        )
                    )
                )
    return cv.Canvas(
        shapes=shapes,
        width=w*size+margin*2,
        height=h*size+margin*2,
    )


def main(page: ft.Page):
    page.title = "KATAMINO Solver"
    WINDOW_WIDTH = 1280
    WINDOW_HEIGHT = 670

    # minos
    minos_margin_horizontal = 100
    icon_width = (page.width - minos_margin_horizontal*2) / 6

    def on_canvas_clicked(e):
        for i in range(6):
            page.controls[1].controls[i] = mino_icon(
                i, icon_width, uses[i], on_canvas_clicked)

        for i in range(6, 12):
            page.controls[3].controls[i-6] = mino_icon(
                i, icon_width, uses[i], on_canvas_clicked)

        global failed
        failed = False
        page.controls[7].controls[0] = result_board(
            board, int(dd_size.value.split("x")[0]), int(dd_size.value.split("x")[1]), WINDOW_WIDTH*0.9, WINDOW_HEIGHT*0.5)
        page.update()

    # upper minos
    page.add(ft.Container(height=5))
    r = []
    for i in range(6):
        e = mino_icon(i, icon_width, uses[i], on_canvas_clicked)
        r.append(e)
    page.add(ft.Row(controls=r, alignment=ft.MainAxisAlignment.CENTER,))

    # lower minos
    page.add(ft.Container(height=5))
    r = []
    for i in range(6, 12):
        e = mino_icon(i, icon_width, uses[i], on_canvas_clicked)
        r.append(e)
    page.add(ft.Row(controls=r, alignment=ft.MainAxisAlignment.CENTER,))

    def on_dropdown_changed(e):
        global failed
        failed = False
        page.controls[7].controls[0] = result_board(
            board, int(e.data.split("x")[0]), int(e.data.split("x")[1]), WINDOW_WIDTH*0.9, WINDOW_HEIGHT*0.5)
        page.update()

    # input board_size & pack button
    page.add(ft.Container(height=5))
    dd_size = ft.Dropdown(
        width=100,
        options=[
            ft.dropdown.Option("10x6"),
            ft.dropdown.Option("12x5"),
            ft.dropdown.Option("15x4"),
            ft.dropdown.Option("20x3"),
            ft.dropdown.Option("11x5"),
            ft.dropdown.Option("10x5"),
            ft.dropdown.Option("9x5"),
            ft.dropdown.Option("15x3"),
            ft.dropdown.Option("10x4"),
            ft.dropdown.Option("8x5"),
            ft.dropdown.Option("7x5"),
            ft.dropdown.Option("10x3"),
            ft.dropdown.Option("6x5"),
            ft.dropdown.Option("5x5"),
            ft.dropdown.Option("10x2"),
            ft.dropdown.Option("5x4"),
            ft.dropdown.Option("5x3"),
        ],
        on_change=on_dropdown_changed,
    )
    dd_size.value = "12x5"

    def on_solve_clicked(e):
        global calculating, failed

        if calculating:
            return

        # start calculating
        calculating = True
        page.controls[5].controls[1].disabled = True
        page.controls[5].controls[2].disabled = True
        page.controls[5].controls[3] = ft.ProgressRing(width=16, height=16)
        page.update()

        # solve
        w, h = int(dd_size.value.split("x")[0]), int(
            dd_size.value.split("x")[1])
        ans = solve(w, h, uses,)

        # finish calculating
        failed = not ans[0]
        page.controls[5].controls[1].disabled = False
        page.controls[5].controls[2].disabled = False
        page.controls[5].controls[3] = ft.Container(width=16, height=16)
        page.controls[7].controls[0] = result_board(
            ans[1], w, h, WINDOW_WIDTH*0.9, WINDOW_HEIGHT*0.5)
        page.update()
        calculating = False

    # loading icon
    loading = ft.Container(width=16, height=16)

    r = ft.Row(
        [
            ft.Text("Size: ", size=20),
            dd_size,
            ft.Button("Solve", on_click=on_solve_clicked),
            loading,
        ],
        alignment=ft.MainAxisAlignment.CENTER,
    )
    page.add(r)

    # result board
    page.add(ft.Container(height=5))
    b = result_board(board, 12, 5, WINDOW_WIDTH*0.9, WINDOW_HEIGHT*0.5)
    page.add(ft.Row(
        [b],
        alignment=ft.MainAxisAlignment.CENTER,
    ))

    page.update()


ft.app(target=main, assets_dir="assets")
