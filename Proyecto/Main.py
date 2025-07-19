from tkinter import Tk, Frame, Label, Entry, Checkbutton, Button, Radiobutton, IntVar, StringVar, OptionMenu, scrolledtext
import os
import json

import Funciones as fun

# Funciones de los Botones
def Cambiar_Todas_Las_Configuraciones():
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
ultimo_resultado = ""  

def Iniciar_Optimizacion():
    Cambiar_Todas_Las_Configuraciones()
    os.system("python Graficadora.py")

def crear_gui():
    global conf_anchocanvas_entry, conf_altocanvas_entry, conf_defcanvas_entry
    global conf_defcolores_entry, conf_numparticulas_entry, conf_pesoinceria_entry
    global conf_ppinicial_entry, conf_ppfinal_entry, conf_pginicial_entry, conf_pgfinal_entry
    global conf_miniteraciones_entry, manual_var, funcion_seleccionada, resultados_scroll

    # Ventana principal
    ventana = Tk()
    ventana.title("MPSO - Ventana Principal")
    ventana.resizable(False, False)
    ventana.iconbitmap("icono.ico")
    ventana.geometry("1000x500")

    # Frame principal
    frame = Frame(ventana)
    frame.configure(width="1000", height="500")
    frame.configure(bg="lightblue")
    frame.pack(fill='both', expand=True, padx=10, pady=10)
    frame.pack_propagate(False) 

    ## Title
    titulo_label = Label(frame, bg="lightblue", font=("Arial", 22), text="Algoritmo PSO")
    titulo_label.pack(pady=(10, 10))

    ## 3 Frames
    frame1 = Frame(ventana, bg="lightgray", width=320, height=430)
    frame2 = Frame(ventana, bg="lightgreen", width=320, height=430)
    frame3 = Frame(ventana, bg="lightcoral", width=320, height=430)

    frame1.place(x=10, y=60)
    frame2.place(x=340, y=60)
    frame3.place(x=670, y=60)

    frame1.pack_propagate(False)
    frame2.pack_propagate(False)
    frame3.pack_propagate(False)

    frame1.grid_propagate(False)
    frame2.grid_propagate(False)
    frame3.grid_propagate(False)


    # Configuración 1 frame
    ## Titulo de configuración
    subtitulo1_label1 = Label(frame1, bg="lightgray", font=("Arial", 12)
                            , text="Tipo de optimización", )
    subtitulo1_label1.grid(row=0, column=0, padx=5, sticky="w", columnspan=2, pady=5)

    ## Un objetivo o Multiple objetivos
    objetivo_var = IntVar(value=1)  # Valor por defecto: 1 (Un objetivo)

    un_objetivo_radio = Radiobutton(frame1, text="Un objetivo", value=1,
                                    variable=objetivo_var, bg="lightgray", 
                                    font=("Arial", 10))
    un_objetivo_radio.grid(row=1, column=0, padx=5, pady=5, sticky="w", columnspan=2)

    multiple_objetivos_radio = Radiobutton(frame1, text="Múltiples objetivos", 
                                        value=2, variable=objetivo_var, 
                                        bg="lightgray", font=("Arial", 10))
    multiple_objetivos_radio.grid(row=1, column=1, padx=5, pady=5, sticky="w", columnspan=2)

    ## Segundo Titulo de funcion objetivo
    subtitulo2_label1 = Label(frame1, bg="lightgray", font=("Arial", 12)
                            , text="Función Objetivo", )
    subtitulo2_label1.grid(row=2, column=0, padx=5, sticky="w", columnspan=2, pady=5)

    ## Selección de función objetivo
    lista_funciones = ["Rastrigin","Ackley", "Sphere","Rosenbrock","Beale",
                    "Goldstein-Price","Booth","Bukin N 6", "Matyas",
                    "Levi N 13", "Griewank", "Himmelblau", "Three-Hump Camel",
                    "Easom","Cross-in-Tray","Eggholder","Holder Table", "McCormick",
                    "Schaffer N. 2", "Schaffer N. 4", "Styblinski-Tang"]
    
    funcion_seleccionada = StringVar(value="Ackley") 
    seleccion_funcion_menu = OptionMenu(frame1, funcion_seleccionada, *lista_funciones,)
    seleccion_funcion_menu.grid(row=3, column=0, padx=5, pady=5, sticky="w", columnspan=2)

    funciones_un_objetivo = {
    "Rastrigin": fun.seleccionar_rastrigin_function,
    "Ackley": fun.seleccionar_ackley_function,
    "Beale": fun.seleccionar_beale_function,
    "Booth": fun.seleccionar_booth_function,
    "Bukin N. 6": fun.seleccionar_bukin_n6_function,
    "Cross-in-tray": fun.seleccionar_cross_in_tray_function,
    "Easom": fun.seleccionar_easom_function, 
    "Egg-holder": fun.seleccionar_egg_holder_function, 
    "Goldstein price": fun.seleccionar_goldstein_price_function, 
    "Himmelblau": fun.seleccionar_himmelblau_function, 
    "Holder table": fun.seleccionar_holder_table_function, 
    "Levi N. 13": fun.seleccionar_levi_n13_function, 
    "Matyas": fun.seleccionar_matyas_function, 
    "McCormick": fun.seleccionar_mc_cormick_function, 
    "Mi función": fun.seleccionar_mi_function, 
    "Rosenbrock": fun.seleccionar_rosenbrock_function, 
    "Schaffaer N. 2": fun.seleccionar_schaffer_n2_function, 
    "Schaffer N. 4": fun.seleccionar_schaffer_n4_function, 
    "Sphere": fun.seleccionar_sphere_function, 
    "Styblinski-Tang": fun.seleccionar_styblinski_tang_function, 
    "Three-Hump Camel": fun.seleccionar_three_hump_camel_function}

    ## Tercer Titulo de configuración canvas
    subtitulo_label3 = Label(frame1, bg="lightgray", font=("Arial", 12)
                            , text="Configuración del Canvas", )
    subtitulo_label3.grid(row=4, column=0, padx=5, sticky="w", columnspan=2, pady=5)

    ## Ancho del Canvas
    conf_anchocanvas_label = Label(frame1, text="Ancho del Canvas:", bg="lightgray", font=("Arial", 10))
    conf_anchocanvas_label.grid(row=5, column=0, padx=5, pady=5, sticky="w")

    conf_anchocanvas_entry = Entry(frame1, font=("Arial", 10), width=5)
    conf_anchocanvas_entry.grid(row=5, column=1, padx=5, pady=5, sticky="w")
    conf_anchocanvas_entry.insert(0, "500")

    conf_anchocanvas_sub_label = Label(frame1, text="(pixeles)", bg="lightgray", font=("Arial", 8))
    conf_anchocanvas_sub_label.grid(row=5, column=2, padx=5, pady=5, sticky="w")

    ## Alto del Canvas
    conf_altocanvas_label = Label(frame1, text="Alto del Canvas:", bg="lightgray", font=("Arial", 10))
    conf_altocanvas_label.grid(row=6, column=0, padx=5, pady=5, sticky="w")

    conf_altocanvas_entry = Entry(frame1, font=("Arial", 10), width=5)
    conf_altocanvas_entry.grid(row=6, column=1, padx=5, pady=5, sticky="w")
    conf_altocanvas_entry.insert(0, "500")

    conf_altocanvas_sub_label = Label(frame1, text="(pixeles)", bg="lightgray", font=("Arial", 8))
    conf_altocanvas_sub_label.grid(row=6, column=2, padx=5, pady=5, sticky="w")

    ## Definicion Canvas
    conf_defcanvas_label = Label(frame1, text="Definición del Canvas:", bg="lightgray", font=("Arial", 10))
    conf_defcanvas_label.grid(row=7, column=0, padx=5, pady=5, sticky="w")

    conf_defcanvas_entry = Entry(frame1, font=("Arial", 10), width=5)
    conf_defcanvas_entry.grid(row=7, column=1, padx=5, pady=5, sticky="w")
    conf_defcanvas_entry.insert(0, "5")

    conf_defcanvas_sub_label = Label(frame1, text="(Resolución)", bg="lightgray", font=("Arial", 8))
    conf_defcanvas_sub_label.grid(row=7, column=2, padx=5, pady=5, sticky="w")

    ## Definicion Colores
    conf_defcolores_label = Label(frame1, text="Definición de Colores:", bg="lightgray", font=("Arial", 10))
    conf_defcolores_label.grid(row=8, column=0, padx=5, pady=5, sticky="w")

    conf_defcolores_entry = Entry(frame1, font=("Arial", 10), width=5)
    conf_defcolores_entry.grid(row=8, column=1, padx=5, pady=5, sticky="w")
    conf_defcolores_entry.insert(0, "100")

    conf_defcolores_sub_label = Label(frame1, text="(Niveles)", bg="lightgray", font=("Arial", 8))
    conf_defcolores_sub_label.grid(row=8, column=2, padx=5, pady=5, sticky="w")

    # Configuración 2 frame
    ## Titulo de configuración
    subtitulo_label2 = Label(frame2, bg="lightgreen", font=("Arial", 12)
                            , text="Configuración del Algoritmo", )
    subtitulo_label2.grid(row=0, column=0, padx=5, sticky="w", columnspan=2, pady=5)

    ## Número de partículas 
    conf_numparticulas_label = Label(frame2, text="Número de Partículas:", bg="lightgreen", font=("Arial", 10))
    conf_numparticulas_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")

    conf_numparticulas_entry = Entry(frame2, font=("Arial", 10), width=5)
    conf_numparticulas_entry.grid(row=1, column=1, padx=5, pady=5, sticky="w")
    conf_numparticulas_entry.insert(0, "15")

    conf_numparticulas_sub_label = Label(frame2, text="(particulas)", bg="lightgreen", font=("Arial", 8))
    conf_numparticulas_sub_label.grid(row=1, column=2, padx=5, pady=5, sticky="w")

    ## Peso de inercia 
    conf_pesoinceria_label = Label(frame2, text="Peso de Inercia (w):", bg="lightgreen", font=("Arial", 10))
    conf_pesoinceria_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")

    conf_pesoinceria_entry = Entry(frame2, font=("Arial", 10), width=5)
    conf_pesoinceria_entry.grid(row=2, column=1, padx=5, pady=5, sticky="w")
    conf_pesoinceria_entry.insert(0, "0.6")

    conf_pesoinceria_sub_label = Label(frame2, text="0.0-1.0", bg="lightgreen", font=("Arial", 8))
    conf_pesoinceria_sub_label.grid(row=2, column=2, padx=5, pady=5, sticky="w")

    ## Minimo iteraciones
    conf_miniteraciones_label = Label(frame2, text="Mínimo Iteraciones:", bg="lightgreen", font=("Arial", 10))
    conf_miniteraciones_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")

    conf_miniteraciones_entry = Entry(frame2, font=("Arial", 10), width=5)
    conf_miniteraciones_entry.grid(row=3, column=1, padx=5, pady=5, sticky="w")
    conf_miniteraciones_entry.insert(0, "25")

    conf_miniteraciones_sub_label = Label(frame2, text="(iteraciones)", bg="lightgreen", font=("Arial", 8))
    conf_miniteraciones_sub_label.grid(row=3, column=2, padx=5, pady=5, sticky="w")

    ## Pp inicial
    conf_ppinicial_label = Label(frame2, text="Pp Inicial:", bg="lightgreen", font=("Arial", 10))
    conf_ppinicial_label.grid(row=4, column=0, padx=5, pady=5, sticky="w")

    conf_ppinicial_entry = Entry(frame2, font=("Arial", 10), width=5)
    conf_ppinicial_entry.grid(row=4, column=1, padx=5, pady=5, sticky="w")
    conf_ppinicial_entry.insert(0, "2.5")

    conf_ppinicial_sub_label = Label(frame2, text="(coeficiente)", bg="lightgreen", font=("Arial", 8))
    conf_ppinicial_sub_label.grid(row=4, column=2, padx=5, pady=5, sticky="w")

    ## Pp final
    conf_ppfinal_label = Label(frame2, text="Pp Final:", bg="lightgreen", font=("Arial", 10))
    conf_ppfinal_label.grid(row=5, column=0, padx=5, pady=5, sticky="w")

    conf_ppfinal_entry = Entry(frame2, font=("Arial", 10), width=5)
    conf_ppfinal_entry.grid(row=5, column=1, padx=5, pady=5, sticky="w")
    conf_ppfinal_entry.insert(0, "0.5")

    conf_ppfinal_sub_label = Label(frame2, text="(coeficiente)", bg="lightgreen", font=("Arial", 8))
    conf_ppfinal_sub_label.grid(row=5, column=2, padx=5, pady=5, sticky="w")

    ## Pg inicial
    conf_pginicial_label = Label(frame2, text="Pg Inicial:", bg="lightgreen", font=("Arial", 10))
    conf_pginicial_label.grid(row=6, column=0, padx=5, pady=5, sticky="w")

    conf_pginicial_entry = Entry(frame2, font=("Arial", 10), width=5)
    conf_pginicial_entry.grid(row=6, column=1, padx=5, pady=5, sticky="w")
    conf_pginicial_entry.insert(0, "0.5")

    conf_pginicial_sub_label = Label(frame2, text="(coeficiente)", bg="lightgreen", font=("Arial", 8))
    conf_pginicial_sub_label.grid(row=6, column=2, padx=5, pady=5, sticky="w")

    ## Pg final
    conf_pgfinal_label = Label(frame2, text="Pg Final:", bg="lightgreen", font=("Arial", 10))
    conf_pgfinal_label.grid(row=7, column=0, padx=5, pady=5, sticky="w")

    conf_pgfinal_entry = Entry(frame2, font=("Arial", 10), width=5)
    conf_pgfinal_entry.grid(row=7, column=1, padx=5, pady=5, sticky="w")
    conf_pgfinal_entry.insert(0, "2.5")

    conf_pgfinal_sub_label = Label(frame2, text="(coeficiente)", bg="lightgreen", font=("Arial", 8))
    conf_pgfinal_sub_label.grid(row=7, column=2, padx=5, pady=5, sticky="w")

    ## Modo manual
    manual_var = IntVar(value=0)  # Valor por defecto: 0 (Automático)
    conf_manual_checkbox = Checkbutton(frame2, text="Modo Manual", bg="lightgreen", font=("Arial", 10), variable=manual_var)
    conf_manual_checkbox.grid(row=8, column=0, padx=5, pady=5, sticky="w")

    ## Botón de inicio
    conf_inicio_button = Button(frame2, text="Iniciar Optimización", 
                                font=("Arial", 12), width=20, height=1, 
                                command=Iniciar_Optimizacion)
    conf_inicio_button.place(x=70, y=350)

    # Configuración 3 frame

    ## Titulo de Resultados
    subtitulo_label3 = Label(frame3, bg="lightcoral", font=("Arial", 12)
                            , text="Resultados", )
    subtitulo_label3.grid(row=0, column=0, padx=5, sticky="w", columnspan=2, pady=5)

    ## Text de resultados
    resultados_scroll = scrolledtext.ScrolledText(frame3, bg="lightyellow", 
                                                font=("Arial", 12), padx=5, pady=5,
                                                width=31, height=18, wrap="word")
    resultados_scroll.insert("insert", "Resultados del algoritmo PSO aparecerán aquí...\n")
    resultados_scroll.configure(state='disabled')

    resultados_scroll.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")
    def Borrar_Resultados():
        resultados_scroll.configure(state='normal')
        resultados_scroll.delete(1.0, 'end')
        resultados_scroll.configure(state='disabled')
        config = {
            'resultados': ("Resultados del algoritmo PSO aparecerán aquí...")
        }
        # Guardar configuración en archivo
        with open('config.json', 'w') as f:
            json.dump(config, f)
    ## Botón de borrar texto
    boton_borrar = Button(frame3, text="Borrar Resultados", font=("Arial", 10), width=16, height=1, command=Borrar_Resultados)
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
                    if nuevo_resultado != ultimo_resultado and nuevo_resultado != "":
                        resultados_scroll.configure(state='normal')
                        resultados_scroll.delete(1.0, 'end')
                        resultados_scroll.insert('end', nuevo_resultado)
                        resultados_scroll.configure(state='disabled')
                        
                        ultimo_resultado = nuevo_resultado

        except:
            pass
        
        # Verificar cada 2 segundos
        ventana.after(2000, verificar_cambios)
    def al_cerrar_ventana():
        config = {
            'resultados': ("Resultados del algoritmo PSO aparecerán aquí...")
        }
        with open('config.json', 'w') as f:
            json.dump(config, f)

        ventana.destroy()

    ventana.protocol("WM_DELETE_WINDOW", al_cerrar_ventana)
    verificar_cambios()
    ventana.mainloop()

if __name__ == "__main__":
    crear_gui()
