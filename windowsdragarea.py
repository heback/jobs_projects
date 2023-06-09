import flet as ft

def main(page: ft.Page):
    page.window_title_bar_hidden = True
    page.window_title_bar_buttons_hidden = True

    page.add(
        ft.Row(
            [
                ft.WindowDragArea(ft.Container(ft.Text("Drag this area to move, maximize and restore application window."), bgcolor=ft.colors.AMBER_300, padding=10), expand=True),
                ft.IconButton(ft.icons.CLOSE, on_click=lambda _: page.window_close())
            ]
        )
    )

ft.app(target=main)