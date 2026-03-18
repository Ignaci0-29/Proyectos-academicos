import numpy as np
class Cola:
    __arre = np.array
    __max = int
    __primer = int
    __ultimo = int
    __cant = int

    def __init__(self, max):
        self.__arre = np.empty(max, dtype=object)
        self.__max = max
        self.__primer = -1
        self.__ultimo = -1
        self.__cant = 0

    def vacia(self):
        return self.__cant == 0

    def insertar(self, x):
        if self.__cant == self.__max:
            raise Exception("Error: la cola esta llena")
        if self.vacia():
            self.__primer = self.__ultimo = (self.__ultimo + 1) % self.__max
            self.__arre[self.__ultimo] = x
        else:
            self.__ultimo = (self.__ultimo + 1) % self.__max
            self.__arre[self.__ultimo] = x
        
        if self.__cant < self.__max:
            self.__cant += 1
    
    def suprimir(self):
        if self.vacia():
            raise IndexError("Error: la cola esta vacia")
        else:
            elem = self.__arre[self.__primer]
            self.__primer = (self.__primer +1) % self.__max
            self.__cant -= 1
            return elem

    def mostrar(self):
        if self.vacia():
            raise IndexError("Error: la cola esta vacia")
        i = self.__primer
        j = 0
        while j < self.__cant:
            print(self.__arre[i])
            i = (i + 1) % self.__max
            j += 1