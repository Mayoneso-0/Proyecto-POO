# Importamos las librerias necesarias
# Necesitamos instalar algunas previamente con:
# pip install matplotlib
# pip install numpy
# pip install colour

import os
import json
import math
from tkinter import Tk, Canvas
from colour import Color

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np

import Funciones as fun
import Algoritmo as alg


# Definimos las variables
if os.path.exists('config.json'):
    with open('config.json', 'r') as f:
        config = json.load(f)
    
    ancho_canva = config['ancho_canva']
    alto_canva = config['alto_canva']
    definicion_canva = config['definicion_canva']
    definicion_colores = config['definicion_colores']
    num_particulas = config['num_particulas']
    w = config['w']
    pp_inicial = config['pp_inicial']
    pp_final = config['pp_final']
    pg_inicial = config['pg_inicial']
    pg_final = config['pg_final']
    min_iteraciones = config['min_iteraciones']
    manual = config['manual']
    funcion_objetivo = config['funcion_objetivo']
    resultados = config['resultados']

"""
Seleccionamos la funcion que queremos graficar
"""
funciones = {
        "Rastrigin": fun.seleccionar_rastrigin_function,
        "Ackley": fun.seleccionar_ackley_function,
        "Beale": fun.seleccionar_beale_function,
        "Booth": fun.seleccionar_booth_function,
        "Bukin N. 6": fun.seleccionar_bukin_n6_function,
        "Cross-in-Tray": fun.seleccionar_cross_in_tray_function,
        "Easom": fun.seleccionar_easom_function, 
        "Eggholder": fun.seleccionar_egg_holder_function, 
        "Goldstein-Price": fun.seleccionar_goldstein_price_function, 
        "Himmelblau": fun.seleccionar_himmelblau_function, 
        "Holder Table": fun.seleccionar_holder_table_function, 
        "Levi N. 13": fun.seleccionar_levi_n13_function, 
        "Griewank": fun.seleccionar_griewank_function,
        "Matyas": fun.seleccionar_matyas_function, 
        "McCormick": fun.seleccionar_mc_cormick_function, 
        "Mi Función": fun.seleccionar_mi_function, 
        "Rosenbrock": fun.seleccionar_rosenbrock_function, 
        "Schaffer N. 2": fun.seleccionar_schaffer_n2_function, 
        "Schaffer N. 4": fun.seleccionar_schaffer_n4_function, 
        "Sphere": fun.seleccionar_sphere_function, 
        "Styblinski-Tang": fun.seleccionar_styblinski_tang_function, 
        "Three-Hump Camel": fun.seleccionar_three_hump_camel_function
    }

funciones[funcion_objetivo]()

iteracion = 0
pp = pp_inicial
pg = pg_inicial
dibujo_particulas = []

seguir_iterando = True

# Creamos la ventana y el canvas
window = Tk()
window.title("Algoritmo PSO")
window.iconbitmap("icono.ico")

# Frame izquierdo para canvas 2D
frame_left = __import__('tkinter').Frame(window)
frame_left.pack(side ='left', fill ='both', expand = True)
# Frame derecho para canvas 3D
frame_right = __import__('tkinter').Frame(window)
frame_right.pack(side ='right', fill = 'both', expand = True)

# Canvas de Tkinter y visualización 2D 
canvas = Canvas(frame_left, width = ancho_canva, height = alto_canva)
canvas.pack(fill = 'both', expand = True)

# Gradiente Colores
colors = list(Color("red").range_to(Color("green"), definicion_colores))

# Graficamos Funcion con normalización adaptable
# Primero calculamos todos los valores de la función en la grilla
valores_fx = []
for i in range(0, ancho_canva, definicion_canva):
    for o in range(0, alto_canva, definicion_canva):
        x = (i-0) * ((fun.final_dom_x - fun.inicio_dom_x) / 
                    (ancho_canva - 0)) + fun.inicio_dom_x
        y = (o-0)*((fun.final_dom_y - fun.inicio_dom_y) /
                   (alto_canva - 0)) + fun.inicio_dom_y
        fx = fun.funcion(x, y)
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
            color_index = int((norm_fx - norm_min) / (
                norm_max - norm_min) * (len(colors)-1))
        else:
            color_index = int((fx - min_fx) / 
                              (max_fx - min_fx) * (len(colors) - 1))
        color_index = max(0, min(color_index, len(colors)-1))
        canvas.create_rectangle(i, o, i + definicion_canva, o+definicion_canva,
                               outline = colors[color_index],
                               fill = colors[color_index])

