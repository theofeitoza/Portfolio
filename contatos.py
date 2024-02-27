from flet import *
from funcoes import *

def contatos(page:Page):
    page.theme_mode = ThemeMode.DARK
    def open_url(e):
        page.launch_url(e.data)

    barra(page)

    titulo(page,'Contatos')
    subtitulo(page,'Contate-me por meio dos meus canais de comunicação')

    page.add(
        Row([
            Container(
                Column([
                    Text('Nome',size=18,color=colors.WHITE),
                    TextField(width=800,height=40,border=border.all(2, colors.GREY),label='Digite seu nome aqui (ex: Théo Feitoza)'),
                    Text('Email',size=18,color=colors.WHITE),
                    TextField(width=800,height=40,border=border.all(2, colors.GREY),label='Digite seu email aqui (ex: theolimaff@gmail.com)'),
                    Text('Assunto',size=18,color=colors.WHITE),
                    TextField(width=800,height=40,border=border.all(2, colors.GREY),label='Digite o assunto aqui (ex: Disponibilidade de projeto)'),
                    Text('Mensagem',size=18,color=colors.WHITE),
                    TextField(width=800,height=40,border=border.all(2, colors.GREY),label='Digite a mensagem aqui (ex: Olá,temos uma ótima oportunidade de trabalho...)',max_lines=5),
                    ElevatedButton(text='Enviar',width=800,height=40)
                ]),margin=40
            ),
            Column([
                Row([
                    Container(
                        Column([
                            Image(src='https://upload.wikimedia.org/wikipedia/commons/4/4e/Gmail_Icon.png',width=30,height=30),
                            Text('Email',color=colors.WHITE,size=18),
                            Text('theolimaff@gmail.com')                                
                        ],horizontal_alignment=CrossAxisAlignment.CENTER),
                        padding=10,
                        width=300,
                        height=150,
                        border_radius=20,
                        border=border.all(2, colors.GREY)),
                    Container(
                        Column([
                            Image(src='https://static-00.iconduck.com/assets.00/github-desktop-icon-2046x2048-r5plljad.png',width=30,height=30),
                            Text('GitHub',color=colors.WHITE,size=18),
                            Text('theofeitoza')                               
                            ],horizontal_alignment=CrossAxisAlignment.CENTER),
                        padding=10,
                        width=300,
                        height=150,
                        border_radius=20,
                        border=border.all(2, colors.GREY)),
                ]),
                Row([
                    Container(
                        Column([
                            Image(src='https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/LinkedIn_logo_initials.png/480px-LinkedIn_logo_initials.png',width=30,height=30),
                            Text('Linkedin',color=colors.WHITE,size=18),
                            Text('theofeitoza')                              
                            ],horizontal_alignment=CrossAxisAlignment.CENTER),
                        padding=10,
                        width=300,
                        height=150,
                        border_radius=20,
                        border=border.all(2, colors.GREY)),
                    Container(
                        Column([
                            Image(src='https://static-00.iconduck.com/assets.00/discord-icon-512x512-xtx725no.png',width=30,height=30),
                            Text('Discord',color=colors.WHITE,size=18),
                            Text('theofeitoza')                                  
                            ],horizontal_alignment=CrossAxisAlignment.CENTER),
                        padding=20,
                        width=300,
                        height=150,
                        border_radius=20,
                        border=border.all(2, colors.GREY))
                ])
            ])
        ])
    )

    page.update()
app(target=contatos, view=WEB_BROWSER)