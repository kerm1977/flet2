import flet as ft

def main(page: ft.Page):
    page.title = "Mi App Flet Básica"

    page.add(
        ft.Container(
            content=ft.NavigationBar(
                bgcolor=ft.colors.TRANSPARENT,
                destinations=[
                    ft.NavigationBarDestination(icon=ft.Icons.HOME, label="Inicio"),
                    ft.NavigationBarDestination(icon=ft.Icons.EVENT, label="Eventos"),  # "Eventos" ahora junto a "Inicio"
                    ft.NavigationBarDestination(
                        icon=ft.Icons.BOOKMARK_BORDER,
                        selected_icon=ft.Icons.BOOKMARK,
                        label="Guardado",
                    ),
                    ft.NavigationBarDestination(icon=ft.Icons.PERSON, label="Mi Cuenta"),  # "Mi Cuenta" al final
                ]
            ),
            alignment=ft.alignment.bottom_center,
            expand=True,
        )
    )

if __name__ == "__main__":
    ft.app(target=main)