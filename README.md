# <h1 align="center">Particle Swarm Optimization (PSO) - Pyhton - POO</h1>
## By Aleph-Zero (ℵ₀)

## 📂 ¿Qué es?

Este proyecto implementa un algoritmo de Optimización por Enjambre de Partículas (PSO) con una interfaz gráfica en Tkinter y Matplotlib para visualizar el comportamiento de las partículas sobre funciones matemáticas clásicas de benchmark.

---

## 📊 Implementación

## 🧩 Requisitos previos

- Versión mínima requerida: Python 3.7.
- Versión recomendada: Python 3.9.

Además, para la visualización de las funciones es necesario instalar
- Colour
- Matplotlib
- Numpy

## 🎮 Funcionamiento 

1. El programa se ejecuta desde 
```cmd
Proyecto/main.py
```
2. Desde la ventana principal se escoge el tipo de optimización, la función, la configuración de la gráfica y los ajustes iniciales del algoritmo.
<img width="1002" height="532" alt="image" src="https://github.com/user-attachments/assets/6e14b5f5-358a-408d-9abd-983a43b7ca2f" />








El main es graficadora y la librería colour es necesaria para manejar la paleta de colores. El comando está comentado en el código de Graficadora.py.
Luego, dentro de la interfaz gráfica selecciona la función deseada  modificando manualmente en el código:
self.funcion = seleccionarAckleyFunction()
Por ahora hay 11 funciones para implementar, las opciones son de esta wiki: https://en.wikipedia.org/wiki/Test_functions_for_optimization.

Teclas asociadas:
      q → iniciar_enjambre()
      w → iterar_algoritmo()
      e → finalizar_algoritmo()
```mermaid
classDiagram
    class Particula {
        -x: float
        -y: float
        -vel_x: float
        -vel_y: float
        -mejor_x: float
        -mejor_y: float
    }

    class Enjambre {
        -num_particulas: int
        -particulas: list
        -mejor_pos_global_x: float
        -mejor_pos_global_y: float
        +crear_enjambre(ancho, alto)
        +iterar_algorimo(ancho, alto, w, pp, pg)
    }

    Enjambre "1" --> "n" Particula

    class Funciones {
        +trans_lin_dom_x(x, a, b)
        +trans_lin_dom_y(x, a, b)
        +funcion(x, y)
        +seleccionar_*()
    }

    Enjambre ..> Funciones : utiliza

    class Ackley
    class McCormick
    class BukinN6
    class LeviN13
    class Easom
    class Rastrigin
    class Sphere
    class Griewank
    class CrossInTray
    class EggHolder
    class HolderTable

    Funciones --> Ackley
    Funciones --> McCormick
    Funciones --> BukinN6
    Funciones --> LeviN13
    Funciones --> Easom
    Funciones --> Rastrigin
    Funciones --> Sphere
    Funciones --> Griewank
    Funciones --> CrossInTray
    Funciones --> EggHolder
    Funciones --> HolderTable

    class Graficadora {
    - canvas: Canvas
    - color: Color
    - window: Tk
    + iniciar_enjambre() 
    + iterar_algoritmo() <w>
    + finalizar_algoritmo() <e>

    }

    Graficadora ..> Enjambre : instancia y usa
    Graficadora ..> Funciones : selecciona función
```
