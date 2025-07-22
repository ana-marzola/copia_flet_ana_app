import flet as ft
from src.views.login_view import LoginView
from src.views.menu_view import MenuView
from src.views.admin_view import AdminView
from src.components.appbar import AppBar
from src.components.drawer import NavigationDrawer
from src.data.database import Database
import json

class RestauranteApp:
    def __init__(self):
        self.page = None
        self.current_user = None
        self.db = Database()
        self.cart_items = []
        
    def main(self, page: ft.Page):
        self.page = page
        self.setup_page()
        self.show_login()
        
    def setup_page(self):
        """Configuración inicial de la página"""
        self.page.title = "Restaurante Appbar"
        self.page.theme_mode = ft.ThemeMode.LIGHT
        self.page.window_width = 400
        self.page.window_height = 800
        self.page.padding = 20
        self.page.spacing = 20
        
    def show_login(self):
        """Muestra la vista de login"""
        login_view = LoginView(self.on_login_success)
        self.page.views.clear()
        self.page.views.append(
            ft.View(
                "/",
                [login_view.build()],
                appbar=ft.AppBar(title=ft.Text("Iniciar Sesión"))
            )
        )
        self.page.update()
        
    def on_login_success(self, user_data):
        """Callback cuando el login es exitoso"""
        self.current_user = user_data
        # Todos los usuarios van al menú, los admins tendrán acceso a la pestaña de administración
        self.show_menu_view()
            
    def show_menu_view(self):
        """Muestra la vista del menú para clientes"""
        menu_view = MenuView(self.current_user, self.cart_items, self.on_logout, self.update_cart, self.page)
        self.page.views.clear()
        self.page.views.append(
            ft.View(
                "/menu",
                [menu_view.build()],
                appbar=AppBar(self.current_user, self.on_logout).build(),
                drawer=NavigationDrawer(self.current_user, self.on_logout).build()
            )
        )
        self.page.update()
        # Inicializar datos después de que la vista esté construida
        menu_view.initialize_data()
        
    def update_cart(self, new_cart_items):
        """Actualiza el carrito desde la vista del menú"""
        self.cart_items = new_cart_items
        
    def show_admin_view(self):
        """Muestra la vista de administrador"""
        admin_view = AdminView(self.current_user, self.on_logout, self.page)
        self.page.views.clear()
        self.page.views.append(
            ft.View(
                "/admin",
                [admin_view.build()],
                appbar=AppBar(self.current_user, self.on_logout).build(),
                drawer=NavigationDrawer(self.current_user, self.on_logout).build()
            )
        )
        self.page.update()
        # Inicializar datos después de que la vista esté construida
        admin_view.initialize_data()
        
    def on_logout(self, e=None):
        """Cierra sesión y vuelve al login"""
        self.current_user = None
        self.cart_items = []
        self.show_login()

def main(page: ft.Page):
    app = RestauranteApp()
    app.main(page)

if __name__ == "__main__":
    ft.app(target=main, view=ft.AppView.FLET_APP, assets_dir="assets")
