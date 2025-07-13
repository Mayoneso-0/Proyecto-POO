#Importaciones necesarias
import math

# Definimos las variables necesarias para las funciones
inicio_dom_x = 0
final_dom_x = 0
inicio_dom_y = 0
final_dom_y = 0

funcion = None

def trans_lin_dom_x(x, a, b):
    respuesta = (x-a)*((final_dom_x-inicio_dom_x)/(b-a))+ inicio_dom_x
    return respuesta
def trans_lin_dom_y(x, a, b):
    respuesta = (x-a)*((final_dom_y-inicio_dom_y)/(b-a))+ inicio_dom_y
    return respuesta

# Definimos las funciones matematicas que vamos a usar
# Cada funcion tiene su dominio y rango
def mi_function(x, y):
    if x < inicio_dom_x or x > final_dom_x or y < inicio_dom_y or y > final_dom_y:
        return 1e10
    resultado = ((x+12)**2+(y-12)**2)**1/2+((x-4)**2+(y-2)**2)**1/2+((x+8)**2+(y+10)**2)**1/2
    return resultado
def seleccionar_mi_function():
    global inicio_dom_x
    inicio_dom_x = -20
    global final_dom_x
    final_dom_x = 20
    global inicio_dom_y
    inicio_dom_y = -20
    global final_dom_y
    final_dom_y = 20

    global funcion
    funcion = mi_function

def rastrigin_function(x, y):
    if x < inicio_dom_x or x > final_dom_x or y < inicio_dom_y or y > final_dom_y:
        return 1e10
    resultado = 10*2 + (x**2 - 10*math.cos(2*math.pi*x)) + \
                (y**2 - 10*math.cos(2*math.pi*y))
    return resultado
def seleccionar_rastrigin_function():
    global inicio_dom_x
    inicio_dom_x = -5.12
    global final_dom_x
    final_dom_x = 5.12
    global inicio_dom_y
    inicio_dom_y = -5.12
    global final_dom_y
    final_dom_y = 5.12

    global funcion
    funcion = rastrigin_function

def ackley_function(x, y):
    if x < inicio_dom_x or x > final_dom_x or y < inicio_dom_y or y > final_dom_y:
        return 1e10
    resultado = -20*math.exp(-0.2*(0.5*(x**2+y**2)**0.5)) \
        -math.exp(0.5*(math.cos(2*math.pi*x)+math.cos(2*math.pi*y))) \
        +math.e+20
    return resultado
def seleccionar_ackley_function():
    global inicio_dom_x
    inicio_dom_x = -5
    global final_dom_x
    final_dom_x = 5
    global inicio_dom_y
    inicio_dom_y = -5
    global final_dom_y
    final_dom_y = 5 

    global funcion
    funcion = ackley_function

def sphere_function(x, y):
    if x < inicio_dom_x or x > final_dom_x or y < inicio_dom_y or y > final_dom_y:
        return 1e10
    resultado = (x**2 + y**2)
    return resultado
def seleccionar_sphere_function():
    global inicio_dom_x
    inicio_dom_x = -2
    global final_dom_x
    final_dom_x = 2
    global inicio_dom_y
    inicio_dom_y = -2
    global final_dom_y
    final_dom_y = 2

    global funcion
    funcion = sphere_function

def rosenbrock_function(x, y):
    if x < inicio_dom_x or x > final_dom_x or y < inicio_dom_y or y > final_dom_y:
        return 1e10
    resultado = (1-x)**2 + 100*(y-x**2)**2
    return resultado
def seleccionar_rosenbrock_function():
    global inicio_dom_x
    inicio_dom_x = -2
    global final_dom_x
    final_dom_x = 2
    global inicio_dom_y
    inicio_dom_y = -1
    global final_dom_y
    final_dom_y = 3

    global funcion
    funcion = rosenbrock_function

def beale_function(x, y):
    if x < inicio_dom_x or x > final_dom_x or y < inicio_dom_y or y > final_dom_y:
        return 1e10
    resultado = (1.5-x+x*y)**2 + (2.25-x+x*y**2)**2 + (2.625-x+x*y**3)**2
    return resultado
def seleccionar_beale_function():
    global inicio_dom_x
    inicio_dom_x = -4.5
    global final_dom_x
    final_dom_x = 4.5
    global inicio_dom_y
    inicio_dom_y = -4.5
    global final_dom_y
    final_dom_y = 4.5

    global funcion
    funcion = beale_function

def goldstein_price_function(x, y):
    if x < inicio_dom_x or x > final_dom_x or y < inicio_dom_y or y > final_dom_y:
        return 1e10
    resultado = (1 + ((x+y+1)**2)*(19-14*x+3*x**2-14*y+6*x*y+3*y**2)) * \
                (30 + ((2*x-3*y)**2)*(18-32*x+12*x**2+48*y-36*x*y+27*y**2))
    return resultado
