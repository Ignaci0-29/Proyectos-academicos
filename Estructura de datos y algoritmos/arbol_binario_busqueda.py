from pila_secu import Pila
class BNodo:
    __valor = int
    __izq = object
    __der = object

    def __init__(self, valor):
        self.__valor = valor
        self.__izq = None
        self.__der = None

    def getValor(self):
        return self.__valor
    def getIzq(self):
        return self.__izq
    def getDer(self):
        return self.__der
    
    def setIzq(self, nva):
        self.__izq = nva
    def setDer(self, nva):
        self.__der = nva

    def grado(self,nodo):
        grado = 0
        if nodo.getIzq() is not None:
            grado += 1
        if nodo.getDer() is not None:
            grado += 1
        return grado

class ArbolBB:
    __raiz = object

    def __init__(self):
        self.__raiz = None

    def getRaiz(self):
        return self.__raiz

    def vacio(self):
        return self.__raiz is None

    # 2. Insertar
    def insertar(self, valor):
        self.__raiz = self._insertar(valor, self.__raiz)

    def _insertar(self, valor, nodo):
        if nodo is None:
            return BNodo(valor)
        if valor == nodo.getValor():
            raise ValueError("El valor ya existe en el árbol.")
        elif valor < nodo.getValor():
            nodo.setIzq(self._insertar(valor, nodo.getIzq()))
        else:
            nodo.setDer(self._insertar(valor, nodo.getDer()))
        return nodo

    # 3. Buscar
    def buscar(self, valor):
        return self._buscar(valor, self.__raiz)

    def _buscar(self, valor, nodo):
        if nodo is None:
            raise IndexError("Valor no encontado")
        if valor == nodo.getValor():
            return nodo
        elif valor < nodo.getValor():
            return self._buscar(valor, nodo.getIzq())
        else:
            return self._buscar(valor, nodo.getDer())

    # 4. Suprimir
    def suprimir(self, valor):
        self.__raiz = self._suprimir(valor, self.__raiz)

    def _suprimir(self, valor, nodo):
        if nodo is None:
            raise ValueError("El valor no existe en el árbol.")
        if valor < nodo.getValor():
            nodo.__izq = self._suprimir(valor, nodo.getIzq())
        elif valor > nodo.getValor():
            nodo.__der = self._suprimir(valor, nodo.getDer())
        else:
            # caso 1: sin hijos
            if nodo.getIzq() is None and nodo.getDer() is None:
                return None
            # caso 2: un hijo
            if nodo.getIzq() is None:
                return nodo.getDer()
            if nodo.getDer() is None:
                return nodo.getIzq()
            # caso 3: dos hijos
            predecesor = self._max(nodo.getIzq())
            nodo.setValor(predecesor.getValor())
            nodo.__izq = self._suprimir(predecesor.getValor(), nodo.getIzq())
        return nodo

    # 5. Nivel
    def nivel (self, valor):
        lvl = 1
        return self._nivel(self.__raiz, valor, lvl)
    
    def _nivel(self, nodo, valor, lvl):
        if nodo is None:
            raise IndexError("No se encontro el nodo")
        if valor == nodo.getValor():
            return lvl
        elif valor < nodo.getValor():
            return self._nivel(nodo.getIzq(), valor, lvl + 1)
        else: return self._nivel(nodo.getDer(), valor, lvl + 1)
        
    
    # 6. Hoja
    def hoja(self, valor):
        result = False
        nodo = self.buscar(valor)
        if nodo.grado(nodo) == 0:
            print("El nodo es hoja")
            result = True
        else: 
            print("El nodo no es hoja")
        return result
        

    # 7. Hijo
    def hijo(self, padre_valor, hijo_valor):
        nodo_padre = self.buscar(padre_valor)
        if nodo_padre is None:
            raise IndexError(f"No se encontro el nodo padre con valor {padre_valor}")
        if nodo_padre.getIzq() is not None and nodo_padre.getIzq().getValor() == hijo_valor:
            print(f"El nodo de valor {hijo_valor} es hijo por izquierda del nodo de valor {padre_valor}")
            return True
        if nodo_padre.getDer() is not None and nodo_padre.getDer().getValor() == hijo_valor:
            print(f"El nodo de valor {hijo_valor} es hijo por derecha del nodo de valor {padre_valor}")
            return True
        print(f"El nodo de valor {hijo_valor} NO es hijo del nodo de valor {padre_valor}")
        return False

    # 8. Padre
    def padre(self, padre_valor, hijo_valor):
        nodo_padre = self.buscar(padre_valor)
        if nodo_padre is None:
            raise IndexError(f"No se encontro el nodo padre con valor {padre_valor}")
        hijo_izq = nodo_padre.getIzq()
        hijo_der = nodo_padre.getDer()
        if hijo_izq is not None and hijo_izq.getValor() == hijo_valor:
            print(f"El nodo de valor {padre_valor} es padre del nodo de valor {hijo_valor}")
            return True
        if hijo_der is not None and hijo_der.getValor() == hijo_valor:
            print(f"El nodo de valor {padre_valor} es padre del nodo de valor {hijo_valor}")
            return True
        print(f"El nodo de valor {padre_valor} NO es padre del nodo de valor {hijo_valor}")
        return False

    # 9. Camino (de X a Z si X es ancestro de Z)
    def camino(self, x_valor, z_valor):
        nodo_x = self.buscar(x_valor)
        camino = Pila()
        if self._camino(nodo_x, z_valor, camino):
            return camino
        return None

    def _camino(self, origen, destino, camino):
        if origen is None:
            return False
        if origen.getValor() == destino:
            camino.insertar(origen.getValor())
            return True
        if destino < origen.getValor():
            if self._camino(origen.getIzq(), destino, camino):
                camino.insertar(origen.getValor())
                return True
        else:
            if self._camino(origen.getDer(), destino, camino):
                camino.insertar(origen.getValor())
                return True
        return False

    # 10. Altura
    def altura(self, nodo):
        if nodo is None:
            return 0
        altura_izquierda = self.altura(nodo.getIzq())
        altura_derecha = self.altura(nodo.getDer())
        return 1 + max(altura_izquierda, altura_derecha)

    # 11. Recorridos
    def inorden(self, nodo): #izquierda -> raiz -> derecha
        if nodo is not None:
            self.inorden(nodo.getIzq())
            print(nodo.getValor(), end=" ")
            self.inorden(nodo.getDer())

    def preorden(self, nodo): #raiz -> izquierda -> derecha
        if nodo is not None:
            print(nodo.getValor(), end=" ")
            self.preorden(nodo.getIzq())
            self.preorden(nodo.getDer())

    def posorden(self, nodo): #izquierda -> derecha -> raiz
        if nodo is not None:
            self.posorden(nodo.getIzq())
            self.posorden(nodo.getDer())
            print(nodo.getValor(), end=" ")

if __name__ == '__main__':
    ar=ArbolBB()
    ar.insertar(50)
    ar.insertar(30)
    ar.insertar(70)
    ar.insertar(20)
    ar.insertar(40)
    ar.buscar(30)
    #ar.buscar(80)
    ar.suprimir(20)
    print("Nivel de 40:", ar.nivel(40))
    ar.hoja(30)
    ar.hoja(40)
    ar.hijo(30,40)
    ar.hijo(40,30)
    ar.padre(30,40)
    ar.padre(40,30)
    cam=ar.camino(50,40)
    print("El camino de 50 a 40 es: "); cam.mostrar()
    if ar.camino(70, 40):
        print("NO hay camino de 70 a 40")
    print(f"La altura del arbol es {ar.altura(ar.getRaiz())}")
    print(f"\n Inorden ", end="")
    ar.inorden(ar.getRaiz()); print()
    print(f"\n Preorden ", end="")
    ar.preorden(ar.getRaiz()); print()
    print(f"\n Posorden ", end="")
    ar.posorden(ar.getRaiz()); print()