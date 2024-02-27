from flet import *
from funcoes import *

def principal(page:Page):
    page.title = "Portfólio"
    page.theme_mode = ThemeMode.DARK
    def open_url(e):
        page.launch_url(e.data)

    barra(page)

    page.add(
        Row([
            Column([
                Container(
                Image(
                    src='https://media.licdn.com/dms/image/D4D03AQGI1jqDhnUQRQ/profile-displayphoto-shrink_400_400/0/1697842582191?e=1712188800&v=beta&t=QHL2FIf3HEyxp8THcm0fEmAEPVP8DoE4KHSfV03MXz8',
                    width=300,
                    border_radius=200
                )
                )
            ],width=750,horizontal_alignment=CrossAxisAlignment.CENTER,alignment=MainAxisAlignment.CENTER),
            Container(
            Column([
                Text('Olá, Me chamo',
                    size=25,
                    color=colors.GREY,
                    weight=FontWeight.BOLD,
                ),
                Text('Théo Lima Fernandes Feitoza',
                    size=35,
                    color=colors.WHITE,
                    weight=FontWeight.BOLD
                ),
                Row([
                    Icon(icons.BOOK),
                    Text('Engenharia Mecatrônica',    
                        size=18,
                        color=colors.GREY,
                        width=240),
                    Icon(icons.COMPUTER),
                    Text('Desenvolvedor Python',size=18,color=colors.GREY)
                ],alignment=MainAxisAlignment.CENTER),
                Row([
                    Icon(icons.BOOK),
                    Text('Técnico em elétrotécnica',
                        size=18,
                        color=colors.GREY,
                        width=240),
                    Icon(icons.COMPUTER),
                    Text('Intusiasta em Automação',
                        size=18,
                        color=colors.GREY
                    )
                ],alignment=MainAxisAlignment.CENTER),
                Text('Buscando contato? Envie um email:',
                    color=colors.GREY),
                Markdown(
                    value="[theolimaff@gmail.com](mailto:theolimaff@gmail.com)",
                    extension_set="gitHubWeb",
                    on_tap_link=open_url
                )
            ],horizontal_alignment=CrossAxisAlignment.CENTER,alignment=MainAxisAlignment.CENTER)
            ,alignment=alignment.center)
        ],width=1500,height=750)
    )
    page.update()   
app(target=principal, view=WEB_BROWSER)