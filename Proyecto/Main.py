from tkinter import Tk, Frame, Label, Entry, Checkbutton, Button, Radiobutton, \
    IntVar, StringVar, OptionMenu, scrolledtext
import os
import subprocess
import threading
import json

import Funciones as fun
from MOPSO import Funciones_MOPSO as fun_mo

objetivo = 1

# Funciones
def Cambiar_Todas_Las_Configuraciones():
    if objetivo == 1:
        config = {
            'ancho_canva': int(conf_anchocanvas_entry.get()),
            'alto_canva': int(conf_altocanvas_entry.get()),
            'definicion_canva': int(conf_defcanvas_entry.get()),
            'definicion_colores': int(conf_defcolores_entry.get()),
            'num_particulas': int(conf_numparticulas_entry.get()),
            'w': float(conf_pesoinceria_entry.get()),
            'min_iteraciones': int(conf_miniteraciones_entry.get()),
            'pp_inicial': float(conf_ppinicial_entry.get()),
            'pp_final': float(conf_ppfinal_entry.get()),
            'pg_inicial': float(conf_pginicial_entry.get()),
            'pg_final': float(conf_pgfinal_entry.get()),
            'manual': bool(manual_var.get()),
            'funcion_objetivo': funcion_seleccionada.get(),
            'resultados': resultados_scroll.get("1.0", "end-1c")
        }
        # Guardar configuración en archivo
        with open('config.json', 'w') as f:
            json.dump(config, f)
    else:
        config = {
            'ancho_canva': int(conf_anchocanvas_entry.get()),
            'alto_canva': int(conf_altocanvas_entry.get()),
            'num_particulas': int(conf_numparticulas_entry.get()),
            'w': float(conf_pesoinceria_entry.get()),
            'pp_inicial': float(conf_ppinicial_entry.get()),
            'pg_inicial': float(conf_pginicial_entry.get()),
            'funcion_objetivo': funcion_seleccionada.get(),
            'resultados': resultados_scroll.get("1.0", "end-1c")
        }
        # Guardar configuración en archivo
        with open('config.json', 'w') as f:
            json.dump(config, f)
ultimo_resultado = ""

def Iniciar_Optimizacion():
    Cambiar_Todas_Las_Configuraciones()
    def lanzar_graficadora_un_objetivo():
        proceso = subprocess.Popen(["python", "Graficadora.py"])
        proceso.wait()
    def lanzar_graficadora_multiobjetivo():
        proceso = subprocess.Popen(["python", "MOPSO/Graficadora_MOPSO.py"])
        proceso.wait()
    if objetivo == 1:
        threading.Thread(target = lanzar_graficadora_un_objetivo, 
                         daemon = True).start()
    else:
        threading.Thread(target = lanzar_graficadora_multiobjetivo, 
                         daemon = True).start()

