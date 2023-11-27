# 5- Em um sistema de comércio eletrônico, os pedidos online são processados em uma fila. Implemente
# uma classe de fila que gerencie os pedidos online e processe-os na ordem de chegada.


import queue
import time


class SistemaDeProcessamentoDePedidos:
    def __init__(self):
        self.fila_de_pedidos = queue.Queue()

    def adicionar_pedido(self, pedido):
        self.fila_de_pedidos.put(pedido)
        print(f"Pedido online '{pedido}' adicionado à fila.")

    def processar_pedidos(self):
        while not self.fila_de_pedidos.empty():
            pedido = self.fila_de_pedidos.get()
            self.processar_pedido(pedido)

    def processar_pedido(self, pedido):
        print(f"Processando pedido online: '{pedido}'")
        time.sleep(1)


if __name__ == "__main__":
    sistema_de_pedidos = SistemaDeProcessamentoDePedidos()

    sistema_de_pedidos.adicionar_pedido("Pedido1")
    sistema_de_pedidos.adicionar_pedido("Pedido2")
    sistema_de_pedidos.adicionar_pedido("Pedido3")

    sistema_de_pedidos.processar_pedidos()
