from math import sin, cos, pi, exp

inicio_dom_x = 0
final_dom_x = 0
inicio_dom_y = 0
final_dom_y = 0
# Se define el delay para las iteraciones
delay = 0 
#Se define el limite de líderes para finalizar el algoritmo
limite_lideres = 200


objectives_func = None
constraints_func = None

def map_to_domain(value, source_range, target_range) -> float:
    """Mapea un valor de un rango de origen a un rango de destino."""
    source_min, source_max = source_range
    target_min, target_max = target_range

    if source_max - source_min == 0:
        return target_min
        
    return target_min + (value - source_min) * (target_max - target_min) / \
            (source_max - source_min)

def map_to_domain_x(value, canvas_max) -> float:
    """Mapea el valor X del canvas al dominio del problema."""
    return map_to_domain(value, (0, canvas_max), (inicio_dom_x, final_dom_x))

def map_to_domain_y(value, canvas_max) -> float:
    """Mapea el valor Y del canvas al dominio del problema."""
    return map_to_domain(value, (0, canvas_max), (inicio_dom_y, final_dom_y))


def binh_and_korn_objectives(x, y) -> tuple:
    #Funciones objetivo de Binh and Korn
    f1 = 4 * x**2 + 4 * y**2
    f2 = (x - 5)**2 + (y - 5)**2
    return (f1, f2)

def binh_and_korn_constraints(x, y) -> bool:
    #Restricciones de la función
    g1 = (x - 5)**2 + y**2 <= 25
    g2 = (x - 8)**2 + (y + 3)**2 >= 7.7
    return g1 and g2

def seleccionar_binh_and_korn():
    global inicio_dom_x, final_dom_x, inicio_dom_y, final_dom_y
    global objectives_func, constraints_func, delay, limite_lideres

    inicio_dom_x = 0
    final_dom_x = 5
    inicio_dom_y = 0
    final_dom_y = 3
    delay = 70
    limite_lideres = 500

    
    objectives_func = binh_and_korn_objectives
    constraints_func = binh_and_korn_constraints
    print("Problema: Binh and Korn")


def schaffer_n1_objectives(x, y) -> tuple:
    #Funciones objetivo de Schaffer N. 1
    f1 = x**2
    f2 = (x - 2)**2
    return (f1, f2)

def schaffer_n1_constraints(x, y) -> bool:
    return True

def seleccionar_schaffer_n1():
    global inicio_dom_x, final_dom_x, inicio_dom_y, final_dom_y
    global objectives_func, constraints_func, delay, limite_lideres

    inicio_dom_x = -100
    final_dom_x = 100
    inicio_dom_y = -100
    final_dom_y = 100
    delay = 10
    limite_lideres = 200

    
    objectives_func = schaffer_n1_objectives
    constraints_func = schaffer_n1_constraints
    print("Problema: Schaffer N. 1")

def chankong_and_haimes_objectives(x, y) -> tuple:
    #Funciones objetivo de Chankong and Haimes
    f1 = 2 + (x - 2)**2 + (y - 1)**2
    f2 = 9*x - (y - 1)**2
    return (f1, f2)

def chankong_and_haimes_constraints(x, y) -> bool:
    #Restricciones de la función
    g1 = (x**2 + y**2) <= 225
    g2 = (x - 3**y + 10) <= 0
    return g1 and g2

def seleccionar_chankong_and_haimes():
    global inicio_dom_x, final_dom_x, inicio_dom_y, final_dom_y
    global objectives_func, constraints_func, delay, limite_lideres

    inicio_dom_x = -20
    final_dom_x = 20
    inicio_dom_y = -20
    final_dom_y = 20
    delay = 0
    limite_lideres = 200

    
    objectives_func = chankong_and_haimes_objectives
    constraints_func = chankong_and_haimes_constraints
    print("Problema: Chankong and Haimes")

def test_function_4_objectives(x, y) -> tuple:
    #Funciones objetivo de Test Function 4
    f1 = x**2 - y
    f2 = -0.5*x - y - 1
    return (f1, f2)

def test_function_4_constraints(x, y) -> bool:
    #Restricciones de la función
    g1 = (6.5 - (x/6) - y) >= 0
    g2 = 7.5 - 0.5*x - y >= 0
    g3 = 30 - 5*x - y >= 0
    return g1 and g2 and g3

def seleccionar_test_function_4():
    global inicio_dom_x, final_dom_x, inicio_dom_y, final_dom_y
    global objectives_func, constraints_func, delay, limite_lideres

    inicio_dom_x = -7
    final_dom_x = 4
    inicio_dom_y = -7
    final_dom_y = 4
    delay = 10
    limite_lideres = 200
    
    objectives_func = test_function_4_objectives
    constraints_func = test_function_4_constraints
    print("Problema: Test Function 4")

