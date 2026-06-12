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

from battle_exterior import Ataque , Defesa

# IMPORTAÇÕES GERAIS
from os import getcwd
import json

'=== CÓDIGO REAL ==='


class JatoDAgua(Magias):
    def __init__(_):
        super().__init__()

        _.nome    = "JATO D'AGUA"

        _.caminho = Linkzin( _.caminho , 'AGUA' , 'BOLA' )
        _.imagem  = _.imagem(Linkzin( _.caminho , 'WaterBall - Startup and Infinite.png' ))

    @staticmethod
    def TIPO() -> Magi:
        Magi.Agua

    @staticmethod
    def dano_magia( STATUS ):
        return int(STATUS[Stat.CARGA]) 

    @staticmethod
    def aplicar_efeitos( autor , alvo ):
        alvo  - Ataque(1) # diminui o dano dos inimigos
        autor + Defesa(1) # aumenta a defesa do Paladino

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
            status_perso  = status_totais["JATO_DAGUA"]

        resultado = {}
        for numero in range(len(status_perso)):
            resultado.update({numero : status_perso[str(numero)]})

        return resultado
        
    def mostrar_animacao(_, coordenadas: tuple) -> Projetil:
        return super().mostrar_animacao( coordenadas )

        
'=== TESTES ==='


if __name__ == "__main__":
    # Example file showing a basic pygame "game loop"
    import pygame
    from pygame.event   import get as capturar_evento
    from pygame.time    import Clock as Relogio
    from pygame.display import set_mode as definir_janela , set_caption as definir_titulo

    # pygame setup
    pygame.init()

    screen = definir_janela((1280, 720))
    definir_titulo("IntroBattle")

    clock = Relogio()
    running = True

    J = JatoDAgua()
    J_anim = J.mostrar_animacao(((100,100),(800,100)))

    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in capturar_evento():
            if event.type == pygame.QUIT:
                running = False

            
        # fill the screen with a color to wipe away anything from last frame
        screen.fill("purple")
        # RENDER YOUR GAME HERE

        if J_anim.running == False:
            J_anim.running = True
        
        J_anim(screen)
        

        # flip() the display to put your work on screen
        pygame.display.flip()

        clock.tick(60)  # limits FPS to 60

    pygame.quit()
    
    