import flet as ft
import requests


drinksBought = []
def getDrinks(e):
    pass

def drinksToCart(e,feedbackBar,router):
    print("ii")
    drinksBought.append(e.control.data)
    feedbackBar.open = True
    router.update()

    

def drinks_View(router):
    feedbackBar = ft.SnackBar(content =ft.Text("Item added successfully to your cart",size=20),bgcolor=ft.colors.BLACK)
    router.overlay.append(feedbackBar)
    drinkRows = []
    response = requests.get("http://127.0.0.1:8000/drinks/")
    for i in range(0,len(response.json()),2):
        data = response.json()[i]
        if i + 1 < len(response.json()):
            drinkRows.append( 
                ft.Row(spacing=40,alignment=ft.MainAxisAlignment.SPACE_AROUND,controls=[
                    ft.Container(height=360,width=250,border=ft.border.all(1,ft.colors.WHITE),alignment=ft.alignment.center,bgcolor=ft.colors.BLUE_200,content= # creating the drink container with drink data
                        ft.Column(alignment=ft.MainAxisAlignment.CENTER,horizontal_alignment=ft.CrossAxisAlignment.CENTER, controls=[
                            ft.Text(text_align=ft.TextAlign.CENTER,value=data["name"],weight="bold", size=20),
                            ft.Image(width=200, height=200, src_base64= data["image"]),
                            ft.Text("$" + str("{:.2f}".format(data["price"])),weight="bold", size=20),
                            ft.FilledButton(data=["Drink",data["name"],str("{:.2f}".format(data["price"]))],text="Add to cart",on_click=lambda e: drinksToCart(e,feedbackBar,router))
                        ])         
                    ),
                    ft.Container(height=360,width=250,border=ft.border.all(1,ft.colors.WHITE),alignment=ft.alignment.center,bgcolor=ft.colors.BLUE_200,content= # creating the drink container with drink data
                        ft.Column(alignment=ft.MainAxisAlignment.CENTER,horizontal_alignment=ft.CrossAxisAlignment.CENTER, controls=[
                            ft.Text(text_align=ft.TextAlign.CENTER,value=response.json()[i+1]["name"],weight="bold", size=20),
                            ft.Image(width=200, height=200, src_base64= response.json()[i+1]["image"]),
                            ft.Text("$" + str("{:.2f}".format(response.json()[i+1]["price"])),weight="bold", size=20),
                            ft.FilledButton(data=["Drink",response.json()[i+1]["name"],response.json()[i+1]["price"]],text="Add to cart",on_click=lambda e: drinksToCart(e,feedbackBar,router))
                        ])         
                    )
                ])   
            )
        else:
            drinkRows.append(
                ft.Row(spacing=40,alignment=ft.MainAxisAlignment.SPACE_AROUND,controls=[
                    ft.Container(height=360,width=250,border=ft.border.all(1,ft.colors.WHITE),alignment=ft.alignment.center,bgcolor=ft.colors.BLUE_200,content= # creating the drink container with drink data
                        ft.Column(alignment=ft.MainAxisAlignment.CENTER,horizontal_alignment=ft.CrossAxisAlignment.CENTER, controls=[
                            ft.Text(text_align=ft.TextAlign.CENTER,value=data["name"],weight="bold", size=20),
                            ft.Image(width=200, height=200, src_base64= data["image"]),
                            ft.Text("$" + str("{:.2f}".format(data["price"])),weight="bold", size=20),
                            ft.FilledButton(data=["Drink",data["name"],str("{:.2f}".format(data["price"]))],text="Add to cart",on_click=lambda e: drinksToCart(e,feedbackBar,router))
                        ])         
                    )
                ])
            )
        drinksDisplayColumn = ft.Column(alignment=ft.MainAxisAlignment.SPACE_AROUND,spacing=50)
    for i in range(len(drinkRows)):
            drinksDisplayColumn.controls.append(ft.Container(padding=ft.padding.symmetric(vertical=20),content=drinkRows[i]))
    


    content = ft.Column(horizontal_alignment=ft.CrossAxisAlignment.CENTER,alignment= ft.MainAxisAlignment.CENTER,controls=[
        ft.Text("Drinks",size=40,weight="bold",),
            drinksDisplayColumn,
        ft.CupertinoButton(text="Drinks Shop",on_click=getDrinks),
    ])
    return content