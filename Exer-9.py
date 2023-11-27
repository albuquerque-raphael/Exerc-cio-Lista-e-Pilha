# 9- Crie uma estrutura que possa ler uma expressão matemática do tipo (2+3)*(8-9)/(7^3) e apresente
# todos os operadores matemáticos existente nessa expressão, utilize a pilha para responder a questão.

class LeitorExpressaoMatematica:
    def __init__(self):
        self.operadores = []

    def identificar_operadores(self, expressao):
        for caractere in expressao:
            if self.e_operador(caractere):
                self.operadores.append(caractere)

    def e_operador(self, caractere):
        operadores_validos = {'+', '-', '*', '/', '^', '(', ')'}
        return caractere in operadores_validos

    def obter_operadores(self):
        return list(set(self.operadores))


if __name__ == "__main__":
    leitor = LeitorExpressaoMatematica()

    expressao = "(2+3)*(8-9)/(7^3)"

    leitor.identificar_operadores(expressao)

    operadores_encontrados = leitor.obter_operadores()

    print(
        f"Operadores encontrados na expressão '{expressao}': {operadores_encontrados}")
