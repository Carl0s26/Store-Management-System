import asyncio
import platform

if platform.system() == "Darwin":
    import uvloop
    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

import flet as ft
import threading
from deliveryApi import run_api
from views.routes import Router
from userControls.userControl import lowerNavBar, upperNavBar

api_thread = threading.Thread(target=run_api, daemon=True)
api_thread.start()

def main(page: ft.Page):
    router = Router(page, ft)
    page.theme_mode = ft.ThemeMode.LIGHT
    page.title = 'Shop name'
    page.window.width = 600
    page.window.height = 800
    page.bgcolor = '#c8eed8'
    page.scroll = True
    page.window.resizable = False
    page.appbar = upperNavBar(page)
    page.bottom_appbar = lowerNavBar(page)
    page.on_route_change = router.route_change
    router.page = page
    page.add(
        router.body,
    )
    page.go('/')

ft.app(target=main, assets_dir="assets")