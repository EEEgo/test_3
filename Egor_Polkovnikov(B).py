import flet as ft
f = open("C:/Users/Unicum_Student/Documents/Новая папка/save.txt",'r+')
num = f.read()


def main(page: ft.Page):
    page.title = "Flet counter example"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    txt_number = ft.TextField(value=num, text_align=ft.TextAlign.RIGHT, width=100)

    def plus_click(e):
        txt_number.value = str(int(txt_number.value) + 1)
        num = int(txt_number.value)
        page.update()
    def zero_click(e):
        txt_number.value = str(int(txt_number.value) * 0)
        num = int(txt_number.value)
        page.update()
    def save(e):
        #f = int(open("C:/Users/Unicum_Student/Documents/Новая папка/save.txt", 'w'))
        f.write(num)


    page.add(
        ft.Row(
            [
                ft.IconButton(ft.icons.EXPOSURE_ZERO, on_click=zero_click),
                txt_number,
                ft.IconButton(ft.icons.ADD, on_click=plus_click),
                ft.IconButton(ft.icons.SAVE, on_click=save)

            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )

ft.app(main)
f.close()