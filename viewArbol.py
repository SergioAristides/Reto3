from pygame import *
from arbolBinary import Arbol
import sys
from tkinter import simpledialog
from tkinter import messagebox
from nodo import Nodo 

init()
#variables globales
arbol=Arbol()

#dimenciones pantalla style
WIDTH=800
HEIGTH=600
size= (WIDTH,HEIGTH)
screen = display.set_mode(size)
display.set_caption("BinaryTree")
isRunning=True
#colors
WHITE =(255,255,255)
BLACK =(0,0,0)
GRIS=(206,200,194)
GREEN=(27,230,17)
#coordenadas de los botones
agregar=Rect(650,60,110,60)
preorden=Rect(650,180,110,60)
inorden=Rect(650,300,110,60)
post_orden=Rect(650,420,110,60)
#Fuente para los botones
myFont=font.SysFont("Pacifico",30)
# the input dialog
def pedir_datos():
    num=None
    bandera=True
    while bandera:
        try:
            num = int(simpledialog.askstring(title="Test",prompt="valor nodo a insertar:"))
            bandera=False
        except:
            messagebox.showinfo(message="except",title="exception")
    return num
#Raiz
def pedirRaiz():
    num=None
    bandera=True
    while bandera:
        try:
            num=int(simpledialog.askstring(title="Test",prompt="ingrese la raiz del arbol:"))
            bandera=False
        except:
            messagebox.showinfo(message="except",title="exception")
    return num
def printPreorden():
    arbol.retorna=""
    ret=arbol.preorden()
    messagebox.showinfo(message=ret, title="Preorden")
def printInorder():
    arbol.retorna=""
    ret=arbol.inorden()
    messagebox.showinfo(message=ret, title="Inorder")
def printPostOrden():
    arbol.retorna=""
    ret=arbol.postorden()
    messagebox.showinfo(message=ret, title="PostOrden")
    
def add_node_tree(value):
    arbol.agregar(value)

#pinta los botones
def pintarBoton(screen,color,boton,palabra):
    draw.rect(screen,color,boton)
    text=myFont.render(palabra,True,BLACK)
    screen.blit(text,(boton.x+(boton.width-text.get_width())/2,
                    boton.y+(boton.height-text.get_height())/2))



def drawArbol(nodo):
    arbol.cambiarCoordenadas()
    if nodo is not None:
        tupla=(nodo.x,nodo.y)
        draw.circle(screen,nodo.color,tupla,nodo.radio,nodo.grosor)
        mitexto=myFont.render(str(nodo.dato),True,BLACK)
        tupla=(nodo.xFont,nodo.yFont)
        screen.blit(mitexto,tupla)
        drawArbol(nodo.izquierda)
        drawArbol(nodo.derecha)
        
        
    pass
def draw_circle():
    draw.circle(screen,[27,230,17 ], (350,250),40,5)
num_insert=pedirRaiz()
arbol.raiz=Nodo(num_insert)
arbol.retorna=""
print(arbol.raiz.dato)
while isRunning:
    for e in event.get():
        if e.type == QUIT:
            isRunning=False
        if e.type==MOUSEBUTTONDOWN:
            if agregar.collidepoint(mouse.get_pos()):
                nuevo_nodo=pedir_datos()
                add_node_tree(nuevo_nodo)
            if preorden.collidepoint(mouse.get_pos()):
                printPreorden()
                pass

            if inorden.collidepoint(mouse.get_pos()):
                printInorder()
                pass
            if post_orden.collidepoint(mouse.get_pos()):
                printPostOrden()
                pass
                
    
    screen.fill(WHITE)
    pintarBoton(screen,GRIS,agregar,"Agregar")
    pintarBoton(screen,GRIS,preorden,"Preorden")
    pintarBoton(screen,GRIS,inorden,"Inorden")
    pintarBoton(screen,GRIS,post_orden,"Post Orden")
    drawArbol(arbol.raiz)
    display.flip()