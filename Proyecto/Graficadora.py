# Importamos las librerias necesarias
from tkinter import Tk, Canvas
from colour import Color # Para este necesitamos instalar la libreria "colour" con
# pip install colour
import math

import Funciones as f

# Definimos las variables necesarias para la ventana y el canvas
AnchoCanva = 500
AltoCanva = 500
DefinicionCanva = 5
DefinicionColores = 100

# Seleccionamos la funcion que queremos graficar
f.seleccionarAckleyFunction()



# Creamos la ventana y el canvas
window = Tk()
Canvas = Canvas(window, width=AnchoCanva, height=AltoCanva)

# Definimos los colores que vamos a usar y haecemos un rango de colores
red = Color("red")
colors = list(Color("red").range_to(Color("green"),DefinicionColores))

# Por cada pixel del canvas, calculamos el valor de la funcion y pintamos el pixel
for i in range(0,AnchoCanva,DefinicionCanva):
    for o in range(0,AltoCanva,DefinicionCanva):
        x = (i-0)*((f.FinalDomX-f.InicioDomX)/(AnchoCanva-0))+f.InicioDomX
        y = (o-0)*((f.FinalDomY-f.InicioDomY)/(AltoCanva-0))+f.InicioDomY
        fx = f.Funcion(x,y)
        colorIndex = round((fx-f.InicioRango)*((len(colors)-0)
                                               /(f.FinalRango-f.InicioRango))+0)
        Canvas.create_rectangle(i,o,i*DefinicionCanva,o*DefinicionCanva,
                                 outline = colors[colorIndex], fill= colors[colorIndex])



# Configuramos el canvas y mostramos la ventana
Canvas.pack()
window.mainloop()
