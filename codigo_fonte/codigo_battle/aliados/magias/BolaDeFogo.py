from sys import path as caminho
from pathlib import Path as Caminhozão

arquivo = Caminhozão(__file__).resolve()
parente , raiz = arquivo.parent, arquivo.parents[1]
caminho.append(str(raiz))

# ABSTRATOS
from battle_exterior import Magias

# ESSÊNCIAIS
from battle_exterior import Magi , Stat
from battle_exterior import Linkzin
from battle_exterior import Projetil

# IMPORTAÇÕES GERAIS
from os import getcwd
import json


'=== CÓDIGO REAL ==='


class BolaDeFogo(Magias):
    def __init__(_):
        super().__init__()

        _.nome    = "BOLA DE FOGO"

        _.caminho = Linkzin( _.caminho , 'FOGO','BOLA')
        _.imagem  = _.imagem(Linkzin(_.caminho,'Firebolt SpriteSheet.png'))

    @staticmethod
    def TIPO() -> Magi:
        Magi.Fogo

    @staticmethod
    def dano_magia( STATUS ):
        return int(STATUS[Stat.CARGA]) + int(STATUS[Stat.ATAQUE])

    @staticmethod
    def aplicar_efeitos( autor , alvo ):
        return None

    @property
    def dano(_) -> int:
        return super().dano

    @dano.setter
    def definir_dano(_, novo: int):
        _.dano = novo

    @property
    def coordenadas_imagem(_) -> set:
        with open(Linkzin(getcwd(),'roteiro','pos_spritesheet_magias.json'),'r') as status:
            status_totais = json.load(status)
            status_perso  = status_totais["BOLA_FOGO"]

        resultado = {}
        for numero in range(len(status_perso)):
            resultado.update({numero : status_perso[str(numero)]})

        return resultado

    def mostrar_animacao(_, coordenadas: tuple) -> Projetil:
        return super().mostrar_animacao( coordenadas )


'=== TESTES ==='


if __name__ == "__main__":
    from os import getcwd

    # Example file showing a basic pygame "game loop"
    import pygame
 
    # pygame setup
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))

    pygame.display.set_caption("IntroBattle")

    clock = pygame.time.Clock()
    running = True

    Fogo = BolaDeFogo( )
    anim = Fogo.mostrar_animacao(((200,200),(800,200)))
    'anim = Projetil(((200,200),(800,200)),Fogo.mostrar_animacao())'
    n = 0

    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # fill the screen with a color to wipe away anything from last frame
        screen.fill("purple")
        # RENDER YOUR GAME HERE

        if anim.running == False:
            anim.running = True

        anim(screen,4)
        

        # flip() the display to put your work on screen
        pygame.display.flip()

        clock.tick(60)  # limits FPS to 60

    pygame.quit()
    