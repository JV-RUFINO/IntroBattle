from sys import path as caminho
from pathlib import Path as Caminhozão

arquivo = Caminhozão(__file__).resolve()
parente , raiz = arquivo.parent, arquivo.parents[1]
caminho.append(str(raiz))

# CODIGO COPIADO
from battle_exterior import Linkzin

# PYGAME
from pygame          import Color   as Cor , Surface as Superficie , Rect as Retangulo
from pygame.draw     import rect    as desenhar_retangulo
from pygame.font     import Font    as Fonte
from pygame.event    import Event

from pygame          import K_LEFT  as ESQUERDA , K_RIGHT as DIREITA

# IMPORTAÇÕES GERAIS
from dataclasses     import dataclass


"=== CÓDIGO REAL ==="


@dataclass
class Printar_Opções:
    cor_geral       : Cor
    opcoes          : tuple = ("LUTAR","MAGIA","FALAR","PULAR")

    __dimenções     : Retangulo = Retangulo( 100 , 550 , 200 , 100 )
    __espaçamento   : int   = 300
    __CONTAGEM      : int   = 0
        
    @staticmethod
    def fonte():
        return Fonte(Linkzin('fonte_jogo',"fontePygame.ttf", act_dir= True),32)

    @property
    def dimenções( _ ):
        return Retangulo( _.__dimenções.left , _.__dimenções.top , _.__dimenções.width , _.__dimenções.height )

    @property
    def opcao_escolhida( _ ):
        return _.opcoes[_.contagem]

    @property
    def contagem( _ ):
        return _.__CONTAGEM

    def mudar_selecionado( _ , evento : Event ):
        if evento == DIREITA:
            resultado = 1
        elif evento == ESQUERDA:
            resultado = -1
        
        _.__CONTAGEM += resultado

        maximo = len( _.opcoes ) - 1

        if _.__CONTAGEM > maximo:
            _.__CONTAGEM = 0
        elif _.__CONTAGEM < 0:
            _.__CONTAGEM = maximo

    @property
    def cor( _ ):
        return _.cor_geral

    @cor.getter
    def cor_borda( _ ):
        return Cor( _.cor_geral.r + 20 , _.cor_geral.b + 20, _.cor_geral.b + 20 )

    @cor.getter
    def cor_borda_alt( _ ):
        return Cor( _.cor_geral.r + 60 , _.cor_geral.b + 60, _.cor_geral.b + 60 )
    
    @property
    def pos_frase( _ ): # posicao da frase
        novo = _.dimenções
        novo.left += 30
        novo.top  += 30

        return novo

    def __call__( _ , screen : Superficie ):
        carregar_fonte  = _.fonte()
        dim_extra       = _.dimenções
        pos_frase       = _.pos_frase
        numero          = 0

        for opcao in _.opcoes:
            cor_borda = _.cor_borda if numero != _.contagem else _.cor_borda_alt

            desenhar_retangulo( screen , _.cor     , dim_extra )
            desenhar_retangulo( screen , cor_borda , dim_extra , width= 14 )

            screen.blit( carregar_fonte.render( opcao, False , (255, 255, 255) ) , 
                            pos_frase ) # texto da caixa
            
            dim_extra.left += _.__espaçamento
            pos_frase.left += _.__espaçamento

            numero += 1


"=== TESTES ==="


if __name__ == "__main__":
    from criar_fase import Criar_Fase
    from pygame import QUIT as SAIR_X
    import pygame

    @Criar_Fase(Criar_Fase.caminho_comum(),'salão.png')
    def teste(
        screen :Superficie, 
                info_extra = None,
                    eventos:list = None):
        for event in eventos:
            if event.type == SAIR_X: # pygame.QUIT
                return False

        opcoes : Printar_Opções = info_extra

        for event in eventos:
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    opcoes.mudar_selecionado( event.key )
                if event.key == pygame.K_RIGHT:
                    opcoes.mudar_selecionado( event.key )


        opcoes(screen)

        return True

    pygame.init()

    screen = pygame.display.set_mode((1280, 720))

    # CÓDIGO PARA TESTAR

    conteudo = Printar_Opções(Cor(125,125,125),("VOLTAR",), Retangulo(500,550,220,100))

    print(conteudo)

    # CÓDIGO PARA TESTAR

    teste(screen, conteudo)

    pygame.quit()