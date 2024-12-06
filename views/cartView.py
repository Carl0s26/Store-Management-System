import flet as ft

#! FINISH the view desing  

def cart_View(router):
    #* defining view content
    content = ft.Column([
        ft.Text("Cart",size=30),
        ft.DataTable(   
            columns=[
                ft.DataColumn(ft.Text("Item Name")),
                ft.DataColumn(ft.Text("Ingridients")),
                ft.DataColumn(ft.Text("Quantity"),numeric = True),
                ft.DataColumn(ft.Text("Untaxed Price"),numeric = True,tooltip="Price before the taxes are taken into account"),
                ft.DataColumn(ft.Text("Taxed Price"), numeric= True,tooltip="The price after taking the taxes into account"),
            ],
            rows=[
                
                #* Sacar datos de una lista no del sql (no deberia estar en el sql si el cliente no la compra.)

                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text("Pizza")),
                        ft.DataCell(ft.Dropdown(hint_text="view",text_size=10,options=[ft.dropdown.Option("ingredient 1"),ft.dropdown.Option("Ingredient 2"),ft.dropdown.Option("ingredient 3"),],)), # make dropdown
                        ft.DataCell(ft.Text("1")),
                        ft.DataCell(ft.Text("43")),
                        ft.DataCell(ft.Text("50")),
                    ],
                ),
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text("cocacola")),
                        ft.DataCell(ft.Text("")),
                        ft.DataCell(ft.Text("4")),
                        ft.DataCell(ft.Text("36")),
                        ft.DataCell(ft.Text("44")),
                    ],
                ),
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text("Axel")),
                        ft.DataCell(ft.Text("algodon")),
                        ft.DataCell(ft.Text("1")),
                        ft.DataCell(ft.Text("390")),
                        ft.DataCell(ft.Text("500")),
                    ],
                ),
            ],
        ),

    #todo mostrar direccion del cliente

    #todo mostrar numero de telefono

    #todo boton para pagar que te vacie el carrito y confirme que todo fue bien

    ])
    return content