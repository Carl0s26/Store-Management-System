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

from views.loginView import profile_View

api_thread = threading.Thread(target=run_api, daemon=True)
api_thread.start()
from userControls.userControl import lowerNavBar
from userControls.userControl import upperNavBar
import pygame # pip install pygame

#? flet run main.py -r 


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

    def on_route_change(route):
        if page.route == "/login" or page.route == "/signUp":
            page.appbar = None
            page.bottom_appbar = None
        else:
            page.appbar = upperNavBar(page)
            page.bottom_appbar = lowerNavBar(page)
        
        if page.route == "/profile":
            id_content = profile_View(router)
            router.body.content = (id_content)
        
        router.route_change(route)
        page.update()

    page.on_route_change = on_route_change
    router.page = page
    
    page.go('/login')
    # page.go('/')

ft.app(target=main, assets_dir="assets")