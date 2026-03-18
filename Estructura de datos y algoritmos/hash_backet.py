import numpy as np

class HashBacket:
    __tabla = np.ndarray
    __conts = np.ndarray
    __tamaño = int
    __areaPrim = int
    __areaOver = int
    __bucket = int

    def __init__(self, clavesEsperadas=800, bucket=5):
        self.__tamaño = round(self.proxPrim((clavesEsperadas / bucket) * 1.2))
        self.__areaPrim = round(clavesEsperadas / bucket)
        self.__areaOver = self.__areaPrim + 1
        self.__bucket = bucket
        self.__tabla = np.zeros((self.__tamaño, bucket), dtype = int)
        self.__conts = np.zeros(self.__tamaño, dtype = int)

    def primo(self, numero):
        if numero <= 1:
            return False
        for i in range(2, int(numero**0.5) + 1):
            if numero % i == 0:
                return False
        return True

    def proxPrim(self, numero):
        while not self.primo(numero):
            numero += 1
        return numero

    def hash_division(self, clave):
        return clave  % self.__M

    def insertar(self, clave):
        claveHash = self.hash_division(clave)
        if self.__conts[claveHash] < self.__bucket:
            self.__tabla[claveHash][self.__conts[claveHash]] = clave
            self.__conts[claveHash] += 1
        else:
            i = self.__areaOver
            while i < self.__tamaño and not self.__conts[i] < self.__bucket:
                i += 1
            if i == self.__tamaño:
                print("Area de overflow llena")
            else:
                self.__tabla[i][self.__conts[i]] = clave
                self.__conts[i] += 1

    def buscar(self, clave):
        claveHash = self.hash_division(clave)
        i = claveHash
        j = 0
        encontro = False 

        while not encontro and j < self.__bucket:
            if self.__tabla[i][j] == clave:
                encontro = True
            else:
                j += 1

        if not encontrado:
            i = self.__areaOver
            j = 0
            while not encontrado and i < self__tamaño:
                while j < self.__conts[i]:
                    if self.__tabla[i][j] == clave:
                        encontrado = True
                    j += 1
                i += 1
                j = 0
            if encontrado:
                print("Se encontro el elemento en el area Overflow")
            else: print("No se encontro el elemento")
        else: print("Se encontro el elemento en el area primaria")

    def recorrerHash(self):
        ANCHO_CELDA = 4
        print("--- INICIO TABLA HASH (buckets) ---")
        print("\n === Area Primaria ===")
        for i in range(self.__tamaño):
            if i == self.__areaOver:
                print("\n === Area Overflow ===")
            elementos_bucket = []
            for j in range(self.__bucket):
                valor_celda = self.__tabla[i][j]
                celda_formateada = f"{str(valor_celda):>{ANCHO_CELDA}}"
                elementos_bucket.append(celda_formateada)
            contenido = " | ".join(elementos_bucket)
            print(f"Bucket {i:02d}: [ {contenido} ]")
        print("--- FIN TABLA HASH ---")

    def mostrarValores(self):
        print(f"""
                Valores:
                Tamaño total: {self.__tamaño}
                Area primaria: {self.__areaPrim}
                Area overflow: {self.__areaOver}
                Buckets: {self.__bucket}
                """)
                