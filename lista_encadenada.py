class Nodo:
    __dato = int
    __sig = object

    def __init__(self, dato):
        self.__dato = dato
        self.__sig = None

    def getDato(self):
        return self.__dato

    def getSig(self):
        return self.__sig

    def setSig(self, sig):
        self.__sig = sig

class Lista:
    __cabeza = Nodo
    __cant = int

    def __init__(self):
        self.__cabeza = None
        self.__cant = 0
    
    def vacia(self):
        return self.__cant == 0

    def insertar(self, dato, pos):
        nuevo_nodo = Nodo(dato)
        if pos < 1 or pos > self.__cant+1:
            raise IndexError("Error: la posicion es invalida.")
        if pos == 1:
            nuevo_nodo.setSig(self.__cabeza)
            self.__cabeza = nuevo_nodo
        else:
            aux = self.__cabeza
            for i in range(1, pos-1): 
                aux = aux.getSig()
            nuevo_nodo.setSig(aux.getSig())
            aux.setSig(nuevo_nodo)
        self.__cant += 1

    def suprimir(self, pos):
        if pos < 1 or pos > self.__cant:
            raise IndexError("Error: La posicion es invalida")
        if self.vacia():
            raise IndexError("Error: La lista esta vacia")
        if pos == 1:
            eliminado_dato = self.__cabeza.getDato()
            self.__cabeza = self.__cabeza.getSig()
            self.__cant -= 1
        else:
            ant = self.__cabeza
            for i in range(1, pos-1):
                ant = ant.getSig()
            eliminado_nodo = ant.getSig()
            eliminado_dato = eliminado_nodo.getDato()
            ant.setSig(eliminado_nodo.getSig())
            self.__cant -= 1
        return eliminado_dato
    
    def recuperar(self, pos):
        if self.vacia():
            raise IndexError("Error: la lista esta vacia")
        if pos < 1 or pos > self.__cant:
            raise IndexError("Error: la posicion es invalida")
        aux = self.__cabeza
        for i in range(1, pos):
            aux = aux.getSig()
        return aux.getDato()
    
    def buscar(self, dato):
        aux = self.__cabeza
        pos = 1
        while aux is not None and aux.getDato() != dato:
            aux = aux.getSig()
            pos += 1
        if aux is not None:
            return pos
        else:
            print("Dato no encontrado")
            return -1

    def primer_elem(self):
        if self.vacia():
            raise IndexError("Error: la lista esta vacia")
        return self.__cabeza
    
    def ultimo_elem(self):
        if self.vacia():
            raise IndexError("Error: la lista esta vacia")
        aux = self.__cabeza
        while aux.getSig() is not None:
            aux = aux.getSig()
        return aux
    
    def anterior(self, pos):
        if pos > 1 and pos <= self.__cant:
            print(f"La posicion anterior es {pos-1}")
            return pos-1
        else: print("No tiene posicion anterior")

    def siguiente(self, pos):
        if pos >= 1 and pos < self.__cant:
            print(f"LA posicion siguiente es {pos+1}")
            return pos+ 1
        else: print("No tiene posicion siguiente")
    
    def recorrerYmostrar(self):
        if self.vacia():
            raise IndexError("Error: la lista esta vacia")
        aux = self.__cabeza
        while aux is not None:
            print(aux.getDato())
            aux = aux.getSig()

    def concatenar(self, lista2):
        if self.vacia():
            self.__cabeza = lista2.__cabeza
            self.__cant =  lista2.__cant
        elif not self.vacia() and not lista2.vacia():
            self.ultimo_elem().setSig(lista2.primer_elem())
            self.__cant += lista2.__cant