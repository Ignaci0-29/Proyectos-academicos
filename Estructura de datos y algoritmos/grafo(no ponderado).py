from pila_secu import Pila
import numpy as np
from cola_secu import Cola
class Grafo:
    __cant_v = int
    __matriz = np.ndarray

    def __init__(self, cant):
        self.__cant_v = cant
        self.__matriz = np.zeros((cant, cant), dtype=int)

    def agregar_arista(self, v1, v2, peso=1):
        if v1 < 0 or v1 > self.__cant_v or v2 < 0 or v2 > self.__cant_v:
            raise IndexError("Vertices invalido")  
        self.__matriz[v1-1, v2-1] = peso
        self.__matriz[v2-1, v1-1] = peso

    def adyacentes (self, v):
        if v < 0 or v >= self.__cant_v:
            raise ValueError("El vertice no es valido")
        for i in range(self.__cant_v):
            if self.__matriz[v-1, i] != 0:
                print(i + 1)  

    def gradoSalida(self, vertice):
        grado = 0
        if self.__cant_v < vertice:
            raise ValueError("El vertice no es valido")
        else:
            for i in range(self.__cant_v):
                if self.__matriz[vertice-1, i] != 0:
                    grado += 1
        return grado

    def gradoEntrada(self, vertice):
        grado = 0
        if self.__cant_v < vertice:
            raise ValueError("El vertice no es valido")
        else:
            for i in range(self.__cant_v):
                if self.__matriz[i, vertice-1] != 0:
                    grado += 1
        return grado

    def camino(self, v1, v2):
        cam = Pila()
        visitados = [False] * self.__cant_v
        encontrado = self._camino(v1, v2, visitados, cam)
        if not encontrado:
            raise ValueError("No existe un camino ")
        return cam
    
    def _camino(self, actual, destino, visitados, camino):
        if actual == destino:
            camino.insertar(actual)
            return True
        visitados[actual] = True
        i = 0
        while i < self.__cant_v:
            if self.__matriz[actual, i] != 0 and not visitados[i]:
                if self._camino(i, destino, visitados, camino):
                    camino.insertar(actual)
                    return True
            i += 1
        return False
    
    def conexo(self):
        visitados = [False] * self.__cant_v
        self._conexoI(0, visitados)
        if True:
            pass

    def _conexo(self, v, visitados):
        i=0
        visitados[v] = True
        while i < self.__cant_v:
            if self.__matriz[v, i] != 0 and not visitados[i]:
                self._conexo(i, visitados)
        
    def nodoFuente(self, vertice):
        if self.gradoEntrada(vertice) == 0 and self.gradoSalida(vertice) > 0:
            return True
        else:
            return False

    def nodoSumidero(self, vertice):
        if self.gradoEntrada(vertice) > 0 and self.gradoSalida(vertice) == 0:
            return True
        else:
            return False

    def recorrerMAtAby(self):
        print(self.__matriz)

    def REAnchura(self, inicio):
        cola = Cola()
        visitados = [False] * self.__cant_v
        recorrido = []
        cola.insertar(inicio)
        visitados[inicio] = True
        while not cola.vacia():
            actual = cola.suprimir()
            recorrido[actual] = True
            for vecino in self.__matriz[actual]:
                if vecino not in visitados:
                    cola.insertar(vecino)
                    visitados[vecino] = True
        return recorrido
    
    def REProfundidad(self, inicio):
        pila = Pila()
        visitados = [False] * self.__cant_v
        recorrido = []

        pila.insertar(inicio)
        visitados[inicio] = True

        while not pila.vacia():
            actual = pila.suprimir()
            recorrido[actual] = True
            for vecino in reversed(self.__matriz[actual]):
                if vecino not in visitados:
                    pila.insertar(vecino)
                    visitados[vecino] = True
        return recorrido

if __name__ == '__main__':
#    int(input())
    g = Grafo(5)
    g.agregar_arista(1, 2)
    g.agregar_arista(1, 3)
    g.agregar_arista(2, 5)
    g.agregar_arista(3, 5)
    g.agregar_arista(5, 4)
    g.adyacentes(1)
    g.camino(1, 4)
    