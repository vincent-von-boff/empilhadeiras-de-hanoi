import pygame as pg
import numpy as np
from recursos import Empilhadeira
import config



def main():
    pg.init()
    tela_largura = config.resolucao[0]
    tela_altura = config.resolucao[1]
    try:
        tela = pg.display.set_mode((tela_largura, tela_altura), display=1)
    except pg.error:
        tela = pg.display.set_mode((tela_largura, tela_altura), display=0)

    pg.display.set_caption("Empilhadeira de Hanoi")
    
    # Inicializa empilhadeira
    emp = Empilhadeira()
        
    #Carrega imagem cenario
    cenario = pg.image.load("Imagens/cenario.jpg")

    # Carrega imagens caixa metal
    caixa = pg.image.load("Imagens/caixa_metal.jpg")
    caixa2 = pg.image.load("Imagens/caixa_metal.jpg")
    caixa3 = pg.image.load("Imagens/caixa_metal.jpg")
    # Re-escala caixas
    caixa = pg.transform.scale_by(caixa, 0.3)
    caixa2 = pg.transform.scale_by(caixa2, 0.3)
    caixa3 = pg.transform.scale_by(caixa3, 0.3)

    pg.draw.rect(tela, (0,0,0), caixa.get_rect(), width=1)

    # Calcula escala do cenario
    cenario_largura = cenario.get_width()
    cenario_altura = cenario.get_height()
    temp = int((tela_altura/cenario_altura)*cenario_largura)
    cenario = pg.transform.scale(cenario, (temp,tela_altura)) # Cenário

    clock = pg.time.Clock()

    branco = (255,255,255)
    preto = (0,0,0)
    emp_x = tela_largura/2.2
    garfo_altura = 0
    direito_clicado = False
    esquerdo_clicado = False
    cima_clicado = 0
    baixo_clicado = 0

    def gerenciador_eventos(direito, esquerdo, cima, baixo,executando):
        for ev in pg.event.get():
            if ev.type == pg.QUIT:
                executando = False
            if ev.type == pg.KEYDOWN:
                if ev.key == pg.K_RIGHT:
                    #forklift_x += 10
                    direito = 1
                    print(emp_x)
                if ev.key == pg.K_LEFT:
                    #forklift_x -= 10
                    esquerdo = 1
                if ev.key == pg.K_UP:
                    #fork_height += 10
                    cima = 1
                if ev.key == pg.K_DOWN:
                    #fork_height -= 10
                    baixo = 1
            if ev.type == pg.KEYUP:
                if ev.key == pg.K_RIGHT:
                    direito = 0
                if ev.key == pg.K_LEFT:
                    esquerdo = 0
                if ev.key == pg.K_UP:
                    cima = 0
                if ev.key == pg.K_DOWN:
                    baixo = 0
        return direito, esquerdo, cima, baixo, executando
    


    executando = True

    while executando:

        garfo_altura = max (0, garfo_altura)
        if (garfo_altura > 140):
            garfo_altura -= 5

        # Desenha o cenário na tela
        tela.blit(cenario, (0, 0))

        # Desenha caixas de metal
        tela.blit(caixa, (750-3*caixa.get_width()/2, 0.70*config.resolucao[1]-150))
        tela.blit(caixa2, (750-(caixa.get_width()/2), 0.70*config.resolucao[1]-150))
        tela.blit(caixa3, (750+caixa.get_width()/2, 0.70*config.resolucao[1]-150))

        emp.blit(tela, (int(emp_x),0), garfo_altura, emp_x)
        rec = pg.Rect((emp_x,tela_altura-200), np.array([200,200]))

        direito_clicado, esquerdo_clicado, cima_clicado, baixo_clicado, executando = gerenciador_eventos(direito_clicado,
                                                                                esquerdo_clicado,
                                                                                cima_clicado, 
                                                                                baixo_clicado,
                                                                                executando)
        emp_x += (direito_clicado - esquerdo_clicado)*2
        garfo_altura += (cima_clicado - baixo_clicado)*1
        clock.tick(100)


        #pg.display.update() # Mesmo efeito de .flip, mas para porções da tela (argumentos: lista de rects)
        pg.display.flip()


    pg.quit()

if __name__ == "__main__":
    main()
