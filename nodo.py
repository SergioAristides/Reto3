from pygame import *
#rama de un arbol o hoja
class Nodo:
    def __init__(self,dato):
        self.dato=dato
        #el de la izquierda hace referencia a los posibles nodos que tiene 
        #nodo a crear
        self.izquierda=None
        self.derecha=None
        self.x=None
        self.y=None
        self.color=(27,230,17)
        self.radio=40
        self.grosor=4
        self.xFont=None
        self.yFont=None
        self.textFont=None
        #self.circle(radius, extent=None, steps=None)