#Importaciones necesarias
import math

# Definimos las variables necesarias para las funciones
inicio_dom_x = 0
final_dom_x = 0
inicio_dom_y = 0
final_dom_y = 0

inicio_rango = 0
final_rango = 0

funcion = None

def trans_lin_dom_x(x, a, b):
    respuesta = (x-a)*((final_dom_x-inicio_dom_x)/(b-a))+ inicio_dom_x
    return respuesta
def trans_lin_dom_y(x, a, b):
    respuesta = (x-a)*((final_dom_y-inicio_dom_y)/(b-a))+ inicio_dom_y
    return respuesta

# Definimos las funciones matematicas que vamos a usar

# Cada funcion tiene su dominio y rango, 
# que se definen en las funciones de seleccion
def ackley_function(x, y):
    if x < inicio_dom_x or x > final_dom_x or y < inicio_dom_y or y > final_dom_y:
        return final_rango
    resultado = -20*math.exp(-0.2*(0.5*(x**2+y**2)**0.5)) \
        -math.exp(0.5*(math.cos(2*math.pi*x)+math.cos(2*math.pi*y))) \
        +math.e+20
    return round(resultado,5)
def seleccionar_ackley_function():
    global inicio_dom_x
    inicio_dom_x = -5
    global final_dom_x
    final_dom_x = 5
    global inicio_dom_y
    inicio_dom_y = -5
    global final_dom_y
    final_dom_y = 5 

    global inicio_rango
    inicio_rango = 0
    global final_rango
    final_rango = 15

    global funcion
    funcion = ackley_function

def mc_cormick_function(x, y):
    if x < inicio_dom_x or x > final_dom_x or y < inicio_dom_y or y > final_dom_y:
        return final_rango
    resultado = (math.sin(x+y)) + (x-y)**2 - 1.5*x + 2.5*y + 1
    return round(resultado,5)
def seleccionar_mc_cormick_function():
    global inicio_dom_x
    inicio_dom_x = -1.5
    global final_dom_x
    final_dom_x = 4
    global inicio_dom_y
    inicio_dom_y = -3
    global final_dom_y
    final_dom_y = 4

    global inicio_rango
    inicio_rango = -2
    global final_rango
    final_rango = 45

    global funcion
    funcion = mc_cormick_function

def bukin_n6_function(x, y):
    if x < inicio_dom_x or x > final_dom_x or y < inicio_dom_y or y > final_dom_y:
        return final_rango
    resultado = 100*(abs(y-0.01*x**2))**0.5+0.01*abs(x+10)
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

    global inicio_rango
    inicio_rango = 0
    global final_rango
    final_rango = 260

    global funcion
    funcion = bukin_n6_function

def levi_n13_function(x, y):
    if x < inicio_dom_x or x > final_dom_x or y < inicio_dom_y or y > final_dom_y:
        return final_rango
    resultado = (math.sin(3*math.pi*x))**2 + (x-1)**2 * \
                (1 + (math.sin(3*math.pi*y)**2)) + (y-1)**2 * \
                (1+(math.sin(2*math.pi*y)**2))
    return round(resultado,5)
def seleccionar_levi_n13_function():
    global inicio_dom_x
    inicio_dom_x = -10
    global final_dom_x
    final_dom_x = 10
    global inicio_dom_y
    inicio_dom_y = -10
    global final_dom_y
    final_dom_y = 10

    global inicio_rango
    inicio_rango = 0
    global final_rango
    final_rango = 460

    global funcion
    funcion = levi_n13_function

def easom_function(x, y):
    if x < inicio_dom_x or x > final_dom_x or y < inicio_dom_y or y > final_dom_y:
        return final_rango
    resultado = -math.cos(x)*math.cos(y)* \
                 math.exp(-((x-math.pi)**2+(y-math.pi)**2))
    return round(resultado,5)
def seleccionar_easom_function():
    global inicio_dom_x
    inicio_dom_x = -1
    global final_dom_x
    final_dom_x = 7
    global inicio_dom_y
    inicio_dom_y = -1
    global final_dom_y
    final_dom_y = 7

    global inicio_rango
    inicio_rango = -1
    global final_rango
    final_rango = 0.1

    global funcion
    funcion = easom_function

