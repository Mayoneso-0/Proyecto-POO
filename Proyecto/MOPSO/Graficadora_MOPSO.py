# Importamos las librerías necesarias
from tkinter import Tk, Canvas, Frame
import random
import os
import json

# Importamos nuestros módulos de MOPSO
import Funciones_MOPSO as fun_mo
import Algoritmo_MOPSO as alg

ancho_canva = 500
alto_canva = 500
num_particulas = 20
w = 0.2
pp = 1.0
pg = 1.0

if os.path.exists('config.json'):
    with open('config.json', 'r') as f:
        config = json.load(f)
    
    ancho_canva = config['ancho_canva']
    alto_canva = config['alto_canva']
    num_particulas = config['num_particulas']
    w = config['w']
    pp = config['pp_inicial']
    pg = config['pg_inicial']
    funcion_objetivo = config['funcion_objetivo']
    resultados = config['resultados']

funciones_multiobjetivo = {
    "Binh and Korn": fun_mo.seleccionar_binh_and_korn,
    "Schaffer N. 1": fun_mo.seleccionar_schaffer_n1,
    "Chankong and Haimes": fun_mo.seleccionar_chankong_and_haimes,
    "Test Function 4": fun_mo.seleccionar_test_function_4,
    "Poloni's Two Objective Function": \
        fun_mo.seleccionar_polonis_two_objective_function,
    "CTP1 Function": fun_mo.seleccionar_ctp1_function,
    "Kursawe": fun_mo.seleccionar_kursawe2,
    "Constr-Ex": fun_mo.seleccionar_constr_ex,
    "Schaffer N. 2": fun_mo.seleccionar_schaffer_n2
}   

funciones_multiobjetivo[funcion_objetivo]()

window = Tk()
window.title("Visualizador MOPSO")

# Seleccionamos el problema a resolver
#fun_mo.seleccionar_schaffer_n2()

# Creamos un Frame principal para organizar los dos gráficos
main_frame = Frame(window)
main_frame.pack(fill="both", expand=True)

decision_space_canvas = Canvas(main_frame, width=ancho_canva, height=alto_canva, 
                               bg='white', highlightthickness=1, 
                               highlightbackground="black")
decision_space_canvas.grid(row=0, column=0, padx=10, pady=10)
padding = 40  # Añadir padding para los ejes

# Dibujar ejes del espacio de decisión
decision_space_canvas.create_line(padding, alto_canva - padding, 
                                  ancho_canva - 10, alto_canva - padding, 
                                  arrow="last")  # Eje X
decision_space_canvas.create_line(padding, alto_canva - padding, padding, 10, 
                                  arrow="last")  # Eje Y
decision_space_canvas.create_text(ancho_canva/2, alto_canva - 15, text="X")
decision_space_canvas.create_text(15, alto_canva/2, text="Y", angle=90)
decision_space_canvas.create_text(10, 10, text="Espacio de Decisión (x, y)", 
                                  anchor="nw")


objective_space_canvas = Canvas(main_frame, width=ancho_canva, height=alto_canva, 
                                bg='ivory', highlightthickness=1, 
                                highlightbackground="black")
objective_space_canvas.grid(row=0, column=1, padx=10, pady=10)

enjambre = alg.Enjambre(num_particulas=num_particulas)
dibujo_particulas = []
dibujo_lideres_decision = [] # Para dibujar los líderes en el canvas de decisión
enjambre_creado = False
iteracion_activa = False # Para evitar múltiples bucles de iteración

def map_value(value, from_min, from_max, to_min, to_max):
    """Función de ayuda para mapear un valor de un rango a otro."""
    if from_max == from_min: 
        return to_min
    return (value - from_min) * (to_max - to_min) / (from_max - from_min) + \
        to_min

def graficar_frente_pareto(canvas, lideres, ancho, alto):
    """Dibuja el Frente de Pareto (los líderes) en el canvas de objetivos."""
    canvas.delete("all")
    canvas.create_text(10, 10, text="Espacio de Objetivos (f1, f2)", anchor="nw")
    padding = 40

    if not lideres:
        canvas.create_text(ancho / 2, alto / 2, text="Esperando líderes...")
        return

    # Filtrar valores inválidos
    lideres_validos = [(x, y, obj) for x, y, obj in lideres \
                       if all(not isinstance(v, complex) and v != float('inf') \
                              for v in obj)]
    if not lideres_validos:
        return

    lideres_f1 = [obj[0] for _, _, obj in lideres_validos]
    lideres_f2 = [obj[1] for _, _, obj in lideres_validos]
    min_f1, max_f1 = min(lideres_f1), max(lideres_f1)
    min_f2, max_f2 = min(lideres_f2), max(lideres_f2)

    margin_f1 = (max_f1 - min_f1) * 0.1 if max_f1 > min_f1 else 1
    margin_f2 = (max_f2 - min_f2) * 0.1 if max_f2 > min_f2 else 1
    f1_range = (min_f1 - margin_f1, max_f1 + margin_f1)
    f2_range = (min_f2 - margin_f2, max_f2 + margin_f2)

    canvas.create_line(padding, alto - padding, ancho - 10, alto - padding, 
                       arrow = "last")
    canvas.create_text(ancho / 2, alto - 15, text = "Objetivo 1 (f1)")
    canvas.create_text(padding, alto - padding + 10, 
                       text = f"{f1_range[0]:.2f}", anchor = "w")
    canvas.create_text(ancho - 10, alto - padding + 10, 
                       text = f"{f1_range[1]:.2f}", anchor = "e")
    
    canvas.create_line(padding, alto - padding, padding, 10, arrow = "last")
    canvas.create_text(15, alto / 2, text = "Objetivo 2 (f2)", angle = 90)
    canvas.create_text(padding - 10, alto - padding, 
                       text = f"{f2_range[0]:.2f}", anchor = "e")
    canvas.create_text(padding - 10, 10, text = f"{f2_range[1]:.2f}", 
                       anchor = "e")

    for _, _, obj in lideres:
        f1, f2 = obj
        plot_x = map_value(f1, f1_range[0], f1_range[1], padding, ancho - 10)
        plot_y = map_value(f2, f2_range[0], f2_range[1], alto - padding, 10)
        canvas.create_oval(plot_x - 3, plot_y - 3, plot_x + 3, plot_y + 3, 
                           fill = 'red', outline = 'red')

