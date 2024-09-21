import pygame as pg
import numpy as np
from recursos import Empilhadeira
import config

from jogo import Jogo
from modo import Modos
from eventos import Eventos


def main():
    pg.init()
    tela_largura = config.resolucao[0]
    tela_altura = config.resolucao[1]
    try:
        tela = pg.display.set_mode((tela_largura, tela_altura), display=1)
    except pg.error:
        tela = pg.display.set_mode((tela_largura, tela_altura), display=0)

    pg.display.set_caption("Empilhadeira de Hanoi")

    jogo = Jogo()
    jogo.set_quant_caixas_mad(3)
    jogo.set_quant_caixas_met(3)

    jogo.inicializar_objetos()
    modos = Modos(3, 3)
    modo_jogo = modos.modos['Jogo']
    jogo.config_inicial(modo_jogo)
    eventos = Eventos(jogo)
    
    clock = pg.time.Clock()

    ceu = (157, 233, 255)
    branco = (255,255,255)
    preto = (0,0,0)
    emp_x = tela_largura/2.2

    while eventos.executando:

        # garfo_altura = max (0, garfo_altura)
        # if (garfo_altura > 140):
        #    garfo_altura -= 5
        
        eventos.gerenciar()
        jogo.atualizar()
        tela.fill(ceu)
        jogo.desenhar(tela)

        clock.tick(120)


        #pg.display.update() # Mesmo efeito de .flip, mas para porções da tela (argumentos: lista de rects)
        pg.display.flip()


    pg.quit()

if __name__ == "__main__":
    main()
