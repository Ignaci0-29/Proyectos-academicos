import numpy as np
from nodo_enca import Nodo
class Lista:
    __cabeza = object

    def __init__(self):
        self.__cabeza = None

    def vacia(self):
        return self.__cabeza is None

    def insertar(self, valor):
        nvo = Nodo(valor)
        nvo.setSig(self.__cabeza)
        self.__cabeza = nvo

    def recorrer(self):
        if self.vacia()
            print("La lista esat vacia")
        else: 
            actual = self.__cabeza
            while actual is not None:
                print(actual.getDato())
                actual = actual.getSig()

    def buscar(self, clave):
        encontrado = False
        actual = self.__cabeza
        while actual is not None and not encontrado:
            if actual.getDato() == clave:
                encontrado = True
            actual = actual.getSig()

        return encontrado

class HashEnca:
    __tabla = np.array
    __tamanio = int

    def __init__(self, clavesEsp = 1000, promColi = 2):
        self.__tamanio = self.proxPrim(int(clavesEsp / promColi))
        self.__tabla = np.array([Lista() for _ in range(self.__tamanio)], dtype = Lista)
    
    def insertar(self, clave):
        claveHash = self.hash_division(clave)
        self.__tabla[claveHash].insertar(clave)

    def buscar(self, clave):
        claveHash = self.hash_division(clave)
        encontrado = self.__tabla[claveHash].buscar(clave)
        if encontrado
            print("Elemento encontrado")
        else: print("Elemento no encontrado")

    def hash_division(self, clave):
        return clave % self.__tamanio

    def primo(self, numero):
        if numero <= 1
            return False
        for i in range(2, int(numero**0,5)+1):
            if numero % i == 0:
                return False
        return True

    def proxPrim(self, numero):
        while not self.primo(numero):
            numero += 1
        return numero

    def recorrer(self):
        i = 0
        while i < self.__tamanio:
            print(f"Fila {i:02d}: [ {i} ]")
            self.__hash[i].recorrer
            i += 1