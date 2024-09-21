from __future__ import annotations
import math

import pygame as pg
from pygame import gfxdraw


class Objeto:
    """
    Nodo da árvore de objetos (imagens, figuras, etc...) do jogo.
    O objeto carrega informações sobre como, aonde e que tamanho que o objeto deve
    ser carregado na tela.

    :Atributos:
    nome : str -- Nome do objeto
    pai : Objeto -- Pai do objeto
    rect : List[float] -- (left, top, width, height) onde left e top definem a posição
    -- enquanto que width e height definem o tamanho do retângulo. Note que tanto a posição como
    -- o tamanho são relativos ao rect do pai (considerando a altura do pai como 100)
    -- Note que o topo esquerdo da tela tem posição (0, 0) e o eixo y cresce de cima para baixo
    -- enquanto que o eixo x tem a direção habitual (esquerda para direita).
    rect_absoluto : List[float] -- Posição e tamanhos absolutos em pixels que será utilizado
    -- para desenhar o objeto na tela
    filhos : List[Objeto] -- Lista contendo os filhos do objeto

    """

    def __init__(self,
                 nome : str,
                 filhos : List[Objeto],
                 pai : Objeto | None = None,
                 _rect : List[float] = None, # Retângulo relativo ao pai (considerando altura do pai como 100 metros)
                 rect_absoluto : List[float] = None # Retângulo contendo as posições absolutas em pixels
                 ):

        self.nome = nome
        self.filhos = filhos
        self.pai = pai
        self._rect = _rect
        self.rect_absoluto = rect_absoluto
    
    """ Setters e Getters nome """
    def set_nome(self, novo_nome : str) -> None:
        self.nome = novo_nome

    def get_nome(self) -> str:
        return self.nome

    """ Setters e Getters pai """
    def set_pai(self, novo_pai : Objeto) -> None:
        self.pai = novo_pai

    def get_pai(self) -> Objeto:
        return self.pai


    """ Setters e Getters filhos """
    def inserir_filho(self, novo_filho : Objeto) -> None:
        self.filhos.append(novo_filho)
        
    def get_filhos(self) -> List[Objeto]:
        return self.filhos


    """ Setters e Getters retângulo """
    def set_rect(self, rect : List[float]) -> None:
        self._rect = rect

    def get_rect(self) -> List[float]:
        return self._rect


    """ Setters e Getters retângulo absoluto """
    def set_rect_absoluto(self, rect_absoluto : List[float]) -> None:
        self.rect_absoluto = rect_absoluto

    def get_rect_absoluto(self) -> List[float]:
        return self.rect_absoluto

    def carregar(self):
        pass

    def config_rect(self):
        pass

    def escalar(self):
        pass

    def atualizar(self):
        pass

    def desenhar(self, tela : pg.Surface) -> None:
        """ 
        Desenha objeto na tela.

        """
        pass


class Imagem(Objeto):
    """ Imagem a ser usada no jogo """

    def __init__(self,
                 nome : str,
                 filhos : List[Objeto],
                 pai : Objeto | None = None,
                 *,
                 _rect : List[float] = None, # Retângulo relativo ao pai (considerando altura do pai como 100 metros)
                 rect_absoluto : List[float] = None, # Retângulo contendo as posições absolutas em pixels):
                 path_imagem : str,
                 imagem : pg.Surface = None,
                 imagem_reescalada : pg.Surface = None,
                 refletido : bool = False
                 ):
        super().__init__(nome, filhos, pai, _rect, rect_absoluto)

        self.path_imagem = path_imagem
        self.imagem = imagem
        self.imagem_reescalada = imagem_reescalada
        self.refletido = refletido

    def refletir(self):
        self.imagem = pg.transform.flip(self.imagem, True, False)
        pass

    def carregar(self) -> None:
        self.imagem = pg.image.load(self.path_imagem)

    def config_rect(self):
        if self.imagem:
            altura_absoluta = self.imagem.get_height()
            largura_absoluta = self.imagem.get_width()
            self._rect[2] = (largura_absoluta / altura_absoluta) * self._rect[3]

    def escalar(self):
        escala = self.rect_absoluto[3] / self.imagem.get_height()
        self.imagem_reescalada = pg.transform.scale_by(self.imagem, escala)

    def atualizar(self) -> None:
        escala = self.rect_absoluto[3] / self.imagem.get_height()
        self.imagem_reescalada = pg.transform.scale_by(self.imagem, escala) 

    def desenhar(self, tela):
        tela.blit(self.imagem_reescalada, (self.rect_absoluto[0], self.rect_absoluto[1]) )


class Retangulo(Objeto):
    """ Figura retangular """
    def __init__(self,
                 nome : str,
                 filhos : List[Objeto],
                 pai : Objeto | None = None,
                 *,
                 _rect : List[float] = None, # Retângulo relativo ao pai (considerando altura do pai como 100 metros)
                 rect_absoluto : List[float] = None, # Retângulo contendo as posições absolutas em pixels):
                 cor : List[int]
                 ):
        super().__init__(nome, filhos, pai, _rect, rect_absoluto)

        self.cor : List[int] = cor# rgb

    # def atualizar(self):
    #     self.escala = self.pai.rect_absoluto[3] / self.pai._rect[3] # Divide alturas dos rects
    #     self.rect_absoluto = [coordenada * self.escala for coordenada in self._rect]

    def desenhar(self, tela : pg.Surface) -> None:
        rect = pg.Rect(self.rect_absoluto)
        pg.draw.rect(tela, self.cor, rect) #  (self.rect_absoluto[0], self.rect_absoluto[1]))

