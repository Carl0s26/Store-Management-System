import flet as ft

def lowerNavBar(page,ft=ft):
    NavBar = ft.BottomAppBar(
        shape=ft.NotchShape.CIRCULAR,
        content = ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_EVENLY,
            controls=[
                ft.IconButton(ft.icons.LOCAL_DRINK,icon_size = 30, on_click=lambda _: page.go('/drinks')),
                ft.IconButton(ft.icons.LOCAL_PIZZA,icon_size = 30, on_click=lambda _: page.go('/pizza')),
                ft.IconButton(ft.icons.HOME,icon_size = 30, on_click=lambda _: page.go('/')),
                ft.IconButton(ft.icons.VIDEOGAME_ASSET,icon_size = 30, on_click=lambda _: page.go('/games')),
                ft.IconButton(ft.icons.DISCOUNT,icon_size = 30, on_click=lambda _: page.go('/offers'))
            ],
        ),
    )
    return NavBar

def upperNavBar(page,ft=ft):
    NavBar = ft.AppBar(
        leading=ft.Row(
            controls=[
                ft.IconButton(ft.icons.ADD, icon_size=30, on_click=lambda _: page.go('/add')),
                ft.IconButton(ft.icons.SETTINGS, icon_size=30, on_click=lambda _: page.go('/settings')),
            ],
            spacing=0,
        ),
        leading_width=80,
        title=ft.Text("Shop Name",size=30),
        center_title=True,
        bgcolor=ft.colors.SURFACE_VARIANT,
        actions=[
            ft.IconButton(ft.icons.SHOPPING_CART,icon_size = 30, on_click=lambda _: page.go('/cart')),
            ft.IconButton(ft.icons.PERSON_ADD_ALT_ROUNDED,icon_size = 30, on_click=lambda _: page.go('/profile')),
        ]
    )
    return NavBar