import flet as ft

#! FINISH the view desing

#! It should allow the user to change their direction/other things and it would automatically update on the sql



def profile_View(router):
    #* defining view content
    
    content = ft.Column([
        ft.Text("Sign Up",size=30),
        ft.Text("Username or email: "),
        ft.IconButton(ft.icons.SHOPPING_CART,icon_size = 30, on_click=lambda _: page.go('/cart')),
        ft.Text("Password: "),
        ft.IconButton(ft.icons.PERSON_ADD_ALT_ROUNDED,icon_size = 30, on_click=lambda _: page.go('/profile')),
        ft.Text("New to shop?: "),
        ft.Text("Create an Account (This is a button): "),

    ])
    return content