from nodo_enca import Nodo
class Pila:
    __cant = int
    __tope = Nodo

    def __init__(self):
        self.__cant = 0 
        self.__tope = None

    def vacio(self):
        return self.__cant == 0
    
    def insertar(self, dato):
        nvo = Nodo(dato)
        nvo.setSig(self.__tope)
        self.__tope = nvo
        self.__cant += 1
        
    def suprimir(self):
        if self.vacio():
            raise IndexError("Error: la pila esta vacia")
        elem = self.__tope.getDato()
        self.__tope = self.__tope.getSig()
        self.__cant -= 1
        return elem

    def mostrar(self):
        if self.vacio():
            raise IndexError("Error: la pila esta vacia")
        aux = self.__tope
        while aux != None:
            print(aux.getDato())
            aux = aux.getSig()
            