import flet as ft
# from views.gamesView import views.gamesView.gamesBought
# from views.pizzaView import views.pizzaView.pizzasList
# from views.drinksView import views.drinksView.drinksBought
import views.gamesView
import views.pizzaView
import views.drinksView
import views.loginView
import requests
#todo mostrar direccion del cliente
#todo mostrar numero de telefono
#todo boton para pagar que te vacie el carrito y confirme que todo fue bien

import sqlite3

quantityDict = {
    "idk": 1
}

def pay(e,router):
    from views.loginView import current_id
    crust = ""
    size = ""
    sauce = ""
    pizzaIngredients = []
    for i in range(len(router.controls[0].content.controls[0].rows)):
        if router.controls[0].content.controls[0].rows[i].cells[0].content.value == "Pizza":
            for j in range(len(router.controls[0].content.controls[0].rows[i].cells[1].content.content.options)):
                print(router.controls[0].content.controls[0].rows[i].cells[1].content.content.options[j].key)
                if router.controls[0].content.controls[0].rows[i].cells[1].content.content.options[j].key in ['Thin Crust','Thick Crust','Stuffed Crust']:
                    crust = router.controls[0].content.controls[0].rows[i].cells[1].content.content.options[j].key
                elif router.controls[0].content.controls[0].rows[i].cells[1].content.content.options[j].key in ['Small','Medium','Big']:
                    size = router.controls[0].content.controls[0].rows[i].cells[1].content.content.options[j].key
                elif router.controls[0].content.controls[0].rows[i].cells[1].content.content.options[j].key in ['Red Sauce','White Sauce','Pesto Sauce','BBQ Sauce']:
                   sauce = router.controls[0].content.controls[0].rows[i].cells[1].content.content.options[j].key
                else:
                    pizzaIngredients.append(router.controls[0].content.controls[0].rows[i].cells[1].content.content.options[j].key)
                    print(crust,size,sauce)
            # pizza
            url = "http://127.0.0.1:8000/pizzas/"
            pizza_data = {
                "crust": crust,
                "size": size,
                "sauce": sauce,
            }
            response = requests.post(url, json=pizza_data)
            if response.status_code != 201:
                print("Error:", response.status_code, response.text)
            else: # User-Pizza
                print(response.json()) 
                pizza_id = response.json().get("PizzaID")
            #?---------------------------------------------------------------------------------------# 
                url = "http://127.0.0.1:8000/customer_pizza_record/"
                data = {
                    "PizzaID": pizza_id,
                    "CustomerID": views.loginView.current_id
                }
                response = requests.post(url, json=data)

                if response.status_code != 201: 
                    print("Error:", response.status_code, response.json())
                else:
                    print("Success:", response.json())
            ##?---------------------------------------------------------------------------------------# 

                    for i in range(len(pizzaIngredients)):
                        
                        url = f"http://127.0.0.1:8000/ingredients/{pizzaIngredients[i]}/"
                        response = requests.get(url)

                        if response.status_code != 201:
                            print("Error:", response.status_code, response.json())
                        else:
                            ingredient_id = response.json().get("ingredientID")
                            print("Success:", response.json())

                            url = "http://127.0.0.1:8000/Pizza_Ingredients/"
                            data = {
                                "PizzaID": pizza_id,
                                "ingredientID": ingredient_id
                            }
                            response = requests.post(url, json=data)

            pizzaIngredients.clear()
    views.pizzaView.pizzasList.clear()
    views.drinksView.drinksBought.clear()
    views.gamesView.gamesBought.clear()
    router.controls[0].content.controls = []

    conn = sqlite3.connect("delivery.db")
    cursor = conn.cursor()

    cursor.execute("SELECT NCF FROM NCF_transactions ORDER BY rowid DESC LIMIT 1")
    last_ncf = cursor.fetchone()
    
    if last_ncf:
        ncf_value = last_ncf[0]
        last_number = ncf_value.split('-')[-1]
        new_number = str(int(last_number) + 1).zfill(len(last_number))
        new_ncf = '-'.join(ncf_value.split('-')[:-1]) + '-' + new_number
        print("New NCF:", new_ncf)
        router.controls[0].content.controls.append(ft.Text(value=f"NCF: {new_ncf}", size=35))
        cursor.execute('''
            INSERT INTO NCF_transactions (NCF, CustomerID) VALUES (?, ?)
                ''', (new_ncf, current_id))
        conn.commit()
    conn.close()
        
    router.controls[0].content.controls.append(
        ft.Row(alignment=ft.MainAxisAlignment.SPACE_EVENLY,vertical_alignment=ft.alignment.center,controls=[
            ft.FilledButton("Reload",on_click=lambda e: Reload(e,router)),
        ]))
    router.update()

    #Todo create the pizza with its unique id



