# Importamos las librerias necesarias
from tkinter import Tk, Canvas
from colour import Color #Para este necesitamos instalar libreria "colour" con
# pip install colour

import Funciones as f
import Algoritmo as alg
import math

# Definimos las variables
ancho_canva = 500
alto_canva = 500
definicion_canva = 5
definicion_colores = 100
dibujo_particulas = []

num_particulas = 12
w = 0.6
pp_inicial = 2.5
pp_final = 0.5
pg_inicial = 0.5
pg_final = 2.5
pp = pp_inicial
pg = pg_inicial
iteracion = 0
min_iteraciones = 25

manual = False 
seguir_iterando = True

# Seleccionamos la funcion que queremos graficar
# egg_holder_function

f.seleccionar_rastrigin_function()

# Creamos la ventana y el canvas
window = Tk()
canvas = Canvas(window, width=ancho_canva, height=alto_canva)

# Gradiente Colores
colors = list(Color("red").range_to(Color("green"),definicion_colores))

# Graficamos Funcion con normalización adaptable
# Primero calculamos todos los valores de la función en la grilla
valores_fx = []
for i in range(0, ancho_canva, definicion_canva):
    for o in range(0, alto_canva, definicion_canva):
        x = (i-0)*((f.final_dom_x-f.inicio_dom_x)/(ancho_canva-0))+f.inicio_dom_x
        y = (o-0)*((f.final_dom_y-f.inicio_dom_y)/(alto_canva-0))+f.inicio_dom_y
        fx = f.funcion(x, y)
        valores_fx.append(fx)

min_fx = min(valores_fx)
max_fx = max(valores_fx)

# Ahora graficamos los valores en el canvas
indice_valor = 0
for i in range(0, ancho_canva, definicion_canva):
    for o in range(0, alto_canva, definicion_canva):
        fx = valores_fx[indice_valor]
        indice_valor += 1
        # Si el rango es muy grande, usamos logaritmo para mejorar contraste
        if max_fx - min_fx > 90:
            norm_fx = math.log(fx - min_fx + 1) # Evitamos log(0) sumando 1
            norm_min = 0
            norm_max = math.log(max_fx - min_fx + 1)
            color_index = int((norm_fx - norm_min) / (norm_max - norm_min) * (len(colors)-1))
        else:
            color_index = int((fx - min_fx) / (max_fx - min_fx) * (len(colors)-1))
        color_index = max(0, min(color_index, len(colors)-1))
        canvas.create_rectangle(i, o, i+definicion_canva, o+definicion_canva,
                               outline=colors[color_index],
                               fill=colors[color_index])
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
    global seguir_iterando,finalizar_algoritmo, pp, pg, iteracion, min_iteraciones
    num_coords_iguales = 0
    mejor_coords_penultima = 0
    mejor_cooords_ultima = (enjambre1.mejor_pos_global_x, enjambre1.mejor_pos_global_y)
    # Si manual es True, iteramos solo una vez
    if manual:
        nuevo_pos_x, nuevo_pos_y = enjambre1.iterar_algorimo(ancho_canva=ancho_canva,
                                                            alto_canva=alto_canva,
                                                            w=w, pp=pp, pg=pg)
        for i in range(0,len(enjambre1.particulas)):
            canvas.move(dibujo_particulas[i],nuevo_pos_x[i],nuevo_pos_y[i])
        # Actualizamos los valores de pp y pg por cada iteración
        if pp > pp_final:
                pp -= 0.1
        if pg < pg_final:
                pg += 0.1
    # Si manual es False, iteramos cada 100ms hasta que converja
    else:
        while seguir_iterando:
            nuevo_pos_x, nuevo_pos_y = enjambre1.iterar_algorimo(ancho_canva=ancho_canva,
                                                                alto_canva=alto_canva,
                                                                w=w, pp=pp, pg=pg)
            for i in range(0,len(enjambre1.particulas)):
                canvas.move(dibujo_particulas[i],nuevo_pos_x[i],nuevo_pos_y[i])
            window.update()
            window.after(100)
            mejor_coords_penultima = mejor_cooords_ultima
            # Comprobamos las coordenadas no cambien desde las ultimas 10 iteraciones
            mejor_cooords_ultima = (enjambre1.mejor_pos_global_x, enjambre1.mejor_pos_global_y)
            if mejor_coords_penultima == mejor_cooords_ultima:
                num_coords_iguales += 1
            else:
                num_coords_iguales = 0
            if num_coords_iguales >= 10 and iteracion > min_iteraciones:
                seguir_iterando = False
                print("El algoritmo ha convergido.")
                finalizar_algoritmo(event)
            # Actualizamos los valores de pp y pg por cada iteración
            if pp > pp_final:
                pp -= 0.1
            if pg < pg_final:
                pg += 0.1
            iteracion += 1
# Iteramos el algoritmo al presionar la tecla "w"
window.bind("<w>", iterar_algoritmo)

def finalizar_algoritmo(event):
    global seguir_iterando
    seguir_iterando = False
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
