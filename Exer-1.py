#1- Você está desenvolvendo um sistema de fila de impressão para uma empresa. Os documentos são
#adicionados à fila e impressos na ordem em que foram recebidos. Implemente um programa Python
#que use a classe de fila para simular esse processo.

import queue
import time

class SistemaDeFilaDeImpressao:
    def __init__(self):
        self.fila = queue.Queue()

    def adicionar_documento(self, documento):
        self.fila.put(documento)
        print(f"Documento '{documento}' adicionado à fila.")

    def imprimir_documentos(self):
        while not self.fila.empty():
            documento = self.fila.get()
            print(f"Imprimindo documento: '{documento}'")
            time.sleep(1) 

if __name__ == "__main__":
    sistema_de_fila = SistemaDeFilaDeImpressao()

    
    sistema_de_fila.adicionar_documento("Documento1")
    sistema_de_fila.adicionar_documento("Documento2")
    sistema_de_fila.adicionar_documento("Documento3")

    
    sistema_de_fila.imprimir_documentos()