def updatePrice(e):
    pass

def calculatePrize(e,router):
    print("si")
    quantityDict.update({e.control.data:e.control.value})
    Reload("1",router)

def delete(e,router):
    # global views.pizzaView.pizzasList
    # global views.drinksView.drinksBought
    # global views.gamesView.gamesBought
    if e.control.data in views.pizzaView.pizzasList:
        views.pizzaView.pizzasList = [pizza for pizza in views.pizzaView.pizzasList if pizza != e.control.data]
    if e.control.data in views.drinksView.drinksBought:
        views.drinksView.drinksBought = [drink for drink in views.drinksView.drinksBought if drink != e.control.data]
    if e.control.data in views.gamesView.gamesBought:
        views.gamesView.gamesBought = [game for game in views.gamesView.gamesBought if game != e.control.data]
    Reload("1",router)

def Reload(e,router):
    # Creating 1 list with all the rows
    print(views.pizzaView.pizzasList)
    DataRows = []
    seenNames = []
    # Drinks bought logic
    for i in range(len(views.gamesView.gamesBought)):
        gameName = views.gamesView.gamesBought[i][1]
        if views.gamesView.gamesBought[i][1] not in seenNames:
            if gameName in quantityDict:
                cells=[
                    ft.DataCell(ft.Text(views.gamesView.gamesBought[i][0])),
                    ft.DataCell(ft.Container(content=ft.Dropdown(hint_text="name",text_size=10,options=[ft.dropdown.Option(views.gamesView.gamesBought[i][1])],on_change= lambda e: Reload(e,router)),expand=True)), #* since the dropdown doesn't have a "See only" feature make the function it calls after a action reset the text
                    ft.DataCell(ft.Container(content=ft.Dropdown(hint_text=quantityDict[gameName],text_size=20,options=[ft.dropdown.Option(1),ft.dropdown.Option(2),ft.dropdown.Option(3),ft.dropdown.Option(4),ft.dropdown.Option(5),ft.dropdown.Option(6),ft.dropdown.Option(7),ft.dropdown.Option(8),ft.dropdown.Option(9),ft.dropdown.Option(10)],data=views.gamesView.gamesBought[i][1],on_change=lambda e: calculatePrize(e,router)),expand=True)),
                    ft.DataCell(ft.Text(round(float(views.gamesView.gamesBought[i][2])*float(quantityDict[gameName]),3))),
                    ft.DataCell(ft.IconButton(icon=ft.icons.CANCEL_PRESENTATION_OUTLINED,data=views.gamesView.gamesBought[i],on_click= lambda e: delete(e,router))),
                ]
            else:
                cells=[
                    ft.DataCell(ft.Text(views.gamesView.gamesBought[i][0])),
                    ft.DataCell(ft.Container(content=ft.Dropdown(hint_text="name",text_size=10,options=[ft.dropdown.Option(views.gamesView.gamesBought[i][1])],on_change= lambda e: Reload(e,router)),expand=True)), #* since the dropdown doesn't have a "See only" feature make the function it calls after a action reset the text
                    ft.DataCell(ft.Container(content=ft.Dropdown(hint_text=str(sum(1 for game in views.gamesView.gamesBought if game[1] == gameName)),text_size=20,options=[ft.dropdown.Option(1),ft.dropdown.Option(2),ft.dropdown.Option(3),ft.dropdown.Option(4),ft.dropdown.Option(5),ft.dropdown.Option(6),ft.dropdown.Option(7),ft.dropdown.Option(8),ft.dropdown.Option(9),ft.dropdown.Option(10)],data=views.gamesView.gamesBought[i][1],on_change=lambda e: calculatePrize(e,router)),expand=True)),
                    ft.DataCell(ft.Text(round(float(views.gamesView.gamesBought[i][2])*float(sum(1 for game in views.gamesView.gamesBought if game[1] == gameName)),3))),
                    ft.DataCell(ft.IconButton(icon=ft.icons.CANCEL_PRESENTATION_OUTLINED,data=views.gamesView.gamesBought[i],on_click= lambda e: delete(e,router))),
                ]
            DataRows.append(ft.DataRow(cells=cells))
        seenNames.append(views.gamesView.gamesBought[i][1])
    seenNames.clear()
    print(views.pizzaView.pizzasList)
    # Drinks bought logic
    for i in range(len(views.drinksView.drinksBought)):
        drinkName = views.drinksView.drinksBought[i][1]
        if views.drinksView.drinksBought[i][1] not in seenNames:
            if drinkName in quantityDict:
                cells=[
                    ft.DataCell(ft.Text(views.drinksView.drinksBought[i][0])),
                    ft.DataCell(ft.Container(content=ft.Dropdown(hint_text="name",text_size=10,options=[ft.dropdown.Option(views.drinksView.drinksBought[i][1])],on_change= lambda e: Reload(e,router)),expand=True)), #* since the dropdown doesn't have a "See only" feature make the function it calls after a action reset the text
                    ft.DataCell(ft.Container(content=ft.Dropdown(hint_text=quantityDict[drinkName],text_size=20,options=[ft.dropdown.Option(1),ft.dropdown.Option(2),ft.dropdown.Option(3),ft.dropdown.Option(4),ft.dropdown.Option(5),ft.dropdown.Option(6),ft.dropdown.Option(7),ft.dropdown.Option(8),ft.dropdown.Option(9),ft.dropdown.Option(10)],data=views.drinksView.drinksBought[i][1],on_change=lambda e: calculatePrize(e,router)),expand=True)),
                    ft.DataCell(ft.Text(round(float(views.drinksView.drinksBought[i][2])*float(quantityDict[drinkName]),3))),
                    ft.DataCell(ft.IconButton(icon=ft.icons.CANCEL_PRESENTATION_OUTLINED,data=views.drinksView.drinksBought[i],on_click= lambda e: delete(e,router))),
                ]
            else:
                cells=[
                    ft.DataCell(ft.Text(views.drinksView.drinksBought[i][0])),
                    ft.DataCell(ft.Container(content=ft.Dropdown(hint_text="name",text_size=10,options=[ft.dropdown.Option(views.drinksView.drinksBought[i][1])],on_change= lambda e: Reload(e,router)),expand=True)), #* since the dropdown doesn't have a "See only" feature make the function it calls after a action reset the text
                    ft.DataCell(ft.Container(content=ft.Dropdown(hint_text=str(sum(1 for drink in views.drinksView.drinksBought if drink[1] == drinkName)),text_size=20,options=[ft.dropdown.Option(1),ft.dropdown.Option(2),ft.dropdown.Option(3),ft.dropdown.Option(4),ft.dropdown.Option(5),ft.dropdown.Option(6),ft.dropdown.Option(7),ft.dropdown.Option(8),ft.dropdown.Option(9),ft.dropdown.Option(10)],data=views.drinksView.drinksBought[i][1],on_change=lambda e: calculatePrize(e,router)),expand=True)),
                    ft.DataCell(ft.Text(round(float(views.drinksView.drinksBought[i][2])*float(sum(1 for drink in views.drinksView.drinksBought if drink[1] == drinkName)),3))),
                    ft.DataCell(ft.IconButton(icon=ft.icons.CANCEL_PRESENTATION_OUTLINED,data=views.drinksView.drinksBought[i],on_click= lambda e: delete(e,router))),
                ]
            DataRows.append(ft.DataRow(cells=cells))
        seenNames.append(views.drinksView.drinksBought[i][1])
    seenNames.clear()
    print(views.pizzaView.pizzasList)
    ingredientsList = []
    ingredientStr = ""
    dropDownOptionsList = []
    for i in range(len(views.pizzaView.pizzasList)):
        ingredientsList.clear()
        print(views.pizzaView.pizzasList)
        for j in range(len(views.pizzaView.pizzasList[i][1])):
            ingredientsList.append((views.pizzaView.pizzasList[i][1][j]))
            ingredientStr += views.pizzaView.pizzasList[i][1][j]
        print(views.pizzaView.pizzasList)
        print(ingredientsList)
        print(ingredientStr)
        if views.pizzaView.pizzasList[i][1] not in seenNames:
            if ingredientStr in quantityDict:
                cells=[
                    ft.DataCell(ft.Text(views.pizzaView.pizzasList[i][0])),
                    ft.DataCell(ft.Container(content=ft.Dropdown(hint_text="Ingredients",text_size=10,options=[ft.dropdown.Option(ingredient) for ingredient in ingredientsList],on_change= lambda e: Reload(e,router)),expand=True)), #* since the dropdown doesn't have a "See only" feature make the function it calls after a action reset the text
                    ft.DataCell(ft.Container(content=ft.Dropdown(hint_text=quantityDict[ingredientStr],text_size=20,options=[ft.dropdown.Option(1),ft.dropdown.Option(2),ft.dropdown.Option(3),ft.dropdown.Option(4),ft.dropdown.Option(5),ft.dropdown.Option(6),ft.dropdown.Option(7),ft.dropdown.Option(8),ft.dropdown.Option(9),ft.dropdown.Option(10)],data=ingredientStr,on_change=lambda e: calculatePrize(e,router)),expand=True)),
                    ft.DataCell(ft.Text(round(float(views.pizzaView.pizzasList[i][2])*float(quantityDict[ingredientStr]),3))),
                    ft.DataCell(ft.IconButton(icon=ft.icons.CANCEL_PRESENTATION_OUTLINED,data=views.pizzaView.pizzasList[i],on_click= lambda e: delete(e,router))),
                ]
            else:
                print(ingredientStr)
                print
                cells=[
                    ft.DataCell(ft.Text(views.pizzaView.pizzasList[i][0])),
                    ft.DataCell(ft.Container(content=ft.Dropdown(hint_text="Ingredients",text_size=10,options=[ft.dropdown.Option(ingredient) for ingredient in ingredientsList],on_change= lambda e: Reload(e,router)),expand=True)), #* since the dropdown doesn't have a "See only" feature make the function it calls after a action reset the text
                    ft.DataCell(ft.Container(content=ft.Dropdown(hint_text=str(sum(1 for pizza in views.pizzaView.pizzasList if pizza[1] == views.pizzaView.pizzasList[i][1])),text_size=20,options=[ft.dropdown.Option(1),ft.dropdown.Option(2),ft.dropdown.Option(3),ft.dropdown.Option(4),ft.dropdown.Option(5),ft.dropdown.Option(6),ft.dropdown.Option(7),ft.dropdown.Option(8),ft.dropdown.Option(9),ft.dropdown.Option(10)],data=ingredientStr,on_change=lambda e: calculatePrize(e,router)),expand=True)),
                    ft.DataCell(ft.Text(round(float(views.pizzaView.pizzasList[i][2])*float(sum(1 for pizza in views.pizzaView.pizzasList if pizza[1] == views.pizzaView.pizzasList[i][1])),3))),
                    ft.DataCell(ft.IconButton(icon=ft.icons.CANCEL_PRESENTATION_OUTLINED,data=views.pizzaView.pizzasList[i],on_click= lambda e: delete(e,router))),
                ]
            print(views.pizzaView.pizzasList)
            DataRows.append(ft.DataRow(cells=cells))
            # print(ingredientStr)
        seenNames.append(views.pizzaView.pizzasList[i][1])

    router.controls[0].content.controls = [] # reseting all column controls
    #router.controls[0].content.controls.append(ft.Text("fewifew")) # appending to the column
    elementsToAppend = []
    router.controls[0].content.controls.append(# Creating a list of all the elements to append on the main column
        ft.DataTable(
            expand=True,
            width=600,
            columns=[
                ft.DataColumn(ft.Text("Item")),
                ft.DataColumn(ft.Text("More Info")),
                ft.DataColumn(ft.Text("Quantity")),
                ft.DataColumn(ft.Text("Prize"), numeric=True),
                ft.DataColumn(ft.Text("Remove"), numeric=True),
            ],
            rows=DataRows
        ) 
    )
    untaxedPrice = 0
    for i in range(len(router.controls[0].content.controls[0].rows)):
        print(router.controls[0].content.controls[0].rows[i].cells[3].content.value)
        untaxedPrice += router.controls[0].content.controls[0].rows[i].cells[3].content.value
    totalPrice = untaxedPrice * 1.1
    elementsToAppend.clear()
    elementsToAppend = [ft.Row(alignment=ft.MainAxisAlignment.END,controls=[
            ft.DataTable(divider_thickness=3,
                columns=[
                    ft.DataColumn(ft.Text("Untaxed Price"),numeric = True,),#tooltip="Price before the taxes are taken into account"),
                    ft.DataColumn(ft.Text("Taxed Price"), numeric= True,)#tooltip="The price after taking the taxes into account"),
                ],
                rows=[
                    ft.DataRow(
                        cells=[
                            ft.DataCell(ft.Text(round(untaxedPrice,3))),
                            ft.DataCell(ft.Text(round(totalPrice,3))),
                        ],
                    ),
                ],
            )
        ]),
        ft.Row(alignment=ft.MainAxisAlignment.SPACE_EVENLY,controls=[
            ft.FilledButton("Reload",on_click=lambda e: Reload(e,router)),
            ft.FilledButton("Pay for Cart",on_click=lambda e: pay(e,router))
        ])
    ]
    for element in elementsToAppend: # Appending all the elements
        router.controls[0].content.controls.append(element)
    router.update()

