import flet as ft
from views.routes import Router
from userControls.userControl import NavBar

def main(page: ft.Page):
    router = Router(page, ft)
    page.title = 'Amason'
    page.window.width = 900
    page.window.height = 900
    page.bgcolor = ft.colors.GREY_700
    page.appbar = NavBar(page)
    page.on_route_change = router.route_change
    router.page = page
    page.add(
        router.body
    )
    page.go('/')

ft.app(target=main, assets_dir="assets")