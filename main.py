from pygame import *
from grafo import Grafo
import sys
from tkinter import *
from tkinter import ttk

grafo=Grafo()
grafo.read_json()

init()

list_destinations=[]
listOrigenes=[]
for i in grafo.vertices:
    listOrigenes.append(grafo.vertices[i].name)
origin = ""
destin=""

def destinations(origin):
    for i in grafo.vertices:
        if grafo.vertices[i].name==origin:
            for j in grafo.vertices[i].vecinos:
                add=j[0].name
                list_destinations.append(add)
            break
    return list_destinations

'''
def dijkstra(origin,destin,ciuds,peso):
    for i in grafo.vertices[origin].vecinos:
        if i[0].name==destin:
            
            return 
        else:
            
    
    pass
''' 
"""
def dijkstra(origin,destin):
    listaCiudades=[]
    list=grafo.vertices[origin].vecinos
    menor=list[1]
    if(origin!=destin):
        for i in grafo.vertices[origin].vecinos:
            if(i[1]<menor):
                menor=i[1]
        listaCiudades.append(grafo.vertices[origin].vecinos.name)
        new_origin=grafo.vertices[origin].vecinos.name
        dijkstra(new_origin,destin)
    else:
        return listaCiudades
    
"""     

        
def obtener2():
    destin=combo2.get()
    origin=combo.get()
    #print(dijkstra(origin,destin))
    ventana.destroy()
    return destin
def obtener():
    origin=combo.get()
    list_destinations=destinations(origin)
    combo2['values']=list_destinations
    combo2.current(0)
    return origin
def initBoxOrigin():
    combo.place(x=50,y=100)
    combo2.place(x=50,y=190)
    combo['values']=listOrigenes
    combo.current(0)
    ventana.geometry("300x300")
    boton=Button(ventana,command=obtener,text="elegir").place(x=80,y=130)
    boton2=Button(ventana,command=obtener2,text="aceptar").place(x=80,y=220)
    return ventana


            
#print(listOrigenes)
#dimensiones pantalla
WIDTH=800
HEIGTH=600
size= (WIDTH,HEIGTH)
screen = display.set_mode(size)
display.set_caption("mode")

#fondMap=image.load("images/mapa.png").convert()
#fond=image.load("images/mapa.png").convert()

fond=image.load("images/FondPrincipal.jpg").convert()
mapFond=image.load("images/mapa.png").convert()
fond=transform.scale(fond,(WIDTH,HEIGTH))
mapFond=transform.scale(mapFond,(WIDTH,HEIGTH))
#colores
BLACK =(0,0,0)
WHITE =(255,255,255)
GREEN =(0,255,0)
BLUE =(255,0,0)
RED =(0,0,255)
YELLOW =(216,255,0)
ORANGE =(255,131,0)
BROWN=(86,44,0)
GRIS=(206,200,194)
#Fuente para los botones
myFont=font.SysFont("Pacifico",30)
#Coordenadas botones
map=Rect(650,60,110,60)
cart=Rect(650,200,110,60)
tree=Rect(650,500,110,60)
elegir=Rect(650,150,110,60)
#pinta los botones
def pintarBoton(screen,color,boton,palabra):
    draw.rect(screen,color,boton)
    text=myFont.render(palabra,True,BLACK)
    screen.blit(text,(boton.x+(boton.width-text.get_width())/2,
                    boton.y+(boton.height-text.get_height())/2))



#controlador de FPS
clock=time.Clock() 
isRunnig =True
def drawPoint():
    for i in grafo.vertices:
        draw.circle(screen, BLACK,grafo.vertices.get(i).coords, 4)
def drawArista():
    for i in grafo.vertices:
        for j in grafo.vertices.get(i).vecinos:
            draw.line(screen, BROWN, grafo.vertices[i].coords, j[0].coords,1)
screen.blit(fond,(0,0))
workInMap=False
while isRunnig:
    for e in event.get():
        if e.type == QUIT:
            isRunnig=False
        if e.type == MOUSEBUTTONDOWN:
            if(map.collidepoint(mouse.get_pos())):
                screen.blit(mapFond,[0,0])
                workInMap=True
            if(cart.collidepoint(mouse.get_pos())):
                pass
            if(tree.collidepoint(mouse.get_pos())):
                pass
            if(elegir.collidepoint(mouse.get_pos())):
                ventana = Tk()
                combo=ttk.Combobox(ventana)
                combo2=ttk.Combobox(ventana)
                box=initBoxOrigin()
                box.mainloop()
    pintarBoton(screen,GRIS,map,"MAP")
    if workInMap:
        pintarBoton(screen,GRIS,map,"MAP")
        pintarBoton(screen, GRIS, elegir,"Destinos")
        drawPoint()
        drawArista()
    else:
        pintarBoton(screen,GRIS,cart,"CART")
        pintarBoton(screen,GRIS,tree,"TREE")
    display.flip()
quit() 