import flet as ft
import threading
from deliveryApi import run_api
from views.routes import Router
from userControls.userControl import lowerNavBar
from userControls.userControl import upperNavBar


# def volumeChange(e):
#     print(e.control.value)
#     pass
#     # change volume

def main(page: ft.Page):
    router = Router(page, ft)
    page.title = 'Shop name'
    page.window.width = 600
    page.window.height = 800
    page.bgcolor = '#808080'
    page.scroll = True
    page.appbar = upperNavBar(page)
    page.bottom_appbar = lowerNavBar(page)
    page.on_route_change = router.route_change
    router.page = page
    page.add(
        router.body,
    )
    page.go('/')
    
    api_thread = threading.Thread(target=run_api, daemon=True)
    api_thread.start()
    

ft.app(target=main, assets_dir="assets")