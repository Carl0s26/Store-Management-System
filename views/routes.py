
#** Importing views functions

import flet as ft
from views.drinksView import drinks_View
from views.gamesView import games_View
from views.pizzaView import pizza_View
from views.homeView import home_View
from views.offertsView import offerts_View
from views.profileView import profile_View
from views.cartView import cart_View
from views.settingsView import settings_View

class Router:
    def __init__(self, page, ft):
        self.page = page
        self.ft = ft
        self.routes = {
            "/" : home_View(page),
            "/games" : games_View(page),
            "/pizza" : pizza_View(page),
            "/drinks" : drinks_View(page),
            "/offerts" : offerts_View(page),
            "/profile" : profile_View(page),
            "/settings" : settings_View(page),
            "/cart" : cart_View(page),
        }
        self.body = ft.Container(content=self.routes['/'])

    def route_change(self, route):
        self.body.content = self.routes[route.route]
        self.body.update()