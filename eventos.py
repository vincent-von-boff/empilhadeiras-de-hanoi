import pygame as pg

class Eventos():

    def __init__(self, jogo):
        self.jogo = jogo
        self.executando = True
        self.emp_flags = { "esquerda" : 0, "direita" : 0 }
        self.garfo_flags = { "cima" : 0, "baixo" : 0 }
    
    def gerenciar(self):
        for ev in pg.event.get():
            if ev.type == pg.QUIT:
                self.executando = False

            if ev.type == pg.KEYDOWN:
                if ev.key == pg.K_RIGHT:
                    self.emp_flags["direita"] = 1
                if ev.key == pg.K_LEFT:
                    self.emp_flags["esquerda"] = 1
                if ev.key == pg.K_UP:
                    self.garfo_flags["cima"] = 1
                if ev.key == pg.K_DOWN:
                    self.garfo_flags["baixo"] = 1

            if ev.type == pg.KEYUP:
                if ev.key == pg.K_RIGHT:
                    self.emp_flags["direita"] = 0
                if ev.key == pg.K_LEFT:
                    self.emp_flags["esquerda"] = 0
                if ev.key == pg.K_UP:
                    self.garfo_flags["cima"] = 0
                if ev.key == pg.K_DOWN:
                    self.garfo_flags["baixo"] = 0
        self.mover_empilhadeira(self.emp_flags)
        self.mover_garfo(self.garfo_flags)

    def mover_empilhadeira(self, flags : dict) -> None:
        if (sum(flags.values()) % 2):
            acrescimo = 0.005
            if flags["direita"]:
                acrescimo *= 1
            if flags["esquerda"]:
                acrescimo *= -1
            angulo = self.jogo.componentes_empilhadeira["Roda Frontal"].get_angulo()
            rect_empilhadeira = self.jogo.empilhadeira.get_rect()
            rect_empilhadeira[0] += acrescimo
            self.jogo.empilhadeira.set_rect(rect_empilhadeira)
            self.jogo.componentes_empilhadeira["Roda Frontal"].set_angulo(angulo + 500*acrescimo)
            self.jogo.componentes_empilhadeira["Roda Traseira"].set_angulo(angulo + 500*acrescimo)

    def mover_garfo(self, flags : dict) -> None:
        if (sum(flags.values()) % 2):
            acrescimo = 0.01
            if flags["cima"]:
                acrescimo *= -1
            if flags["baixo"]:
                acrescimo *= 1
            rect_torre = self.jogo.componentes_empilhadeira["Torre"].get_rect()
            rect_garfo = self.jogo.componentes_empilhadeira["Garfo"].get_rect()
            rect_torre[1] += acrescimo
            rect_torre[3] -= acrescimo
            rect_garfo[1] += acrescimo
            self.jogo.componentes_empilhadeira["Torre"].set_rect(rect_torre)
            self.jogo.componentes_empilhadeira["Garfo"].set_rect(rect_garfo)
        