def seleccionar_goldstein_price_function():
    global inicio_dom_x
    inicio_dom_x = -2
    global final_dom_x
    final_dom_x = 2
    global inicio_dom_y
    inicio_dom_y = -2
    global final_dom_y
    final_dom_y = 2

    global funcion
    funcion = goldstein_price_function

def booth_function(x, y):
    if x < inicio_dom_x or x > final_dom_x or y < inicio_dom_y or y > final_dom_y:
        return 1e10
    resultado = (x+2*y-7)**2 + (2*x+y-5)**2 
    return resultado
def seleccionar_booth_function():
    global inicio_dom_x
    inicio_dom_x = -10
    global final_dom_x
    final_dom_x = 10
    global inicio_dom_y
    inicio_dom_y = -10
    global final_dom_y
    final_dom_y = 10

    global funcion
    funcion = booth_function

def bukin_n6_function(x, y):
    if x < inicio_dom_x or x > final_dom_x or y < inicio_dom_y or y > final_dom_y:
        return 1e10
    resultado = 100*(abs(y-0.01*x**2))**1/2+0.01*abs(x+10)
    return resultado
def seleccionar_bukin_n6_function():
    global inicio_dom_x
    inicio_dom_x = -15
    global final_dom_x
    final_dom_x = -5
    global inicio_dom_y
    inicio_dom_y = -4
    global final_dom_y
    final_dom_y = 6

    global funcion
    funcion = bukin_n6_function

def matyas_function(x, y):
    if x < inicio_dom_x or x > final_dom_x or y < inicio_dom_y or y > final_dom_y:
        return 1e10
    resultado = 0.26*(x**2+y**2) - 0.48*x*y
    return resultado
def seleccionar_matyas_function():
    global inicio_dom_x
    inicio_dom_x = -10
    global final_dom_x
    final_dom_x = 10
    global inicio_dom_y
    inicio_dom_y = -10
    global final_dom_y
    final_dom_y = 10

    global funcion
    funcion = matyas_function

def levi_n13_function(x, y):
    if x < inicio_dom_x or x > final_dom_x or y < inicio_dom_y or y > final_dom_y:
        return 1e10
    resultado = (math.sin(3*math.pi*x))**2 + (x-1)**2 * \
                (1 + (math.sin(3*math.pi*y)**2)) + (y-1)**2 * \
                (1+(math.sin(2*math.pi*y)**2))
    return resultado
def seleccionar_levi_n13_function():
    global inicio_dom_x
    inicio_dom_x = -10
    global final_dom_x
    final_dom_x = 10
    global inicio_dom_y
    inicio_dom_y = -10
    global final_dom_y
    final_dom_y = 10

    global funcion
    funcion = levi_n13_function

def griewank_function(x, y):
    if x < inicio_dom_x or x > final_dom_x or y < inicio_dom_y or y > final_dom_y:
        return 1e10
    resultado = 1 + 1/4000 * (x**2 + y**2) - (math.cos(x) * math.cos(y/2**0.5))
    return resultado
def seleccionar_griewank_function():
    global inicio_dom_x
    inicio_dom_x = -10
    global final_dom_x
    final_dom_x = 10
    global inicio_dom_y
    inicio_dom_y = -10
    global final_dom_y
    final_dom_y = 10

    global funcion
    funcion = griewank_function

def himmelblau_function(x, y):
    if x < inicio_dom_x or x > final_dom_x or y < inicio_dom_y or y > final_dom_y:
        return 1e10
    resultado = (x**2 + y - 11)**2 + (x + y**2 - 7)**2
    return resultado
def seleccionar_himmelblau_function():
    global inicio_dom_x
    inicio_dom_x = -5
    global final_dom_x
    final_dom_x = 5
    global inicio_dom_y
    inicio_dom_y = -5
    global final_dom_y
    final_dom_y = 5

    global funcion
    funcion = himmelblau_function

def three_hump_camel_function(x, y):
    if x < inicio_dom_x or x > final_dom_x or y < inicio_dom_y or y > final_dom_y:
        return 1e10
    resultado = 2*x**2 - 1.05*x**4 + (x**6)/6 + x*y + y**2
    return resultado
def seleccionar_three_hump_camel_function():
    global inicio_dom_x
    inicio_dom_x = -5
    global final_dom_x
    final_dom_x = 5
    global inicio_dom_y
    inicio_dom_y = -5
    global final_dom_y
    final_dom_y = 5

    global funcion
    funcion = three_hump_camel_function

def easom_function(x, y):
    if x < inicio_dom_x or x > final_dom_x or y < inicio_dom_y or y > final_dom_y:
        return 1e10
    resultado = -math.cos(x)*math.cos(y)* \
                 math.exp(-((x-math.pi)**2+(y-math.pi)**2))
    return resultado
