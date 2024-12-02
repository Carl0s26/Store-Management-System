
#** Importing views functions

import flet as ft
from views.drinksView import drinks_View
from views.gamesView import games_View
from views.pizzaView import pizza_View
from views.homeView import home_View

class Router:
    def __init__(self, page, ft):
        self.page = page
        self.ft = ft
        self.routes = {
            "/" : home_View(page),
            "/games" : games_View(page),
            "/pizza" : pizza_View(page),
            "/drinks" : drinks_View(page),
        }
        self.body = ft.Container(content=self.routes['/'])

    def route_change(self, route):
        self.body.content = self.routes[route.route]
        self.body.update()