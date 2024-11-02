import flet as ft

def main(pagina: ft.Page):
    # Define o tema do app
    tema = ft.Theme(
        color_scheme=ft.ColorScheme(
            primary=ft.colors.AMBER,  # Cor primária dourada
            secondary=ft.colors.AMBER,  # Cor secundária dourada
            background=ft.colors.BLACK,  # Cor de fundo preta
        )
    )

    # Aplica o tema à página
    pagina.theme = tema
    pagina.bgcolor = tema.color_scheme.background  # Define a cor de fundo da página

    # Adiciona um AppBar
    pagina.appbar = ft.AppBar(
        title=ft.Text("The best team", color=ft.colors.WHITE),
        bgcolor=tema.color_scheme.primary
    )

    # Cria textos estilizados
    title = ft.Text("This is the best player", size=30, color=tema.color_scheme.primary)
    primeiro = ft.Text("I'm better!", size=24, color=ft.colors.WHITE, weight=ft.FontWeight.BOLD)

    # Adiciona a imagem do diretório de ativos
    imagem_local = ft.Image(
        src="https://blogdoiata.com/wp-content/uploads/2014/11/escudo-real-madrid.jpg",  # URL da imagem que deseja exibir
        fit=ft.ImageFit.COVER,  # Ajusta a imagem
        width=400,  # Largura da imagem
        height=300  # Altura da imagem
    )

    # Cria um botão com tema
    button = ft.ElevatedButton(
        "Clique Aqui!",
        bgcolor=tema.color_scheme.primary,
        color=ft.colors.WHITE
    )

    # Evento do botão
    def on_button_click(e):
        pagina.add(ft.Text("You are definitely the best!!", color=tema.color_scheme.primary))

    button.on_click = on_button_click

    # Adiciona elementos à página
    pagina.add(title, primeiro, imagem_local, button)

# Adiciona a configuração de ativos
#ft.app(target=main, assets_dir="assets")