def seleccionar_easom_function():
    global inicio_dom_x
    inicio_dom_x = -1
    global final_dom_x
    final_dom_x = 7
    global inicio_dom_y
    inicio_dom_y = -1
    global final_dom_y
    final_dom_y = 7

    global funcion
    funcion = easom_function

def cross_in_tray_function(x, y):
    if x < inicio_dom_x or x > final_dom_x or y < inicio_dom_y or y > final_dom_y:
        return 1e10
    resultado = -0.0001 * (abs(math.sin(x)*math.sin(y)* \
                               math.exp(abs(100-((x**2+y**2) \
                               **0.5)/math.pi))) + 1)**0.1
    return resultado
def seleccionar_cross_in_tray_function():
    global inicio_dom_x
    inicio_dom_x = -10
    global final_dom_x
    final_dom_x = 10
    global inicio_dom_y
    inicio_dom_y = -10
    global final_dom_y
    final_dom_y = 10

    global funcion
    funcion = cross_in_tray_function

def egg_holder_function(x, y):
    if x < inicio_dom_x or x > final_dom_x or y < inicio_dom_y or y > final_dom_y:
        return 1e10
    resultado = -(y+47)*math.sin((abs(x/2+(y+47)))**0.5)- \
                x*math.sin((abs(x-(y+47)))**0.5)
    return resultado
def seleccionar_egg_holder_function():
    global inicio_dom_x
    inicio_dom_x = -512
    global final_dom_x
    final_dom_x = 512
    global inicio_dom_y
    inicio_dom_y = -512
    global final_dom_y
    final_dom_y = 512

    global funcion
    funcion = egg_holder_function

def holder_table_function(x, y):
    if x < inicio_dom_x or x > final_dom_x or y < inicio_dom_y or y > final_dom_y:
        return 1e10
    resultado = -abs(math.sin(x)*math.cos(y)*math.exp( \
                     abs(1-((x**2+y**2)**0.5)/math.pi)))
    return resultado
def seleccionar_holder_table_function():
    global inicio_dom_x
    inicio_dom_x = -10
    global final_dom_x
    final_dom_x = 10
    global inicio_dom_y
    inicio_dom_y = -10
    global final_dom_y
    final_dom_y = 10

    global funcion
    funcion = holder_table_function

def mc_cormick_function(x, y):
    if x < inicio_dom_x or x > final_dom_x or y < inicio_dom_y or y > final_dom_y:
        return 1e10
    resultado = (math.sin(x+y)) + (x-y)**2 - 1.5*x + 2.5*y + 1
    return resultado
def seleccionar_mc_cormick_function():
    global inicio_dom_x
    inicio_dom_x = -1.5
    global final_dom_x
    final_dom_x = 4
    global inicio_dom_y
    inicio_dom_y = -3
    global final_dom_y
    final_dom_y = 4

    global funcion
    funcion = mc_cormick_function

def schaffer_n2_function(x, y):
    if x < inicio_dom_x or x > final_dom_x or y < inicio_dom_y or y > final_dom_y:
        return 1e10
    resultado = 0.5 + (math.sin(x**2 - y**2)**2 - 0.5) / \
                (1 + 0.001*(x**2 + y**2))**2
    return resultado
def seleccionar_schaffer_n2_function():
    global inicio_dom_x
    inicio_dom_x = -50
    global final_dom_x
    final_dom_x = 50
    global inicio_dom_y
    inicio_dom_y = -50
    global final_dom_y
    final_dom_y = 50

    global funcion
    funcion = schaffer_n2_function

def schaffer_n4_function(x, y):
    if x < inicio_dom_x or x > final_dom_x or y < inicio_dom_y or y > final_dom_y:
        return 1e10
    resultado = 0.5 + (math.cos(math.sin(abs(x**2 - y**2)))**2 - 0.5) / \
                (1 + 0.001*(x**2 + y**2))**2
    return resultado
def seleccionar_schaffer_n4_function():
    global inicio_dom_x
    inicio_dom_x = -50
    global final_dom_x
    final_dom_x = 50
    global inicio_dom_y
    inicio_dom_y = -50
    global final_dom_y
    final_dom_y = 50

    global funcion
    funcion = schaffer_n4_function

def styblinski_tang_function(x, y):
    if x < inicio_dom_x or x > final_dom_x or y < inicio_dom_y or y > final_dom_y:
        return 1e10
    resultado = (x**4 - 16*x**2 + 5*x + y**4 - 16*y**2 + 5*y) / 2
    return resultado
def seleccionar_styblinski_tang_function():
    global inicio_dom_x
    inicio_dom_x = -5
    global final_dom_x
    final_dom_x = 5
    global inicio_dom_y
    inicio_dom_y = -5
    global final_dom_y
    final_dom_y = 5

    global funcion
    funcion = styblinski_tang_function