def crear_gui():
    global conf_anchocanvas_entry, conf_altocanvas_entry, \
        conf_defcanvas_entry
    global conf_defcolores_entry, conf_numparticulas_entry, \
        conf_pesoinceria_entry
    global conf_ppinicial_entry, conf_ppfinal_entry, \
        conf_pginicial_entry, conf_pgfinal_entry
    global conf_miniteraciones_entry, manual_var, funcion_seleccionada, \
        resultados_scroll
    global seleccion_funcion_menu, funcion_seleccionada

    # Ventana principal
    ventana = Tk()
    ventana.title("MPSO - Ventana Principal")
    ventana.resizable(False, False)
    ventana.iconbitmap("icono.ico")
    ventana.geometry("1000x500")

    # Frame principal
    frame = Frame(ventana)
    frame.configure(width = "1000", height = "500")
    frame.configure(bg = "#F8F9FA")
    frame.pack(fill = 'both', expand = True, padx = 10, pady = 10)
    frame.pack_propagate(False) 

    ## Title
    titulo_label = Label(frame, bg = "#F8F9FA", fg = "#2C3E50",
                          font = ("Arial", 22, "bold"), text = "Algoritmo PSO")
    titulo_label.pack(pady = (10, 10))

    ## 3 Frames
    frame1 = Frame(ventana, bg = "#FFFFFF", width = 320, height = 430)
    frame2 = Frame(ventana, bg = "#F1F2F6", width = 320, height = 430)
    frame3 = Frame(ventana, bg = "#E9ECEF", width = 320, height = 430)

    frame1.place(x = 10, y = 60)
    frame2.place(x = 340, y = 60)
    frame3.place(x = 670, y = 60)

    frame1.pack_propagate(False)
    frame2.pack_propagate(False)
    frame3.pack_propagate(False)

    frame1.grid_propagate(False)
    frame2.grid_propagate(False)
    frame3.grid_propagate(False)

    objetivo_var = IntVar(value = 1)  # Valor por defecto: 1 (Un objetivo)

    # Configuración 1 frame
    ## Titulo de configuración
    subtitulo1_label1 = Label(frame1, bg = "#FFFFFF", fg = "#495057", 
                              font=("Arial", 12, "bold"), 
                              text="Tipo de optimización")
    subtitulo1_label1.grid(row = 0, column = 0, padx = 5, sticky = "w", 
                           columnspan = 2, pady = 5)

    ## Un objetivo o Multiple objetivos

    un_objetivo_radio = Radiobutton(frame1, text = "Un objetivo", value = 1,
                                    variable = objetivo_var, bg = "#FFFFFF", 
                                    fg = "#495057", font = ("Arial", 10), 
                                    selectcolor = "#DEE2E6")
    un_objetivo_radio.grid(row = 1, column = 0, padx = 5, pady = 5, 
                           sticky = "w", columnspan = 2)

    multiple_objetivos_radio = Radiobutton(frame1, text = "Múltiples objetivos", 
                                        value = 2, variable = objetivo_var, 
                                        bg = "#FFFFFF", fg = "#495057", 
                                        font = ("Arial", 10), 
                                        selectcolor = "#DEE2E6")
    multiple_objetivos_radio.grid(row = 1, column = 1, padx = 5, pady = 5, 
                                  sticky = "w", columnspan = 2)

    ## Segundo Titulo de funcion objetivo
    subtitulo2_label1 = Label(frame1, bg = "#FFFFFF", fg = "#495057", 
                              font = ("Arial", 12, "bold"), 
                              text = "Función Objetivo", )
    subtitulo2_label1.grid(row = 2, column = 0, padx = 5, sticky = "w", 
                           columnspan = 2, pady = 5)

    ## Selección de función objetivo
    lista_funciones_unobjetivo = ["Mi Función", "Rastrigin", "Ackley", "Sphere",
                                  "Rosenbrock", "Beale", "Goldstein-Price", 
                                  "Booth", "Bukin N. 6", "Matyas", "Levi N. 13", 
                                  "Griewank", "Himmelblau", "Three-Hump Camel", 
                                  "Easom", "Cross-in-Tray", "Eggholder", 
                                  "Holder Table", "McCormick", "Schaffer N. 2", 
                                  "Schaffer N. 4", "Styblinski-Tang"]
    lista_funciones_multiobjetivo = ["Binh and Korn", "Schaffer N. 1", 
                                     "Chankong and Haimes", "Test Function 4", 
                                     "Poloni's Two Objective Function", 
                                     "CTP1 Function", "Kursawe", "Constr-Ex", 
                                     "Schaffer N. 2"]

    funcion_seleccionada = StringVar(value = "Ackley") 
    seleccion_funcion_menu = OptionMenu(frame1, funcion_seleccionada, *lista_funciones_unobjetivo,)
    seleccion_funcion_menu.grid(row = 3, column = 0, padx = 5, pady = 5, 
                                sticky = "w", columnspan = 2)

    funciones_un_objetivo = {
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

    ## Tercer Titulo de configuración canvas
    subtitulo_label3 = Label(frame1, bg = "#FFFFFF", fg = "#495057", 
                             font = ("Arial", 12, "bold"), 
                             text="Configuración del Canvas")
    subtitulo_label3.grid(row = 4, column = 0, padx = 5, sticky = "w", 
                          columnspan = 2, pady = 5)

    ## Ancho del Canvas
    conf_anchocanvas_label = Label(frame1, text = "Ancho del Canvas:", 
                                   bg = "#FFFFFF", fg = "#6C757D", 
                                   font = ("Arial", 10))
    conf_anchocanvas_label.grid(row = 5, column = 0, padx = 5, pady = 5, 
                                sticky = "w")

    conf_anchocanvas_entry = Entry(frame1, font = ("Arial", 10), width = 5, 
                                   bg = "#F8F9FA", fg = "#495057", 
                                   relief = "solid", bd = 1)
    conf_anchocanvas_entry.grid(row = 5, column = 1, padx = 5, pady = 5, 
                                sticky = "w")
    conf_anchocanvas_entry.insert(0, "500")

    conf_anchocanvas_sub_label = Label(frame1, text = "(pixeles)", 
                                       bg = "#FFFFFF", fg = "#ADB5BD", 
                                       font = ("Arial", 8))
    conf_anchocanvas_sub_label.grid(row = 5, column = 2, padx = 5, pady = 5, 
                                    sticky = "w")

    ## Alto del Canvas
    conf_altocanvas_label = Label(frame1, text = "Alto del Canvas:", 
                                  bg = "#FFFFFF", fg = "#6C757D", 
                                  font = ("Arial", 10))
    conf_altocanvas_label.grid(row = 6, column = 0, padx = 5, pady = 5, 
                               sticky = "w")

    conf_altocanvas_entry = Entry(frame1, font = ("Arial", 10), width = 5, 
                                  bg = "#F8F9FA", fg = "#495057", 
                                  relief = "solid", bd = 1)
    conf_altocanvas_entry.grid(row = 6, column = 1, padx = 5, pady = 5, 
                               sticky = "w")
    conf_altocanvas_entry.insert(0, "500")

    conf_altocanvas_sub_label = Label(frame1, text = "(pixeles)", 
                                      bg = "#FFFFFF", fg = "#ADB5BD", 
                                      font = ("Arial", 8))
    conf_altocanvas_sub_label.grid(row = 6, column = 2, padx = 5, pady = 5, 
                                   sticky = "w")

    ## Definicion Canvas
    conf_defcanvas_label = Label(frame1, text = "Definición del Canvas:", 
                                 bg = "#FFFFFF", fg = "#6C757D", 
                                 font = ("Arial", 10))
    conf_defcanvas_label.grid(row = 7, column = 0, padx = 5, pady = 5, 
                              sticky = "w")

    conf_defcanvas_entry = Entry(frame1, font = ("Arial", 10), width = 5, 
                                 bg = "#F8F9FA", fg = "#495057", 
                                 relief = "solid", bd = 1)
    conf_defcanvas_entry.grid(row = 7, column = 1, padx = 5, pady = 5, 
                              sticky = "w")
    conf_defcanvas_entry.insert(0, "5")

    conf_defcanvas_sub_label = Label(frame1, text = "(Resolución)", 
                                     bg = "#FFFFFF", fg = "#ADB5BD", 
                                     font = ("Arial", 8))
    conf_defcanvas_sub_label.grid(row = 7, column = 2, padx = 5, pady = 5, 
                                  sticky = "w")

    ## Definicion Colores
    conf_defcolores_label = Label(frame1, text = "Definición de Colores:", 
                                  bg = "#FFFFFF", fg = "#6C757D", 
                                  font = ("Arial", 10))
    conf_defcolores_label.grid(row = 8, column = 0, padx = 5, pady = 5, 
                               sticky = "w")

    conf_defcolores_entry = Entry(frame1, font = ("Arial", 10), width = 5, 
                                  bg = "#F8F9FA", fg = "#495057", 
                                  relief = "solid", bd = 1)
    conf_defcolores_entry.grid(row = 8, column = 1, padx = 5, pady = 5, 
                               sticky = "w")
    conf_defcolores_entry.insert(0, "100")

    conf_defcolores_sub_label = Label(frame1, text = "(Niveles)", 
                                      bg = "#FFFFFF", fg = "#ADB5BD", 
                                      font = ("Arial", 8))
    conf_defcolores_sub_label.grid(row = 8, column = 2, padx = 5, pady = 5, 
                                   sticky = "w")

    # Configuración 2 frame
    ## Titulo de configuración
    subtitulo_label2 = Label(frame2, bg = "#F1F2F6", fg = "#343A40", 
                             font = ("Arial", 12, "bold"), 
                             text = "Configuración del Algoritmo", )
    subtitulo_label2.grid(row = 0, column = 0, padx = 5, sticky = "w", 
                          columnspan = 2, pady = 5)

    ## Número de partículas 
    conf_numparticulas_label = Label(frame2, text = "Número de Partículas:", 
                                     bg = "#F1F2F6", fg = "#495057", 
                                     font = ("Arial", 10))
    conf_numparticulas_label.grid(row = 1, column = 0, padx = 5, pady = 5, 
                                  sticky = "w")

    conf_numparticulas_entry = Entry(frame2, font = ("Arial", 10), width = 5, 
                                     bg = "#FFFFFF", fg = "#495057", 
                                     relief = "solid", bd = 1)
    conf_numparticulas_entry.grid(row = 1, column = 1, padx = 5, pady = 5, 
                                  sticky = "w")
    conf_numparticulas_entry.insert(0, "15")

    conf_numparticulas_sub_label = Label(frame2, text = "(particulas)", 
                                         bg = "#F1F2F6", fg = "#6C757D", 
                                         font = ("Arial", 8))
    conf_numparticulas_sub_label.grid(row = 1, column = 2, padx = 5, pady = 5, 
                                      sticky = "w")

    ## Peso de inercia 
    conf_pesoinceria_label = Label(frame2, text = "Peso de Inercia (w):", 
                                   bg = "#F1F2F6", fg = "#495057", 
                                   font = ("Arial", 10))
    conf_pesoinceria_label.grid(row = 2, column = 0, padx = 5, pady = 5, 
                                sticky = "w")

    conf_pesoinceria_entry = Entry(frame2, font = ("Arial", 10), width = 5, 
                                   bg = "#FFFFFF", fg = "#495057", 
                                   relief = "solid", bd = 1)
    conf_pesoinceria_entry.grid(row = 2, column = 1, padx = 5, pady = 5, 
                                sticky = "w")
    conf_pesoinceria_entry.insert(0, "0.6")

    conf_pesoinceria_sub_label = Label(frame2, text = "0.0-1.0", 
                                       bg = "#F1F2F6", fg = "#6C757D", 
                                       font = ("Arial", 8))
    conf_pesoinceria_sub_label.grid(row = 2, column = 2, padx = 5, pady = 5, 
                                    sticky = "w")

    ## Minimo iteraciones
    conf_miniteraciones_label = Label(frame2, text = "Mínimo Iteraciones:", 
                                      bg = "#F1F2F6", fg = "#495057", 
                                      font = ("Arial", 10))
    conf_miniteraciones_label.grid(row = 3, column = 0, padx = 5, pady = 5, 
                                   sticky = "w")

    conf_miniteraciones_entry = Entry(frame2, font = ("Arial", 10), width = 5, 
                                      bg = "#FFFFFF", fg = "#495057",
                                     relief = "solid", bd = 1)
    conf_miniteraciones_entry.grid(row = 3, column = 1, padx = 5, pady = 5, 
                                   sticky = "w")
    conf_miniteraciones_entry.insert(0, "25")

    conf_miniteraciones_sub_label = Label(frame2, text = "(iteraciones)", 
                                          bg = "#F1F2F6", fg = "#6C757D", 
                                          font = ("Arial", 8))
    conf_miniteraciones_sub_label.grid(row = 3, column = 2, padx = 5, pady = 5, 
                                       sticky = "w")

    ## Pp inicial
    conf_ppinicial_label = Label(frame2, text = "Pp Inicial:", 
                                 bg = "#F1F2F6", fg = "#495057", 
                                 font = ("Arial", 10))
    conf_ppinicial_label.grid(row = 4, column = 0, padx = 5, pady = 5, 
                              sticky = "w")

    conf_ppinicial_entry = Entry(frame2, font = ("Arial", 10), width = 5, 
                                 bg = "#FFFFFF", fg = "#495057",
                                relief = "solid", bd = 1)
    conf_ppinicial_entry.grid(row = 4, column = 1, padx = 5, pady = 5, 
                              sticky = "w")
    conf_ppinicial_entry.insert(0, "2.5")

    conf_ppinicial_sub_label = Label(frame2, text = "(coeficiente)", 
                                     bg = "#F1F2F6", fg = "#6C757D", 
                                     font = ("Arial", 8))
    conf_ppinicial_sub_label.grid(row = 4, column = 2, padx = 5, pady = 5, 
                                  sticky = "w")

    ## Pp final
    conf_ppfinal_label = Label(frame2, text = "Pp Final:", bg = "#F1F2F6", 
                               fg = "#495057", font = ("Arial", 10))
    conf_ppfinal_label.grid(row = 5, column = 0, padx = 5, pady = 5, 
                            sticky = "w")

    conf_ppfinal_entry = Entry(frame2, font = ("Arial", 10), width = 5, 
                               bg = "#FFFFFF", fg = "#495057", 
                               relief = "solid", bd = 1)
    conf_ppfinal_entry.grid(row = 5, column = 1, padx = 5, pady = 5, 
                            sticky = "w")
    conf_ppfinal_entry.insert(0, "0.5")

    conf_ppfinal_sub_label = Label(frame2, text = "(coeficiente)", 
                                   bg = "#F1F2F6", fg = "#6C757D", 
                                   font = ("Arial", 8))
    conf_ppfinal_sub_label.grid(row = 5, column = 2, padx = 5, pady = 5, 
                                sticky = "w")

    ## Pg inicial
    conf_pginicial_label = Label(frame2, text = "Pg Inicial:", bg = "#F1F2F6", 
                                 fg = "#495057", font = ("Arial", 10))
    conf_pginicial_label.grid(row = 6, column = 0, padx = 5, pady = 5, 
                              sticky = "w")

    conf_pginicial_entry = Entry(frame2, font = ("Arial", 10), width = 5, 
                                 bg = "#FFFFFF", fg = "#495057",
                                relief = "solid", bd = 1)
    conf_pginicial_entry.grid(row = 6, column = 1, padx = 5, pady = 5, 
                              sticky = "w")
    conf_pginicial_entry.insert(0, "0.5")

    conf_pginicial_sub_label = Label(frame2, text = "(coeficiente)", 
                                     bg = "#F1F2F6", fg = "#6C757D", 
                                     font = ("Arial", 8))
    conf_pginicial_sub_label.grid(row = 6, column = 2, padx = 5, pady = 5, 
                                  sticky = "w")

    ## Pg final
    conf_pgfinal_label = Label(frame2, text = "Pg Final:", bg = "#F1F2F6", 
                               fg = "#495057", font = ("Arial", 10))
    conf_pgfinal_label.grid(row = 7, column = 0, padx = 5, pady = 5, 
                            sticky = "w")

    conf_pgfinal_entry = Entry(frame2, font = ("Arial", 10), width = 5, 
                               bg = "#FFFFFF", fg = "#495057", 
                               relief = "solid", bd = 1)
    conf_pgfinal_entry.grid(row = 7, column = 1, padx = 5, pady = 5, 
                            sticky = "w")
    conf_pgfinal_entry.insert(0, "2.5")

    conf_pgfinal_sub_label = Label(frame2, text = "(coeficiente)", 
                                   bg = "#F1F2F6", fg = "#6C757D", 
                                   font = ("Arial", 8))
    conf_pgfinal_sub_label.grid(row = 7, column = 2, padx = 5, pady = 5, 
                                sticky = "w")

    ## Modo manual
    manual_var = IntVar(value = 0)  # Valor por defecto: 0 (Automático)
    conf_manual_checkbox = Checkbutton(frame2, text = "Modo Manual", 
                                       bg = "#F1F2F6", fg = "#495057", 
                                      font = ("Arial", 10), 
                                      variable = manual_var, 
                                      selectcolor = "#CED4DA")
    conf_manual_checkbox.grid(row = 8, column = 0, padx = 5, pady = 5, 
                              sticky = "w")

    ## Botón de inicio
    conf_inicio_button = Button(frame2, text = "Iniciar Optimización", 
                                font = ("Arial", 12, "bold"), width = 20, 
                                height = 1, 
                                command = Iniciar_Optimizacion, 
                                bg = "#495057", fg = "#FFFFFF",
                                activebackground = "#343A40", 
                                activeforeground = "#FFFFFF",
                                relief = "solid", bd = 1)
    conf_inicio_button.place(x = 70, y = 350)

    # Configuración 3 frame

    ## Titulo de Resultados
    subtitulo_label3 = Label(frame3, bg = "#E9ECEF", fg = "#343A40", 
                             font = ("Arial", 12, "bold"), text = "Resultados")
    subtitulo_label3.grid(row = 0, column = 0, padx = 5, sticky = "w", 
                          columnspan = 2, pady = 5)

    ## Text de resultados
    resultados_scroll = scrolledtext.ScrolledText(frame3, bg = "#FFFFFF", 
                                                font = ("Arial", 12), padx = 5, 
                                                pady = 5, width = 31, 
                                                height = 18, wrap = "word",
                                                fg = "#495057", 
                                                selectbackground = "#DEE2E6")
    resultados_scroll.insert("insert", 
                             "Resultados del algoritmo PSO aparecerán aquí...\n")
    resultados_scroll.configure(state = 'disabled')

    resultados_scroll.grid(row = 1, column = 0, padx = 5, pady = 5, 
                           sticky = "nsew")

    def actualizar_funcion_objetivo(*args):
        global seleccion_funcion_menu, funcion_seleccionada
        global objetivo

        if objetivo_var.get() == 1:
            objetivo = 1
            # Elementos que se quitan
            conf_defcanvas_label.grid()
            conf_defcanvas_entry.grid()
            conf_defcanvas_sub_label.grid()

            conf_defcolores_label.grid()
            conf_defcolores_entry.grid()
            conf_defcolores_sub_label.grid()

            conf_miniteraciones_label.grid()
            conf_miniteraciones_entry.grid()
            conf_miniteraciones_sub_label.grid()

            conf_ppfinal_label.grid()
            conf_ppfinal_entry.grid()
            conf_ppfinal_sub_label.grid()

            conf_pgfinal_label.grid()
            conf_pgfinal_entry.grid()
            conf_pgfinal_sub_label.grid()

            conf_manual_checkbox.grid()

            seleccion_funcion_menu.grid_remove()
            funcion_seleccionada = StringVar(value="Ackley") 
            seleccion_funcion_menu = OptionMenu(frame1, funcion_seleccionada, 
                                                *lista_funciones_unobjetivo)
            seleccion_funcion_menu.grid(row=3, column=0, padx=5, pady=5, 
                                        sticky="w", columnspan=2)

            # Elementos que se configuran
            conf_numparticulas_entry.delete(0, 'end')
            conf_pesoinceria_entry.delete(0, 'end')
            conf_ppinicial_entry.delete(0, 'end')
            conf_pginicial_entry.delete(0, 'end')

            conf_numparticulas_entry.insert(0, "15")
            conf_pesoinceria_entry.insert(0, "0.6")
            conf_ppinicial_entry.insert(0, "2.5")
            conf_pginicial_entry.insert(0, "0.5")

            conf_ppinicial_label.config(text="Pp Inicial:")

            conf_pginicial_label.config(text="Pg Inicial:")


        else:
            objetivo = 2
            # Elementos que se quitan
            conf_defcanvas_label.grid_remove()
            conf_defcanvas_entry.grid_remove()
            conf_defcanvas_sub_label.grid_remove()

            conf_defcolores_label.grid_remove()
            conf_defcolores_entry.grid_remove()
            conf_defcolores_sub_label.grid_remove()

            conf_miniteraciones_label.grid_remove()
            conf_miniteraciones_entry.grid_remove()
            conf_miniteraciones_sub_label.grid_remove()

            conf_ppfinal_label.grid_remove()
            conf_ppfinal_entry.grid_remove()
            conf_ppfinal_sub_label.grid_remove()

            conf_pgfinal_label.grid_remove()
            conf_pgfinal_entry.grid_remove()
            conf_pgfinal_sub_label.grid_remove()

            conf_manual_checkbox.grid_remove()

            # Elementos que se configuran
            conf_numparticulas_entry.delete(0, 'end')
            conf_pesoinceria_entry.delete(0, 'end')
            conf_ppinicial_entry.delete(0, 'end')
            conf_pginicial_entry.delete(0, 'end')

            conf_numparticulas_entry.insert(0, "20")
            conf_pesoinceria_entry.insert(0, "0.2")
            conf_ppinicial_entry.insert(0, "1.0")
            conf_pginicial_entry.insert(0, "1.0")

            conf_ppinicial_label.config(text="Pp: ")

            conf_pginicial_label.config(text="Pg: ")

            seleccion_funcion_menu.grid_remove()
            funcion_seleccionada = StringVar(value="Binh and Korn") 
            seleccion_funcion_menu = OptionMenu(frame1, funcion_seleccionada, 
                                                *lista_funciones_multiobjetivo)
            seleccion_funcion_menu.grid(row=3, column=0, padx=5, pady=5, 
                                        sticky="w", columnspan=2)

    objetivo_var.trace_add("write", actualizar_funcion_objetivo)
    def Borrar_Resultados():
        resultados_scroll.configure(state='normal')
        resultados_scroll.delete(1.0, 'end')
        resultados_scroll.configure(state='disabled')
        # Leer config existente
        if os.path.exists('config.json'):
            with open('config.json', 'r') as f:
                config = json.load(f)
        else:
            config = {}
        # Actualizar solo el campo 'resultados'
        config['resultados'] = \
            "Resultados del algoritmo PSO aparecerán aquí...\n\n"
        # Guardar configuración completa
        with open('config.json', 'w') as f:
            json.dump(config, f)
    ## Botón de borrar texto
    boton_borrar = Button(frame3, text="Borrar Resultados", 
                          font=("Arial", 10, "bold"), 
                          width=16, height=1, command=Borrar_Resultados, 
                          bg="#6C757D", fg="#FFFFFF", 
                          activebackground="#495057", 
                          activeforeground="#FFFFFF", relief="solid", bd=1)
    boton_borrar.grid(row=2, column=0, padx=5, pady=5, columnspan=2)

    def verificar_cambios():
        global ultimo_resultado
        
        try:
            if os.path.exists('config.json'):
                with open('config.json', 'r') as f:
                    config = json.load(f)
                
                if 'resultados' in config:
                    nuevo_resultado = config['resultados']
                    
                    # Solo actualizar si hay un cambio real
                    if nuevo_resultado != \
                        ultimo_resultado and nuevo_resultado != "":
                        resultados_scroll.configure(state='normal')
                        resultados_scroll.delete(1.0, 'end')
                        resultados_scroll.insert('end', nuevo_resultado)
                        resultados_scroll.configure(state='disabled')
                        
                        ultimo_resultado = nuevo_resultado
        except:
            pass
        
        # Verificar cada 2 segundos
        ventana.after(2000, verificar_cambios)
    def cerrar_ventana():
        # Leer config existente
        if os.path.exists('config.json'):
            with open('config.json', 'r') as f:
                config = json.load(f)
        else:
            config = {}
        # Actualizar solo el campo 'resultados'
        config['resultados'] = \
            "Resultados del algoritmo PSO aparecerán aquí...\n\n"
        with open('config.json', 'w') as f:
            json.dump(config, f)
        ventana.destroy()
        os._exit(0)

    ventana.protocol("WM_DELETE_WINDOW", cerrar_ventana)
    verificar_cambios()
    ventana.mainloop()

if __name__ == "__main__":
    crear_gui()
