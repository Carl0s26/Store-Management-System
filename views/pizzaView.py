import flet as ft

pizzasList = [] #* for conflicts when deleting in cart maybe change this to have the value of watever is returned after a function in the cart view
size = None
crust = None
sauce = None
ingredients = []

class Pizza:
    def __init__(self,size,crust,ingredients):
        self.size = size
        self.crust = crust
        self.ingredients = ingredients

def createPizza(router): # adds the pizza to the lists
    print("Arrived here")
    pizzasList.append(Pizza(size=size,crust=crust,ingredients=ingredients))
    print(pizzasList)
    router.go('/')

def addIngredient(e): # customizes pizza
    if e.control.value:
        ingredients.append(e.control.data)
    else:
        ingredients.remove(e.control.data)
    print(f'ingredients: {ingredients}')

    #todo search how to make the checks work.
    #* Maybe create a list of pizza objects to store the pizza info.

def pizza_View(router):
    #* defining view content

    content = ft.Column([
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
                width= 140,
                options=[
                        ft.dropdown.Option("Small"),
                        ft.dropdown.Option("Medium"),
                        ft.dropdown.Option("Big"),
                ]),
                ft.Dropdown(
                width=140,
                options=[
                        ft.dropdown.Option("Thin Crust"),
                        ft.dropdown.Option("Thick Crust"),
                        ft.dropdown.Option("Stuffed Crust"),
                ]),
                ft.Dropdown(
                width=140,
                options=[
                        ft.dropdown.Option("Red Sauce"),
                        ft.dropdown.Option("White Sauce"),
                        ft.dropdown.Option("Pesto Sauce"),
                        ft.dropdown.Option("BBQ Sauce"),
                ]),
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
    
    ft.Row(controls=[ft.ElevatedButton(text="Add Pizza",on_click=lambda e: createPizza(router))], alignment= ft.MainAxisAlignment.CENTER)
    
    ],
    )
    return content