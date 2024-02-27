from flet import *
from funcoes import *

def sobre(page:Page):
    page.theme_mode = ThemeMode.DARK
    def open_url(e):
        page.launch_url(e.data)

    barra(page)

    titulo(page,'Sobre')
    subtitulo(page,'Conheça minhas experiencias, metas e interesses')

    page.add(
        Column([
            Row([
                Container(
                    Column([
                        Text('Introdução',
                            text_align=alignment.top_left,
                            size=22,
                            color=colors.WHITE,
                            weight=FontWeight.BOLD,
                        ),
                        Text('Théo, um jovem de 21 anos imerso na engenharia mecatrônica, dedica-se aos estudos nessa área inovadora que combina mecânica, eletrônica e automação.'
                            'Sua paixão por desafios técnicos e soluções criativas é evidente, especialmente em Python. Buscando aplicar seus conhecimentos em projetos inovadores, ele combina compreensão teórica sólida com uma mentalidade prática.'
                            'Em seu tempo livre, explora novas tecnologias e tendências em mecatrônica e programação, compartilhando sua empolgação para inspirar e contribuir positivamente para o campo.',
                            size=18,width=650,text_align=TextAlign.JUSTIFY,color=colors.GREY)
                    ]),
                    padding=20,
                    width=700,
                    height=280,
                    border=border.all(1, colors.GREY),
                    border_radius=20,
                ),
                Container(
                    Column([
                        Text('Experiencias',
                            size=22,
                            color=colors.WHITE,
                            weight=FontWeight.BOLD),
                        Text('Estes são alguns fatos sobre mim:',size=18,color=colors.GREY),
                        Row([
                            Column([
                            Icon(icons.NOTE,color=colors.RED),
                            Icon(icons.CALENDAR_MONTH,color=colors.BLUE),
                            Icon(icons.LANGUAGE,color=colors.GREEN),
                            Icon(icons.PEOPLE,color=colors.YELLOW),
                            Icon(icons.COMPUTER,color=colors.PURPLE),
                            ]),
                            Column([
                            Text('Nome é Théo Lima Fernandes Feitoza',size=17),
                            Text('Nascido em 08.10.2002',size=17),
                            Text('Vivo em Catalão, Brasil (GMT-3)',size=17),
                            Text('Trabalho em português e Inglês',size=17),
                            Text('Já estudei C++, Java, HTML e CSS',size=17)
                            ])
                        ]),
                    ]),
                    padding=20,
                    width=700,
                    height=280,
                    border_radius=20,
                    border=border.all(1, colors.GREY)
                )],alignment=MainAxisAlignment.CENTER
            ),
            Row([
                Container(
                    Column([
                        Text('Metas',
                            size=25,
                            color=colors.WHITE,
                            weight=FontWeight.BOLD),
                        Text('Já se passaram alguns anos desde que entrei no espaço tecnológico. Tendo alcançado marcos significativos, estou agora dedicado a seguir essas metas:',
                            size=18,width=660,text_align=TextAlign.JUSTIFY,color=colors.GREY),
                        Row([
                            Column([
                                Icon(icons.COMPUTER,color=colors.CYAN),
                                Icon(icons.STREAM,color=colors.YELLOW),
                                Icon(icons.SCHOOL,color=colors.DEEP_ORANGE),
                                Icon(icons.HOUSE,color=colors.YELLOW),
                            ]),
                            Column([
                                Text('Aprender e desenvolver redes neurais',size=17),
                                Text('Criar sistemas eletrônicos com arduino',size=17),
                                Text('Estar em constante aprendizado',size=17),
                                Text('Trabalhar para aplicar o aprendizado',size=17),
                            ])
                        ])
                    ]),
                    padding=20,
                    width=700,
                    height=260,
                    border_radius=20,
                    border=border.all(1, colors.GREY)   
                ),
                Container(
                    Column([
                        Text('Interesses',
                            size=25,
                            color=colors.WHITE,
                            weight=FontWeight.BOLD),
                        Text('Deixe me contar alguns de meus interesses:',
                            size=18,width=660,text_align=TextAlign.JUSTIFY,color=colors.GREY),
                        Row([
                            Column([
                                Icon(icons.BOOK,color=colors.BLUE),
                                Icon(icons.WIFI,color=colors.RED),
                                Icon(icons.PEOPLE,color=colors.GREEN),
                                Icon(icons.PAGES,color=colors.INDIGO)
                            ]),
                            Column([
                                Text('Desenvolver projetos para meu portfólio',size=17),
                                Text('Desenvolver redes neurais voltadas a aprendizado profundo',size=17),
                                Text('Criar softwares que facilitem o dia a dia humano',size=17),
                                Text('Implementar visuais par aproximar o código ao usuário',size=17)
                            ])
                    ])
                    ]),
                    padding=20,
                    width=700,
                    height=260,
                    border_radius=20,
                    border=border.all(1, colors.GREY)
                )
                ],alignment=MainAxisAlignment.CENTER)],scroll=ScrollMode.ALWAYS,)
    )

    page.update()
app(target=sobre, view=WEB_BROWSER)