# 10- Palíndromos são palavras, frases ou sequências que mantêm sua mesma forma quando invertidos. Por
# exemplo, a palavra "radar" é um palíndromo, pois se você a ler de trás para frente, ela ainda será
# radar". Construa um programa que possa ler uma palavras ou frase e dizer se ela é um Palíndromo,
# use a estrutura de pilha para responder essa questão.


class VerificadorPalindromo:
    def __init__(self):
        self.pilha = []

    def limpar_texto(self, texto):
        return ''.join(texto.split()).lower()

    def adicionar_caractere(self, caractere):
        self.pilha.append(caractere)

    def comparar_palindromo(self, texto):
        texto = self.limpar_texto(texto)

        for caractere in texto:
            self.adicionar_caractere(caractere)

        texto_invertido = ''.join(reversed(self.pilha))
        return texto == texto_invertido


if __name__ == "__main__":
    verificador = VerificadorPalindromo()

    palavra = input(
        "Digite uma palavra ou frase para verificar se é um palíndromo: ")

    if verificador.comparar_palindromo(palavra):
        print(f"A palavra/frase '{palavra}' é um palíndromo.")
    else:
        print(f"A palavra/frase '{palavra}' não é um palíndromo.")
