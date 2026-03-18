import numpy as np
class Pila:
    __item = np.array
    __tope = int
    __cant = int
    def __init__(self, cant=50):
        self.__item = np.empty(cant, dtype=object)
        self.__cant = cant
        self.__tope = -1

    def vacio (self):
        return self.__tope == -1
    
    def insertar (self, x):
        if self.__tope < self.__cant-1:
            self.__tope += 1
            self.__item[self.__tope] = x
        else: raise OverflowError("Error: la pila esta llena (Stack Overflow).")
        
    def suprimir (self):
        if self.vacio():
            raise IndexError("Error: la pila esta vacia")
        elem = self.__item[self.__tope]
        self.__tope -= 1
        return elem
        
    def mostrar (self):
        if self.vacio():
            raise IndexError("Error: la pila esta vacia")
        else:
            for i in range(self.__tope, -1, -1):
                print(self.__item[i])