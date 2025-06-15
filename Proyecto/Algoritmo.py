import random

import Funciones as f

# Clase de particula que representa cada partícula en el enjambre
class Particula:
    def __init__(self, x, y, vel_x, vel_y):
        self.x = x
        self.y = y
        self.vel_x = vel_x
        self.vel_y = vel_y
        self.mejor_x = x
        self.mejor_y = y
        
# Clase que representa el enjambre de partículas
class Enjambre:
    # Las variables propiedades del enjambre
    def __init__(self, num_particulas):
        self.num_particulas = num_particulas
        self.particulas = []
        self.mejor_pos_global_x = 0
        self.mejor_pos_global_y = 0

    # Función para crear el enjambre de partículas
    def crear_enjambre(self,ancho_canva,alto_canva):
        # Generamos las particulas segun ancho y alto del canvas
        # Se usa de 1 a num_particulas+1 para que tengan margen en el canvas
        for o in range(1,self.num_particulas+1): 
            for u in range(1,self.num_particulas+1):
                x = ancho_canva/(self.num_particulas+1)
                y = alto_canva/(self.num_particulas+1)
                # velocidades aleatorias al inicio
                vel_x = random.randrange(-abs(ancho_canva-0),abs(ancho_canva-0))
                vel_y = random.randrange(-abs(alto_canva-0),abs(alto_canva-0))
                self.particulas.append(Particula(o*x,u*y,vel_x,vel_y))
        # Inicializamos la mejor posicion global
        for i in range(len(self.particulas)):
            # Si la mejor posición de la partícula es mejor que la mejor 
            # posición global, actualizamos la mejor posición global
            if f.funcion(f.trans_lin_dom_x(self.particulas[i].mejor_x,
                                           0,ancho_canva),
                         f.trans_lin_dom_y(self.particulas[i].mejor_y,
                                           0,alto_canva)) < \
                         f.funcion(f.trans_lin_dom_x(self.mejor_pos_global_x,
                                                     0,ancho_canva),
                         f.trans_lin_dom_y(self.mejor_pos_global_y,
                                           0,alto_canva)):
                self.mejor_pos_global_x = self.particulas[i].mejor_x
                self.mejor_pos_global_y = self.particulas[i].mejor_y

    # Función para iterar el algoritmo PSO
    def iterar_algorimo(self,ancho_canva,alto_canva,w,pp,pg):
        # Actualizamos las velocidades y posiciones de las partículas
        for i in range(len(self.particulas)):
            ranP = random.random()
            ranG = random.random()
            self.particulas[i].vel_x = w * self.particulas[i].vel_x + \
                                       pp*ranP*(self.particulas[i].mejor_x - \
                                       self.particulas[i].x) + \
                                       pg*ranG*(self.mejor_pos_global_x - \
                                       self.particulas[i].x)
        for i in range(len(self.particulas)):
            ranP = random.random()
            ranG = random.random()
            self.particulas[i].vel_y = w * self.particulas[i].vel_y + \
                                       pp*ranP*(self.particulas[i].mejor_y - \
                                       self.particulas[i].y) + \
                                       pg*ranG*(self.mejor_pos_global_y - \
                                       self.particulas[i].y)
        
        # Actualizamos las posiciones de las partículas sumando 
        # a la posición actual la velocidad
        for i in range(len(self.particulas)):
            self.particulas[i].x = self.particulas[i].x + \
                                   self.particulas[i].vel_x
            self.particulas[i].y = self.particulas[i].y + \
                                   self.particulas[i].vel_y
        # Verificamos si alguna partícula ha encontrado una mejor posición
        for i in range(len(self.particulas)):
            if f.funcion(f.trans_lin_dom_x(self.particulas[i].x,0,ancho_canva),
                         f.trans_lin_dom_y(self.particulas[i].y,0,alto_canva))<\
               f.funcion(f.trans_lin_dom_x(self.particulas[i].mejor_x,
                                           0,ancho_canva),
                         f.trans_lin_dom_y(self.particulas[i].mejor_y,
                                           0,alto_canva)):
                self.particulas[i].mejor_x = self.particulas[i].x
                self.particulas[i].mejor_y = self.particulas[i].y
                # Actualizamos la mejor posición global si es necesario
                if f.funcion(f.trans_lin_dom_x(self.particulas[i].mejor_x,
                                               0,ancho_canva),
                             f.trans_lin_dom_y(self.particulas[i].mejor_y,
                                               0,alto_canva)) < \
                   f.funcion(f.trans_lin_dom_x(self.mejor_pos_global_x,
                                               0,ancho_canva),
                             f.trans_lin_dom_y(self.mejor_pos_global_y,
                                               0,alto_canva)):
                    self.mejor_pos_global_x = self.particulas[i].mejor_x
                    self.mejor_pos_global_y = self.particulas[i].mejor_y
        # Imprimimos las coordenadas de la mejor posición global 
        # en coordenadas del canvas y en coordenadas de la función
        print("Coords Canva: ",
              format(self.mejor_pos_global_x,".9f"),
              format(self.mejor_pos_global_y,".9f"))
        print("Coords: ",
              format(f.trans_lin_dom_x(self.mejor_pos_global_x,0,ancho_canva),
                     ".9f"),
              format(f.trans_lin_dom_y(self.mejor_pos_global_y,0,alto_canva),
                     ".9f"))
        # Devolvemos las velocidades de las partículas
        return [p.vel_x for p in self.particulas], \
               [p.vel_y for p in self.particulas]


