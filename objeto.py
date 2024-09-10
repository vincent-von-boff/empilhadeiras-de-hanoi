import recursos
import math
import pygame as pg
import config

class Objeto:
    #   Objetos (imagens) do jogo. Um objeto é formado de uma lista de imagens assim como posições
    # relativa a imagens[0] (primeira imagem da lista) e tamanhos relativos ao cenário do jogo.

    def __init__(self, imagens):
        self.imag = {                      
            'super': None,               # Superfícies ou rects das imagens (nesta ordem)
            'pos_x': None,               # Posição em pixels left do rect contendo objeto
            'pos_y': None,               # Posição em pixels up do rect contendo objeto
            'dim_x': None,               # Largura em pixels objeto (largura, altura)
            'dim_y': None,               # Altura em pixels objeto (largura, altura)
            # O tamanho relativo considera o tamanho da superfície relativa a altura
            # do cenário (geralmente 100 unidades). Isso garante consistência entre 
            # os tamanhos dos objetos do jogo independente da resolução inicia escolhida.
            'largura_rel': None,         # Largura relativa ao cenário em jogo
            'escala': None,              # Número que deve imagem original deve ser escalada
            'refletido': None            # Bool: imagem está refletida ou não
        }

        self.carregar_imagens(imagens)
        self.set_largura_rel()
