import flet as ft
from flet import *


def main(page: Page):
    t = Text(value="Hello, world!", color="green")
    page.controls.append(t)
    page.update()


ft.app(target=main)

