# 4- Você está criando um aplicativo de lista de tarefas pendentes. As tarefas são adicionadas à fila e
# concluídas uma por uma. Use a classe de fila para implementar a lista de tarefas e concluir as tarefas
# na ordem em que foram adicionadas.


import queue
import time


class ListaDeTarefasPendentes:
    def __init__(self):
        self.fila_de_tarefas = queue.Queue()

    def adicionar_tarefa(self, tarefa):
        self.fila_de_tarefas.put(tarefa)
        print(f"Tarefa '{tarefa}' adicionada à lista de tarefas pendentes.")

    def concluir_tarefas(self):
        while not self.fila_de_tarefas.empty():
            tarefa = self.fila_de_tarefas.get()
            print(f"Concluindo a tarefa: '{tarefa}'")
            time.sleep(1)


if __name__ == "__main__":
    lista_de_tarefas = ListaDeTarefasPendentes()

    lista_de_tarefas.adicionar_tarefa("Limpar a casa")
    lista_de_tarefas.adicionar_tarefa("Fazer compras")
    lista_de_tarefas.adicionar_tarefa("Estudar Python")

    lista_de_tarefas.concluir_tarefas()
