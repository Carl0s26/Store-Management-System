import flet as ft
import requests

#? flet run main.py -r
gamesBought = []
#! FINISH the view desing
def getGames(e):
    pass

def gameToCart(e,feedbackBar,router):
    gamesBought.append(e.control.data) # creating the datacells here due to an issue when creating them in the cart view
    feedbackBar.open = True
    router.update()
    #print(gamesBought)

def games_View(router):
    feedbackBar = ft.SnackBar(content =ft.Text("Item successfully to your cart",size=20),bgcolor=ft.colors.BLACK)
    router.overlay.append(feedbackBar)
    gameRows = []
    response = requests.get("http://127.0.0.1:8000/games/")
    for i in range(0,len(response.json()),2):
        data = response.json()[i]
        if i + 1 < len(response.json()):
            gameRows.append( 
                ft.Row(spacing=40,alignment=ft.MainAxisAlignment.SPACE_AROUND,controls=[
                    ft.Container(height=500,width=250,border=ft.border.all(1,ft.colors.WHITE),alignment=ft.alignment.center,bgcolor=ft.colors.RED_300,content= # creating the game container with game data
                        ft.Column(alignment=ft.MainAxisAlignment.CENTER,horizontal_alignment=ft.CrossAxisAlignment.CENTER, controls=[
                            ft.Text(text_align=ft.TextAlign.CENTER,value=data["name"],weight="bold",),
                            ft.Image(width=200, height=200, src_base64= data["image"]),
                            ft.Text(text_align=ft.TextAlign.CENTER,size=10, value= data["description"]),
                            ft.Text(data["category"],weight="bold",),
                            ft.Text(data["rating"]),
                            ft.Text("$" + str("{:.2f}".format(data["price"]))),
                            ft.FilledButton(data=["Video Game",data["name"],str("{:.2f}".format(data["price"]))],text="Add to cart",on_click=lambda e: gameToCart(e,feedbackBar,router))
                        ])         
                    ),
                    ft.Container(height=500,width=250,border=ft.border.all(1,ft.colors.WHITE),alignment=ft.alignment.center,bgcolor=ft.colors.RED_300,content= # creating the game container with game data
                        ft.Column(alignment=ft.MainAxisAlignment.CENTER,horizontal_alignment=ft.CrossAxisAlignment.CENTER, controls=[
                            ft.Text(text_align=ft.TextAlign.CENTER,value=response.json()[i+1]["name"],weight="bold",),
                            ft.Image(width=200, height=200, src_base64= response.json()[i+1]["image"]),
                            ft.Text(text_align=ft.TextAlign.CENTER,size=10, value= response.json()[i+1]["description"]),
                            ft.Text(response.json()[i+1]["category"],weight="bold",),
                            ft.Text(response.json()[i+1]["rating"]),
                            ft.Text("$" + str("{:.2f}".format(response.json()[i+1]["price"]))),
                            ft.FilledButton(data=["Video Game",response.json()[i+1]["name"],response.json()[i+1]["price"]],text="Add to cart",on_click=lambda e: gameToCart(e,feedbackBar,router))
                        ])         
                    )
                ])   
            )
        else:
            gameRows.append(
                ft.Row(spacing=40,alignment=ft.MainAxisAlignment.SPACE_AROUND,controls=[
                    ft.Container(height=500,width=250,border=ft.border.all(1,ft.colors.WHITE),alignment=ft.alignment.center,bgcolor=ft.colors.RED_300,content= # creating the game container with game data
                        ft.Column(alignment=ft.MainAxisAlignment.CENTER,horizontal_alignment=ft.CrossAxisAlignment.CENTER, controls=[
                            ft.Text(text_align=ft.TextAlign.CENTER,value=data["name"],weight="bold",),
                            ft.Image(width=200, height=200, src_base64= data["image"]),
                            ft.Text(text_align=ft.TextAlign.CENTER,size=10, value= data["description"]),
                            ft.Text(data["category"],weight="bold",),
                            ft.Text(data["rating"]),
                            ft.Text("$" + str("{:.2f}".format(data["price"]))),
                            ft.FilledButton(data=["Video Game",data["name"],str("{:.2f}".format(data["price"]))],text="Add to cart",on_click=lambda e: gameToCart(e,feedbackBar,router))
                        ])         
                    )
                ])
            )
    gamesDisplayColumn = ft.Column(alignment=ft.MainAxisAlignment.SPACE_AROUND,spacing=50)
    for i in range(len(gameRows)):
        gamesDisplayColumn.controls.append(ft.Container(padding=ft.padding.symmetric(vertical=20),content=gameRows[i]))
    



    content = ft.Column(horizontal_alignment=ft.CrossAxisAlignment.CENTER,alignment= ft.MainAxisAlignment.CENTER,controls=[
        ft.Text("Games",size=40, weight="bold"),
        gamesDisplayColumn,
        ft.CupertinoButton(text="Games Shop",on_click=getGames),
    ])
    return content