import flet as ft
from theme import StationeryTheme
from views.home_view import HomeView
from views.registration_view import RegistrationView
from views.history_view import HistoryView
from views.dashboard_view import DashboardView
import asyncio

INACTIVITY_TIMEOUT = 5 * 60  # 5 minutos em segundos

async def main(page: ft.Page):
    page.title = "App Vendeu Amor"
    page.fonts = StationeryTheme.get_fonts()
    page.theme = StationeryTheme.get_theme()
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 0
    
    # Configuração de Janela Mobile
    page.window.width = 390
    page.window.height = 800
    page.window.resizable = False

    # --- Timer de Inatividade ---
    inactivity_task = None

    async def reset_inactivity_timer():
        nonlocal inactivity_task
        if inactivity_task:
            inactivity_task.cancel()
        inactivity_task = asyncio.create_task(inactivity_handler())

    async def inactivity_handler():
        await asyncio.sleep(INACTIVITY_TIMEOUT)
        # Só redireciona se não estiver já na Home
        if page.route != "/":
            print("Inactividade detectada — voltando para Home")
            await route_change_manual("/")

    async def route_change_manual(route):
        page.views.clear()
        if route == "/":
            view = HomeView(page).render()
        elif route == "/register":
            view = RegistrationView(page).render()
        elif route == "/history":
            view = HistoryView(page).render()
        elif route == "/dashboard":
            view = DashboardView(page).render()
        else:
            view = ft.View(route="/404", controls=[ft.Text("404")])
        page.views.append(view)
        page.route = route
        page.update()
        await reset_inactivity_timer()

    async def route_change(e):
        route = page.route
        print(f"--- Route Change: {route} ---")
        page.views.clear()
        
        if route == "/":
            view = HomeView(page).render()
        elif route == "/register":
            view = RegistrationView(page).render()
        elif route == "/history":
            view = HistoryView(page).render()
        elif route == "/dashboard":
            view = DashboardView(page).render()
        else:
            view = ft.View(route="/404", controls=[ft.Text("404")])

        page.views.append(view)
        page.update()
        print(f"--- Rendered: {len(page.views)} views ---")
        await reset_inactivity_timer()

    async def view_pop(e):
        if len(page.views) > 1:
            page.views.pop()
            top_view = page.views[-1]
            await page.push_route(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop

    
    # Sempre inicia na Home
    if page.route == "/":
        await route_change(None)
    else:
        await page.push_route("/")

if __name__ == "__main__":
    ft.run(main)
