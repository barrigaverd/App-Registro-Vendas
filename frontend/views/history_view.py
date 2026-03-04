import flet as ft
from theme import StationeryTheme
from services.api_service import ApiService
import asyncio

class HistoryView:
    def __init__(self, page: ft.Page):
        self.page = page
        self.sales_list = ft.ListView(expand=True, spacing=15, padding=20)
        self.total_text = ft.Text(
            "Total: R$ 0,00",
            font_family=StationeryTheme.HEADING_FONT,
            size=22,
            weight=ft.FontWeight.W_600,
            color=StationeryTheme.TEXT_PRIMARY
        )

    async def load_sales(self):
        try:
            vendas = await ApiService.get_sales_today()
            self.sales_list.controls.clear()
            total_geral = sum(v["valor"] * v["quantidade"] for v in vendas)
            for sale in vendas:
                self.sales_list.controls.append(self.create_sale_card(sale))
            self.total_text.value = f"Total: R$ {total_geral:.2f}"
            self.page.update()
        except Exception as ex:
            snack = ft.SnackBar(content=ft.Text(f"Erro ao carregar: {ex}"), bgcolor=StationeryTheme.ERROR)
            self.page.overlay.append(snack)
            snack.open = True
            self.page.update()

    def create_sale_card(self, sale):
        return ft.Container(
            padding=15,
            bgcolor=StationeryTheme.SURFACE,
            border_radius=15,
            border=ft.Border(
                left=ft.BorderSide(6, StationeryTheme.PRIMARY),
                top=ft.BorderSide(1, StationeryTheme.BORDER_LIGHT),
                right=ft.BorderSide(1, StationeryTheme.BORDER_LIGHT),
                bottom=ft.BorderSide(1, StationeryTheme.BORDER_LIGHT)
            ),
            shadow=ft.BoxShadow(spread_radius=1, blur_radius=15, color=ft.Colors.with_opacity(0.04, ft.Colors.BLACK), offset=ft.Offset(0, 4)),
            content=ft.Row(
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                controls=[
                    ft.Column(
                        spacing=4,
                        controls=[
                            ft.Text(sale["nome"], size=16, font_family=StationeryTheme.BODY_FONT, weight=ft.FontWeight.W_600, color=StationeryTheme.TEXT_PRIMARY),
                            ft.Text(f"{sale['quantidade']}x R$ {sale['valor']:.2f}", color=StationeryTheme.TEXT_SECONDARY, size=14),
                        ]
                    ),
                    ft.Row(
                        spacing=0,
                        controls=[
                            ft.IconButton(
                                ft.Icons.EDIT_OUTLINED,
                                icon_color=StationeryTheme.TEXT_SECONDARY,
                                icon_size=20,
                                on_click=lambda _, s=sale: asyncio.create_task(self.open_edit_dialog(s))
                            ),
                            ft.IconButton(
                                ft.Icons.DELETE_OUTLINE,
                                icon_color=StationeryTheme.ERROR,
                                icon_size=20,
                                on_click=lambda _, sid=sale["id"]: asyncio.create_task(self.delete_sale_click(sid))
                            ),
                        ]
                    )
                ]
            )
        )

    async def open_edit_dialog(self, sale):
        # Campos preenchidos com os dados atuais da venda
        input_style = {
            "border_color": "transparent",
            "border_radius": 12,
            "focused_border_color": StationeryTheme.PRIMARY,
            "bgcolor": StationeryTheme.BACKGROUND,
            "filled": True,
        }
        nome_field = ft.TextField(label="Nome", value=sale["nome"], **input_style)
        valor_field = ft.TextField(label="Valor", value=str(sale["valor"]), keyboard_type=ft.KeyboardType.NUMBER, **input_style)
        qtd_field = ft.TextField(label="Quantidade", value=str(sale["quantidade"]), keyboard_type=ft.KeyboardType.NUMBER, **input_style)
        obs_field = ft.TextField(label="Observações", value=sale.get("observacoes") or "", **input_style)

        dlg = ft.AlertDialog(
            modal=True,
            title=ft.Text("Editar Venda", font_family=StationeryTheme.HEADING_FONT, size=20, color=StationeryTheme.TEXT_PRIMARY),
            content=ft.Column(
                spacing=12,
                tight=True,
                controls=[nome_field, valor_field, qtd_field, obs_field]
            ),
            actions=[
                ft.TextButton("Cancelar", on_click=lambda _: self._close_dialog(dlg)),
                ft.TextButton(
                    "Salvar",
                    style=ft.ButtonStyle(color=StationeryTheme.PRIMARY),
                    on_click=lambda _: asyncio.create_task(
                        self._do_update(dlg, sale["id"], nome_field, valor_field, qtd_field, obs_field)
                    )
                ),
            ],
        )
        self.page.overlay.append(dlg)
        dlg.open = True
        self.page.update()

    async def _do_update(self, dlg, sale_id, nome_field, valor_field, qtd_field, obs_field):
        try:
            data = {
                "nome": nome_field.value,
                "valor": float(valor_field.value.replace(",", ".")),
                "quantidade": int(qtd_field.value),
                "observacoes": obs_field.value,
            }
            await ApiService.update_sale(sale_id, data)
            dlg.open = False
            await self.load_sales()
            snack = ft.SnackBar(content=ft.Text("Venda atualizada com sucesso!"), bgcolor=StationeryTheme.SUCCESS)
            self.page.overlay.append(snack)
            snack.open = True
            self.page.update()
        except Exception as ex:
            snack = ft.SnackBar(content=ft.Text(f"Erro ao atualizar: {ex}"), bgcolor=StationeryTheme.ERROR)
            self.page.overlay.append(snack)
            snack.open = True
            self.page.update()

    async def delete_sale_click(self, sale_id):
        dlg = ft.AlertDialog(
            modal=True,
            title=ft.Text("Confirmar exclusão", font_family=StationeryTheme.HEADING_FONT, color=StationeryTheme.TEXT_PRIMARY),
            content=ft.Text("Tem certeza que deseja deletar esta venda?", font_family=StationeryTheme.BODY_FONT),
            actions=[
                ft.TextButton("Cancelar", on_click=lambda _: self._close_dialog(dlg)),
                ft.TextButton(
                    "Deletar",
                    style=ft.ButtonStyle(color=StationeryTheme.ERROR),
                    on_click=lambda _: asyncio.create_task(self._do_delete(dlg, sale_id))
                ),
            ],
        )
        self.page.overlay.append(dlg)
        dlg.open = True
        self.page.update()

    def _close_dialog(self, dlg):
        dlg.open = False
        self.page.update()

    async def _do_delete(self, dlg, sale_id):
        dlg.open = False
        self.page.update()
        try:
            await ApiService.delete_sale(sale_id)
            await self.load_sales()
            snack = ft.SnackBar(content=ft.Text("Venda deletada!"), bgcolor=StationeryTheme.SUCCESS)
            self.page.overlay.append(snack)
            snack.open = True
            self.page.update()
        except Exception as ex:
            snack = ft.SnackBar(content=ft.Text(f"Erro ao deletar: {ex}"), bgcolor=StationeryTheme.ERROR)
            self.page.overlay.append(snack)
            snack.open = True
            self.page.update()

    def render(self):
        asyncio.create_task(self.load_sales())
        
        return ft.View(
            route="/history",
            appbar=ft.AppBar(
                title=ft.Text("Vendas de Hoje", font_family=StationeryTheme.HEADING_FONT, size=24, color=StationeryTheme.TEXT_PRIMARY),
                bgcolor=StationeryTheme.BACKGROUND,
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
            floating_action_button=ft.FloatingActionButton(
                icon=ft.Icons.FAVORITE,
                bgcolor=StationeryTheme.PRIMARY,
                shape=ft.CircleBorder(),
                on_click=lambda _: asyncio.create_task(self.page.push_route("/register"))
            ),
            controls=[
                ft.Container(
                    padding=20,
                    margin=ft.Margin(left=20, top=10, right=20, bottom=10),
                    bgcolor=StationeryTheme.SECONDARY,
                    border_radius=20,
                    content=ft.Row(
                        alignment=ft.MainAxisAlignment.CENTER,
                        spacing=10,
                        controls=[
                            ft.Icon(ft.Icons.AUTO_AWESOME, color=StationeryTheme.PRIMARY, size=22),
                            self.total_text,
                        ]
                    )
                ),
                self.sales_list
            ],
            bgcolor=StationeryTheme.BACKGROUND
        )