def polonis_two_objective_function_objectives(x, y) -> tuple:
    #Parametros necesarios para la función
    A1 = 0.5*sin(1) - 2*cos(1) + sin(2) - 1.5*cos(2)
    A2 = 1.5*sin(1) - cos(1) + 2*sin(2) - 0.5*cos(2)
    B1 = 0.5*sin(x) - 2*cos(x) + sin(y) - 1.5*cos(y)
    B2 = 1.5*sin(x) - cos(x) + 2*sin(y) - 0.5*cos(y)
    #Funciones objetivo de Poloni's Two Objective Function
    f1 = 1 + (A1 - B1)**2 + (A2 - B2)**2
    f2 = (x + 3)**2 + (y + 1)**2
    return (f1, f2)

def polonis_two_objective_function_constraints(x, y) -> bool:
    return True

def seleccionar_polonis_two_objective_function():
    global inicio_dom_x, final_dom_x, inicio_dom_y, final_dom_y
    global objectives_func, constraints_func, delay, limite_lideres

    inicio_dom_x = -pi
    final_dom_x = pi
    inicio_dom_y = -pi
    final_dom_y = pi
    delay = 0
    limite_lideres = 200
    

    objectives_func = polonis_two_objective_function_objectives
    constraints_func = polonis_two_objective_function_constraints
    print("Problema: Poloni's Two Objective Function")


def ctp1_function_objectives(x, y) -> tuple:
    # Prevenir división por cero y valores negativos
    if y < -0.999:  # Evitar y = -1
        y = -0.999
    
    f1 = x
    f2 = (1 + y) * exp(-x / (1 + y)) if (1 + y) != 0 else float('inf')
    return (f1, f2)

def ctp1_function_constraints(x, y) -> bool:
    if y < -0.999:  # Evitar y = -1
        return False
        
    f2 = (1 + y) * exp(-x / (1 + y)) if (1 + y) != 0 else float('inf')
    
    # Restricciones originales de CTP1
    g1 = f2 >= 0.858 * exp(-0.541 * x)
    g2 = f2 >= 0.728 * exp(-0.295 * x)
    
    return g1 and g2

def seleccionar_ctp1_function():
    global inicio_dom_x, final_dom_x, inicio_dom_y, final_dom_y
    global objectives_func, constraints_func, delay, limite_lideres

    inicio_dom_x = 0
    final_dom_x = 1
    inicio_dom_y = -1
    final_dom_y = 1
    delay = 0
    limite_lideres = 200
    
    objectives_func = ctp1_function_objectives
    constraints_func = ctp1_function_constraints
    print("Problema: CTP1 Function")


def kursawe2_objectives(x, y) -> tuple:
    f1 = -10 * exp(-0.2 * (x*x + y*y)**0.5)
    # f2: dos términos (i = 1, 2)
    f2 = (
        abs(x)**0.8 + 5 * sin(x**3)
      + abs(y)**0.8 + 5 * sin(y**3)
    )
    return (f1, f2)

def kursawe2_constraints(x, y) -> bool:
    # Sin restricciones
    return True

def seleccionar_kursawe2():
    global inicio_dom_x, final_dom_x
    global inicio_dom_y, final_dom_y
    global objectives_func, constraints_func, delay, limite_lideres

    inicio_dom_x = inicio_dom_y = -5
    final_dom_x = final_dom_y = 5
    delay = 10

    objectives_func = kursawe2_objectives
    constraints_func = kursawe2_constraints

    print("Problema: Kursawe (n=2)")

def constr_ex_objectives(x, y) -> tuple:
    # Funciones objetivo de Constr - Ex
    f1 = x
    f2 = (1+y)/x
    return (f1, f2)

def constr_ex_constraints(x, y) -> bool:
    g1 = (y + 9*x) >= 6
    g2 = (-y + 9*x) >= 1
    return g1 and g2

def seleccionar_constr_ex():
    global inicio_dom_x, final_dom_x
    global inicio_dom_y, final_dom_y
    global objectives_func, constraints_func, delay, limite_lideres

    inicio_dom_x = 0.1
    final_dom_x = 1
    inicio_dom_y = 0
    final_domy = 5
    delay = 10
    limite_lideres = 800

    objectives_func = constr_ex_objectives
    constraints_func = constr_ex_constraints
    print("Problema: Constr - Ex")

def schaffer_n2_objectives(x, y) -> tuple:
    # Funciones objetivo de Schaffer N. 2
    if x <= 1:
        f1 = -x
    elif 1 < x <= 3:
        f1 = x - 2
    elif 3 < x <= 4:
        f1 = 4 - x
    elif x > 4:
        f1 = x - 4
    
    f2 = (x - 5)**2
    return (f1, f2)

def schaffer_n2_constraints(x, y) -> bool:
    # Sin restricciones
    return True

def seleccionar_schaffer_n2():
    global inicio_dom_x, final_dom_x
    global inicio_dom_y, final_dom_y
    global objectives_func, constraints_func, delay, limite_lideres

    inicio_dom_x = -5
    final_dom_x = 10
    inicio_dom_y = -5
    final_dom_y = 10
    delay = 10
    limite_lideres = 300

    objectives_func = schaffer_n2_objectives
    constraints_func = schaffer_n2_constraints
    print("Problema: Schaffer N. 2")

