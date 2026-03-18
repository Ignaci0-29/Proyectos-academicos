import numpy as np
class Lista:
    __arre = np.array
    __cant = int
    __max = int

    def __init__(self, cap=100):
        self.__arre = np.empty(cap, dtype=object)
        self.__cant = 0
        self.__max = cap

    def vacia(self):
        return self.__cant == 0

    def insertar_pos(self, dato, pos):
        if pos < 1 or pos > self.__cant + 1:
            raise IndexError("Error: posicion invalida")
        if self.__cant == self.__max:
            raise OverflowError("Error: la lista esta llena")
        for i in range(self.__cant, pos-1, -1):
            self.__arre[i] = self.__arre[i-1]
        self.__arre[pos-1] = dato
        self.__cant += 1

    def insertar_ordenado(self, dato):
        if self.__cant == self.__max:
            raise OverflowError("Error: la lista esta llena")
        pos = 0
        while pos < self.__cant and self.__arre[pos] < dato:
            pos += 1
        self.insertar_pos(dato, pos+1)

    def suprimir_pos(self, pos):
        if pos < 1 or pos > self.__cant:
            raise IndexError("Error: posicion invalida")
        x = self.__arre[pos-1]
        for i in range(pos-1, self.__cant-1):
            self.__arre[i] = self.__arre[i+1]
        self.__cant -= 1
        return x

    def suprimir_ordenado(self, dato):
        pos = self.busqueda_binaria(dato)
        if pos == -1:
            raise ValueError("Error: dato no encontrado")
        self.suprimir_pos(pos+1)

    def busqueda_binaria(self, dato):
        izq = 0
        der = self.__cant - 1
        while izq <= der:
            medio = (izq + der) // 2
            if self.__arre[medio] == dato:
                return medio + 1
            elif self.__arre[medio] < dato:
                izq = medio + 1
            else:
                der = medio - 1
        return -1
    
    def busqueda_secuencial(self, dato):
        pos = 1
        while pos <= self.__cant and self.__arre[pos-1] != dato:
            pos += 1
        if pos > self.__cant:
            raise ValueError("Error: dato no encontrado")
        return pos

    def recuperar (self, pos):
        if pos < 1 or pos > self.__cant:
            raise IndexError("Error: posicion invalida")
        return self.__arre[pos-1]

    def primer_elem(self):
        if self.vacia():
            raise IndexError("Error: la lista esta vacia")
        return self.__arre[0]
    
    def ultimo_elem(self):
        if self.vacia():
            raise IndexError("Error: la lista esta vacia")
        return self.__arre[self.__cant-1]

    def recorrer(self):
        if self.vacia():
            raise IndexError("Error: la lista esta vacia")
        for i in range(self.__cant):
            print(self.__arre[i], end=" ")
