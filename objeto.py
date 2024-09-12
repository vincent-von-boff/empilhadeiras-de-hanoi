from __future__ import annotations

import pygame as pg
from dataclasses import dataclass

@dataclass
class Objeto:
    """
    Nodo da árvore de objetos (imagens, figuras, etc...) do jogo.
    O objeto carrega informações sobre como, aonde e que tamanho que o objeto deve
    ser carregado na tela.

    :Atributos:
    nome : str -- Nome do objeto
    pai : Objeto -- Pai do objeto
    rentangulo : pygame.Rect -- (left, top, width, height) onde left e top definem a posição
    -- enquanto que width e height definem o tamanho do retângulo. Note que tanto a posição como
    -- o tamanho são relativos ao rect do pai (considerando a altura do pai como 100)
    -- Note que o topo esquerdo da tela tem posição (0, 0) e o eixo y cresce de cima para baixo
    -- enquanto que o eixo x tem a direção habitual (esquerda para direita).
    filhos : List[Objeto] -- Lista contendo os filhos do objeto

    """

    nome : str
    pai: Objeto | None
    retangulo: pg.Rect # Retângulo relativo ao pai (considerando altura do pai como 100)
    filhos : List[Objeto]
    
    def set_pai(self, novo_pai : Objeto) -> None:
        self.pai = novo_pai

    def get_pai(self) -> Objeto:
        return self.pai

    def inserir_filho(self, novo_filho : Objeto) -> None:
        self.filhos.append(novo_filho)
        
    def get_filhos(self) -> List[Objeto]:
        return self.filhos

    def desenhar(self) -> None:
        """ 
        Desenha objeto na tela.

        """
        pass