class Roda(Objeto):
    """ Roda da empilhadeira """
    def __init__(self,
                 nome : str,
                 filhos : List[Objeto],
                 pai : Objeto | None = None,
                 *,
                 _rect : List[float] = None, # Retângulo relativo ao pai (considerando altura do pai como 100 metros)
                 rect_absoluto : List[float] = None, # Retângulo contendo as posições absolutas em pixels):
                 raio : float = None,
                 angulo : float = 0,
                 numero_parafusos : int = 12,
                 cor_calota : List[int] = (237, 136, 5),
                 cor_pneu : List[int] = (0, 0, 0)
                 ):
        
        super().__init__(nome, filhos, pai, _rect, rect_absoluto)

        self.raio = raio
        self.angulo = angulo
        self.numero_parafusos = numero_parafusos
        self.cor_calota = cor_calota
        self.cor_pneu = cor_pneu

    def get_angulo(self) -> None:
        return self.angulo

    def set_angulo(self, angulo : float):
        self.angulo = angulo

    def atualizar(self):
        # escala = self.pai.rect_absoluto[3] / self.pai._rect[3] # Divide alturas dos rects
        # self.rect_absoluto = [coordenada * escala for coordenada in self._rect]
        self.raio = self.rect_absoluto[2]/2

    def desenhar(self, tela : pg.Surface):
        """ Constrói e desenha a roda """

        pos_x = int(self.rect_absoluto[0]) # + self.rect_absoluto[2]/2)
        pos_y = int(self.rect_absoluto[1]) # + self.rect_absoluto[3]/2)
        raio = self.raio
        angulo = self.angulo
        preto = (0, 0, 0)

        # Circulo anti-alias
        #Pneu
        pg.gfxdraw.aacircle(tela, pos_x, pos_y, int((raio/50)*50), preto)
        #Calota
        pg.gfxdraw.aacircle(tela, pos_x, pos_y, int((raio/50)*30), self.cor_calota)
        #Eixo central
        pg.gfxdraw.aacircle(tela, pos_x, pos_y, int(raio*(13/50)), preto)

        ## Circulo preenchido
        #Pneu
        pg.gfxdraw.filled_circle(tela, pos_x, pos_y, int((raio/50)*50), preto)
        #Calota
        pg.gfxdraw.filled_circle(tela, pos_x, pos_y, int((raio/50)*30), self.cor_calota)
        #Eixo central
        pg.gfxdraw.filled_circle(tela, pos_x, pos_y, int((raio/50)*12), preto)

        #Parafusos
        for id_paraf in range(self.numero_parafusos):
            rad_ang = (2*math.pi/360) * angulo
            ang_paraf = 2*math.pi/(self.numero_parafusos)
            pos_x_parafuso = round(pos_x + 17 * (raio/50) * math.cos(id_paraf*ang_paraf + rad_ang))
            pos_x_parafuso2 = round(pos_x + 2*17 * (raio/50) * math.cos(id_paraf*ang_paraf + rad_ang))
            pos_y_parafuso = round(pos_y + 17 * (raio/50) * math.sin(id_paraf*ang_paraf + rad_ang))
            pos_y_parafuso2 = round(pos_y + 2*17 * (raio/50) * math.sin(id_paraf*ang_paraf + rad_ang))
            raio_parafuso = int(raio*(2/50))
            pg.gfxdraw.aacircle(tela, pos_x_parafuso, pos_y_parafuso, raio_parafuso, (0,0,0))
            pg.gfxdraw.filled_circle(tela, pos_x_parafuso, pos_y_parafuso, raio_parafuso, (0,0,0))
            # if (id_paraf % self.numero_parafusos == 0):
            #     pg.draw.aaline(tela, (0,0,0), (pos_x, pos_y), (pos_x_parafuso2, pos_y_parafuso2))

class Caixa(Imagem):
    """ Caixa de madeira (torre da Torre de Hanoi) """

    def __init__(self,
                 nome : str,
                 filhos : List[Objeto],
                 pai : Objeto | None = None,
                 *,
                 _rect : List[float] = None, # Retângulo relativo ao pai (considerando altura do pai como 100 metros)
                 rect_absoluto : List[float] = None, # Retângulo contendo as posições absolutas em pixels):
                 path_imagem : str,
                 imagem : pg.Surface = None,
                 imagem_reescalada : pg.Surface = None,
                 refletido : bool = False,
                 peso : float = 0
                 ):
        super().__init__(nome, filhos, path_imagem = path_imagem)

        self.peso = peso


    # Peso para calcular ordem das caixas
    peso : float = 0

    def set_peso(self, novo_peso : float) -> None:
        self.peso = novo_peso




