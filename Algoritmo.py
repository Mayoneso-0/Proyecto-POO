import random

import Funciones as f

class Particula:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
class Enjambre:
    def __init__(self, num_particulas):
        self.num_particulas = num_particulas
        self.particulas = []
        self.vel_x_particulas = []
        self.vel_y_particulas = []
        self.mejor_pos_particula = []
        self.mejor_pos_global_x = 4
        self.mejor_pos_global_y = 4

    def crear_enjambre(self,ancho_canva,alto_canva):
        for o in range(1,self.num_particulas+1):
            for u in range(1,self.num_particulas+1):
                x = ancho_canva/(self.num_particulas+1)
                y = alto_canva/(self.num_particulas+1)
                self.particulas.append(Particula(o*x,u*y))
        for i in range(0,len(self.particulas)):
            self.mejor_pos_particula.append(Particula(self.particulas[i].x,self.particulas[i].y))
        
        for i in range(0,len(self.mejor_pos_particula)):
            if f.Funcion(f.transformarLineaADomX(self.mejor_pos_particula[i].x,0,ancho_canva),
                         f.transformarLineaADomY(self.mejor_pos_particula[i].y,0,alto_canva))\
                         < f.Funcion(f.transformarLineaADomY(self.mejor_pos_global_x,0,ancho_canva),
                                     f.transformarLineaADomY(self.mejor_pos_global_y,0,alto_canva)):
                self.mejor_pos_global_x = self.mejor_pos_particula[i].x
                self.mejor_pos_global_y = self.mejor_pos_particula[i].y
        for i in self.particulas:
            self.vel_x_particulas.append(random.randrange(-abs(ancho_canva-0),abs(ancho_canva-0)))
            self.vel_y_particulas.append(random.randrange(-abs(alto_canva-0),abs(alto_canva-0)))          

    def iterar_algorimo(self,ancho_canva,alto_canva,w,pp,pg):
        self.vel_x_particulas_tempo = []
        self.vel_y_particulas_tempo = []
        for i in range(0,len(self.particulas)):
            ranP = random.random()
            ranG = random.random()
            self.vel_x_particulas_tempo.append(w * self.vel_x_particulas[i] + pp*ranP*(self.mejor_pos_particula[i].x - self.particulas[i].x) + pg*ranG*(self.mejor_pos_global_x - self.particulas[i].x))
        for i in range(0,len(self.particulas)):
            ranP = random.random()
            ranG = random.random()
            self.vel_y_particulas_tempo.append(w * self.vel_y_particulas[i] + pp*ranP*(self.mejor_pos_particula[i].y - self.particulas[i].y) + pg*ranG*(self.mejor_pos_global_y - self.particulas[i].y))
        
        self.vel_x_particulas = []
        self.vel_y_particulas = []
        for i in range(0,len(self.vel_x_particulas_tempo)):
            self.vel_x_particulas.append(self.vel_x_particulas_tempo[i])
        for i in range(0,len(self.vel_y_particulas_tempo)):
            self.vel_y_particulas.append(self.vel_y_particulas_tempo[i])
        
        for i in range(0,len(self.particulas)):
            self.particulas[i].x = self.particulas[i].x + self.vel_x_particulas[i]
            self.particulas[i].y = self.particulas[i].y + self.vel_y_particulas[i]
        for i in range(0,len(self.particulas)):
            if f.Funcion(f.transformarLineaADomX(self.particulas[i].x,0,ancho_canva),f.transformarLineaADomY(self.particulas[i].y,0,alto_canva)) < f.Funcion(f.transformarLineaADomX(self.mejor_pos_particula[i].x,0,ancho_canva),f.transformarLineaADomY(self.mejor_pos_particula[i].y,0,alto_canva)):
                self.mejor_pos_particula[i].x = self.particulas[i].x
                self.mejor_pos_particula[i].y = self.particulas[i].y
                if f.Funcion(f.transformarLineaADomX(self.mejor_pos_particula[i].x,0,ancho_canva),f.transformarLineaADomY(self.mejor_pos_particula[i].y,0,alto_canva)) < f.Funcion(f.transformarLineaADomX(self.mejor_pos_global_x,0,ancho_canva), f.transformarLineaADomY(self.mejor_pos_global_y,0,alto_canva)):
                    self.mejor_pos_global_x = self.mejor_pos_particula[i].x
                    self.mejor_pos_global_y = self.mejor_pos_particula[i].y
        print("Coords Canva: ",self.mejor_pos_global_x,self.mejor_pos_global_y)
        print("Coords: ", f.transformarLineaADomX(self.mejor_pos_global_x,0,ancho_canva),f.transformarLineaADomY(self.mejor_pos_global_y,0,alto_canva))
        return self.vel_x_particulas, self.vel_y_particulas