done = False
def cart_View(router):
    content = ft.Column([
        ft.DataTable(
            expand=True,
            width=600,
            columns=[
                ft.DataColumn(ft.Text("Item")),
                ft.DataColumn(ft.Text("More Info")),
                ft.DataColumn(ft.Text("Quantity")),
                ft.DataColumn(ft.Text("Prize"), numeric=True),
                ft.DataColumn(ft.Text("Remove"), numeric=True),
            ],
        ),
        ft.FilledButton("Reload",on_click=lambda e: Reload(e,router))
    ])
    return content


        #         ft.DataRow(
        #             cells=[
        #                 ft.DataCell(ft.Text("Pizza")),
        #                 ft.DataCell(ft.Container(content=ft.Dropdown(disabled=True,hint_text="Ingredients",text_size=10,options=[ft.dropdown.Option("ingredient 1"),ft.dropdown.Option("Ingredient 2"),ft.dropdown.Option("ingredient 3"),],),expand=True)), #* since the dropdown doesn't have a "See only" feature make the function it calls after a action reset the text
        #                 ft.DataCell(ft.Container(content=ft.Dropdown(hint_text="",text_size=20,options=[ft.dropdown.Option(" 1"),ft.dropdown.Option(" 2"),ft.dropdown.Option(" 3"),],),expand=True)),
        #                 ft.DataCell(ft.Text("1")),
        #                 ft.DataCell(ft.IconButton(icon=ft.icons.CANCEL_PRESENTATION_OUTLINED,on_click= lambda e: testlists(e))),
        #             ],
        #         ),
        #     ],
        # ),
        # ft.Row(alignment=ft.MainAxisAlignment.END,controls=[
        #     ft.DataTable(divider_thickness=3,
        #         columns=[
        #             ft.DataColumn(ft.Text("Untaxed Price"),numeric = True,),#tooltip="Price before the taxes are taken into account"),
        #             ft.DataColumn(ft.Text("Final Price"), numeric= True,)#tooltip="The price after taking the taxes into account"),
        #         ],
        #         rows=[
        #             ft.DataRow(
        #                 cells=[
        #                     ft.DataCell(ft.Text("43")),
        #                     ft.DataCell(ft.Text("50")),
        #                 ],
        #             ),
        #         ],
        #     )

        


    # print(views.gamesView.gamesBought)
    # for i in range(len(views.gamesView.gamesBought)):
    #     dropdownOptions.clear()
    #     for j in range(len(views.gamesView.gamesBought[i][1])):
    #         dropdownOptions.append(ft.dropdown.Option(views.gamesView.gamesBought[i][1][j]))
    #     DataRows.append(ft.DataRow(
    #         cells=[
    #             ft.DataCell(ft.Text(views.gamesView.gamesBought[i][0])),
    #             ft.DataCell(ft.Container(content=ft.Dropdown(hint_text="Ingredients",text_size=10,options=dropdownOptions),expand=True)), #* since the dropdown doesn't have a "See only" feature make the function it calls after a action reset the text
    #             ft.DataCell(ft.Container(content=ft.Dropdown(hint_text="",text_size=20,options=[ft.dropdown.Option("1"),ft.dropdown.Option("2"),ft.dropdown.Option("3"),ft.dropdown.Option("4"),ft.dropdown.Option("5"),ft.dropdown.Option("6"),ft.dropdown.Option("7"),ft.dropdown.Option("8"),ft.dropdown.Option("9"),ft.dropdown.Option("10")],),expand=True)),
    #             ft.DataCell(ft.Text("1")),
    #             ft.DataCell(ft.IconButton(icon=ft.icons.CANCEL_PRESENTATION_OUTLINED,on_click= lambda e: testlists(e))),
    #         ],
    #     ),)
    #     print(DataRows)
    # print(DataRows)