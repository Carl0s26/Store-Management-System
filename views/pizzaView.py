import flet as ft


#! MISSING: text aligned, padding for correctly aligning ingredients

def pizza_View(router):
    #* defining view content

    content = ft.Column([
        ft.Row(
                alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                controls =[
                ft.Text("Size",size=30),
                ft.Text("Crust",size=30),
                ft.Text("Sauce",size=30),
        ]),
        ft.Row(
                alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                controls=[
                ft.Dropdown( 
                width=100,
                options=[
                        ft.dropdown.Option("Small"),
                        ft.dropdown.Option("Medium"),
                        ft.dropdown.Option("Big"),
                ]),
                ft.Dropdown(
                width=100,
                options=[
                        ft.dropdown.Option("Thin Crust"),
                        ft.dropdown.Option("Thick Crust"),
                        ft.dropdown.Option("Stuffed Crust"),
                ]),
                ft.Dropdown(
                width=100,
                options=[
                        ft.dropdown.Option("Red Sauce"),
                        ft.dropdown.Option("White Sauce"),
                        ft.dropdown.Option("Pesto Sauce"),
                        ft.dropdown.Option("BBQ Sauce"),
                ]),
        ]),
        ft.Text("Ingredients",size=30),
        ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_AROUND,
                controls=[
                        ft.CupertinoCheckbox(label="Pepperoni"),  
                        ft.CupertinoCheckbox(label="Mushrooms"),
                ]  
        ),
        ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_AROUND,
            controls=[
                ft.CupertinoCheckbox(label="Onions"),
                ft.CupertinoCheckbox(label="Green Peppers"),
            ]
        ),
        ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_AROUND,
            controls=[
                ft.CupertinoCheckbox(label="Black Olives"),
                ft.CupertinoCheckbox(label="Italian Sausage"),
            ]
        ),
        ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_AROUND,
            controls=[
                ft.CupertinoCheckbox(label="Bacon"),
                ft.CupertinoCheckbox(label="Ham"),
            ]
        ),
        ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_AROUND,
            controls=[
                ft.CupertinoCheckbox(label="Pineapple"),
                ft.CupertinoCheckbox(label="Spinach"),
            ]
        ),
        ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_AROUND,
            controls=[
                ft.CupertinoCheckbox(label="Garlic"),
                ft.CupertinoCheckbox(label="Basil"),
            ]
        ),
        ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_AROUND,
            controls=[
                ft.CupertinoCheckbox(label="Tomato Slices"),
                ft.CupertinoCheckbox(label="Chicken"),
            ]
        ),
        ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_AROUND,
            controls=[
                ft.CupertinoCheckbox(label="Jalapeños"),
                ft.CupertinoCheckbox(label="Anchovies"),
            ]
        ),
        ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_AROUND,
            controls=[
                ft.CupertinoCheckbox(label="Artichokes"),
                ft.CupertinoCheckbox(label="Sun-Dried Tomatoes"),
            ]
        ),
        ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_AROUND,
            controls=[
                ft.CupertinoCheckbox(label="Arugula"),
                ft.CupertinoCheckbox(label="Red Peppers"),
            ]
        ),
        ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_AROUND,
            controls=[
                ft.CupertinoCheckbox(label="Broccoli"),
                ft.CupertinoCheckbox(label="Eggplant"),
            ]
        ),
        ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_AROUND,
            controls=[
                ft.CupertinoCheckbox(label="Zucchini"),
                ft.CupertinoCheckbox(label="Prosciutto"),
            ]
        ),
        ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_AROUND,
            controls=[
                ft.CupertinoCheckbox(label="Salami"),
                ft.CupertinoCheckbox(label="Crushed Red Pepper"),
            ]
        ),
        ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_AROUND,
            controls=[
                ft.CupertinoCheckbox(label="Oregano"),
                ft.CupertinoCheckbox(label="Thyme"),
            ]
        ),
        ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_AROUND,
            controls=[
                ft.CupertinoCheckbox(label="Truffle Oil"),
                ft.CupertinoCheckbox(label="Olive Oil"),
            ]
        ),
        ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_AROUND,
            controls=[
                ft.CupertinoCheckbox(label="Capers"),
                ft.CupertinoCheckbox(label="Sweet Corn"),
            ]
        ),
        ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_AROUND,
            controls=[
                ft.CupertinoCheckbox(label="Ground Beef"),
                ft.CupertinoCheckbox(label="Chorizo"),
            ]
        ),
        ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_AROUND,
            controls=[
                ft.CupertinoCheckbox(label="Turkey"),
                ft.CupertinoCheckbox(label="Tofu"),
            ]
        ),
        ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_AROUND,
            controls=[
                ft.CupertinoCheckbox(label="Caramelized Onions"),
                ft.CupertinoCheckbox(label="Roasted Garlic"),
            ]
        ),
        ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_AROUND,
            controls=[
                ft.CupertinoCheckbox(label="Chili Flakes"),
                ft.CupertinoCheckbox(label="Lemon Zest"),
            ]
        ),
        ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_AROUND,
            controls=[
                ft.CupertinoCheckbox(label="Sour Cream"),
            ]
        ),  
    ],
    scroll=True)
    return content