import flet as ft

def lowerNavBar(page,ft=ft):
    NavBar = ft.BottomAppBar(
        bgcolor='#eca53b',
        shape=ft.NotchShape.CIRCULAR,
        content = ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_EVENLY,
            controls=[
                ft.IconButton(ft.icons.LOCAL_DRINK,icon_size = 30, on_click=lambda _: page.go('/drinks'), icon_color="blue"),
                ft.IconButton(ft.icons.LOCAL_PIZZA,icon_size = 30, on_click=lambda _: page.go('/pizza'), icon_color="blue"),
                ft.IconButton(ft.icons.HOME,icon_size = 30, on_click=lambda _: page.go('/'), icon_color="blue"),
                ft.IconButton(ft.icons.VIDEOGAME_ASSET,icon_size = 30, on_click=lambda _: page.go('/games'), icon_color="blue"),
                ft.IconButton(ft.icons.DISCOUNT,icon_size = 30,disabled = True, on_click=lambda _: page.go('/offers'))
            ],
        ),
    )
    return NavBar

def upperNavBar(page,ft=ft):
    NavBar = ft.AppBar(
        leading=ft.Row(
            controls=[
                ft.IconButton(ft.icons.ADD, icon_size=30, on_click=lambda _: page.go('/add'), icon_color="black"),
                ft.IconButton(ft.icons.SETTINGS, icon_size=30, on_click=lambda _: (page.go('/settings'), page.update()), icon_color="black"),
            ],
            spacing=0,
        ),
        leading_width=80,
        title=ft.Text("Shop Name",size=30),
        center_title=True,
        bgcolor= '#67e0ba',
        actions=[
            ft.IconButton(ft.icons.SHOPPING_CART,icon_size = 30, on_click=lambda _: page.go('/cart'),icon_color="black"),
            ft.IconButton(ft.icons.PERSON,icon_size = 30, on_click=lambda _: page.go('/profile'), icon_color="black"),
        ]
    )
    return NavBar