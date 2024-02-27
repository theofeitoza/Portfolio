from flet import *
from funcoes import *
from principal import *
from contatos import *
from sobre import *
from formacao import *
from repositorio import *


def main(page:Page):
    
    def route_change(route):
        page.views.clear()
        page.views.append(
            View(
                "/",
                [
                    principal()
                ]
            )
        )
        if page.route == "/formacao":
            page.views.append(
                View(
                    [
                        formacao()
                    ]
                )
            )
        elif page.route == "/contatos":
            page.views.append(
                View(
                    [
                        contatos()
                    ]
                )
            )
        elif page.route == "/sobre":
            page.views.append(
                View(
                    [
                        sobre()
                    ]
                )
            )
        elif page.route == "/repositorio":
            page.views.append(
                View(
                    [
                        repositorio()
                    ]
                )
            )
        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)


app(target=main, view=AppView.WEB_BROWSER)