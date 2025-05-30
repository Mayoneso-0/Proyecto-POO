# Importamos las librerias necesarias
from tkinter import Tk, Canvas
from colour import Color # Para este necesitamos instalar la libreria "colour" con
# pip install colour

import Funciones as f
import Algoritmo as alg

# Definimos las variables
AnchoCanva = 500
AltoCanva = 500
DefinicionCanva = 5
DefinicionColores = 100
DibujoParticulas = []

NumParticulas = 5
w = 0.2
pp = 0.5
pg = 1

# Seleccionamos la funcion que queremos graficar
f.seleccionarAckleyFunction()


# Creamos la ventana y el canvas
window = Tk()
Canvas = Canvas(window, width=AnchoCanva, height=AltoCanva)

# Gradiente Colores
colors = list(Color("red").range_to(Color("green"),DefinicionColores))

# Graficamos Funcion
for i in range(0,AnchoCanva,DefinicionCanva):
    for o in range(0,AltoCanva,DefinicionCanva):
        x = (i-0)*((f.FinalDomX-f.InicioDomX)/(AnchoCanva-0))+f.InicioDomX
        y = (o-0)*((f.FinalDomY-f.InicioDomY)/(AltoCanva-0))+f.InicioDomY
        fx = f.Funcion(x,y)
        colorIndex = round((fx-f.InicioRango)*((len(colors)-0)
                                               /(f.FinalRango-f.InicioRango))+0)
        Canvas.create_rectangle(i,o,i*DefinicionCanva,o*DefinicionCanva,
                                 outline = colors[colorIndex], fill= colors[colorIndex])
Canvas.pack()

enjambre1 = alg.Enjambre(num_particulas = NumParticulas)

def IniciarEnjamre(event):
    enjambre1.crear_enjambre(ancho_canva= AnchoCanva, alto_canva= AltoCanva)
    for i in enjambre1.particulas:
        DibujoParticulas.append(Canvas.create_rectangle(i.x,i.y,i.x+5,i.y+5, fill="blue"))
window.bind("<q>",IniciarEnjamre)

def IterarAlgoritmo(event):
    nuevoPosX, nuevoPosY = enjambre1.iterar_algorimo(ancho_canva= AnchoCanva, alto_canva= AltoCanva,w= w, pp= pp, pg=pg)
    for i in range(0,len(enjambre1.particulas)):
        Canvas.move(DibujoParticulas[i],nuevoPosX[i],nuevoPosY[i])
window.bind("<w>",IterarAlgoritmo)

def FinalizarAlgoritmo(event):
    pass
window.bind("<e>",FinalizarAlgoritmo)

# Blucle de ventana
window.mainloop()
