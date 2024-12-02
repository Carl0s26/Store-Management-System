import flet as ft

def NavBar(page,ft=ft):
    NavBar = ft.AppBar(
            leading=ft.Icon(ft.icons.TAG_FACES_ROUNDED),
            leading_width=40,
            title=ft.Text("Flet Router"),
            center_title=False,
            bgcolor=ft.colors.SURFACE_VARIANT,
            actions=[
                ft.IconButton(ft.icons.HOME, on_click=lambda _: page.go('/')),
                ft.IconButton(ft.icons.LOCAL_DRINK, on_click=lambda _: page.go('/drinks')),
                ft.IconButton(ft.icons.VIDEOGAME_ASSET, on_click=lambda _: page.go('/games')),
                ft.IconButton(ft.icons.LOCAL_PIZZA, on_click=lambda _: page.go('/pizza'))
            ]
        )
    return NavBar