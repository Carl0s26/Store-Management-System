import flet as ft
from views.gamesView import gamesBought

# def exampleFunction(page):
#     # Modify content after navigating to /cart
#     if page.route == '/cart':
#         gamesDataRows = []
#         for i in range(len(gamesBought)):
#             gamesDataRows.append(ft.DataRow(
#                 cells=[
#                     ft.DataCell(ft.Text(gamesBought[i][0])),
#                     ft.DataCell(ft.Container(content=ft.Dropdown(hint_text="name",text_size=10,options=[gamesBought[i][1]]),expand=True)), #* since the dropdown doesn't have a "See only" feature make the function it calls after a action reset the text
#                     ft.DataCell(ft.Container(content=ft.Dropdown(hint_text="",text_size=20,options=[ft.dropdown.Option("1"),ft.dropdown.Option("2"),ft.dropdown.Option("3"),ft.dropdown.Option("4"),ft.dropdown.Option("5"),ft.dropdown.Option("6"),ft.dropdown.Option("7"),ft.dropdown.Option("8"),ft.dropdown.Option("9"),ft.dropdown.Option("10")],),expand=True)),
#                     ft.DataCell(ft.Text(gamesBought[i][2])),
#                     ft.DataCell(ft.IconButton(icon=ft.icons.CANCEL_PRESENTATION_OUTLINED,))#on_click= lambda e: delete(e))),
#                 ],
#             ),)
#         print(gamesDataRows)
#         print(page.controls[0].content.controls[0])
#         print(page.controls[0].content.controls)
#         print(page.controls[0].content)
#         print(page.controls[0])
#         print(page.controls)
#         # page.controls[0].content.controls[0].rows = gamesDataRows 
#         # print(page.controls[0].content.controls[0].rows)
#         page.update()




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