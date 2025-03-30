from typing import Dict
from config import resolucao

res_x, res_y = resolucao

""" Dicionário contendo posições e tamanhos relativos do retângulos em relação ao pai.
    Os dados são definidos da seguinte forma:
    considerando a altura do pai como 1, e a posição (top-left) como (0,0).
    Por exemplo, se o objeto O e o pai P são quadrados e lado l(O) = l(P)/2
    (l: Objeto -> Int sendo o lado) e a posição top-left de O sendo no centro de A,
    então rect de O será [top=0.5, left=0.5, largura=0.5, altura= 0.5].
                                x
    P --------------------------------------------------------------->
    |(0,0)                                                          (1,1)
    |
    |
    |
    |
    |
    |
    |
    |
    |
    |
    |
    |
    |                             O _________________________________
   y|                             |(0.5, 0.5)
    |                             |
    |                             |
    |                             |
    |                             |
    |                             |
    |                             |
    |                             |
    |                             |
    |                             |
    |                             |
    |                             |
    |                             |
    |                             |
    V (0,1)

"""
class Modos():
    
    def __init__(self, quant_caixas_madeira : int, quant_caixas_metal : int):

        self.modos : Dict = {
                'Jogo' : {},
                'Menu' : {}
                }
        
        self.modos['Jogo'].update( { 'Janela' : [0, 0, res_x, res_y] } )
        
        self.modos['Jogo'].update( { 'Cenário' : [0, 0, None, 1] } )

        self.modos['Jogo'].update( { 'Corpo da Empilhadeira' : [0.2, 0.61, None, 0.2] } )

        self.modos['Jogo'].update( { 'Garfo da Empilhadeira' : [-0.52, 0.661, 0.525, 0.285] } )
        self.modos['Jogo'].update( { 'Roda Frontal da Empilhadeira' : [0.225, 0.863, 0.36, 0.36] } )
        self.modos['Jogo'].update( { 'Roda Traseira da Empilhadeira' : [0.98, 0.9, 0.3, 0.3] } )
        self.modos['Jogo'].update( { 'Torre da Empilhadeira' : [0.005, 0.7, 0.05, -0.69] } )

        for quantidade in range(quant_caixas_madeira):
            self.modos['Jogo'].update( { f'Caixa de Madeira {quantidade}' : [0.05, 0.67-0.075, None, 0.15] } )
        
        self.modos['Jogo'].update( { f'Caixa de Metal 0' : [0.05, 0.67+0.15-0.075, None, 0.075] } )
        # self.modos['Jogo'].update( { f'Caixa de Metal 0' : [0.5, 0.5, None, 0.075] } )

        for quantidade in range(1,quant_caixas_metal):
            self.modos['Jogo'].update( { f'Caixa de Metal {quantidade}' : [1, 0, None, 1] } )

















