from flet import *
from funcoes import *

def repositorio(page:Page):
    page.theme_mode = ThemeMode.DARK
    def open_url(e):
        page.launch_url(e.data)

    barra(page)

    titulo(page,'Repositório')
    subtitulo(page,'Descubra alguns códigos e programas desenvolvidos por mim')

    page.add(
        Row([
            Container(
                Column([
                    Image(src="https://terminalroot.com.br/assets/img/python/vscode-python.png",
                    width=250,height=200),
                    Text('Calculadora',size=20,weight=FontWeight.BOLD),
                    Text('Calculadora desenvolvida em python com utilização da biblioteca Tkinter.',width=250,color=colors.GREY)
                ]),
                padding=20,
                width=290,
                height=350,
                border_radius=20,
                border=border.all(2, colors.GREY)),
            Container(
                Column([
                    Image(src="https://terminalroot.com.br/assets/img/python/vscode-python.png",
                    width=250,height=200),
                    Text('Titulo',size=20,weight=FontWeight.BOLD),
                    Text('Texto auxiliar sobre o programa')
                ]),
                padding=20,
                width=290,
                height=350,
                border_radius=20,
                border=border.all(2, colors.GREY)),
            Container(
                Column([
                    Image(src="https://terminalroot.com.br/assets/img/python/vscode-python.png",
                    width=250,height=200),
                    Text('Titulo',size=20,weight=FontWeight.BOLD),
                    Text('Texto auxiliar sobre o programa')
                ]),
                padding=20,
                width=290,
                height=350,
                border_radius=20,
                border=border.all(2, colors.GREY)),
            Container(
                Column([
                    Image(src="https://terminalroot.com.br/assets/img/python/vscode-python.png",
                    width=250,height=200),
                    Text('Titulo',size=20,weight=FontWeight.BOLD),
                    Text('Texto auxiliar sobre o programa')
                ]),
                padding=20,
                width=290,
                height=350,
                border_radius=20,
                border=border.all(2, colors.GREY)),
            Container(
                Column([
                    Image(src="https://terminalroot.com.br/assets/img/python/vscode-python.png",
                    width=250,height=200),
                    Text('Titulo',size=20,weight=FontWeight.BOLD),
                    Text('Texto auxiliar sobre o programa')
                ]),
                padding=20,
                width=290,
                height=350,
                border_radius=20,
                border=border.all(2, colors.GREY)),
            Container(
                Column([
                    Image(src="https://terminalroot.com.br/assets/img/python/vscode-python.png",
                    width=250,height=200),
                    Text('Titulo',size=20,weight=FontWeight.BOLD),
                    Text('Texto auxiliar sobre o programa')
                ]),
                padding=20,
                width=290,
                height=350,
                border_radius=20,
                border=border.all(2, colors.GREY)),
            Container(
                Column([
                    Image(src="https://terminalroot.com.br/assets/img/python/vscode-python.png",
                    width=250,height=200),
                    Text('Titulo',size=20,weight=FontWeight.BOLD),
                    Text('Texto auxiliar sobre o programa')
                ]),
                padding=20,
                width=290,
                height=350,
                border_radius=20,
                border=border.all(2, colors.GREY)),
            Container(
                Column([
                    Image(src="https://terminalroot.com.br/assets/img/python/vscode-python.png",
                    width=250,height=200),
                    Text('Titulo',size=20,weight=FontWeight.BOLD),
                    Text('Texto auxiliar sobre o programa')
                ]),
                padding=20,
                width=290,
                height=350,
                border_radius=20,
                border=border.all(2, colors.GREY)),
            ],alignment=MainAxisAlignment.CENTER,expand=1,scroll="always")
    )

    page.update()
app(target=repositorio, view=WEB_BROWSER)