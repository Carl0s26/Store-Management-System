import flet as ft
import requests

#? flet run main.py -r
gamesBought = []
#! FINISH the view desing
def getGames(e):
    pass

def gameToCart(e):
    gamesBought.append(e.control.data)


def games_View(router):
    #* defining view content
    gameRows = []
    response = requests.get("http://127.0.0.1:8000/games/")
    for i in range(0,len(response.json()),2): # looping trhought all the games
        data = response.json()[i]
        if i + 1 < len(response.json()): # if last element
            gameRows.append( 
                ft.Row(spacing=40,alignment=ft.MainAxisAlignment.SPACE_AROUND,controls=[
                    ft.Container(height=500,width=250,border=ft.border.all(1,ft.colors.WHITE),alignment=ft.alignment.center,bgcolor=ft.colors.RED_300,content= # creating the game container with game data
                        ft.Column(alignment=ft.MainAxisAlignment.CENTER,horizontal_alignment=ft.CrossAxisAlignment.CENTER, controls=[
                            ft.Text(text_align=ft.TextAlign.CENTER,value=data["name"]),
                            ft.Image(width=200, height=200, src_base64= data["image"]),
                            ft.Text(text_align=ft.TextAlign.CENTER,size=10, value= "Description: " + data["description"]),
                            ft.Text("Category: " + data["category"]),
                            ft.Text("Rating: " + data["rating"]),
                            ft.Text("price: " + str(data["price"])),
                            ft.FilledButton(data=data,text="Add to cart",on_click=gameToCart)
                        ])         
                    ),
                    ft.Container(height=500,width=250,border=ft.border.all(1,ft.colors.WHITE),alignment=ft.alignment.center,bgcolor=ft.colors.RED_300,content= # creating the game container with game data
                        ft.Column(alignment=ft.MainAxisAlignment.CENTER,horizontal_alignment=ft.CrossAxisAlignment.CENTER, controls=[
                            ft.Text(text_align=ft.TextAlign.CENTER,value=response.json()[i+1]["name"]),
                            ft.Image(width=200, height=200, src_base64= response.json()[i+1]["image"]),
                            ft.Text(text_align=ft.TextAlign.CENTER,size=10, value= "Description: " + response.json()[i+1]["description"]),
                            ft.Text("Category: " + response.json()[i+1]["category"]),
                            ft.Text("Rating: " + response.json()[i+1]["rating"]),
                            ft.Text("price: " + str(response.json()[i+1]["price"])),
                            ft.FilledButton(data=response.json()[i+1],text="Add to cart",on_click=gameToCart)
                        ])         
                    )
                ])   
            )
        else:
            gameRows.append(
                ft.Row(spacing=40,alignment=ft.MainAxisAlignment.SPACE_AROUND,controls=[
                    ft.Container(height=500,width=250,border=ft.border.all(1,ft.colors.WHITE),alignment=ft.alignment.center,bgcolor=ft.colors.RED_300,content= # creating the game container with game data
                        ft.Column(alignment=ft.MainAxisAlignment.CENTER,horizontal_alignment=ft.CrossAxisAlignment.CENTER, controls=[
                            ft.Text(text_align=ft.TextAlign.CENTER,value=data["name"]),
                            ft.Image(width=200, height=200, src_base64= data["image"]),
                            ft.Text(text_align=ft.TextAlign.CENTER,size=10, value= "Description: " + data["description"]),
                            ft.Text("Category: " + data["category"]),
                            ft.Text("Rating: " + data["rating"]),
                            ft.Text("price: " + str(data["price"])),
                            ft.FilledButton(data=data,text="Add to cart",on_click=gameToCart)
                        ])         
                    )
                ])
            )
    gamesDisplayColumn = ft.Column(alignment=ft.MainAxisAlignment.SPACE_AROUND,spacing=50)
    for i in range(len(gameRows)):
        gamesDisplayColumn.controls.append(ft.Container(padding=ft.padding.symmetric(vertical=20),content=gameRows[i]))
    



    content = ft.Column(horizontal_alignment=ft.CrossAxisAlignment.CENTER,alignment= ft.MainAxisAlignment.CENTER,controls=[
        ft.Text("Games",size=40),
        gamesDisplayColumn,
        ft.CupertinoButton(text="Games Shop",on_click=getGames),
    ])
    return content