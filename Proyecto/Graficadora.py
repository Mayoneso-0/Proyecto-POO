# Importamos las librerias necesarias
from tkinter import Tk, Canvas
from colour import Color #Para este necesitamos instalar libreria "colour" con
# pip install colour

import Funciones as f
import Algoritmo as alg

# Definimos las variables
ancho_canva = 500
alto_canva = 500
definicion_canva = 5
definicion_colores = 100
dibujo_particulas = []

num_particulas = 8
w = 0.4
pp = 0.5
pg = 0.7

# Seleccionamos la funcion que queremos graficar
f.seleccionar_rastrigin_function()

# Creamos la ventana y el canvas
window = Tk()
canvas = Canvas(window, width=ancho_canva, height=alto_canva)

# Gradiente Colores
colors = list(Color("red").range_to(Color("green"),definicion_colores))

# Graficamos Funcion 
for i in range(0,ancho_canva,definicion_canva):
    for o in range(0,alto_canva,definicion_canva):
        x = (i-0)*((f.final_dom_x-f.inicio_dom_x)/(ancho_canva-0))+f.inicio_dom_x
        y = (o-0)*((f.final_dom_y-f.inicio_dom_y)/(alto_canva-0))+f.inicio_dom_y
        fx = f.funcion(x,y)
        color_index = round((fx-f.inicio_rango)*((len(colors)-0)
                                               /(f.final_rango-f.inicio_rango))+0)
        canvas.create_rectangle(i,o,i+definicion_canva,o+definicion_canva,
                                 outline = colors[color_index],
                                 fill= colors[color_index])
canvas.pack()

# Creamos el enjambre de particulas
enjambre1 = alg.Enjambre(num_particulas = num_particulas)

# Definimos las funciones de los eventos del teclado
enjambre_creado = False
def iniciar_enjambre(event):
    global enjambre_creado
    if not enjambre_creado:
        enjambre1.crear_enjambre(ancho_canva=ancho_canva, alto_canva=alto_canva)
        for i in enjambre1.particulas:
            dibujo_particulas.append(canvas.create_rectangle(i.x,i.y,i.x+5,i.y+5,
                                                            fill="blue"))
        enjambre_creado = True
# Creamos el enjambre al presionar la tecla "q"
window.bind("<q>", iniciar_enjambre)

def iterar_algoritmo(event):
    nuevo_pos_x, nuevo_pos_y = enjambre1.iterar_algorimo(ancho_canva=ancho_canva,
                                                        alto_canva=alto_canva,
                                                        w=w, pp=pp, pg=pg)
    for i in range(0,len(enjambre1.particulas)):
        canvas.move(dibujo_particulas[i],nuevo_pos_x[i],nuevo_pos_y[i])
# Iteramos el algoritmo al presionar la tecla "w"
window.bind("<w>", iterar_algoritmo)

def finalizar_algoritmo(event):
    window.destroy()
    print()
    print("Algoritmo finalizado.")
    print("Mejor posicion global encontrada:",
          format(f.trans_lin_dom_x(enjambre1.mejor_pos_global_x,0,ancho_canva),
                 ".5f"),
          format(f.trans_lin_dom_y(enjambre1.mejor_pos_global_y,0,alto_canva),
                 ".5f"))
    print("Mejor valor encontrado:",
          format(f.funcion(f.trans_lin_dom_x \
                           (enjambre1.mejor_pos_global_x,0,ancho_canva),
                           f.trans_lin_dom_y \
                           (enjambre1.mejor_pos_global_y,0,alto_canva)),
                            ".5f"))
# Finalizamos el algoritmo al presionar la tecla "e"
window.bind("<e>", finalizar_algoritmo)

# Bucle de ventana
window.mainloop()
