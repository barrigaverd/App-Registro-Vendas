import flet as ft
from theme import StationeryTheme
from services.api_service import ApiService
from datetime import datetime
import asyncio

class RegistrationView:
    def __init__(self, page: ft.Page):
        self.page = page
        
        input_style = {
            "border_color": "transparent",
            "border_radius": 15,
            "focused_border_color": StationeryTheme.PRIMARY,
            "bgcolor": StationeryTheme.BACKGROUND,
            "filled": True,
            "content_padding": 20,
        }
        
        self.product_name = ft.TextField(label="Nome do Produto", prefix_icon=ft.Icons.CARD_GIFTCARD, **input_style)
        self.value = ft.TextField(label="Valor da Venda", prefix_icon=ft.Icons.ATTACH_MONEY_ROUNDED, keyboard_type=ft.KeyboardType.NUMBER, **input_style)
        self.quantity = ft.TextField(label="Quantidade", prefix_icon=ft.Icons.INVENTORY_2_OUTLINED, keyboard_type=ft.KeyboardType.NUMBER, value="1", **input_style)
        self.observations = ft.TextField(label="Observações (Opcional)", multiline=True, min_lines=3, **input_style)
        self.error_text = ft.Text(color=StationeryTheme.ERROR, visible=False, size=14, font_family=StationeryTheme.BODY_FONT)

    async def register_sale(self, _):
        if not self.product_name.value or not self.value.value:
            self.error_text.value = "Por favor, preencha o nome e o valor!"
            self.error_text.visible = True
            self.page.update()
            return
        
        valor_limpo = self.value.value.replace(",", ".")
        try:
            data = {
                "nome": self.product_name.value,
                "valor": float(valor_limpo),
                "quantidade": int(self.quantity.value),
                "observacoes": self.observations.value,
                "data": datetime.now().isoformat()
            }
            await ApiService.create_sale(data)
            
            snack = ft.SnackBar(content=ft.Text("Venda registrada com sucesso! ✨"), bgcolor=StationeryTheme.SUCCESS)
            self.page.overlay.append(snack)
            snack.open = True
            self.page.update()
            
            await asyncio.sleep(0.5)  # Pequena pausa para o snackbar aparecer
            await self.page.push_route("/history")
        except Exception as ex:
            self.error_text.value = f"Ops! Ocorreu um erro: {str(ex)}"
            self.error_text.visible = True
            self.page.update()

    def render(self):
        return ft.View(
            route="/register",
            appbar=ft.AppBar(
                title=ft.Text("Novo Registro", font_family=StationeryTheme.HEADING_FONT, size=24, color=StationeryTheme.TEXT_PRIMARY),
                bgcolor=StationeryTheme.BACKGROUND,
                color=StationeryTheme.TEXT_PRIMARY,
                elevation=0,
                leading=ft.IconButton(
                    ft.Icons.ARROW_BACK_IOS_NEW,
                    icon_color=StationeryTheme.TEXT_PRIMARY,
                    on_click=lambda _: asyncio.create_task(self.page.push_route("/"))
                ),
                actions=[
                    ft.IconButton(
                        ft.Icons.DASHBOARD_OUTLINED,
                        icon_color=StationeryTheme.TEXT_SECONDARY,
                        tooltip="Dashboard",
                        on_click=lambda _: asyncio.create_task(self.page.push_route("/dashboard"))
                    )
                ]
            ),
            controls=[
                ft.Container(
                    padding=20,
                    content=ft.Container(
                        bgcolor=StationeryTheme.SURFACE,
                        border_radius=25,
                        padding=25,
                        shadow=ft.BoxShadow(
                            spread_radius=1,
                            blur_radius=15,
                            color=ft.Colors.with_opacity(0.08, StationeryTheme.PRIMARY),
                            offset=ft.Offset(0, 5)
                        ),
                        content=ft.Column(
                            spacing=15,
                            controls=[
                                ft.Container(
                                    alignment=ft.Alignment.CENTER,
                                    margin=ft.Margin(bottom=10, left=0, right=0, top=0),
                                    content=ft.Text("Destaque do Dia", font_family=StationeryTheme.ACCENT_FONT, size=40, color=StationeryTheme.PRIMARY)
                                ),
                                self.product_name,
                                self.value,
                                self.quantity,
                                self.observations,
                                self.error_text,
                                ft.Container(height=10),
                                ft.Button(
                                    content=ft.Container(
                                        content=ft.Text("REGISTRAR COM AMOR", font_family=StationeryTheme.BODY_FONT, weight=ft.FontWeight.W_600, size=16),
                                        padding=ft.Padding.symmetric(vertical=18),
                                        alignment=ft.Alignment.CENTER,
                                    ),
                                    style=ft.ButtonStyle(
                                        color=StationeryTheme.SURFACE,
                                        bgcolor=StationeryTheme.PRIMARY,
                                        shape=ft.RoundedRectangleBorder(radius=15),
                                    ),
                                    width=float("inf"),
                                    on_click=self.register_sale
                                )
                            ]
                        )
                    )
                )
            ],
            bgcolor=StationeryTheme.BACKGROUND
        )
