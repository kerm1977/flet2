import flet as ft

page_ref = None  # Variable global para la página

def create_login_form(switch_to_register):
    username = ft.TextField(label="Usuario")
    password = ft.TextField(label="Contraseña", password=True, can_reveal_password=True)
    remember_me = ft.Checkbox(label="Recordarme")
    login_button = ft.ElevatedButton("Iniciar Sesión", on_click=lambda e: login(e, username.value, password.value))
    register_link = ft.TextButton("¿No tienes cuenta? Regístrate aquí", on_click=switch_to_register)
    error_text = ft.Text("", color=ft.colors.RED)

    def login(e, username_value, password_value):
        if username_value and password_value:
            error_text.value = ""
            page_ref.update()
            print(f"Intento de inicio de sesión con: {username_value}, {password_value}, Recordarme: {remember_me.value}")
            # Aquí podrías navegar a la siguiente pantalla de la aplicación
        else:
            error_text.value = "Por favor, introduce usuario y contraseña."
            page_ref.update()

    return ft.Column(
        [
            username,
            password,
            remember_me,
            login_button,
            register_link,
            error_text,
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )

def create_register_form(switch_to_login):
    username = ft.TextField(label="Usuario")
    email = ft.TextField(label="Email", keyboard_type=ft.KeyboardType.EMAIL)
    phone = ft.TextField(label="Teléfono", keyboard_type=ft.KeyboardType.PHONE)
    password = ft.TextField(label="Contraseña", password=True, can_reveal_password=True)
    confirm_password = ft.TextField(label="Confirmar Contraseña", password=True, can_reveal_password=True)
    register_button = ft.ElevatedButton("Registrar", on_click=lambda e: register(e, username.value, email.value, phone.value, password.value, confirm_password.value))
    login_link = ft.TextButton("¿Ya tienes cuenta? Inicia sesión aquí", on_click=switch_to_login)
    error_text = ft.Text("", color=ft.colors.RED)

    def register(e, username_value, email_value, phone_value, password_value, confirm_password_value):
        if not all([username_value, email_value, phone_value, password_value, confirm_password_value]):
            error_text.value = "Por favor, completa todos los campos."
            page_ref.update()
        elif password_value != confirm_password_value:
            error_text.value = "Las contraseñas no coinciden."
            page_ref.update()
        else:
            # Simulación de registro exitoso
            error_text.value = ""
            page_ref.update()
            print(f"Intento de registro con: {username_value}, {email_value}, {phone_value}, {password_value}")
            switch_to_login(None) # Volver al formulario de login después del registro simulado

    return ft.Column(
        [
            username,
            email,
            phone,
            password,
            confirm_password,
            register_button,
            login_link,
            error_text,
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )

def inicio_view(navigate_to_account_func):
    return ft.Stack(
        expand=True,
        controls=[
            ft.Container(
                alignment=ft.alignment.center,
                content=ft.Text("Contenido principal de la aplicación", expand=True),
            ),
            ft.Container(  # Contenedor para la NavigationBar en la parte inferior (inicial)
                content=ft.NavigationBar(
                    bgcolor=ft.colors.TRANSPARENT,
                    destinations=[
                        ft.NavigationBarDestination(icon=ft.Icons.HOME, label="Inicio"),
                        ft.NavigationBarDestination(icon=ft.Icons.EVENT, label="Eventos"),
                        ft.NavigationBarDestination(
                            icon=ft.Icons.BOOKMARK_BORDER,
                            selected_icon=ft.Icons.BOOKMARK,
                            label="Guardado",
                        ),
                        ft.NavigationBarDestination(icon=ft.Icons.PERSON, label="Mi Cuenta"),
                    ],
                    on_change=lambda e: navigate_to_home(e.control.selected_index) # Asociar la acción al icono "Inicio"
                ),
                alignment=ft.alignment.bottom_center,
                expand=True,
            ),
            ft.GestureDetector(
                ft.Container( # El control a detectar va como primer argumento
                    content=ft.Icon(ft.Icons.PERSON_OUTLINE, size=30),
                    padding=10,
                    alignment=ft.alignment.top_right,
                ),
                on_tap=navigate_to_account_func, # Usar la función pasada como argumento
            ),
        ]
    )

def main(page: ft.Page):
    global page_ref
    page_ref = page
    page.title = "Mi App Flet Básica"

    def show_login(e):
        page_ref.clean()
        login_form = create_login_form(switch_to_register=show_register)
        page_ref.add(
            ft.Column( # Usamos una Column para apilar el formulario y la NavigationBar
                [
                    ft.Container(
                        content=ft.Card(content=ft.Container(content=login_form, padding=20), expand=False),
                        alignment=ft.alignment.center,
                        expand=True,
                    ),
                    ft.Container(  # Contenedor para la NavigationBar
                        content=ft.NavigationBar(
                            bgcolor=ft.colors.TRANSPARENT,
                            destinations=[
                                ft.NavigationBarDestination(icon=ft.Icons.HOME, label="Inicio"),
                                ft.NavigationBarDestination(icon=ft.Icons.EVENT, label="Eventos"),
                                ft.NavigationBarDestination(
                                    icon=ft.Icons.BOOKMARK_BORDER,
                                    selected_icon=ft.Icons.BOOKMARK,
                                    label="Guardado",
                                ),
                                ft.NavigationBarDestination(icon=ft.Icons.PERSON, label="Mi Cuenta"),
                            ],
                            on_change=lambda e: navigate_to_home(e.control.selected_index) # También en la vista de login/registro
                        ),
                        alignment=ft.alignment.bottom_center,
                        width=page_ref.width, # Asegurar que la barra ocupe el ancho
                    ),
                ],
                expand=True,
            )
        )
        page_ref.update()

    def show_register(e):
        page_ref.clean()
        register_form = create_register_form(switch_to_login=show_login)
        page_ref.add(
            ft.Column( # Usamos una Column para apilar el formulario y la NavigationBar
                [
                    ft.Container(
                        content=ft.Card(content=ft.Container(content=register_form, padding=20), expand=False),
                        alignment=ft.alignment.center,
                        expand=True,
                    ),
                    ft.Container(  # Contenedor para la NavigationBar
                        content=ft.NavigationBar(
                            bgcolor=ft.colors.TRANSPARENT,
                            destinations=[
                                ft.NavigationBarDestination(icon=ft.Icons.HOME, label="Inicio"),
                                ft.NavigationBarDestination(icon=ft.Icons.EVENT, label="Eventos"),
                                ft.NavigationBarDestination(
                                    icon=ft.Icons.BOOKMARK_BORDER,
                                    selected_icon=ft.Icons.BOOKMARK,
                                    label="Guardado",
                                ),
                                ft.NavigationBarDestination(icon=ft.Icons.PERSON, label="Mi Cuenta"),
                            ],
                            on_change=lambda e: navigate_to_home(e.control.selected_index) # También en la vista de login/registro
                        ),
                        alignment=ft.alignment.bottom_center,
                        width=page_ref.width, # Asegurar que la barra ocupe el ancho
                    ),
                ],
                expand=True,
            )
        )
        page_ref.update()

    def navigate_to_account(e):
        show_login(None) # Mostrar el formulario de login al presionar el icono de usuario

    def navigate_to_home(index):
        if index == 0: # El índice 0 corresponde al icono "Inicio"
            page_ref.clean()
            page_ref.add(inicio_view(navigate_to_account))
            page_ref.update()

    page_ref.add(inicio_view(navigate_to_account)) # Agregar la vista de inicio al cargar la aplicación

if __name__ == "__main__":
    ft.app(target=main)