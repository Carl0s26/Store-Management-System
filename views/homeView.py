
import flet as ft
import sqlite3

#? flet run main.py -r 

#! FINISH the view desing

def home_View(router):
    #* defining view content
    conn = sqlite3.connect("delivery.db")
    conn.row_factory = sqlite3.Row  
    cursor = conn.cursor()

    cursor.execute("SELECT image FROM data WHERE name = ?", ("drink",))
    drink_image = cursor.fetchone()["image"]


    cursor.execute("SELECT image FROM data WHERE name = ?", ("game",))
    game_image = cursor.fetchone()["image"]

    cursor.execute("SELECT image FROM data WHERE name = ?", ("pizza",))
    pizza_image = cursor.fetchone()["image"]

    cursor.execute("SELECT image FROM data WHERE name = ?", ("unavailable_offer",))
    offer_image = cursor.fetchone()["image"]

    conn.close()

    content = ft.Container(
        content=ft.Column(spacing=25,controls=[
            ft.Row(controls=[ft.Text("Home", size=35, weight="bold")],alignment=ft.MainAxisAlignment.CENTER),
            ft.Row(alignment=ft.MainAxisAlignment.SPACE_AROUND,controls=[
                ft.Column(spacing=30,controls=[
                    ft.Container(on_click=lambda _: router.go('/drinks'), content=ft.Column(controls=[
                        ft.Text("Drinks", size=30, weight="bold"),
                         ft.Image(src_base64=drink_image, width=200, height=200, fit="contain"),
                ],alignment=ft.MainAxisAlignment.CENTER, 
                horizontal_alignment=ft.CrossAxisAlignment.CENTER)),
                    ft.Container(on_click=lambda _: router.go('/games'), content=ft.Column(controls=[
                        ft.Text("Games", size=30, weight="bold"),
                         ft.Image(src_base64=game_image, width=200, height=200, fit="contain"),
                    ], alignment=ft.MainAxisAlignment.CENTER, 
                horizontal_alignment=ft.CrossAxisAlignment.CENTER)),
                ]),
                ft.Column(spacing=30,controls=[
                    ft.Container(on_click=lambda _: router.go('/pizza'), content=ft.Column(controls=[
                        ft.Text("Pizza", size=30, weight="bold"),
                         ft.Image(src_base64=pizza_image, width=200, height=200, fit="contain"),
                    ], alignment=ft.MainAxisAlignment.CENTER, 
                horizontal_alignment=ft.CrossAxisAlignment.CENTER)),
                    ft.Container(on_click=lambda _: router.go('/offers'),disabled=True, content=ft.Column(controls=[
                        ft.Text("Offers", size=30, weight="bold"),
                         ft.Image(src_base64=offer_image, width=200, height=200, fit="contain"),
                    ], alignment=ft.MainAxisAlignment.CENTER, 
                horizontal_alignment=ft.CrossAxisAlignment.CENTER)),
                ])
            ])
            
            #ft.Row(controls=[
            #ft.ElevatedButton("Go to View 1", on_click=lambda e: viewHandler(videogamesView)),
            #ft.ElevatedButton("Go to View 2", on_click=lambda e: viewHandler(pizzaView)),=
        ])
    )
    return content
