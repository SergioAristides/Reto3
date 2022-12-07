from nodo import Nodo 
class Arbol:
    #alk crear el arbol creamos la raiz
    def __init__(self,*args):
        if len(args)==1:
            self.raiz=Nodo(args[0])
            self.retorna=""
        if len(args)==0:
            self.raiz=None
            self.retorna=None
    #agregacion recursiva dependiendo de su valor 
    def agregar_recursivo(self,nodo,dato):
        if dato<nodo.dato:
            if nodo.izquierda is None:
                nodo.izquierda=Nodo(dato)
            else:
                self.agregar_recursivo(nodo.izquierda,dato)
        else:
            if nodo.derecha is None:
                nodo.derecha=Nodo(dato)
            else:
                self.agregar_recursivo(nodo.derecha,dato)
    #simplemente visitamos toda la izquierda luego el actual y despues toda la derecha
    def inorderden_recursivo(self,nodo):
        if nodo is not None:
            self.inorderden_recursivo(nodo.izquierda)
            self.retorna+=str(nodo.dato)+", "
            #print(nodo.dato,end=", ")
            self.inorderden_recursivo(nodo.derecha)
        return self.retorna
    #se visita el actual despues la izquierda y despues la derecha

    def preorden_recursivo(self,nodo):
        if nodo is not None:
            self.retorna+=str(nodo.dato)+", "
            #print(nodo.dato,end=", ")
            self.preorden_recursivo(nodo.izquierda)
            self.preorden_recursivo(nodo.derecha)
        return self.retorna
    # primero la izquierda luego la derecha y finalmente el nodo actual    
    def post_orden_recursivo(self,nodo):
        if nodo is not None:
            self.post_orden_recursivo(nodo.izquierda)
            self.post_orden_recursivo(nodo.derecha)
            #print(nodo.dato,end=", ")
            self.retorna+=str(nodo.dato)+", "
        return self.retorna
    def coordenadasNodosRecursivo(self,nodo,x,y):
        if nodo is not None:
            nodo.x=x
            nodo.y=y
            nodo.textFont=str(nodo.dato)
            nodo.xFont=x-8
            nodo.yFont=y-8
            self.coordenadasNodosRecursivo(nodo.izquierda,x-100,y+100)
            self.coordenadasNodosRecursivo(nodo.derecha,x+100,y+100)
        pass
        
    #funciones publicas
    def cambiarCoordenadas(self):
        self.coordenadasNodosRecursivo(self.raiz,380,50)
    def agregar(self,dato):
        self.agregar_recursivo(self.raiz,dato)
    def inorden(self):
        print("imprimeiendo arbol indorden")
        retorna=self.inorderden_recursivo(self.raiz)
        return retorna
        print("")
    def preorden(self):
        print("imprimiendo arbol preorden")
        retorna=self.preorden_recursivo(self.raiz)
        return retorna
        print("")
    def postorden(self):
        print("imprimiendo arbol postorden: ")
        retorna=self.post_orden_recursivo(self.raiz)
        return retorna
        print("")