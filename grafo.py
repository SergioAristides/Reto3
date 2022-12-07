from vertice import Vertice
from tkinter import simpledialog
from tkinter import messagebox
import json
class Grafo:
    def __init__(self):
        self.vertices={}
        self.root=None
    def agregar_vertice(self,name,id,coord):
        if id not in self.vertices:
            self.vertices[id]=Vertice(name,id,coord)
    def agregar_arista(self,a,b,p):
        if a.id in self.vertices and b.id in self.vertices:
            self.vertices[a.id].agregarVecino(b,p)
            self.vertices[b.id].agregarVecino(a,p)
    def buscarVertice(self,vertice,buscado,visitados):
        if vertice.id == buscado:
            return vertice
        elif vertice not in visitados:
            visitados.append(vertice)
            for i in vertice.vecinos:
                actual=self.buscarVertice(i[0],buscado,visitados)
                if actual is not None:
                    return actual
            return None
        else:
            return None
    def read_json(self):
        with open('./.json') as data:
            ciudades = json.load(data)
            ciudades=ciudades.get('Colombia').get('stations')
            for ciudad in ciudades:
                self.agregar_vertice(ciudad.get('name'), ciudad.get('iata_code'),(ciudad.get('x'),ciudad.get('y')))
            visitados=[]
            for ciudad in self.vertices:
                for ciudadJson in ciudades:
                    if (ciudadJson.get('iata_code'))==ciudad:
                        for ciud in ciudadJson.get('destinations'):
                            for cf in self.vertices:
                                if cf==ciud:
                                    band=True
                                    for i in visitados:
                                        if i[0]==cf and i[1]==ciudad:
                                            band=False
                                    if band:
                                        visitados.append([ciudad,cf])
                                        pes=None
                                        while True:
                                            try:
                                                pes=int(simpledialog.askstring(title="Peso",prompt=("Ingrese el peso de "+self.vertices[ciudad].name+" y "+self.vertices[cf].name)))
                                                break
                                            except:
                                                messagebox.showwarning(message="Ingrese un numero",title="Error")

                                        self.agregar_arista(self.vertices.get(ciudad), self.vertices.get(cf), pes)
