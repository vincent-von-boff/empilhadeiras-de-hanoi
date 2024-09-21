import pygame as pg
import math
import numpy as np
from pygame import gfxdraw
import config


class Empilhadeira():
    def __init__(self):
        
        # Carrega as imagens
        self.corpo = pg.image.load("Imagens/corpo_empilhadeira_crop.png")
        self.garfo = pg.image.load("Imagens/garfo_crop.png")


        # Calcula escala da emp relativa ao cenario
        larg_corpo = self.corpo.get_width() # largura imagem do corpo em pixels
        print("larg: ", larg_corpo)
        lar_corpo_original = (larg_corpo * config.altura_cenario) / config.resolucao[1]  #Tamanho em metros co corpo antes da escala
        self.escala = config.largura_empilhadeira / lar_corpo_original
        #self.escala = 0.7


        # Posições relativas das partes da empilhadeira, o topo esquerdo da emp representa (0,0)
        # Lembrando que x aumenta da esquerda para a direita e y aumenta de cima para baixo.
        #self.garfo_dif = (310*self.escala,179*self.escala)  # representa base esquerda (bottom left)
        #self.garfo_dif = [310, 179]  # representa base esquerda (bottom left)
        self.garfo_dif = [0, 178]  # representa base esquerda (bottom left)
        self.garfo_dif = [self.escala * i for i in self.garfo_dif]  # representa base esquerda (bottom left)
        self.roda_frente_dif = (-250*self.escala,234*self.escala) # representa o centro
        self.roda_traseira_dif = (-43*self.escala, 244*self.escala) # centro
        self.raio_roda_frente = 48*self.escala
        self.raio_roda_traseira = 40*self.escala

        self.torre_dif = (np.array([131,147]) - np.array([133,155]))

        # Aplica transformação de escala
        self.corpo = pg.transform.scale_by(self.corpo, self.escala) #0.8
        #print(self.corpo.get_width()/larg_corpo)
        self.garfo = pg.transform.scale_by(self.garfo, self.escala)

        # Reflete a imagem ao redor do eixo vertical
        #self.corpo = pg.transform.flip(self.corpo, True, False)
        #self.garfo = pg.transform.flip(self.garfo, True, False)


        # TO DO: deal with this
        self.rot = 0

    def escalar(self, escala):
        for i in []:
            pass

    def blit(self, tela, posicao, posicao_garfo, velocidade):
        pos = np.array([posicao[0], posicao[1]+0.80*config.resolucao[1] - self.corpo.get_height()])
        pg.draw.aaline(tela, (0,0,0), (0,0.68*config.resolucao[1]+self.corpo.get_height()+6),
                       (config.resolucao[0], config.resolucao[1]*0.68+self.corpo.get_height()+20))
        self.rot = velocidade
        tela.blit(self.corpo, pos)
        recta = pg.Rect(pos, self.corpo.get_size())
        pg.draw.rect(tela,(0,0,0), recta, width=1)
        tela.blit(self.garfo, pos - [0, posicao_garfo] - [self.garfo.get_width(),0 ]+ self.garfo_dif)
        print(-self.garfo.get_width()/(self.corpo.get_width()))
        print(self.garfo.get_height()/self.corpo.get_height())
        #print(self.corpo.get_size())
        # Numeros abaixo relativos ao tamanho (310,270) do corpo (original)
        pos_rodaf_x = self.roda_frente_dif[0] + self.corpo.get_width() # 60
        pos_rodaf_y = self.roda_frente_dif[1] # 234
        pos_rodat_x = self.roda_traseira_dif[0] + self.corpo.get_width() # 267
        pos_rodat_y = self.roda_traseira_dif[1] # 243
        #print("pos x roda frontal: ", pos_rodaf_x)
        #print("pos y roda frontal: ", pos_rodaf_y)
        #print("pos x roda traseira: ", pos_rodat_x)
        #print("pos y roda traseira: ", pos_rodat_y)
        self.draw_wheel(tela,
                   round(pos[0] + pos_rodaf_x),
                   round(pos[1] + pos_rodaf_y),
                   self.raio_roda_frente,
                   angulo=self.rot)
        self.draw_wheel(tela,
                    round(pos[0] + pos_rodat_x),
                    round(pos[1] + pos_rodat_y),
                    self.raio_roda_traseira,
                    angulo=self.rot)
        # rec = pg.Rect((500,500), (100,20))
        # rec2 = pg.Surface((40,10))
        # rec2.fill((255,0,0))
        # rec2.set_alpha(100)
        # pg.draw.rect(tela, (0,0,0), rec)
        # tela.blit(rec2, (530,505))
    
    def draw_wheel(self, tela, pos_x, pos_y, raio, angulo, cor_calota=(237,136,5)):
        # Circulo anti-alias
        #Pneu
        pg.gfxdraw.aacircle(tela, pos_x, pos_y, int((raio/50)*50), (0,0,0))
        #Calota
        pg.gfxdraw.aacircle(tela, pos_x, pos_y, int((raio/50)*30), (237,136,5))
        #Eixo central
        pg.gfxdraw.aacircle(tela, pos_x, pos_y, int(raio*(13/50)), (0,0,0))

        ## Circulo preenchido
        #Pneu
        pg.gfxdraw.filled_circle(tela, pos_x, pos_y, int((raio/50)*50), (0,0,0))
        #Calota
        pg.gfxdraw.filled_circle(tela, pos_x, pos_y, int((raio/50)*30), (237,136,5))
        #Eixe central
        pg.gfxdraw.filled_circle(tela, pos_x, pos_y, int((raio/50)*12), (0,0,0))

        #Parafusos
        numero_parafusos = 3 # Numero de parafusos por quadrantes (12 ao total)
        for id_paraf in range(4*numero_parafusos):
            rad_ang = (2*math.pi/360) * angulo
            ang_paraf = 2*math.pi/(4*numero_parafusos)
            pos_x_parafuso = round(pos_x + 17 * (raio/50) * math.cos(id_paraf*ang_paraf + rad_ang))
            pos_x_parafuso2 = round(pos_x + 2*17 * (raio/50) * math.cos(id_paraf*ang_paraf + rad_ang))
            pos_y_parafuso = round(pos_y + 17 * (raio/50) * math.sin(id_paraf*ang_paraf + rad_ang))
            pos_y_parafuso2 = round(pos_y + 2*17 * (raio/50) * math.sin(id_paraf*ang_paraf + rad_ang))
            raio_parafuso = int(raio*(2/50))
            pg.gfxdraw.aacircle(tela, pos_x_parafuso, pos_y_parafuso, raio_parafuso, (0,0,0))
            pg.gfxdraw.filled_circle(tela, pos_x_parafuso, pos_y_parafuso, raio_parafuso, (0,0,0))
            # if (id_paraf % numero_parafusos == 0):
                # pg.draw.aaline(tela, (0,0,0), (pos_x, pos_y), (pos_x_parafuso2, pos_y_parafuso2))

class Caixa:
    def __init__(self, peso):
        # Carrega imagem da caixa
        self.imagem = pg.image.load("Imagens/caixa2.png")

        # Peso para calcular ordem das caixas
        self.peso = peso

        self.posicao = (0,0)
        print(self.atualizar())
        

    def atualizar():
        x=1
        return x

x = Empilhadeira()
x.blit(pg.Surface((10,10)), (0,0), 0, 1)
