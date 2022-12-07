class Vertice:
    def __init__(self,name,id,coord):
        self.id=id
        self.coords=coord
        self.vecinos=[]
        self.visitado=False
        self.padre=None
        self.name=name

    def agregarVecino(self,vertice,peso):
        if vertice not in self.vecinos:
            self.vecinos.append([vertice,peso])
