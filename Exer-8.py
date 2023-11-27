# 8- Em um programa de edição de texto, implemente a funcionalidade de "Desfazer" e "Refazer" usando
# uma pilha para armazenar o histórico de comandos executados pelo usuário.

class EditorDeTexto:
    def __init__(self):
        self.texto = ""
        self.historico_comandos = []
        self.historico_desfazer = []

    def adicionar_texto(self, texto):
        self.texto += texto
        self.historico_comandos.append(("adicionar", texto))
        
        self.historico_desfazer = []

    def desfazer(self):
        if self.historico_comandos:
            comando_desfeito = self.historico_comandos.pop()
            tipo, texto = comando_desfeito
            if tipo == "adicionar":
                self.texto = self.texto[:-len(texto)]
                self.historico_desfazer.append(comando_desfeito)
            elif tipo == "desfazer":
                self.texto += texto
                self.historico_desfazer.append(comando_desfeito)

    def refazer(self):
        if self.historico_desfazer:
            comando_refeito = self.historico_desfazer.pop()
            tipo, texto = comando_refeito
            if tipo == "adicionar":
                self.texto += texto
                self.historico_comandos.append(comando_refeito)
            elif tipo == "desfazer":
                self.texto = self.texto[:-len(texto)]
                self.historico_comandos.append(comando_refeito)

    def obter_texto(self):
        return self.texto

if __name__ == "__main__":
    editor = EditorDeTexto()

    
    editor.adicionar_texto("Olá, ")
    editor.adicionar_texto("mundo!")

    print("Texto atual:", editor.obter_texto())

    
    editor.desfazer()
    print("Texto após desfazer:", editor.obter_texto())


    editor.refazer()
    print("Texto após refazer:", editor.obter_texto())