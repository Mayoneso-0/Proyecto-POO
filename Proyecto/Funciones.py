#Importaciones necesarias
import math

# Definimos las variables necesarias para las funciones
InicioDomX = 0
FinalDomX = 0
InicioDomY = 0
FinalDomY = 0

InicioRango = 0
FinalRango = 0

Funcion = None


# Definimos las funciones matematicas que vamos a usar
# Cada funcion tiene su dominio y rango, que se definen en las funciones de seleccion
def ackleyFunction(x, y):
    resultado = -20*math.exp(-0.2*(0.5*(x**2+y**2)**0.5)) \
        -math.exp(0.5*(math.cos(2*math.pi*x)+math.cos(2*math.pi*y))) \
        +math.e+20
    return round(resultado,5)
def seleccionarAckleyFunction():
    global InicioDomX
    InicioDomX = -5
    global FinalDomX
    FinalDomX = 5
    global InicioDomY
    InicioDomY = -5
    global FinalDomY
    FinalDomY = 5 

    global InicioRango
    InicioRango = 0
    global FinalRango
    FinalRango = 15

    global Funcion
    Funcion = ackleyFunction

def mcCormickFunction(x, y):
    resultado = (math.sin(x+y)) + (x-y)**2 - 1.5*x + 2.5*y + 1
    return round(resultado,5)
def seleccionarMcCormickFunction():
    global InicioDomX
    InicioDomX = -1.5
    global FinalDomX
    FinalDomX = 4
    global InicioDomY
    InicioDomY = -3
    global FinalDomY
    FinalDomY = 4

    global InicioRango
    InicioRango = -2
    global FinalRango
    FinalRango = 45

    global Funcion
    Funcion = mcCormickFunction

def bukinN6Function(x, y):
    resultado = 100*(abs(y-0.01*x**2))**0.5+0.01*abs(x+10)
    return resultado
def seleccionarBukinN6Function():
    global InicioDomX
    InicioDomX = -15
    global FinalDomX
    FinalDomX = -5
    global InicioDomY
    InicioDomY = -4
    global FinalDomY
    FinalDomY = 6

    global InicioRango
    InicioRango = 0
    global FinalRango
    FinalRango = 260

    global Funcion
    Funcion = bukinN6Function

def leviN13Function(x, y):
    resultado = (math.sin(3*math.pi*x))**2 + (x-1)**2 * (1 + (math.sin(3*math.pi*y)**2)) + (y-1)**2 * (1+(math.sin(2*math.pi*y)**2))
    return round(resultado,5)
def seleccionarLeviN13Function():
    global InicioDomX
    InicioDomX = -10
    global FinalDomX
    FinalDomX = 10
    global InicioDomY
    InicioDomY = -10
    global FinalDomY
    FinalDomY = 10

    global InicioRango
    InicioRango = 0
    global FinalRango
    FinalRango = 460

    global Funcion
    Funcion = leviN13Function

def easomFunction(x, y):
    resultado = -math.cos(x)*math.cos(y)*math.exp(-((x-math.pi)**2+(y-math.pi)**2))
    return round(resultado,5)
def seleccionarEasomFunction():
    global InicioDomX
    InicioDomX = -1
    global FinalDomX
    FinalDomX = 7
    global InicioDomY
    InicioDomY = -1
    global FinalDomY
    FinalDomY = 7

    global InicioRango
    InicioRango = -1
    global FinalRango
    FinalRango = 0.1

    global Funcion
    Funcion = easomFunction

def rastriginFunction(x, y):
    resultado = 10*2 + (x**2 - 10*math.cos(2*math.pi*x)) + (y**2 - 10*math.cos(2*math.pi*y))
    return round(resultado,5)
def seleccionarRastriginFunction():
    global InicioDomX
    InicioDomX = -5.12
    global FinalDomX
    FinalDomX = 5.12
    global InicioDomY
    InicioDomY = -5.12
    global FinalDomY
    FinalDomY = 5.12

    global InicioRango
    InicioRango = 0
    global FinalRango
    FinalRango = 85

    global Funcion
    Funcion = rastriginFunction

def sphereFunction(x, y):
    resultado = (x**2 + y**2)
    return round(resultado,5)
def seleccionarSphereFunction():
    global InicioDomX
    InicioDomX = -2
    global FinalDomX
    FinalDomX = 2
    global InicioDomY
    InicioDomY = -2
    global FinalDomY
    FinalDomY = 2

    global InicioRango
    InicioRango = 0
    global FinalRango
    FinalRango = 9

    global Funcion
    Funcion = sphereFunction

def griewankFunction(x, y):
    resultado = 1 + 1/4000 * (x**2 + y**2) - (math.cos(x) * math.cos(y/2**0.5))
    return round(resultado,5)
def seleccionarGriewankFunction():
    global InicioDomX
    InicioDomX = -10
    global FinalDomX
    FinalDomX = 10
    global InicioDomY
    InicioDomY = -10
    global FinalDomY
    FinalDomY = 10

    global InicioRango
    InicioRango = 0
    global FinalRango
    FinalRango = 2.1

    global Funcion
    Funcion = griewankFunction

def crossInTrayFunction(x, y):
    resultado = -0.0001 * (abs(math.sin(x)*math.sin(y)*math.exp(abs(100-((x**2+y**2)**0.5)/math.pi))) + 1)**0.1
    return round(resultado,5)
def seleccionarCrossInTrayFunction():
    global InicioDomX
    InicioDomX = -10
    global FinalDomX
    FinalDomX = 10
    global InicioDomY
    InicioDomY = -10
    global FinalDomY
    FinalDomY = 10

    global InicioRango
    InicioRango = -2.1
    global FinalRango
    FinalRango = 0.5

    global Funcion
    Funcion = crossInTrayFunction

def eggHolderFunction(x, y):
    resultado = -(y+47)*math.sin((abs(x/2+(y+47)))**0.5)-x*math.sin((abs(x-(y+47)))**0.5)
    return round(resultado,5)
def seleccionarEggHolderFunction():
    global InicioDomX
    InicioDomX = -1000
    global FinalDomX
    FinalDomX = 1000
    global InicioDomY
    InicioDomY = -1000
    global FinalDomY
    FinalDomY = 1000

    global InicioRango
    InicioRango = -2000
    global FinalRango
    FinalRango = 2000

    global Funcion
    Funcion = eggHolderFunction

def holderTableFunction(x, y):
    resultado = -abs(math.sin(x)*math.cos(y)*math.exp(abs(1-((x**2+y**2)**0.5)/math.pi)))
    return round(resultado,5)
def seleccionarHolderTableFunction():
    global InicioDomX
    InicioDomX = -10
    global FinalDomX
    FinalDomX = 10
    global InicioDomY
    InicioDomY = -10
    global FinalDomY
    FinalDomY = 10

    global InicioRango
    InicioRango = -20
    global FinalRango
    FinalRango = 0.5

    global Funcion
    Funcion = holderTableFunction