fig = plt.figure(figsize = (ancho_canva/100, alto_canva/100))
ax = fig.add_subplot(111, projection='3d')
# Crear malla para la función objetivo
x = np.linspace(fun.inicio_dom_x, fun.final_dom_x, 100)
y = np.linspace(fun.inicio_dom_y, fun.final_dom_y, 100)
X, Y = np.meshgrid(x, y)
Z = np.vectorize(fun.funcion)(X, Y)
surf = ax.plot_surface(X, Y, Z, cmap ='RdYlGn', edgecolor ='none', alpha = 0.9)
ax.set_title('Función objetivo (3D)')
ax.set_xlabel('x')
ax.set_ylabel('y')  
ax.set_zlabel('f(x, y)')

# Creamos el enjambre de particulas
enjambre1 = None
# Embezamos la figura 3D en Tkinter a la derecha
canvas3d = FigureCanvasTkAgg(fig, master = frame_right)
canvas3d.draw()
canvas3d.get_tk_widget().pack(fill='both', expand=True)

# Definimos las funciones de los eventos del teclado
enjambre_creado = False
def iniciar_enjambre(event):
    global enjambre_creado, enjambre1, dibujo_particulas
    if not enjambre_creado:
        enjambre1 = alg.Enjambre(num_particulas = num_particulas)
        enjambre1.crear_enjambre(ancho_canva = ancho_canva, 
                                 alto_canva = alto_canva)
        for i in enjambre1.particulas:
            dibujo_particulas.append(canvas.create_rectangle(i.x, i.y, 
                                                             i.x + 5, i.y + 5, 
                                                             fill = "blue"))
        enjambre_creado = True
# Creamos el enjambre al presionar la tecla "q"
window.bind("<q>", iniciar_enjambre)

def iterar_algoritmo(event):
    global seguir_iterando,finalizar_algoritmo, pp, pg, iteracion, min_iteraciones
    if enjambre1 is None:
        print("Primero debes crear el enjambre presionando 'q'.")
        return
    num_coords_iguales = 0
    mejor_coords_penultima = 0
    mejor_cooords_ultima = (enjambre1.mejor_pos_global_x, 
                            enjambre1.mejor_pos_global_y)
    # Si manual es True, iteramos solo una vez
    if manual:
        nuevo_pos_x, nuevo_pos_y = enjambre1.iterar_algorimo(ancho_canva = ancho_canva,
                                                            alto_canva = alto_canva,
                                                            w = w, pp = pp, pg = pg)
        for i in range(0, len(enjambre1.particulas)):
            canvas.move(dibujo_particulas[i], nuevo_pos_x[i], nuevo_pos_y[i])
        # Actualizamos los valores de pp y pg por cada iteración
        if pp > pp_final:
                pp -= 0.1
        if pg < pg_final:
                pg += 0.1
    # Si manual es False, iteramos cada 100ms hasta que converja
    else:
        while seguir_iterando:
            nuevo_pos_x, nuevo_pos_y = enjambre1.iterar_algorimo(ancho_canva = ancho_canva,
                                                                alto_canva = alto_canva,
                                                                w = w, pp = pp, pg = pg)
            for i in range(0,len(enjambre1.particulas)):
                canvas.move(dibujo_particulas[i], nuevo_pos_x[i], nuevo_pos_y[i])
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

def finalizar_algoritmo(event=None):
    try:
        global seguir_iterando
        seguir_iterando = False
        if os.path.exists('config.json'):
            with open('config.json', 'r') as f:
                config = json.load(f)
        else:
            config = {}
        config['resultados'] = (
            resultados+
            "\nAlgoritmo finalizado." +
            "\nMejor posicion global encontrada: "+
            format(fun.trans_lin_dom_x(enjambre1.mejor_pos_global_x, 0, 
                                       ancho_canva), ".5f") + " " +
            format(fun.trans_lin_dom_y(enjambre1.mejor_pos_global_y,0 
                                       ,alto_canva), ".5f") +
            "\nMejor valor encontrado: "+
            format(fun.funcion(fun.trans_lin_dom_x \
                    (enjambre1.mejor_pos_global_x, 0, ancho_canva),
                    fun.trans_lin_dom_y \
                    (enjambre1.mejor_pos_global_y, 0, alto_canva)), ".5f")+
            "\n"
        )
        with open('config.json', 'w') as f:
            json.dump(config, f)
        window.destroy()
        os._exit(0)
    except Exception as e:
        seguir_iterando = False
        if os.path.exists('config.json'):
            with open('config.json', 'r') as f:
                config = json.load(f)
        else:
            config = {}
        config['resultados'] = resultados 
        + "Algoritmo no finalizado correctamente.\n\n"
        with open('config.json', 'w') as f:
            json.dump(config, f)
        window.destroy()
        os._exit(0)

# Finalizamos el algoritmo al presionar la tecla "e"
window.bind("<e>", finalizar_algoritmo)
window.protocol("WM_DELETE_WINDOW", finalizar_algoritmo)

# Bucle de ventana
window.mainloop()
