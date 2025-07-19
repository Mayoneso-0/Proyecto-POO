import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import subprocess
import sys
import os

class PSOGUIApplication(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("PSO Optimization Suite")
        self.geometry("1000x500")
        self.configure(bg='#f0f0f0')
        
        # Apply modern style
        style = ttk.Style()
        style.theme_use('clam')
        
        # Configure styles
        style.configure('Title.TLabel', font=('Arial', 16, 'bold'))
        style.configure('Section.TLabel', font=('Arial', 12, 'bold'))
        style.configure('Action.TButton', font=('Arial', 10, 'bold'))
        
        self.initialize_variables()
        self.create_widgets()
        self.update_parameter_visibility()

    def initialize_variables(self):
        # Common variables
        self.objetivo_tipo = tk.StringVar(value="Single")
        self.funcion = tk.StringVar(value="Rastrigin")
        
        # Single objective variables (graficadora)
        self.ancho_canva = tk.IntVar(value=500)
        self.alto_canva = tk.IntVar(value=500)
        self.definicion_canva = tk.IntVar(value=5)
        self.definicion_colores = tk.IntVar(value=100)
        self.num_particulas = tk.IntVar(value=12)
        self.w = tk.DoubleVar(value=0.6)
        self.pp_inicial = tk.DoubleVar(value=2.5)
        self.pp_final = tk.DoubleVar(value=0.5)
        self.pg_inicial = tk.DoubleVar(value=0.5)
        self.pg_final = tk.DoubleVar(value=2.5)
        self.min_iteraciones = tk.IntVar(value=25)
        self.manual = tk.BooleanVar(value=False)
        
        # Multi-objective variables (mopso)
        self.num_particulas_mo = tk.IntVar(value=50)
        self.max_iteraciones_mo = tk.IntVar(value=100)
        self.w_mo = tk.DoubleVar(value=0.5)
        self.c1_mo = tk.DoubleVar(value=2.0)
        self.c2_mo = tk.DoubleVar(value=2.0)
        self.mutation_rate = tk.DoubleVar(value=0.1)
        self.archivo_size = tk.IntVar(value=100)
        self.grid_divisions = tk.IntVar(value=10)
        
        self.running = False

    def create_widgets(self):
        # Main container
        main_frame = ttk.Frame(self)
        main_frame.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Title
        title_label = ttk.Label(main_frame, text="🔬 PSO Optimization Suite", style='Title.TLabel')
        title_label.pack(pady=(0, 10))
        
        # Create horizontal layout
        content_frame = ttk.Frame(main_frame)
        content_frame.pack(fill='both', expand=True)
        
        # Left side - Configuration (wider)
        config_frame = ttk.Frame(content_frame)
        config_frame.pack(side='left', fill='both', expand=True, padx=(0, 10))
        
        # Right side - Results (smaller)
        results_frame = ttk.Frame(content_frame, width=300)
        results_frame.pack(side='right', fill='y', padx=(10, 0))
        results_frame.pack_propagate(False)
        
        self.create_config_section(config_frame)
        self.create_results_section(results_frame)

    def create_config_section(self, parent):
        # Create main configuration container without scrolling
        config_container = ttk.Frame(parent)
        config_container.pack(fill='both', expand=True)
        
        # Create two columns for parameters
        left_column = ttk.Frame(config_container)
        left_column.pack(side='left', fill='both', expand=True, padx=(0, 10))
        
        right_column = ttk.Frame(config_container)
        right_column.pack(side='left', fill='both', expand=True, padx=(10, 0))
        
        # Objective type selection (left column)
        obj_frame = ttk.LabelFrame(left_column, text="Tipo de Optimización", padding=8)
        obj_frame.pack(fill='x', pady=(0, 8))
        
        ttk.Radiobutton(
            obj_frame, 
            text="🎯 Un Objetivo", 
            variable=self.objetivo_tipo, 
            value="Single",
            command=self.update_parameter_visibility
        ).pack(anchor='w', pady=1)
        
        ttk.Radiobutton(
            obj_frame, 
            text="🎯🎯 Multi-Objetivo", 
            variable=self.objetivo_tipo, 
            value="Multi",
            command=self.update_parameter_visibility
        ).pack(anchor='w', pady=1)
        
        # Function selection (left column)
        func_frame = ttk.LabelFrame(left_column, text="Función Objetivo", padding=8)
        func_frame.pack(fill='x', pady=(0, 8))
        
        functions = ['Rastrigin', 'Sphere', 'Ackley', 'Rosenbrock', 'Griewank', 'Himmelblau', 'Booth', 'Matyas', 'McCormick', 'Schaffer', 'Easom', 'CrossInTray', 'Eggholder', 'HolderTable', 'Bukin', 'BinhKorn', 'ChankongHaimes', 'TestFunction4', 'PolonisTwoObjective', 'CTP1', 'Kursawe2', 'ConstrEx', 'SchafferN2']
        func_combo = ttk.Combobox(func_frame, textvariable=self.funcion, values=functions, state='readonly')
        func_combo.pack(fill='x')
        
        # Single objective parameters
        self.single_frame_left = ttk.LabelFrame(left_column, text="Parámetros Canvas", padding=8)
        self.single_frame_left.pack(fill='x', pady=(0, 8))
        
        single_params_left = [
            ('Ancho canvas', self.ancho_canva, 'pixels'),
            ('Alto canvas', self.alto_canva, 'pixels'),
            ('Definición canvas', self.definicion_canva, 'resolución'),
            ('Definición colores', self.definicion_colores, 'niveles'),
        ]
        
        for label, var, hint in single_params_left:
            self.create_parameter_row(self.single_frame_left, label, var, hint)
        
        self.single_frame_right = ttk.LabelFrame(right_column, text="Parámetros PSO", padding=8)
        self.single_frame_right.pack(fill='x', pady=(0, 8))
        
        single_params_right = [
            ('Número de partículas', self.num_particulas, 'partículas'),
            ('Peso de inercia (w)', self.w, '0.0-1.0'),
            ('Mínimo iteraciones', self.min_iteraciones, 'iteraciones'),
            ('pp inicial', self.pp_inicial, 'coeficiente'),
            ('pp final', self.pp_final, 'coeficiente'),
            ('pg inicial', self.pg_inicial, 'coeficiente'),
            ('pg final', self.pg_final, 'coeficiente')
        ]
        
        for label, var, hint in single_params_right:
            self.create_parameter_row(self.single_frame_right, label, var, hint)
        
        # Manual step checkbox
        ttk.Checkbutton(
            self.single_frame_right, 
            text='🖱️ Modo manual', 
            variable=self.manual
        ).pack(anchor='w', pady=5)
        
        # Multi-objective parameters
        self.multi_frame_left = ttk.LabelFrame(left_column, text="MOPSO Básico", padding=8)
        self.multi_frame_left.pack(fill='x', pady=(0, 8))
        
        multi_params_left = [
            ('Número de partículas', self.num_particulas_mo, 'partículas'),
            ('Máximo iteraciones', self.max_iteraciones_mo, 'iteraciones'),
            ('Peso de inercia (w)', self.w_mo, '0.0-1.0'),
            ('Coeficiente c1', self.c1_mo, 'cognitivo')
        ]
        
        for label, var, hint in multi_params_left:
            self.create_parameter_row(self.multi_frame_left, label, var, hint)
        
        self.multi_frame_right = ttk.LabelFrame(right_column, text="MOPSO Avanzado", padding=8)
        self.multi_frame_right.pack(fill='x', pady=(0, 8))
        
        multi_params_right = [
            ('Coeficiente c2', self.c2_mo, 'social'),
            ('Tasa de mutación', self.mutation_rate, '0.0-1.0'),
            ('Tamaño archivo', self.archivo_size, 'soluciones'),
            ('Divisiones grid', self.grid_divisions, 'divisiones')
        ]
        
        for label, var, hint in multi_params_right:
            self.create_parameter_row(self.multi_frame_right, label, var, hint)
        
        # Control button (right column)
        control_frame = ttk.LabelFrame(right_column, text="Control", padding=8)
        control_frame.pack(fill='x', pady=8)
        
        self.start_btn = ttk.Button(
            control_frame, 
            text="🚀 Iniciar Optimización", 
            command=self.iniciar_pso,
            style='Action.TButton'
        )
        self.start_btn.pack(fill='x')

    def create_results_section(self, parent):
        # Results display
        results_label_frame = ttk.LabelFrame(parent, text="📊 Resultados", padding=8)
        results_label_frame.pack(fill='both', expand=True)
        
        self.results_text = scrolledtext.ScrolledText(
            results_label_frame,
            wrap=tk.WORD,
            width=35,
            height=15,
            font=('Consolas', 9)
        )
        self.results_text.pack(fill='both', expand=True)
        
        # Clear results button
        ttk.Button(
            results_label_frame, 
            text="🗑️ Limpiar", 
            command=self.clear_results
        ).pack(pady=(5, 0))

    def create_parameter_row(self, parent, label, var, hint):
        frame = ttk.Frame(parent)
        frame.pack(fill='x', pady=2)
        
        ttk.Label(frame, text=f"{label}:", width=20).pack(side='left')
        
        entry = ttk.Entry(frame, textvariable=var, width=10)
        entry.pack(side='left', padx=(5, 10))
        
        ttk.Label(frame, text=f"({hint})", foreground='gray').pack(side='left')

    def update_parameter_visibility(self):
        if self.objetivo_tipo.get() == "Single":
            # Show single objective frames
            self.single_frame_left.pack(fill='x', pady=(0, 8))
            self.single_frame_right.pack(fill='x', pady=(0, 8))
            # Hide multi objective frames
            self.multi_frame_left.pack_forget()
            self.multi_frame_right.pack_forget()
        else:
            # Hide single objective frames
            self.single_frame_left.pack_forget()
            self.single_frame_right.pack_forget()
            # Show multi objective frames
            self.multi_frame_left.pack(fill='x', pady=(0, 8))
            self.multi_frame_right.pack(fill='x', pady=(0, 8))

    def iniciar_pso(self):
        # Clear previous results
        self.results_text.delete(1.0, tk.END)
        
        # Disable button during execution
        self.start_btn.config(state='disabled')
        self.results_text.insert(tk.END, "🔄 Iniciando optimización...\n")
        self.results_text.update()
        
        # Use after to avoid blocking the GUI
        self.after(100, self._ejecutar_optimizacion)

    def _ejecutar_optimizacion(self):
        try:
            if self.objetivo_tipo.get() == "Single":
                self.ejecutar_single_objetivo()
            else:
                self.ejecutar_multi_objetivo()
        except Exception as e:
            self.results_text.insert(tk.END, f"❌ Error general: {str(e)}\n")
        finally:
            # Re-enable button - SIEMPRE se ejecuta
            self.start_btn.config(state='normal')
            self.results_text.update()
            self.results_text.insert(tk.END, "\n🔓 Botón habilitado nuevamente\n")
            self.results_text.update()

    def ejecutar_single_objetivo(self):
        # Mostrar parámetros utilizados
        self.results_text.insert(tk.END, "=" * 40 + "\n")
        self.results_text.insert(tk.END, "OPTIMIZACIÓN DE UN OBJETIVO\n")
        self.results_text.insert(tk.END, "=" * 40 + "\n\n")
        
        self.results_text.insert(tk.END, f"Función: {self.funcion.get()}\n")
        self.results_text.insert(tk.END, f"Canvas: {self.ancho_canva.get()}x{self.alto_canva.get()}\n")
        self.results_text.insert(tk.END, f"Partículas: {self.num_particulas.get()}\n")
        self.results_text.insert(tk.END, f"Iteraciones: {self.min_iteraciones.get()}\n")
        self.results_text.insert(tk.END, f"Peso inercia: {self.w.get()}\n")
        self.results_text.insert(tk.END, f"pp: {self.pp_inicial.get()}->{self.pp_final.get()}\n")
        self.results_text.insert(tk.END, f"pg: {self.pg_inicial.get()}->{self.pg_final.get()}\n")
        self.results_text.insert(tk.END, f"Manual: {'Sí' if self.manual.get() else 'No'}\n\n")
        self.results_text.update()
        
        try:
            # Limpiar imports anteriores para forzar reimportación
            modules_to_clear = ['Graficadora', 'Funciones', 'Algoritmo']
            for mod in modules_to_clear:
                if mod in sys.modules:
                    del sys.modules[mod]
            
            # Importar módulos
            import Graficadora
            import Funciones
            
            self.results_text.insert(tk.END, "📊 Módulos importados correctamente\n")
            self.results_text.update()
            
            # Configurar función ANTES de asignar variables a Graficadora
            func_name = self.funcion.get().lower()
            func_mapping = {
                'rastrigin': 'seleccionar_rastrigin_function',
                'sphere': 'seleccionar_sphere_function', 
                'ackley': 'seleccionar_ackley_function',
                'rosenbrock': 'seleccionar_rosenbrock_function',
                'griewank': 'seleccionar_griewank_function',
                'himmelblau': 'seleccionar_himmelblau_function',
                'booth': 'seleccionar_booth_function',
                'matyas': 'seleccionar_matyas_function',
                'mccormick': 'seleccionar_mc_cormick_function',
                'schaffer': 'seleccionar_schaffer_n2_function',
                'easom': 'seleccionar_easom_function',
                'crossintray': 'seleccionar_cross_in_tray_function',
                'eggholder': 'seleccionar_egg_holder_function',
                'holdertable': 'seleccionar_holder_table_function',
                'bukin': 'seleccionar_bukin_n6_function'
            }
            
            selected_func = func_mapping.get(func_name, 'seleccionar_rastrigin_function')
            
            # Ejecutar la función de selección EN EL MÓDULO Funciones
            if hasattr(Funciones, selected_func):
                getattr(Funciones, selected_func)()
                self.results_text.insert(tk.END, f"✅ Función {self.funcion.get()} configurada\n")
                
                # Verificar que la función se configuró correctamente
                if hasattr(Funciones, 'funcion') and Funciones.funcion is not None:
                    self.results_text.insert(tk.END, f"🎯 Función activa: {Funciones.funcion.__name__}\n")
                else:
                    self.results_text.insert(tk.END, "⚠️ Error: función no se configuró correctamente\n")
            else:
                Funciones.seleccionar_rastrigin_function()
                self.results_text.insert(tk.END, "⚠️ Función no encontrada, usando Rastrigin por defecto\n")
            
            # Asignar las variables al módulo Graficadora
            Graficadora.ancho_canva = self.ancho_canva.get()
            Graficadora.alto_canva = self.alto_canva.get()
            Graficadora.definicion_canva = self.definicion_canva.get()
            Graficadora.definicion_colores = self.definicion_colores.get()
            Graficadora.num_particulas = self.num_particulas.get()
            Graficadora.w = self.w.get()
            Graficadora.pp_inicial = self.pp_inicial.get()
            Graficadora.pp_final = self.pp_final.get()
            Graficadora.pg_inicial = self.pg_inicial.get()
            Graficadora.pg_final = self.pg_final.get()
            Graficadora.min_iteraciones = self.min_iteraciones.get()
            Graficadora.manual = self.manual.get()
            
            # Resetear las variables de estado de Graficadora
            Graficadora.enjambre_creado = False
            Graficadora.seguir_iterando = True
            Graficadora.iteracion = 0
            Graficadora.dibujo_particulas = []
            Graficadora.pp = self.pp_inicial.get()
            Graficadora.pg = self.pg_inicial.get()
            
            self.results_text.insert(tk.END, "⚙️ Variables configuradas en Graficadora\n")
            
            # Comentar la línea f.seleccionar_rastrigin_function() en Graficadora.py si existe
            # ya que hemos configurado la función desde aquí
            
            self.results_text.insert(tk.END, "🚀 Abriendo ventana de optimización...\n")
            self.results_text.update()
            
            # Crear callback para cuando se cierre la ventana de Graficadora
            def on_graficadora_close():
                self.results_text.insert(tk.END, "\n" + "=" * 40 + "\n")
                self.results_text.insert(tk.END, "RESULTADOS DE LA OPTIMIZACIÓN\n")
                self.results_text.insert(tk.END, "=" * 40 + "\n")
                
                # Intentar obtener los resultados del enjambre
                if hasattr(Graficadora, 'enjambre1') and Graficadora.enjambre1 is not None:
                    mejor_x = Graficadora.enjambre1.mejor_pos_global_x
                    mejor_y = Graficadora.enjambre1.mejor_pos_global_y
                    
                    # Convertir coordenadas del canvas al dominio de la función
                    mejor_x_dom = Funciones.trans_lin_dom_x(mejor_x, 0, Graficadora.ancho_canva)
                    mejor_y_dom = Funciones.trans_lin_dom_y(mejor_y, 0, Graficadora.alto_canva)
                    mejor_valor = Funciones.funcion(mejor_x_dom, mejor_y_dom)
                    
                    self.results_text.insert(tk.END, f"🎯 Mejor posición encontrada:\n")
                    self.results_text.insert(tk.END, f"   x = {mejor_x_dom:.6f}\n")
                    self.results_text.insert(tk.END, f"   y = {mejor_y_dom:.6f}\n")
                    self.results_text.insert(tk.END, f"� Mejor valor de función: {mejor_valor:.6f}\n")
                    self.results_text.insert(tk.END, f"🔄 Iteraciones ejecutadas: {Graficadora.iteracion}\n")
                else:
                    self.results_text.insert(tk.END, "⚠️ No se pudieron obtener resultados del enjambre\n")
                
                self.results_text.insert(tk.END, "✅ Optimización completada\n")
                self.results_text.update()
            
            # Registrar el callback para cuando se cierre Graficadora
            if hasattr(Graficadora, 'window'):
                Graficadora.window.protocol("WM_DELETE_WINDOW", on_graficadora_close)
            
            self.results_text.insert(tk.END, "📋 Ventana de optimización abierta\n")
            self.results_text.insert(tk.END, "🎮 Controles:\n")
            self.results_text.insert(tk.END, "   Q: Crear enjambre\n")
            self.results_text.insert(tk.END, "   W: Iterar algoritmo\n")
            self.results_text.insert(tk.END, "   E: Finalizar\n")
            
        except ImportError as e:
            self.results_text.insert(tk.END, f"⚠️ Error de importación: {str(e)}\n")
            self.results_text.insert(tk.END, "📁 Asegúrate de que Graficadora.py y Funciones.py estén en el directorio\n")
        except Exception as e:
            self.results_text.insert(tk.END, f"❌ Error inesperado: {str(e)}\n")
        
        self.results_text.update()

    def ejecutar_multi_objetivo(self):
        # Mostrar parámetros utilizados
        self.results_text.insert(tk.END, "=" * 40 + "\n")
        self.results_text.insert(tk.END, "OPTIMIZACIÓN MULTI-OBJETIVO\n")
        self.results_text.insert(tk.END, "=" * 40 + "\n\n")
        
        self.results_text.insert(tk.END, f"Función: {self.funcion.get()}\n")
        self.results_text.insert(tk.END, f"Partículas: {self.num_particulas_mo.get()}\n")
        self.results_text.insert(tk.END, f"Iteraciones: {self.max_iteraciones_mo.get()}\n")
        self.results_text.insert(tk.END, f"Peso inercia: {self.w_mo.get()}\n")
        self.results_text.insert(tk.END, f"c1/c2: {self.c1_mo.get()}/{self.c2_mo.get()}\n")
        self.results_text.insert(tk.END, f"Mutación: {self.mutation_rate.get()}\n")
        self.results_text.insert(tk.END, f"Archivo: {self.archivo_size.get()}\n")
        self.results_text.insert(tk.END, f"Grid: {self.grid_divisions.get()}\n\n")
        self.results_text.update()
        
        try:
            # Agregar el directorio MOPSO al path del sistema
            current_dir = os.path.dirname(os.path.abspath(__file__))
            mopso_dir = os.path.join(current_dir, 'MOPSO')
            
            # Agregar el directorio MOPSO al path si existe
            if os.path.exists(mopso_dir):
                if mopso_dir not in sys.path:
                    sys.path.insert(0, mopso_dir)
                self.results_text.insert(tk.END, f"📁 Directorio MOPSO encontrado\n")
            else:
                self.results_text.insert(tk.END, f"⚠️ Directorio MOPSO no encontrado\n")
                self.results_text.insert(tk.END, f"   Buscando en: {mopso_dir}\n")
                
            self.results_text.update()
            
            # Intentar importar los módulos MOPSO
            try:
                # Limpiar imports anteriores
                modules_to_clear = ['Funciones_MOPSO', 'Graficadora_MOPSO', 'Algoritmo_MOPSO']
                for mod in modules_to_clear:
                    if mod in sys.modules:
                        del sys.modules[mod]
                
                # Importar Funciones_MOPSO primero
                from MOPSO import Funciones_MOPSO as f_mo
                self.results_text.insert(tk.END, "✅ Funciones_MOPSO importado\n")
                
                # Configurar la función según la selección
                func_name = self.funcion.get().lower()
                func_mapping = {
                    # Funciones single-objective adaptadas para MOPSO
                    'rastrigin': 'seleccionar_schaffer_n2',
                    'sphere': 'seleccionar_schaffer_n1', 
                    'ackley': 'seleccionar_binh_and_korn',
                    'rosenbrock': 'seleccionar_chankong_and_haimes',
                    'griewank': 'seleccionar_test_function_4',
                    'himmelblau': 'seleccionar_polonis_two_objective_function',
                    'booth': 'seleccionar_ctp1_function',
                    'matyas': 'seleccionar_kursawe2',
                    'mccormick': 'seleccionar_constr_ex',
                    'schaffer': 'seleccionar_schaffer_n2',
                    'easom': 'seleccionar_schaffer_n2',
                    'crossintray': 'seleccionar_schaffer_n2',
                    'eggholder': 'seleccionar_schaffer_n2',
                    'holdertable': 'seleccionar_schaffer_n2',
                    'bukin': 'seleccionar_schaffer_n2',
                    # Funciones multi-objetivo nativas
                    'binhkorn': 'seleccionar_binh_and_korn',
                    'chankonghaimes': 'seleccionar_chankong_and_haimes',
                    'testfunction4': 'seleccionar_test_function_4',
                    'polonistwo': 'seleccionar_polonis_two_objective_function',
                    'ctp1': 'seleccionar_ctp1_function',
                    'kursawe2': 'seleccionar_kursawe2',
                    'constrex': 'seleccionar_constr_ex',
                    'schaffern2': 'seleccionar_schaffer_n2'
                }
                
                selected_func = func_mapping.get(func_name, 'seleccionar_schaffer_n2')
                
                if hasattr(f_mo, selected_func):
                    getattr(f_mo, selected_func)()
                    self.results_text.insert(tk.END, f"🎯 Función {selected_func} configurada\n")
                else:
                    f_mo.seleccionar_schaffer_n2()
                    self.results_text.insert(tk.END, "🎯 Función por defecto (Schaffer N2) configurada\n")
                
                # Ahora importar Graficadora_MOPSO
                try:
                    from MOPSO import Graficadora_MOPSO
                    self.results_text.insert(tk.END, "✅ Graficadora_MOPSO importado\n")
                    
                    # Configurar las variables del módulo
                    if hasattr(Graficadora_MOPSO, 'num_particulas'):
                        Graficadora_MOPSO.num_particulas = self.num_particulas_mo.get()
                    if hasattr(Graficadora_MOPSO, 'w'):
                        Graficadora_MOPSO.w = self.w_mo.get()
                    if hasattr(Graficadora_MOPSO, 'pp'):
                        Graficadora_MOPSO.pp = self.c1_mo.get()
                    if hasattr(Graficadora_MOPSO, 'pg'):
                        Graficadora_MOPSO.pg = self.c2_mo.get()
                    if hasattr(Graficadora_MOPSO, 'ancho_canva'):
                        Graficadora_MOPSO.ancho_canva = 500
                    if hasattr(Graficadora_MOPSO, 'alto_canva'):
                        Graficadora_MOPSO.alto_canva = 500
                        
                    self.results_text.insert(tk.END, "⚙️ Variables MOPSO configuradas\n")
                    self.results_text.insert(tk.END, "🚀 Ejecutando MOPSO...\n")
                    self.results_text.insert(tk.END, "📋 Ventana MOPSO abierta\n")
                    self.results_text.insert(tk.END, "🎮 Controles:\n")
                    self.results_text.insert(tk.END, "   Q: Crear enjambre\n")
                    self.results_text.insert(tk.END, "   W: Iterar algoritmo\n")
                    self.results_text.insert(tk.END, "   E: Finalizar\n")
                    
                    # Programar verificación de resultados para MOPSO
                    self.after(2000, self.verificar_resultados_mopso)
                    
                except ImportError as e2:
                    self.results_text.insert(tk.END, f"❌ Error importando Graficadora_MOPSO: {str(e2)}\n")
                    
                    # Intentar ejecutar como subprocess
                    try:
                        self.results_text.insert(tk.END, "🔄 Intentando ejecutar MOPSO como proceso separado...\n")
                        
                        # Crear un archivo temporal con la configuración
                        config_script = f"""
import sys
import os
sys.path.insert(0, r'{mopso_dir}')

try:
    import Funciones_MOPSO as f_mo
    import Graficadora_MOPSO
    
    # Configurar función
    selected_func = '{selected_func}'
    if hasattr(f_mo, selected_func):
        getattr(f_mo, selected_func)()
    else:
        f_mo.seleccionar_schaffer_n2()
    
    # Configurar variables
    Graficadora_MOPSO.num_particulas = {self.num_particulas_mo.get()}
    Graficadora_MOPSO.w = {self.w_mo.get()}
    if hasattr(Graficadora_MOPSO, 'pp'):
        Graficadora_MOPSO.pp = {self.c1_mo.get()}
    if hasattr(Graficadora_MOPSO, 'pg'):
        Graficadora_MOPSO.pg = {self.c2_mo.get()}
    
    print("MOPSO configurado y ejecutándose...")
    
except Exception as e:
    print(f"Error en MOPSO: {{e}}")
"""
                        
                        # Guardar script temporal
                        temp_script = os.path.join(current_dir, 'temp_mopso.py')
                        with open(temp_script, 'w', encoding='utf-8') as f:
                            f.write(config_script)
                        
                        # Ejecutar el script
                        subprocess.Popen([sys.executable, temp_script])
                        
                        self.results_text.insert(tk.END, "✅ MOPSO iniciado como proceso separado\n")
                        
                        # Limpiar archivo temporal después de un tiempo
                        def cleanup_temp():
                            try:
                                if os.path.exists(temp_script):
                                    os.remove(temp_script)
                            except:
                                pass
                        
                        self.after(5000, cleanup_temp)
                        
                    except Exception as e3:
                        self.results_text.insert(tk.END, f"❌ Error ejecutando subprocess: {str(e3)}\n")
                
            except ImportError as e:
                self.results_text.insert(tk.END, f"❌ Error importando módulos MOPSO: {str(e)}\n")
                self.results_text.insert(tk.END, "📋 Verifica que existan estos archivos en la carpeta MOPSO:\n")
                self.results_text.insert(tk.END, "   - Graficadora_MOPSO.py\n")
                self.results_text.insert(tk.END, "   - Funciones_MOPSO.py\n")
                self.results_text.insert(tk.END, "   - Algoritmo_MOPSO.py\n")
                
        except Exception as e:
            self.results_text.insert(tk.END, f"❌ Error general: {str(e)}\n")
        
        self.results_text.update()

    def verificar_resultados_graficadora(self):
        """Verifica periódicamente si hay resultados disponibles en Graficadora"""
        try:
            import Graficadora
            import Funciones
            
            # Verificar si el enjambre existe y tiene datos
            if (hasattr(Graficadora, 'enjambre1') and 
                Graficadora.enjambre1 is not None and 
                hasattr(Graficadora, 'seguir_iterando') and 
                not Graficadora.seguir_iterando):
                
                # Mostrar resultados finales
                self.mostrar_resultados_single()
            else:
                # Continuar verificando cada 2 segundos
                self.after(2000, self.verificar_resultados_graficadora)
                
        except:
            # Si hay error, continuar verificando
            self.after(2000, self.verificar_resultados_graficadora)

    def verificar_resultados_mopso(self):
        """Verifica periódicamente si hay resultados disponibles en MOPSO"""
        try:
            # Intentar acceder a los módulos MOPSO
            mopso_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'MOPSO')
            if mopso_dir in sys.path:
                from MOPSO import Graficadora_MOPSO
                
                # Verificar si hay líderes disponibles
                if (hasattr(Graficadora_MOPSO, 'enjambre') and 
                    hasattr(Graficadora_MOPSO.enjambre, 'lideres') and
                    len(Graficadora_MOPSO.enjambre.lideres) > 0):
                    
                    self.mostrar_resultados_mopso()
                else:
                    # Continuar verificando cada 3 segundos
                    self.after(3000, self.verificar_resultados_mopso)
            else:
                # Si no se puede acceder, intentar nuevamente
                self.after(3000, self.verificar_resultados_mopso)
                
        except:
            # Si hay error, continuar verificando
            self.after(3000, self.verificar_resultados_mopso)

    def mostrar_resultados_single(self):
        """Muestra los resultados del algoritmo single-objetivo"""
        try:
            import Graficadora
            import Funciones
            
            self.results_text.insert(tk.END, "\n" + "=" * 40 + "\n")
            self.results_text.insert(tk.END, "RESULTADOS DE LA OPTIMIZACIÓN\n")
            self.results_text.insert(tk.END, "=" * 40 + "\n")
            
            # Intentar obtener los resultados del enjambre
            if hasattr(Graficadora, 'enjambre1') and Graficadora.enjambre1 is not None:
                mejor_x = Graficadora.enjambre1.mejor_pos_global_x
                mejor_y = Graficadora.enjambre1.mejor_pos_global_y
                
                # Convertir coordenadas del canvas al dominio de la función
                mejor_x_dom = Funciones.trans_lin_dom_x(mejor_x, 0, Graficadora.ancho_canva)
                mejor_y_dom = Funciones.trans_lin_dom_y(mejor_y, 0, Graficadora.alto_canva)
                mejor_valor = Funciones.funcion(mejor_x_dom, mejor_y_dom)
                
                self.results_text.insert(tk.END, f"🎯 Mejor posición encontrada:\n")
                self.results_text.insert(tk.END, f"   x = {mejor_x_dom:.6f}\n")
                self.results_text.insert(tk.END, f"   y = {mejor_y_dom:.6f}\n")
                self.results_text.insert(tk.END, f"📊 Mejor valor de función: {mejor_valor:.6f}\n")
                self.results_text.insert(tk.END, f"🔄 Iteraciones ejecutadas: {getattr(Graficadora, 'iteracion', 'N/A')}\n")
                
                # Información adicional del dominio de la función
                self.results_text.insert(tk.END, f"📐 Dominio de la función:\n")
                self.results_text.insert(tk.END, f"   x: [{Funciones.inicio_dom_x:.3f}, {Funciones.final_dom_x:.3f}]\n")
                self.results_text.insert(tk.END, f"   y: [{Funciones.inicio_dom_y:.3f}, {Funciones.final_dom_y:.3f}]\n")
                
            else:
                self.results_text.insert(tk.END, "⚠️ No se pudieron obtener resultados del enjambre\n")
            
            self.results_text.insert(tk.END, "✅ Optimización completada\n")
            self.results_text.update()
            
        except Exception as e:
            self.results_text.insert(tk.END, f"❌ Error al mostrar resultados: {str(e)}\n")
            self.results_text.update()

    def mostrar_resultados_mopso(self):
        """Muestra los resultados del algoritmo MOPSO"""
        try:
            import sys
            # Intentar acceder a los módulos MOPSO
            mopso_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'MOPSO')
            if mopso_dir in sys.path:
                from MOPSO import Graficadora_MOPSO
                
                self.results_text.insert(tk.END, "\n" + "=" * 40 + "\n")
                self.results_text.insert(tk.END, "RESULTADOS MOPSO\n")
                self.results_text.insert(tk.END, "=" * 40 + "\n")
                
                # Intentar obtener los líderes del frente de Pareto
                if (hasattr(Graficadora_MOPSO, 'enjambre') and 
                    hasattr(Graficadora_MOPSO.enjambre, 'lideres')):
                    
                    lideres = Graficadora_MOPSO.enjambre.lideres
                    self.results_text.insert(tk.END, f"🏆 Soluciones en el Frente de Pareto: {len(lideres)}\n")
                    
                    if lideres:
                        self.results_text.insert(tk.END, "📊 Primeras 5 soluciones:\n")
                        for i, (x, y, obj) in enumerate(lideres[:5]):
                            f1, f2 = obj
                            self.results_text.insert(tk.END, f"   {i+1}: x={x:.4f}, y={y:.4f} → f1={f1:.4f}, f2={f2:.4f}\n")
                    
                else:
                    self.results_text.insert(tk.END, "⚠️ No se pudieron obtener resultados del frente de Pareto\n")
                
                self.results_text.insert(tk.END, "✅ Optimización MOPSO completada\n")
            else:
                self.results_text.insert(tk.END, "⚠️ No se pudo acceder a los resultados MOPSO\n")
                
        except Exception as e:
            self.results_text.insert(tk.END, f"❌ Error al mostrar resultados MOPSO: {str(e)}\n")
        
        self.results_text.update()

    def clear_results(self):
        self.results_text.delete(1.0, tk.END)

if __name__ == '__main__':
    app = PSOGUIApplication()
    try:
        app.mainloop()
    except KeyboardInterrupt:
        app.quit()
    except Exception as e:
        print(f"Error al cerrar la aplicación: {e}")
    finally:
        try:
            app.destroy()
        except:
            pass

