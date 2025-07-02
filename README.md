Este proyecto implementa un algoritmo de optimización por enjambre de partículas (PSO) con una interfaz gráfica en Tkinter para visualizar el comportamiento de las partículas sobre funciones matemáticas clásicas de benchmark.

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
