# 6- Imagine que você está desenvolvendo um navegador web simplificado. Use uma pilha para armazenar
# o histórico de páginas visitadas pelos usuários e implementar as funcionalidades de voltar e avançar
# na navegação.


class NavegadorWebSimplificado:
    def __init__(self):
        self.historico = []
        self.historico_avanco = []

    def abrir_pagina(self, pagina):
        print(f"Abrindo a página: {pagina}")
        self.historico.append(pagina)

        self.historico_avanco = []

    def voltar_pagina(self):
        if len(self.historico) > 1:
            pagina_atual = self.historico.pop()
            self.historico_avanco.append(pagina_atual)
            pagina_anterior = self.historico[-1]
            print(f"Voltando para a página anterior: {pagina_anterior}")

    def avancar_pagina(self):
        if self.historico_avanco:
            pagina_proxima = self.historico_avanco.pop()
            self.historico.append(pagina_proxima)
            print(f"Indo para a próxima página: {pagina_proxima}")
        else:
            print("Não há páginas para avançar.")


if __name__ == "__main__":
    navegador = NavegadorWebSimplificado()

    navegador.abrir_pagina("www.hotmail.com")
    navegador.abrir_pagina("www.uol.com")
    navegador.abrir_pagina("www.wscom.com")

    navegador.voltar_pagina()
    navegador.avancar_pagina()
    navegador.voltar_pagina()
    navegador.voltar_pagina()
    navegador.avancar_pagina()
