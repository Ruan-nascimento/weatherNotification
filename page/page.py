import flet as ft
from functions.findWeatherPrevision import get_weather

def main(page: ft.Page):
    # Configurações da página
    page.title = "Previsão do Tempo"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.window.width = 500
    page.window.height = 700
    page.window.resizable = False

    # Campos de entrada e exibição
    city_input = ft.TextField(label="Digite o nome da cidade")
    container_result = ft.Container(
        border_radius=20,
        width=300,
        height=400,
        content=ft.Column([
            ft.Text(scale=1.2),
            ft.Text()
        ],
        alignment=ft.MainAxisAlignment.START,  # Espaçamento vertical
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,  # Alinhamento horizontal)
    ))

    error_message = ft.Text()


    # Função para exibir a previsão
    def show_weather(e):
        city = city_input.value.strip()
        if city:
            weather = get_weather(city)
            if "error" in weather:
                error_message.value = weather["error"]
            else:
               container_result.content.controls[0].value = weather["city"]
               container_result.content.controls[1].value =  f"Temperatura: {weather['temp']}°C"
                
        else:
            error_message.value = "Por favor, insira o nome da cidade."
        page.update()

    # Botão para buscar a previsão
    search_button = ft.ElevatedButton("Buscar previsão", on_click=show_weather)

    # Adicionar elementos na página
    page.add(
        ft.Column(
            [
                city_input,
                search_button,
                container_result,
                error_message
                
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )