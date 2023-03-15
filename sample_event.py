import flet as ft
from flet import *


def main(page):
    def add_clicked(e):
        page.add(Checkbox(label=new_task.value))
        new_task.value = ""
        new_task.focus()
        new_task.update()

    new_task = TextField(
        hint_text="Whats needs to be done?",
        width=300
    )
    page.add(Row([new_task, ElevatedButton("Add", on_click=add_clicked)]))


ft.app(target=main)


