from flet import *
from funcoes import *

def formacao(page:Page):
    page.theme_mode = ThemeMode.DARK
    def open_url(e):
        page.launch_url(e.data)

    barra(page)

    titulo(page,'Formação')
    subtitulo(page,'Descubra a minha formação e instituições')

    page.add(
        Row([
                Container(
                    Row([  
                            Image(
                                src='https://upload.wikimedia.org/wikipedia/commons/thumb/9/9b/Instituto_Federal_de_Goi%C3%A1s_-_Marca_Vertical_2015.svg/800px-Instituto_Federal_de_Goi%C3%A1s_-_Marca_Vertical_2015.svg.png',
                                width=100,border_radius=20),
                            Column([
                                Text('Ensino médio integrado ao técnico em Elétrotécnica',
                                    size=18,
                                    color=colors.WHITE,
                                    weight=FontWeight.BOLD),
                                Text('Instituto Federal de Goiás',size=15,color=colors.GREY),
                                    Text('2018 - 2021',size=15,color=colors.GREY),
                                    Text('Nível Técnico',size=15,color=colors.GREY)
                            ])
                ]),
                padding=20,
                width=700,
                height=150,
                border_radius=20,
                border=border.all(2, colors.GREY)),
                Container(
                    Row([
                        Image(
                            src='https://files.cercomp.ufg.br/weby/up/519/o/UFCAT_-_Identidade_Visual_Original.png',
                            height=100,width=100,border_radius=20),
                    Column([
                                Text('Engenharia Mecatrônica',
                                size=18,
                                color=colors.WHITE,
                                weight=FontWeight.BOLD),
                                    Text('Universidade Federal de Catalão',size=15,color=colors.GREY),
                                    Text('2022 - 2026',size=15,color=colors.GREY),
                                    Text('Graduação',size=15,color=colors.GREY)
                        ])
                    ]),
                padding=20,
                width=700,
                height=150,
                border_radius=20,
                border=border.all(2, colors.GREY))
            ],alignment=MainAxisAlignment.CENTER
        )
    )

    subtitulo(page,'Formação extra')

    page.add(
        Row([
            Container(
                Row([
                    Image(
                        src='https://yt3.googleusercontent.com/zITOOUrlHDSfO5nlp-ILRaL4nrX2wQuL_IGUtU9jW6CZBDVZMZy-kBUWIkdLIRgAQIXYQJK-uXM=s176-c-k-c0x00ffffff-no-rj-mo',
                        width=100,border_radius=20),
                    Column([
                        Text('Python 3 Módulos 1, 2 e 3',
                            size=18,
                            color=colors.WHITE,
                            weight=FontWeight.BOLD),
                        Text('Curso em Vídeo',size=15,color=colors.GREY),
                        Text('Março 2023 - Dezembro 2023',size=15,color=colors.GREY),
                        Text('Nível Iniciante',size=15,color=colors.GREY)
                    ])
                ]),
                padding=20,
                width=700,
                height=150,
                border_radius=20,
                border=border.all(2, colors.GREY)),
            Container(
                Row([
                    Image(
                        src='https://pbs.twimg.com/profile_images/1417157967124721666/xShJF4Km_400x400.png',
                        height=100,width=100,border_radius=20),
                    Column([
                        Text('Curso de Python 3 do básico ao avançado - Projetos Reais',
                            size=18,
                            color=colors.WHITE,
                            weight=FontWeight.BOLD),
                        Text('Udemy',size=15,color=colors.GREY),
                        Text('Agosto 2023 - Março 2024',size=15,color=colors.GREY),
                        Text('Nível Avançado',size=15,color=colors.GREY)
                    ])
                ]),
                padding=20,
                width=700,
                height=150,
                border_radius=20,
                border=border.all(2, colors.GREY))
        ],alignment=MainAxisAlignment.CENTER)
    )

    page.add(
        Row([
            Container(
                Row([
                    Image(
                        src='https://media.licdn.com/dms/image/C4D0BAQFTyRSkwUGxHQ/company-logo_200_200/0/1631353064133?e=2147483647&v=beta&t=JU2sPDg6MSZuRBtaWTtQn7wDm-dQylHx9TSJWnzVuYc',
                        width=100,border_radius=20),
                    Column([
                        Text('Lógica de Programação',
                            size=18,
                            color=colors.WHITE,
                            weight=FontWeight.BOLD),
                        Text('Senai - Goiás',size=15,color=colors.GREY),
                        Text('Agosto 2021',size=15,color=colors.GREY),
                        Text('Nível Básico',size=15,color=colors.GREY)
                    ])
                ]),
                padding=20,
                width=700,
                height=150,
                border_radius=20,
                border=border.all(2, colors.GREY)),
            Container(
                Row([
                    Image(
                        src='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSQ8fCycYOqgf7bkG_-trOBI54zXfJt-PMFvhvyeqI07g&s',
                        height=100,width=100,border_radius=20),
                    Column([
                        Text('Microsoft Excel',
                            size=18,
                            color=colors.WHITE,
                            weight=FontWeight.BOLD),
                        Text('Fundação Bradesco',size=15,color=colors.GREY),
                        Text('Março 2021',size=15,color=colors.GREY),
                        Text('Nível Básico e Intermediário',size=15,color=colors.GREY)
                    ])
                ]),
                padding=20,
                width=700,
                height=150,
                border_radius=20,
                border=border.all(2, colors.GREY))
        ],alignment=MainAxisAlignment.CENTER)
    )

    page.update()
app(target=formacao, view=WEB_BROWSER)