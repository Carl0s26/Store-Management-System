
#** Importing views functions

import flet as ft
from views.drinksView import drinks_View
from views.gamesView import games_View
from views.pizzaView import pizza_View
from views.homeView import home_View
from views.offersView import offers_View
from views.loginView import profile_View
from views.cartView import cart_View
from views.settingsView import settings_View
from views.addView import add_View
from views.loginView import login_View
from views.signUpView import signUp_View

class Router:
    def __init__(self, page, ft):
        self.page = page
        self.ft = ft
        self.routes = {
            "/" : home_View(page),
            "/games" : games_View(page),
            "/pizza" : pizza_View(page),
            "/drinks" : drinks_View(page),
            "/offers" : offers_View(page),
            "/profile" : profile_View(page),
            "/settings" : settings_View(page),
            "/cart" : cart_View(page),
            "/add" : add_View(page),
            "/login": login_View(page),
            "/signUp": signUp_View(page),
        }
        self.body = ft.Container(content=self.routes['/'])

    def route_change(self, route):
        self.body.content = self.routes[route.route]
        self.body.update()

    def update(self): 
        self.page.update()