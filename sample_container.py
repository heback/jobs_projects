import flet as ft
from flet import *


def main(page: Page):
    page.add(
        Row(controls=[
            Text("A"),
            Text("B"),
            Text("C")
        ])
    )
    page.update()


ft.app(target=main)


