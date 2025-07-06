import random

import Funciones_MOPSO as f

def domina(objetivo1: float, objetivo2: float) -> bool:
    es_mejor_o_igual = all(a <= b for a, b in zip(objetivo1, objetivo2))
    es_estrictamente_mejor = any(a < b for a, b in zip(objetivo1, objetivo2))
    
    return es_mejor_o_igual and es_estrictamente_mejor

# Clase de particula que representa cada partícula en el enjambre
class Particula:
    def __init__(self, x, y, vel_x, vel_y):
        self.x = x
        self.y = y
        self.vel_x = vel_x
        self.vel_y = vel_y
        self.mejor_x = x
        self.mejor_y = y
        # Mejor individual (f1, f2)
        self.mejores_individuales = (float('inf'), float('inf'))

        
# Clase que representa el enjambre de partículas
class Enjambre:
    # Las variables propiedades del enjambre
    def __init__(self, num_particulas):
        self.num_particulas = num_particulas
        self.particulas = []
        self.lideres = []

    def crear_enjambre(self, ancho_canva, alto_canva):
        # Generamos las particulas segun ancho y alto del canvas
        # Se usa de 1 a num_particulas+1 para que tengan margen en el canvas
        for o in range(1, self.num_particulas + 1): 
            for u in range(1, self.num_particulas + 1):
                x = ancho_canva / (self.num_particulas + 1)
                y = alto_canva / (self.num_particulas + 1)
                # velocidades aleatorias al inicio
                vel_x = random.uniform(-abs(ancho_canva - 0), abs(ancho_canva - 0))
                vel_y = random.uniform(-abs(alto_canva - 0), abs(alto_canva - 0))
                self.particulas.append(Particula(o * x, u * y, vel_x, vel_y))
    
    def actualizar_lideres(self, x_particula, y_particula, objetivos_particula):
        es_dominada = False
        for _, _, objetivos_lider in self.lideres:
            if domina(objetivos_lider, objetivos_particula):
                es_dominada = True
                break
        if es_dominada:
                return
        self.lideres = [(lx, ly, l_obj) for lx, ly, l_obj in self.lideres 
            if not domina(objetivos_particula, l_obj)]
        self.lideres.append((x_particula, y_particula, objetivos_particula))
    
    def iterar_algorimo(self, ancho_canva, alto_canva, w, pp, pg):
        for p in self.particulas:
            #Mapear la posición de la partícula al dominio del problema
            x_dominio = f.map_to_domain_x(p.x, ancho_canva)
            y_dominio = f.map_to_domain_y(p.y, alto_canva)

            #Verificar restricciones y calcular objetivos
            if f.constraints_func(x_dominio, y_dominio):
                objetivos_actuales = f.objectives_func(x_dominio, y_dominio)

                #Actualizar el mejor individual usando dominancia
                if domina(objetivos_actuales, p.mejores_objetivos_personales):
                    p.mejores_individuales = objetivos_actuales
                    p.mejor_x = p.x
                    p.mejor_y = p.y
                
                # Actualizar el archivo de líderes globales con la posición actual
                self.actualizar_lideres(p.x, p.y, objetivos_actuales)

        for p in self.particulas:
        #Si no hay líderes, la partícula se mueve solo por su inercia y pbest
            if not self.lideres:
                lider_x, lider_y = p.mejor_x, p.mejor_y
            else:
                lider_x, lider_y, _ = random.choice(self.lideres)

            #Ecuaciones de velocidad
            ranP = random.random()
            ranG = random.random()
            p.vel_x = w * p.vel_x + pp * ranP * (p.mejor_x - p.x) + pg * ranG * (lider_x - p.x)
            p.vel_y = w * p.vel_y + pp * ranP * (p.mejor_y - p.y) + pg * ranG * (lider_y - p.y)
            # Actualizar posición
            p.x += p.vel_x
            p.y += p.vel_y
            
        return [p.vel_x for p in self.particulas], [p.vel_y for p in self.particulas]
    