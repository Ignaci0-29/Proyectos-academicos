import numpy as np
class HashAbierto:
    __M = int
    __tabla = np.array
    __ocupado = int

    def __init__(self, tamaño=100, fCarga = 0.7):
        self.__M = round(self.proxPrim(tamaño) / fCarga)
        self.__tabla = np.zeros(self.__M, dtype=int)
        self.__ocupado = 0
    
    def primo(self, n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def proxPrim(self, n):
        while not self.primo(n):
            n += 1
        return n
    
    def hash_division(self, clave):
        return clave  % self.__M

    def hash_extraccion(self, clave):    
        claveH = str(clave)
        seleccion = claveH[2] + claveH[3] + claveH[4] #Puedo elegir de la menra que quiera
        num = int(seleccion)
        return num % self.__M

    def insersion(self, clave):
        #if self.__ocupado >= self.__M:
        #   raise OverflowError("Tabla llena. Nopuede insertar mas.")
        claveHash = self.hash_division(clave)
        if self.__tabla[claveHash] == 0:
            self.__tabla[claveHash] = clave
            self.__ocupado += 1
        else:
            i = claveHash
            j = 0
            while self.__tabla[i] != 0 and j < self.__M:
                i = (i + 1) % self.__M
                j += 1
            if self.__M == j:
                raise OverflowError("Tabla llena. Nopuede insertar mas.")
            else: 
                self.__tabla[i] = clave
                self.__ocupado += 1

    def buscar (self, clave):
        claveHash = self.hash_division(clave)
        if self.__tabla[claveHash] == clave:
            print("Se encontro la clave por acceso hash")
        else:
            i = claveHash
            j = 0
            while self.__tabla[i] != clave and j < self.__M:
                i = (i + 1) % self.__M
                j += 1
            if j == self.__M:
                print("No se encontro la clave")
            else:
                print("Se encontro la clave en la posicion ", i)

    def recorren (self):
        for i in range(self.__M):
            print(f"Fila { i:02d}: [{self.__tabla[i]}]")

    def obtInsersiones(self):
        return self.__ocupado