# LÓGICA DE CONTROL DEL ALGORITMO
def iniciar_enjambre(event = None):
    global enjambre_creado
    if not enjambre_creado:
        enjambre.crear_enjambre(ancho_canva = ancho_canva - padding * 2, 
                               alto_canva = alto_canva - padding * 2)
        for p in enjambre.particulas:
            x_canvas = map_value(p.x, 0, ancho_canva - padding * 2, padding, 
                               ancho_canva - padding)
            y_canvas = map_value(p.y, 0, alto_canva - padding * 2, 
                               alto_canva - padding, padding)
            rect = decision_space_canvas.create_oval(
                x_canvas - 3, y_canvas - 3, 
                x_canvas + 3, y_canvas + 3, 
                fill = "blue", outline = "blue"
            )
            dibujo_particulas.append(rect)
        enjambre_creado = True
        print("Enjambre creado. Presiona 'W' para iterar.")

def iterar_algoritmo(event = None):
    global iteracion_activa
    if not enjambre_creado:
        print("Primero crea el enjambre con la tecla 'Q'.")
        return
    if iteracion_activa:
        return 
    # Evita que se inicien múltiples bucles si se presiona 'W' varias veces
    
    iteracion_activa = True
    print("Iniciando iteraciones...")
    ejecutar_un_paso()

def ejecutar_un_paso():
    global dibujo_lideres_decision, iteracion_activa
    limite_lideres = fun_mo.limite_lideres
    if not iteracion_activa: return
    # Verificar si alcanzamos el límite de líderes
    if len(enjambre.lideres) >= limite_lideres:
        iteracion_activa = False
        print(f"\nAlgoritmo finalizado: Se alcanzaron {limite_lideres} \
              lideres en el frente de Pareto")
        return

    # Ejecutar una iteración del algoritmo MOPSO
    velocidades_x, velocidades_y = enjambre.iterar_algoritmo(
        ancho_canva - padding * 2, alto_canva - padding * 2, w, pp, pg
    )

    # Actualizar posiciones mapeadas al espacio del canvas
    for i, p in enumerate(enjambre.particulas):
        vel_x_canvas = map_value(velocidades_x[i], -ancho_canva, ancho_canva, 
                                 -padding, padding)
        vel_y_canvas = map_value(velocidades_y[i], -alto_canva, alto_canva, 
                                 -padding, padding)
        decision_space_canvas.move(dibujo_particulas[i], vel_x_canvas, 
                                   vel_y_canvas)

    # Actualizar líderes
    for lider_dibujado in dibujo_lideres_decision:
        decision_space_canvas.delete(lider_dibujado)
    dibujo_lideres_decision.clear()

    for x, y, _ in enjambre.lideres:
        x_canvas = map_value(x, 0, ancho_canva-padding * 2, padding, 
                             ancho_canva - padding)
        y_canvas = map_value(y, 0, alto_canva-padding * 2, alto_canva - padding, 
                             padding)
        rect = decision_space_canvas.create_oval(
            x_canvas - 4, y_canvas - 4,
            x_canvas + 4, y_canvas + 4,
            fill = "green", outline = "green"
        )
        dibujo_lideres_decision.append(rect)
    
    graficar_frente_pareto(objective_space_canvas, enjambre.lideres, ancho_canva, 
                           alto_canva)
    window.update()
    window.after(fun_mo.delay + 50, ejecutar_un_paso) #Sumamos los delays

def finalizar_algoritmo(event = None):
    global iteracion_activa
    iteracion_activa = False
    print("\nAlgoritmo finalizado.")
    print(f"Total de líderes en el Frente de Pareto: {len(enjambre.lideres)}")
    window.destroy()

# VINCULACIÓN DE TECLAS Y BUCLE PRINCIPAL
window.bind("<q>", iniciar_enjambre)
window.bind("<w>", iterar_algoritmo)
window.bind("<e>", finalizar_algoritmo)
# También se puede finalizar cerrando la ventana
window.protocol("WM_DELETE_WINDOW", finalizar_algoritmo)

print("--- Instrucciones ---")
print(" 'Q': Crear el enjambre de partículas.")
print(" 'W': Iniciar las iteraciones del algoritmo.")
print(" 'E' o cerrar la ventana: Finalizar el programa.")

window.mainloop()
window.mainloop()
