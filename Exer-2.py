# 2- Você está desenvolvendo um sistema de fila de atendimento para um banco. Os clientes entram na
# fila e são atendidos pelos funcionários na ordem de chegada. Use a classe de fila para simular o
# atendimento dos clientes.


import queue
import time


class SistemaDeFilaDeAtendimento:
    def __init__(self):
        self.fila_de_atendimento = queue.Queue()

    def entrar_na_fila(self, cliente):
        self.fila_de_atendimento.put(cliente)
        print(f"Cliente '{cliente}' entrou na fila de atendimento.")

    def atender_clientes(self):
        while not self.fila_de_atendimento.empty():
            cliente = self.fila_de_atendimento.get()
            print(f"Atendendo o cliente: '{cliente}'")
            time.sleep(1)


if __name__ == "__main__":
    sistema_de_atendimento = SistemaDeFilaDeAtendimento()

    sistema_de_atendimento.entrar_na_fila("Cliente1")
    sistema_de_atendimento.entrar_na_fila("Cliente2")
    sistema_de_atendimento.entrar_na_fila("Cliente3")

    sistema_de_atendimento.atender_clientes()
