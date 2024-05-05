import flet as ft

def main(page: ft.page):

    def toggle_icon_button(e):
        e.control.selected = not e.control.selected
        e.control.update()

    page.add(ft.Row(
    [
        ft.IconButton(icon=("star"),
            on_click=toggle_icon_button,
            style=ft.ButtonStyle(color={"selected": ft.colors.YELLOW, "": ft.colors.WHITE}),),
        ft.IconButton(icon=("star"),
            on_click=toggle_icon_button,
            style=ft.ButtonStyle(color={"selected": ft.colors.YELLOW, "": ft.colors.WHITE}),),
        ft.IconButton(icon=("star"),
            on_click=toggle_icon_button,
            style=ft.ButtonStyle(color={"selected": ft.colors.YELLOW, "": ft.colors.WHITE}),),
        ft.IconButton(icon=("star"),
            on_click=toggle_icon_button,
            style=ft.ButtonStyle(color={"selected": ft.colors.YELLOW, "": ft.colors.WHITE}),),
        ft.IconButton(icon=("star"),
            on_click=toggle_icon_button,
            style=ft.ButtonStyle(color={"selected": ft.colors.YELLOW, "": ft.colors.WHITE}),),
        ft.IconButton(icon=("star"),
            on_click=toggle_icon_button,
            style=ft.ButtonStyle(color={"selected": ft.colors.YELLOW, "": ft.colors.WHITE}),),
        ft.IconButton(icon=("star"),
            on_click=toggle_icon_button,
            style=ft.ButtonStyle(color={"selected": ft.colors.YELLOW, "": ft.colors.WHITE}),),
        ft.IconButton(icon=("star"),
            on_click=toggle_icon_button,
            style=ft.ButtonStyle(color={"selected": ft.colors.YELLOW, "": ft.colors.WHITE}),),
        ft.IconButton(icon=("star"),
            on_click=toggle_icon_button,
            style=ft.ButtonStyle(color={"selected": ft.colors.YELLOW, "": ft.colors.WHITE}),),
        ft.IconButton(icon=("star"),
            on_click=toggle_icon_button,
            style=ft.ButtonStyle(color={"selected": ft.colors.YELLOW, "": ft.colors.WHITE}),),
    ]
        ))
    



    def addComment(p):
        checkBoxText = ft.Text(value=textField.value, width=350, bgcolor="#4D869C", size=15, color='BLACK')
        commentkRow= ft.Row(controls=[checkBoxText], alignment=ft.MainAxisAlignment.START)
        page.add(commentkRow)

    page.window_width=625
    page.window_height=700
    page.bgcolor= '#A0DEFF'
    page.title = "YORUM SAYFASI"


    textField =ft.TextField(width=490, autofocus=True, color='BLACK', border_color='BLACK',
                            max_length=250, hint_text="Yorumunuzu yazınız")
    addBtn= ft.ElevatedButton(text="Ekle", on_click=addComment, bgcolor='WHITE', color='BLACK')
    

    checkBoxText= ft.Text(value='Yorum 1', width= 350, bgcolor='WHITE',size=15, color='BLACK')

    entriesRow= ft.Row(controls=[textField, addBtn], alignment=ft.MainAxisAlignment.SPACE_BETWEEN)

    page.add(entriesRow)

ft.app(target=main)
