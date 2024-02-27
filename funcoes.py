from flet import *

def barra(page):
    page.appbar = AppBar(
        toolbar_height=40,
        leading=Icon(icons.EMAIL),
        leading_width=10,
        title=Text("theolimaff@gmail.com"),
        center_title=False,
        actions=[
            TextButton('Sobre',height=100,width=100,style=ButtonStyle(shape=RoundedRectangleBorder(radius=10),color=colors.WHITE),on_click=lambda _: page.go("sobre.py")),
            TextButton("Formação",height=100,width=100,style=ButtonStyle(shape=RoundedRectangleBorder(radius=10),color=colors.WHITE),on_click=lambda _: page.go("/formacao")),
            TextButton('Experiência',height=100,width=100,style=ButtonStyle(shape=RoundedRectangleBorder(radius=10),color=colors.WHITE),on_click=lambda _: page.go("/experiencia")),
            TextButton('Repositório',height=100,width=100,style=ButtonStyle(shape=RoundedRectangleBorder(radius=10),color=colors.WHITE),on_click=lambda _: page.go("/repositorio")),
            TextButton('Contatos',height=100,width=100,style=ButtonStyle(shape=RoundedRectangleBorder(radius=10),color=colors.WHITE),on_click=lambda _: page.go("/contatos"))
        ]
    )
    page.add(
        Container(
            bgcolor=colors.GREY,
            height=1
        )
    )

def titulo(page,titulo):
    page.add(
    Row([
        Text(value=f'{titulo}',
            size=25,
            color=colors.WHITE,
            weight=FontWeight.BOLD)
        ],alignment=MainAxisAlignment.CENTER)
    )

def subtitulo(page,subtitulo):
    page.add(
        Row([
            Text(value=f'{subtitulo}',
            size=16,
            color=colors.GREY,
            )
            ],alignment=MainAxisAlignment.CENTER)
    )

def conteiner_formacao(page,imagem,curso,local,data,nivel):
    page.add(
        Row([
        Container(
            Column([    
                Image(
                    src=f'{imagem}',
                    width=100,border_radius=20),
            ]),
            Column([
                Text(f'{curso}',
                    size=18,
                    color=colors.WHITE,
                    weight=FontWeight.BOLD),
                Text(f'{local}',size=15,color=colors.GREY),
                Text(f'{data}',size=15,color=colors.GREY),
                Text(f'{nivel}',size=15,color=colors.GREY)
            ]),
            padding=20,
            width=700,
            height=150,
            border_radius=20,
            border=border.all(2, colors.GREY)
        )
        ])
    )
    
def xxx():
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
                border=border.all(2, colors.GREY))

def conteiner(page,imagem,titulo,texto):
    ...

def texto_padrao():
    ...