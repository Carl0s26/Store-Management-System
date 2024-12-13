import flet as ft

pizzasList = [] #* for conflicts when deleting in cart maybe change this to have the value of watever is returned after a function in the cart view
size = None
crust = None
sauce = None
ingredients = []

# class Pizza:
#     def __init__(self,size,crust,ingredients):
#         self.size = size
#         self.crust = crust
#         self.ingredients = ingredients

def createPizza(e,feedbackBar,router): # adds the pizza to the lists
    size = router.controls[0].content.controls[2].controls[0].value
    crust = router.controls[0].content.controls[2].controls[1].value
    sauce = router.controls[0].content.controls[2].controls[2].value
    ingredients.append(size)
    ingredients.append(crust)
    ingredients.append(sauce)
    print(ingredients)
    price = 0
    price += ((len(ingredients)-3)*0.5)
    if size == "Small":
        price += 10
    elif size == "Medium":
        price +=12
    else:
        price += 15
    pizzasList.append(["Pizza",[],price])
    ingredients.sort()
    for ingredient in ingredients:
        pizzasList[len(pizzasList)-1][1].append(ingredient)
    print(pizzasList)
    feedbackBar.open = True
    router.update()
    for i in range(len(router.controls[0].content.controls[4].controls[0].controls)): # reseting the ingredients value on the view
        if router.controls[0].content.controls[4].controls[0].controls[i].value == True:
            router.controls[0].content.controls[4].controls[0].controls[i].value = False
            # router.controls[0].content.controls[4].controls[1].controls[i].update()
    for i in range(len(router.controls[0].content.controls[4].controls[0].controls)):
        if router.controls[0].content.controls[4].controls[1].controls[i].value == True:
            router.controls[0].content.controls[4].controls[1].controls[i].value = False
            # router.controls[0].content.controls[4].controls[1].controls[i].update()
    ingredients.clear()
    router.update()


def addIngredient(e): # customizes pizza
    if e.control.value:
        ingredients.append(e.control.data)
    else:
        ingredients.remove(e.control.data)
    print(f'ingredients: {ingredients}')



    #* Maybe create a list of pizza objects to store the pizza info.

def pizza_View(router):
    #* defining view content
    feedbackBar = ft.SnackBar(content =ft.Text("Item added successfully to your cart",size=20),bgcolor=ft.colors.BLACK)
    router.overlay.append(feedbackBar)
    content = ft.Column([
        ft.Text("Make Your Own Pizza", size=40, weight = "bold"),
        ft.Row(
                alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                controls =[
                ft.Text("Size",size=25),
                ft.Text("Crust",size=25),
                ft.Text("Sauce",size=25),
        ]),
        ft.Row(
                alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                controls=[
                ft.Dropdown( 
                    value = "Small",
                    width= 140,
                    bgcolor="green",
                    options=[
                        ft.dropdown.Option("Small"),
                        ft.dropdown.Option("Medium"),
                        ft.dropdown.Option("Big"),
                    ]
                ),
                ft.Dropdown(
                    value= "Thin Crust",
                    width=140,
                    bgcolor="white",
                    options=[
                        ft.dropdown.Option("Thin Crust"),
                        ft.dropdown.Option("Thick Crust"),
                        ft.dropdown.Option("Stuffed Crust"),
                    ]
                ),
                ft.Dropdown(
                    value = "Red Sauce",
                    width=140,
                    bgcolor="red",
                    options=[
                        ft.dropdown.Option("Red Sauce"),
                        ft.dropdown.Option("White Sauce"),
                        ft.dropdown.Option("Pesto Sauce"),
                        ft.dropdown.Option("BBQ Sauce"),
                    ]
                ),
        ]),
        ft.Row(controls=[ft.Text("Ingredients",size=30)],alignment=ft.MainAxisAlignment.CENTER),
        ft.Row(alignment=ft.MainAxisAlignment.SPACE_AROUND,controls=[
            ft.Column(controls=[
                ft.CupertinoCheckbox(label="Pepperoni", value=False, data="Pepperoni",on_change=addIngredient),
                ft.CupertinoCheckbox(label="Black Olives", value=False, data="Black Olives",on_change=addIngredient),
                ft.CupertinoCheckbox(label="Bacon", value=False, data="Bacon",on_change=addIngredient),
                ft.CupertinoCheckbox(label="Pineapple", value=False, data="Pineapple",on_change=addIngredient),
                ft.CupertinoCheckbox(label="Jalapeños", value=False, data="Jalapeños",on_change=addIngredient),
                ft.CupertinoCheckbox(label="Salami", value=False, data="Salami",on_change=addIngredient),
                ft.CupertinoCheckbox(label="Oregano", value=False, data="Oregano",on_change=addIngredient),
                ft.CupertinoCheckbox(label="Turkey", value=False, data="Turkey",on_change=addIngredient),
                ft.CupertinoCheckbox(label="Caramelized Onions", value=False, data="Caramelized Onions",on_change=addIngredient),
            ]),
            ft.Column([
                ft.CupertinoCheckbox(label="Mushrooms", value=False, data="Mushrooms",on_change=addIngredient),
                ft.CupertinoCheckbox(label="Green Peppers", value=False, data="Green Peppers",on_change=addIngredient),
                ft.CupertinoCheckbox(label="Italian Sausage", value=False, data="Italian Sausage",on_change=addIngredient),
                ft.CupertinoCheckbox(label="Ham", value=False, data="Ham",on_change=addIngredient),
                ft.CupertinoCheckbox(label="Spinach", value=False, data="Spinach",on_change=addIngredient),
                ft.CupertinoCheckbox(label="Chicken", value=False, data="Chicken",on_change=addIngredient),
                ft.CupertinoCheckbox(label="Anchovies", value=False, data="Anchovies",on_change=addIngredient),
                ft.CupertinoCheckbox(label="Sun-Dried Tomatoes", value=False, data="Sun-Dried Tomatoes",on_change=addIngredient),
                ft.CupertinoCheckbox(label="Roasted Garlic", value=False, data="Roasted Garlic",on_change=addIngredient),
            ]),
        ]),
    
    ft.Row(controls=[ft.ElevatedButton(text="Add Pizza",on_click=lambda e: createPizza(e,feedbackBar,router))], alignment= ft.MainAxisAlignment.CENTER)
    
    ],alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )
    return content