from nodo_enca import Nodo
class Cola:
    __cant = int
    __primero = object
    __ultimo = object

    def __init__(self):
        self.__cant = 0
        self.__primero = None
        self.__ultimo = None

    def vacia(self):
        return self.__cant == 0
    
    def insertar(self, x):
        nuevo = Nodo(x)
        if self.vacia():
            self.__primero = self.__ultimo = nuevo
        else:
            self.__ultimo.setSig(nuevo)
            self.__ultimo = nuevo
        self.__cant += 1   

    def suprimir(self):
        if self.vacia():
            raise IndexError("Error: la cola esta vacia")
        elem = self.__primero.getDato()
        self.__primero = self.__primero.getSig()
        if self.__primero == None:
            self.__ultimo = None
        self.__cant -= 1
        return elem
    
    def mostrar(self):
        if self.vacia():
            raise IndexError("Error: la cola esta vacia")
        aux = self.__primero
        while aux != None:
            print(aux.getDato())
            aux = aux.getSig()