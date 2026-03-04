import flet as ft
from theme import StationeryTheme
import asyncio

class HomeView:
    def __init__(self, page: ft.Page):
        self.page = page

    def render(self):
        return ft.View(
            route="/",
            controls=[
                ft.Container(
                    expand=True,
                    alignment=ft.Alignment.CENTER,
                    padding=20,
                    content=ft.Column(
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        spacing=30,
                        controls=[
                            ft.Icon(ft.Icons.FAVORITE, color=StationeryTheme.PRIMARY, size=48),
                            ft.Column(
                                spacing=0,
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                controls=[
                                    ft.Text(
                                        "Vendeu",
                                        size=42,
                                        font_family=StationeryTheme.HEADING_FONT,
                                        color=StationeryTheme.TEXT_PRIMARY,
                                        text_align=ft.TextAlign.CENTER,
                                    ),
                                    ft.Text(
                                        "Amor?",
                                        size=64,
                                        font_family=StationeryTheme.ACCENT_FONT,
                                        color=StationeryTheme.PRIMARY,
                                        text_align=ft.TextAlign.CENTER,
                                    ),
                                ]
                            ),
                            ft.Container(height=20),
                            ft.Button(
                                content=ft.Container(
                                    content=ft.Text("SIM, Vendi!", size=20, font_family=StationeryTheme.BODY_FONT, weight=ft.FontWeight.W_500),
                                    padding=ft.Padding.symmetric(horizontal=40, vertical=15),
                                ),
                                style=ft.ButtonStyle(
                                    color=StationeryTheme.SURFACE,
                                    bgcolor=StationeryTheme.PRIMARY,
                                    shape=ft.RoundedRectangleBorder(radius=30),
                                ),
                                on_click=lambda _: asyncio.create_task(self.page.push_route("/register"))
                            ),
                            ft.TextButton(
                                "Ver Histórico",
                                style=ft.ButtonStyle(color=StationeryTheme.TEXT_SECONDARY),
                                on_click=lambda _: asyncio.create_task(self.page.push_route("/history"))
                            ),
                            ft.TextButton(
                                "📊 Dashboard",
                                style=ft.ButtonStyle(color=StationeryTheme.TEXT_ACCENT),
                                on_click=lambda _: asyncio.create_task(self.page.push_route("/dashboard"))
                            ),
                        ]
                    )
                )
            ],
            bgcolor=StationeryTheme.BACKGROUND
        )
