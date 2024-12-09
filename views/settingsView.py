import flet as ft
#! FINISH the view desing

def settings_View(router):
    #from main import volumeChange # imported inside the function due to a "Circular import" issue
    #* defining view content

    content = ft.Column([
        ft.Column(controls=[
            ft.Text("Contact info: 809-214-8977"),
            ft.Text("operational hours"),
            ft.Text("Clear Cart"),
            ft.Text("delivery instroctions"),
            ft.Slider(
                min=0,
                max=1,
                value=0.5,
                divisions=10,
                #on_change=volumeChange,
            ),
            ft.Text("Save button"),
        ])
    

        


    ])
    return content