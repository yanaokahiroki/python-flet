import flet as ft
from flet_core.control_event import ControlEvent


def main(page: ft.Page):
    page.title = "Flet Counter"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    text_number = ft.TextField(value="0", text_align=ft.TextAlign.RIGHT, width=100)

    def decrement(e: ControlEvent) -> None:
        """テキストの数字を1減らす"""
        text_number.value = str(int(text_number.value) - 1)
        page.update()

    def increment(e: ControlEvent) -> None:
        """テキストの数字を1増やす"""
        text_number.value = str(int(text_number.value) + 1)
        page.update()

    page.add(
        ft.Row(
            controls=[
                ft.IconButton(ft.icons.REMOVE, on_click=decrement),
                text_number,
                ft.IconButton(ft.icons.ADD, on_click=increment),
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )


ft.app(target=main, view=ft.AppView.WEB_BROWSER)
