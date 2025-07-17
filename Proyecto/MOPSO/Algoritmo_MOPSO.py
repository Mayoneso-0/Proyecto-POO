import random
import Funciones_MOPSO as f

def domina(objetivo1: tuple, objetivo2: tuple) -> bool:
    """Verifica si el objetivo1 domina al objetivo2."""
    es_mejor_o_igual = all(a <= b for a, b in zip(objetivo1, objetivo2))
    es_estrictamente_mejor = any(a < b for a, b in zip(objetivo1, objetivo2))
    
    return es_mejor_o_igual and es_estrictamente_mejor

class Particula:
    """Clase que representa cada partícula en el enjambre."""
    def __init__(self, x, y, vel_x, vel_y):
        self.x = x
        self.y = y
        self.vel_x = vel_x
        self.vel_y = vel_y
        self.mejor_x = x
        self.mejor_y = y
        self.mejores_individuales = (float('inf'), float('inf'))

class Enjambre:
    """Clase que representa el enjambre de partículas."""
    def __init__(self, num_particulas):
        # El número de partículas será num_particulas * num_particulas
        self.num_particulas = num_particulas
        self.particulas = []
        self.lideres = []

    def crear_enjambre(self, ancho_canva, alto_canva):
        """Genera las partículas en una grilla inicial."""
        # Se crean num_particulas * num_particulas partículas en total
        for o in range(1, self.num_particulas + 1): 
            for u in range(1, self.num_particulas + 1):
                x = ancho_canva / (self.num_particulas + 1) * o
                y = alto_canva / (self.num_particulas + 1) * u
                vel_x = random.uniform(-ancho_canva/10, ancho_canva/10)
                vel_y = random.uniform(-alto_canva/10, alto_canva/10)
                self.particulas.append(Particula(x, y, vel_x, vel_y))
    
    def actualizar_lideres(self, x_particula, y_particula, objetivos_particula):
        """Actualiza el archivo de líderes (frente de Pareto)."""
        es_dominada = False
        for _, _, objetivos_lider in self.lideres:
            if domina(objetivos_lider, objetivos_particula):
                es_dominada = True
                break
        if es_dominada:
            return
        
        # Elimina líderes que son dominados por la nueva partícula
        self.lideres = [(lx, ly, l_obj) for lx, ly, l_obj in self.lideres 
                        if not domina(objetivos_particula, l_obj)]
        # Agrega la nueva partícula a los líderes
        self.lideres.append((x_particula, y_particula, objetivos_particula))
    
    def iterar_algoritmo(self, ancho_canva, alto_canva, w, pp, pg):
        velocidades_calculadas_x = []
        velocidades_calculadas_y = []

        for p in self.particulas:
            # Mapear la posición de la partícula al dominio del problema
            x_dominio = f.map_to_domain_x(p.x, ancho_canva)
            y_dominio = f.map_to_domain_y(p.y, alto_canva)

            # Verificar restricciones y calcular objetivos
            if f.constraints_func(x_dominio, y_dominio):
                objetivos_actuales = f.objectives_func(x_dominio, y_dominio)

                if domina(objetivos_actuales, p.mejores_individuales):
                    p.mejores_individuales = objetivos_actuales
                    p.mejor_x = p.x
                    p.mejor_y = p.y
                
                # Actualizar el archivo de líderes globales con la posición actual
                self.actualizar_lideres(p.x, p.y, objetivos_actuales)

        for p in self.particulas:
            if not self.lideres:
                lider_x, lider_y = p.mejor_x, p.mejor_y
            else:
                # Seleccionar un líder aleatorio del frente de Pareto
                lider_x, lider_y, _ = random.choice(self.lideres)

            # Ecuaciones de velocidad de PSO
            ranP = random.random()
            ranG = random.random()
            p.vel_x = w * p.vel_x + pp * ranP * (p.mejor_x - p.x) + pg * ranG * (lider_x - p.x)
            p.vel_y = w * p.vel_y + pp * ranP * (p.mejor_y - p.y)
            
            # Actualizar posición
            p.x += p.vel_x
            p.y += p.vel_y
            
            velocidades_calculadas_x.append(p.vel_x)
            velocidades_calculadas_y.append(p.vel_y)
            
        return velocidades_calculadas_x, velocidades_calculadas_y
