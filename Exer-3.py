# 3-Imagine um sistema de gerenciamento de pedidos para um restaurante. Os pedidos dos clientes são
# colocados em uma fila e processados na ordem em que foram feitos. Use a classe de fila para
# gerenciar os pedidos e processá-los na ordem correta.

import queue
import time


class SistemaDeGerenciamentoDePedidos:
    def __init__(self):
        self.fila_de_pedidos = queue.Queue()

    def fazer_pedido(self, pedido):
        self.fila_de_pedidos.put(pedido)
        print(f"Pedido '{pedido}' adicionado à fila.")

    def processar_pedidos(self):
        while not self.fila_de_pedidos.empty():
            pedido = self.fila_de_pedidos.get()
            print(f"Processando pedido: '{pedido}'")
            time.sleep(1)


if __name__ == "__main__":
    sistema_de_pedidos = SistemaDeGerenciamentoDePedidos()

    sistema_de_pedidos.fazer_pedido("Hamburguer")
    sistema_de_pedidos.fazer_pedido("Pizza")
    sistema_de_pedidos.fazer_pedido("Salada")

    sistema_de_pedidos.processar_pedidos()
