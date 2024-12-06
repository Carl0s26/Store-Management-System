import flet as ft


#! MISSING: text aligned, padding for correctly aligning ingredients



def addIngredient(e):
    print(e)

    #todo search how to make the checks work.
    #* Could give the checkboxes names.

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
                width= 130,
                options=[
                        ft.dropdown.Option("Small"),
                        ft.dropdown.Option("Medium"),
                        ft.dropdown.Option("Big"),
                ]),
                ft.Dropdown(
                width=130,
                options=[
                        ft.dropdown.Option("Thin Crust"),
                        ft.dropdown.Option("Thick Crust"),
                        ft.dropdown.Option("Stuffed Crust"),
                ]),
                ft.Dropdown(
                width=130,
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
                ft.CupertinoCheckbox(label="Pepperoni"),
                ft.CupertinoCheckbox(label="Onions"),
                ft.CupertinoCheckbox(label="Black Olives"),
                ft.CupertinoCheckbox(label="Bacon"),
                ft.CupertinoCheckbox(label="Pineapple"),
                ft.CupertinoCheckbox(label="Garlic"),
                ft.CupertinoCheckbox(label="Tomato Slices"),
                ft.CupertinoCheckbox(label="Jalapeños"),
                ft.CupertinoCheckbox(label="Artichokes"),
                ft.CupertinoCheckbox(label="Arugula"),
                ft.CupertinoCheckbox(label="Broccoli"),
                ft.CupertinoCheckbox(label="Zucchini"),
                ft.CupertinoCheckbox(label="Salami"),
                ft.CupertinoCheckbox(label="Oregano"),
                ft.CupertinoCheckbox(label="Truffle Oil"),
                ft.CupertinoCheckbox(label="Ground Beef"),
                ft.CupertinoCheckbox(label="Turkey"),
                ft.CupertinoCheckbox(label="Caramelized Onions"),
                ft.CupertinoCheckbox(label="Chili Flakes"),
                ft.CupertinoCheckbox(label="Sour Cream")
            ]),
            ft.Column([
                ft.CupertinoCheckbox(label="Mushrooms"),
                ft.CupertinoCheckbox(label="Green Peppers"),
                ft.CupertinoCheckbox(label="Italian Sausage"),
                ft.CupertinoCheckbox(label="Ham"),
                ft.CupertinoCheckbox(label="Spinach"),
                ft.CupertinoCheckbox(label="Basil"),
                ft.CupertinoCheckbox(label="Chicken"),
                ft.CupertinoCheckbox(label="Anchovies"),
                ft.CupertinoCheckbox(label="Sun-Dried Tomatoes"),
                ft.CupertinoCheckbox(label="Red Peppers"),
                ft.CupertinoCheckbox(label="Eggplant"),
                ft.CupertinoCheckbox(label="Prosciutto"),
                ft.CupertinoCheckbox(label="Crushed Red Pepper"),
                ft.CupertinoCheckbox(label="Thyme"),
                ft.CupertinoCheckbox(label="Olive Oil"),
                ft.CupertinoCheckbox(label="Sweet Corn"),
                ft.CupertinoCheckbox(label="Chorizo"),
                ft.CupertinoCheckbox(label="Tofu"),
                ft.CupertinoCheckbox(label="Roasted Garlic"),
                ft.CupertinoCheckbox(label="Lemon Zest")
            ]),
        ]),
    
    ft.Row(controls=[ft.ElevatedButton(text="Add Pizza",on_click=lambda _: router.go('/'))], alignment= ft.MainAxisAlignment.CENTER)
    
    ],
    )
    return content