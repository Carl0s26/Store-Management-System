
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

















# conn = sqlite3.connect("delivery.db")
    # conn.row_factory = sqlite3.Row  
    # cursor = conn.cursor()

    # cursor.execute("SELECT image FROM data WHERE name = ?", ("drink",))
    # drink_image = cursor.fetchone()["image"]


    # cursor.execute("SELECT image FROM data WHERE name = ?", ("game",))
    # game_image = cursor.fetchone()["image"]

    # cursor.execute("SELECT image FROM data WHERE name = ?", ("pizza",))
    # pizza_image = cursor.fetchone()["image"]

    # cursor.execute("SELECT image FROM data WHERE name = ?", ("offer",))
    # offer_image = cursor.fetchone()["image"]
    # conn.close()


#---------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------#


    # videogamesView = ft.Container(
    #     content=[
    #         ft.Text("This is View 1", size=20),
    #         ft.ElevatedButton("Go to Home", on_click=lambda e: viewHandler(homeView)),
    #         ft.ElevatedButton("Go to View 2", on_click=lambda e: viewHandler(pizzaView)),
    #     ],
    # )

    # pizzaView = ft.Container(
    #     content=[
    #         ft.Text("This is View 2", size=20),
    #         ft.ElevatedButton("Go to Home", on_click=lambda e: viewHandler(homeView)),
    #         ft.ElevatedButton("Go to View 2", on_click=lambda e: viewHandler(videogamesView)),
    #     ]
    # )
    # pizzaView.visible = False
    # videogamesView.visible = False
    # page.add(homeView,videogamesView,pizzaView)
    # def viewHandler(view):
    #     pizzaView.visible = False
    #     videogamesView.visible = False
    #     homeView.visible = False
    #     view.visible = True
    #     page.update()

#---------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------#

# conn = sqlite3.connect("images.db", check_same_thread=False)
# cursor = conn.cursor()

# cursor.execute("""
# CREATE TABLE IF NOT EXISTS images (
#     id INTEGER PRIMARY KEY,
#     name TEXT NOT NULL,
#     img_string TEXT NOT NULL,
#     price FLOAT NOT NULL
# )
# """)
# conn.commit()

# def main(page: ft.Page):
#     page.scroll = 'auto'  # type: ignore
#     you_data = ft.Column()
#     preview = ft.Image(visible=False, width=100, height=100, fit="contain") # type: ignore
#     txt_name = ft.TextField(label="Item name:")
#     txt_price = ft.TextField(label="Price:")
#     save = ft.ElevatedButton("Save", icon=ft.icons.SAVE, disabled=True)
#     convertImgToString = ''
#     page.title = 'Amason'
#     page.window.width = 900
#     page.window.height = 900

#     def load_images():
#         you_data.controls.clear()
#         cursor.execute("SELECT id, name, img_string, price FROM images")
#         data = cursor.fetchall()

#         grid = ft.GridView(
#             max_extent=500,  # Maximum width per grid item
#             spacing=15,      # Space between items
#             run_spacing=15, # Space between rows
#         )
        
#         def on_item_click(id, name, price):
#             print(f"Item clicked: {name}, Price: {price}, ID: {id}")
#             page.update()
            
#         for id, name, img_string, price in data:
#             grid.controls.append(
#                 ft.Container(
#                     content=ft.Column([
#                         ft.Image(src_base64=img_string, width=300, height=300, fit="contain"),  # type: ignore
#                         ft.Column([ft.Text(name, size=20, weight="bold"), ft.Text("$" + f"{price:.2f}", size=25)]) # type: ignore
#                     ]),
#                     padding=10,
#                     border=ft.border.all(1, ft.colors.GREY),
#                     border_radius=ft.border_radius.all(8),
#                     alignment=ft.alignment.center,
#                     width=100,
#                     height=100,   
#                     on_click=lambda e, id=id, name=name, img_string=img_string, price=price: on_item_click(id, name, price)
#                 )
#             )

#         you_data.controls.append(grid)
#         page.update()

#     def dets(e):
#         cursor.execute("DELETE FROM images WHERE id = (SELECT MAX(id) FROM images)")
#         conn.commit()
#         load_images()

#     def upload_now(e: ft.FilePickerResultEvent):
#         nonlocal convertImgToString
#         if e.files:
#             for x in e.files:  # type: ignore
#                 try:
#                     with open(x.path, "rb") as image_file:
#                         convertImgToString = base64.b64encode(image_file.read()).decode()
#                         preview.visible = True
#                         preview.src_base64=convertImgToString
#                         save.disabled = False
#                 except Exception as e:  # type: ignore
#                     print(f"Error: {e}")
#         page.update()
        
#     def confirm(e):
#         nonlocal convertImgToString
#         cursor.execute("INSERT INTO images (name, img_string, price) VALUES (?, ?, ?)",
#                        (txt_name.value, convertImgToString, txt_price.value))
#         conn.commit()
#         txt_name.value = ''
#         txt_price.value = ''
#         convertImgToString = ''
#         preview.visible = False
#         save.disabled = True
#         load_images()


#     file_picker = ft.FilePicker(on_result=upload_now)
#     page.overlay.append(file_picker)

#     save.on_click = confirm
#     load_images()

#     page.add(
#         ft.Column([
#             ft.Text("Amason", size=30),
#             txt_name,
#             txt_price,
#             ft.Row([ft.FilledButton("Upload new Image",icon=ft.icons.FILE_UPLOAD_OUTLINED, on_click=lambda e: file_picker.pick_files()), 
#                     ft.FilledButton("Delete Last",icon=ft.icons.DELETE, on_click=dets),
#                     save,
#                     preview,
#                     ]),
#             you_data,
#         ])
#     )

# ft.app(target=main)