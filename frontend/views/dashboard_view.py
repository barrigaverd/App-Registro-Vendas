import flet as ft
from theme import StationeryTheme
from services.api_service import ApiService
import asyncio

class DashboardView:
    def __init__(self, page: ft.Page):
        self.page = page
        self.total_text = ft.Text("R$ 0,00", size=32, font_family=StationeryTheme.HEADING_FONT, weight=ft.FontWeight.W_600, color=StationeryTheme.TEXT_PRIMARY)
        self.items_text = ft.Text("0 itens", size=20, font_family=StationeryTheme.BODY_FONT, color=StationeryTheme.TEXT_SECONDARY)
        self.top_product_text = ft.Text("—", size=18, font_family=StationeryTheme.BODY_FONT, color=StationeryTheme.TEXT_PRIMARY, weight=ft.FontWeight.W_600)
        self.recent_list = ft.Column(spacing=10)

    async def load_data(self):
        try:
            vendas = await ApiService.get_sales_today()
            if not vendas:
                self.total_text.value = "R$ 0,00"
                self.items_text.value = "Nenhuma venda hoje"
                self.top_product_text.value = "—"
                self.page.update()
                return

            total = sum(v["valor"] * v["quantidade"] for v in vendas)
            total_items = sum(v["quantidade"] for v in vendas)
            top = max(vendas, key=lambda v: v["valor"] * v["quantidade"])

            self.total_text.value = f"R$ {total:.2f}"
            self.items_text.value = f"{total_items} {'item' if total_items == 1 else 'itens'} vendidos"
            self.top_product_text.value = top["nome"]

            # Últimas 3 vendas
            self.recent_list.controls.clear()
            for sale in vendas[-3:][::-1]:
                self.recent_list.controls.append(
                    ft.Container(
                        bgcolor=StationeryTheme.SURFACE,
                        border_radius=12,
                        padding=12,
                        border=ft.Border.all(1, StationeryTheme.BORDER_LIGHT),
                        content=ft.Row(
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                            controls=[
                                ft.Text(sale["nome"], font_family=StationeryTheme.BODY_FONT, color=StationeryTheme.TEXT_PRIMARY, size=14),
                                ft.Text(f"R$ {sale['valor'] * sale['quantidade']:.2f}", font_family=StationeryTheme.BODY_FONT, color=StationeryTheme.PRIMARY, size=14, weight=ft.FontWeight.W_600),
                            ]
                        )
                    )
                )
            self.page.update()
        except Exception as ex:
            self.total_text.value = "Erro ao carregar"
            self.page.update()

    def _metric_card(self, icon, label, value_widget, color=None):
        return ft.Container(
            bgcolor=StationeryTheme.SURFACE,
            border_radius=20,
            padding=20,
            shadow=ft.BoxShadow(spread_radius=1, blur_radius=12, color=ft.Colors.with_opacity(0.06, ft.Colors.BLACK), offset=ft.Offset(0, 4)),
            border=ft.Border.all(1, StationeryTheme.BORDER_LIGHT),
            content=ft.Column(
                spacing=6,
                controls=[
                    ft.Row(spacing=8, controls=[
                        ft.Icon(icon, color=color or StationeryTheme.PRIMARY, size=22),
                        ft.Text(label, size=13, color=StationeryTheme.TEXT_SECONDARY, font_family=StationeryTheme.BODY_FONT),
                    ]),
                    value_widget,
                ]
            )
        )

    def render(self):
        asyncio.create_task(self.load_data())

        return ft.View(
            route="/dashboard",
            appbar=ft.AppBar(
                title=ft.Text("Dashboard", font_family=StationeryTheme.HEADING_FONT, size=24, color=StationeryTheme.TEXT_PRIMARY),
                bgcolor=StationeryTheme.BACKGROUND,
                elevation=0,
                leading=ft.IconButton(
                    ft.Icons.ARROW_BACK_IOS_NEW,
                    icon_color=StationeryTheme.TEXT_PRIMARY,
                    on_click=lambda _: asyncio.create_task(self.page.push_route("/"))
                )
            ),
            controls=[
                ft.Container(
                    padding=20,
                    content=ft.Column(
                        spacing=16,
                        controls=[
                            ft.Text("Vendas de Hoje", font_family=StationeryTheme.ACCENT_FONT, size=36, color=StationeryTheme.PRIMARY),

                            # Card Total
                            self._metric_card(ft.Icons.ATTACH_MONEY_ROUNDED, "Total Arrecadado", self.total_text),

                            # Card Itens
                            self._metric_card(ft.Icons.INVENTORY_2_OUTLINED, "Quantidade de Itens", self.items_text),

                            # Card Top Produto
                            self._metric_card(ft.Icons.WORKSPACE_PREMIUM_OUTLINED, "Produto Destaque", self.top_product_text, color="#F59E0B"),

                            # Últimas Vendas
                            ft.Container(height=4),
                            ft.Text("Últimas Vendas", font_family=StationeryTheme.HEADING_FONT, size=20, color=StationeryTheme.TEXT_PRIMARY),
                            self.recent_list,
                        ]
                    )
                )
            ],
            bgcolor=StationeryTheme.BACKGROUND
        )
