from __future__ import annotations
from dataclasses import dataclass

from objeto import Objeto, Imagem, Retangulo, Roda, Caixa

@dataclass
class Jogo():


    def set_quant_caixas_mad(self, quantidade : int):
        self.quantidade_caixas_mad = quantidade

    def get_quant_caixas_mad(self) -> int:
        return self.quantidade_caixas_mad

    def set_quant_caixas_met(self, quantidade : int):
        self.quantidade_caixas_met = quantidade

    def get_quant_caixas_met(self) -> int:
        return self.quantidade_caixas_met

    def inicializar_objetos(self) -> None:

        self.caixas_metal = []
        self.caixas_madeira = []
        self.componentes_empilhadeira = {}

        for numero in range(1,self.quantidade_caixas_mad):
            temp = Caixa(
                nome = f"Caixa de Madeira {numero}",
                filhos = [],
                path_imagem = "Imagens/caixa2.png"
                )
            self.caixas_madeira.append(temp)

        self.caixa_madeira_principal = Caixa(
            nome = "Caixa de Madeira 0",
            filhos = self.caixas_madeira,
            path_imagem = "Imagens/caixa2.png"
            )
       
        for quant in range(1, self.quantidade_caixas_met):
            temp = Imagem(
                nome = f"Caixa de Metal {quant}",
                filhos = [],
                path_imagem = "Imagens/caixa_metal.jpg"
                )
            self.caixas_metal.append(temp)
            
        self.caixa_metal_principal = Imagem(
            nome = "Caixa de Metal 0",
            filhos = self.caixas_metal,
            path_imagem = "Imagens/caixa_metal.jpg"
            )


        self.componentes_empilhadeira.update({
            "Garfo" : Imagem(
            nome = "Garfo da Empilhadeira",
            filhos = [],
            path_imagem = "Imagens/garfo_crop.png"
            )})

        self.componentes_empilhadeira.update({
            "Roda Frontal" : Roda(
            nome = "Roda Frontal da Empilhadeira",
            filhos = []
            )})

        self.componentes_empilhadeira.update({
            "Roda Traseira" : Roda(
            nome = "Roda Traseira da Empilhadeira",
            filhos = []
            )})

        self.componentes_empilhadeira.update({
            "Torre" : Retangulo(
            nome = "Torre da Empilhadeira", 
            filhos = [],
            cor = [45, 55, 77]
            # cor = [22, 28, 38]
            )})

        self.empilhadeira = Imagem(
            nome = "Corpo da Empilhadeira",
            filhos = self.componentes_empilhadeira.values(),
            path_imagem = "Imagens/corpo_empilhadeira_crop.png"
            )

        self.cenario = Imagem(
            nome = "Cenário",
            filhos = [self.caixa_madeira_principal,
                      self.caixa_metal_principal,
                      self.empilhadeira],
            path_imagem = "Imagens/cenario.jpg"
            )

        self.janela = Objeto(
            nome = "Janela",
            filhos = [self.cenario],
            pai = None
            )

        # self.set_pais(self.janela)
        self.raiz = self.janela

    def add_caixa(self):
        numero = self.quantidade_caixas_mad
        self.caixas_madeira.append(Caixa(
                nome = f"Caixa de Madeira {numero}",
                filhos = [],
                path_imagem = "Imagens/caixa2.png"
                ))
        self.quantidade_caixas_mad = numero + 1
        


        

    # def set_pais(self, obj : Objeto):
    #     x = obj.get_filhos()
    #     # breakpoint()
    #     if not (x == []):
    #         for filho in x:
    #             filho.set_pai(obj)
    #             self.set_pais(filho)
        

    def calcular_rect_absoluto(self, objeto : Objeto):
        pai = objeto.get_pai()
        if pai == None:
            objeto.set_rect_absoluto(objeto.get_rect())
        else:
            pai_rect = pai.get_rect_absoluto()
            rect_absoluto = []
            rect_absoluto.append(pai_rect[0] + pai_rect[3] * objeto.get_rect()[0])
            rect_absoluto.append(pai_rect[1] + pai_rect[3] * objeto.get_rect()[1])
            rect_absoluto.append(pai_rect[3] * objeto.get_rect()[2])
            rect_absoluto.append(pai_rect[3] * objeto.get_rect()[3])
            objeto.set_rect_absoluto(rect_absoluto)


    def config_inicial_objetos(self, modo : dict, objeto : Objeto):
        """ Modo: jogo ou menu """

        nome = objeto.get_nome()

        objeto.set_rect( modo[ nome ] ) 
        objeto.carregar()
        objeto.config_rect()
        self.calcular_rect_absoluto(objeto)
        objeto.atualizar()
        for filho in objeto.get_filhos():
            filho.set_pai(objeto)
            self.config_inicial_objetos(modo, filho)

    def config_inicial(self, modo : dict):
        self.config_inicial_objetos(modo, self.raiz)

    def atualizar_objetos(self, objeto : Objeto):
        # get_time_elapsed
        self.calcular_rect_absoluto(objeto)
        objeto.atualizar()
        for filho in objeto.get_filhos():
            self.atualizar_objetos(filho)

    def atualizar(self):
        self.atualizar_objetos(self.raiz)



    def desenhar_subarvore(self, objeto : Objeto, tela):
        """ Argumento dado (objeto) é a raiz da sub-árvore a ser desenhada """
        objeto.desenhar(tela)
        filhos = objeto.get_filhos()
        if filhos:
            for filho in filhos:
                self.desenhar_subarvore(filho, tela)

    def desenhar(self, tela):
        self.desenhar_subarvore(self.raiz, tela)
        




