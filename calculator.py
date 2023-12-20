import flet as ft

buttons = [
    {"operator": "AC", "font": ft.colors.BLACK, "bg_color": ft.colors.BLUE_GREY_100},
    {"operator": "±", "font": ft.colors.BLACK, "bg_color": ft.colors.BLUE_GREY_100},
    {"operator": "%", "font": ft.colors.BLACK, "bg_color": ft.colors.BLUE_GREY_100},
    {"operator": "/", "font": ft.colors.WHITE, "bg_color": ft.colors.ORANGE},
    {"operator": "7", "font": ft.colors.WHITE, "bg_color": ft.colors.WHITE12},
    {"operator": "8", "font": ft.colors.WHITE, "bg_color": ft.colors.WHITE12},
    {"operator": "9", "font": ft.colors.WHITE, "bg_color": ft.colors.WHITE12},
    {"operator": "*", "font": ft.colors.WHITE, "bg_color": ft.colors.ORANGE},
    {"operator": "4", "font": ft.colors.WHITE, "bg_color": ft.colors.WHITE12},
    {"operator": "5", "font": ft.colors.WHITE, "bg_color": ft.colors.WHITE12},
    {"operator": "6", "font": ft.colors.WHITE, "bg_color": ft.colors.WHITE12},
    {"operator": "-", "font": ft.colors.WHITE, "bg_color": ft.colors.ORANGE},
    {"operator": "1", "font": ft.colors.WHITE, "bg_color": ft.colors.WHITE12},
    {"operator": "2", "font": ft.colors.WHITE, "bg_color": ft.colors.WHITE12},
    {"operator": "3", "font": ft.colors.WHITE, "bg_color": ft.colors.WHITE12},
    {"operator": "+", "font": ft.colors.WHITE, "bg_color": ft.colors.ORANGE},
    {"operator": "0", "font": ft.colors.WHITE, "bg_color": ft.colors.WHITE12},
    {"operator": ".", "font": ft.colors.WHITE, "bg_color": ft.colors.WHITE12},
    {"operator": "=", "font": ft.colors.WHITE, "bg_color": ft.colors.ORANGE},
]


def main(page: ft.Page):
    page.title = "Calculator"
    page.window_resizable = False
    page.bgcolor = ft.colors.BLACK
    page.window_width = 270
    page.window_height = 380

    result = ft.Text(value="0", color=ft.colors.WHITE, size=20)

    def calculate(operator, value_at):
        try:
            if operator == "%":
                return str(eval(value_at) / 100)
            elif operator == "±":
                return str(-eval(value_at))
            else:
                return str(eval(value_at))
        except Exception as e:
            return "ERROR!"

    def select(event):
        value_at = result.value if result.value not in ("0", "ERROR!") else " "
        value = event.control.content.value

        if value.isdigit() or value == ".":
            value = value_at + value
        elif value == "AC":
            value = "0"
        else:
            if value_at and value_at[-1] in ("/", "*", "-", "+", "."):
                value_at = value_at[:-1]

            value = value_at + value

            if value[-1] in ("=", "%", "±"):
                value = calculate(operator=value[-1], value_at=value_at)

        result.value = value
        result.update()

    display = ft.Row(width=250, controls=[result], alignment="end")

    btns = [
        ft.Container(
            content=ft.Text(value=btn["operator"], color=btn["font"]),
            width=50,
            height=50,
            bgcolor=btn["bg_color"],
            border_radius=100,
            alignment=ft.alignment.center,
            on_click=select,
        )
        for btn in buttons
    ]

    keyboard = ft.Row(width=250, wrap=True, controls=btns, alignment="end")

    page.add(display, keyboard)


ft.app(target=main)