def rastrigin_function(x, y):
    if x < inicio_dom_x or x > final_dom_x or y < inicio_dom_y or y > final_dom_y:
        return final_rango
    resultado = 10*2 + (x**2 - 10*math.cos(2*math.pi*x)) + \
                (y**2 - 10*math.cos(2*math.pi*y))
    return round(resultado,5)
def seleccionar_rastrigin_function():
    global inicio_dom_x
    inicio_dom_x = -5.12
    global final_dom_x
    final_dom_x = 5.12
    global inicio_dom_y
    inicio_dom_y = -5.12
    global final_dom_y
    final_dom_y = 5.12

    global inicio_rango
    inicio_rango = 0
    global final_rango
    final_rango = 85

    global funcion
    funcion = rastrigin_function

def sphere_function(x, y):
    if x < inicio_dom_x or x > final_dom_x or y < inicio_dom_y or y > final_dom_y:
        return final_rango
    resultado = (x**2 + y**2)
    return round(resultado,5)
def seleccionar_sphere_function():
    global inicio_dom_x
    inicio_dom_x = -2
    global final_dom_x
    final_dom_x = 2
    global inicio_dom_y
    inicio_dom_y = -2
    global final_dom_y
    final_dom_y = 2

    global inicio_rango
    inicio_rango = 0
    global final_rango
    final_rango = 9

    global funcion
    funcion = sphere_function

def griewank_function(x, y):
    if x < inicio_dom_x or x > final_dom_x or y < inicio_dom_y or y > final_dom_y:
        return final_rango
    resultado = 1 + 1/4000 * (x**2 + y**2) - (math.cos(x) * math.cos(y/2**0.5))
    return round(resultado,5)
def seleccionar_griewank_function():
    global inicio_dom_x
    inicio_dom_x = -10
    global final_dom_x
    final_dom_x = 10
    global inicio_dom_y
    inicio_dom_y = -10
    global final_dom_y
    final_dom_y = 10

    global inicio_rango
    inicio_rango = 0
    global final_rango
    final_rango = 2.1

    global funcion
    funcion = griewank_function

def cross_in_tray_function(x, y):
    if x < inicio_dom_x or x > final_dom_x or y < inicio_dom_y or y > final_dom_y:
        return final_rango
    resultado = -0.0001 * (abs(math.sin(x)*math.sin(y)* \
                               math.exp(abs(100-((x**2+y**2) \
                               **0.5)/math.pi))) + 1)**0.1
    return round(resultado,5)
def seleccionar_cross_in_tray_function():
    global inicio_dom_x
    inicio_dom_x = -10
    global final_dom_x
    final_dom_x = 10
    global inicio_dom_y
    inicio_dom_y = -10
    global final_dom_y
    final_dom_y = 10

    global inicio_rango
    inicio_rango = -2.1
    global final_rango
    final_rango = 0.5

    global funcion
    funcion = cross_in_tray_function

def egg_holder_function(x, y):
    if x < inicio_dom_x or x > final_dom_x or y < inicio_dom_y or y > final_dom_y:
        return final_rango
    resultado = -(y+47)*math.sin((abs(x/2+(y+47)))**0.5)- \
                x*math.sin((abs(x-(y+47)))**0.5)
    return round(resultado,5)
def seleccionar_egg_holder_function():
    global inicio_dom_x
    inicio_dom_x = -512
    global final_dom_x
    final_dom_x = 512
    global inicio_dom_y
    inicio_dom_y = -512
    global final_dom_y
    final_dom_y = 512

    global inicio_rango
    inicio_rango = -2000
    global final_rango
    final_rango = 2000

    global funcion
    funcion = egg_holder_function

def holder_table_function(x, y):
    if x < inicio_dom_x or x > final_dom_x or y < inicio_dom_y or y > final_dom_y:
        return final_rango
    resultado = -abs(math.sin(x)*math.cos(y)*math.exp( \
                     abs(1-((x**2+y**2)**0.5)/math.pi)))
    return round(resultado,5)
def seleccionar_holder_table_function():
    global inicio_dom_x
    inicio_dom_x = -10
    global final_dom_x
    final_dom_x = 10
    global inicio_dom_y
    inicio_dom_y = -10
    global final_dom_y
    final_dom_y = 10

    global inicio_rango
    inicio_rango = -20
    global final_rango
    final_rango = 0.5

    global funcion
    funcion = holder_table_function
