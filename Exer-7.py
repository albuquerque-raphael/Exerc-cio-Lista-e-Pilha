# 7- Crie uma calculadora que avalia expressões matemáticas no formato Notação Polonesa Reversa
# (RPN). Use uma pilha para armazenar os operandos e operadores e realizar os cálculos.


class CalculadoraRPN:
    def __init__(self):
        self.pilha = []

    def avaliar_rpn(self, expressao):
        tokens = expressao.split()

        for token in tokens:
            if token.isdigit() or (token[0] == '-' and token[1:].isdigit()):

                self.pilha.append(float(token))
            elif token in {'+', '-', '*', '/'}:

                if len(self.pilha) < 2:
                    raise ValueError(
                        "Expressão RPN inválida: não há operandos suficientes.")
                operando2 = self.pilha.pop()
                operando1 = self.pilha.pop()
                resultado = self.realizar_operacao(operando1, operando2, token)
                self.pilha.append(resultado)
            else:
                raise ValueError(f"Token desconhecido: {token}")

        if len(self.pilha) == 1:
            return self.pilha[0]
        else:
            raise ValueError(
                "Expressão RPN inválida: sobram operandos na pilha.")

    def realizar_operacao(self, operando1, operando2, operador):
        if operador == '+':
            return operando1 + operando2
        elif operador == '-':
            return operando1 - operando2
        elif operador == '*':
            return operando1 * operando2
        elif operador == '/':
            if operando2 == 0:
                raise ValueError("Divisão por zero.")
            return operando1 / operando2


if __name__ == "__main__":
    calculadora = CalculadoraRPN()

    expressao_rpn = "3 4 + 2 *"

    try:
        resultado = calculadora.avaliar_rpn(expressao_rpn)
        print(f"Resultado da expressão RPN '{expressao_rpn}': {resultado}")
    except ValueError as e:
        print(f"Erro: {e}")
