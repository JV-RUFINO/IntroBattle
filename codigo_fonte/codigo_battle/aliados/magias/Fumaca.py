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

from battle_exterior import Velocidade , Ataque

# IMPORTAÇÕES GERAIS
from os import listdir


'=== CÓDIGO REAL ==='


class Fumaça(Magias):
    def __init__(_):
        super().__init__()

        _.nome        = "FUMAÇA"

        _.caminho     = Linkzin( _.caminho , 'FUMAÇA' , 'VFX 2 Separated frames' )
        _.todos_nomes = listdir( Linkzin( _.caminho ) )

    @staticmethod
    def TIPO() -> Magi:
        Magi.Fumaça

    @staticmethod
    def dano_magia( STATUS ):
        return int(STATUS[Stat.CARGA])

    @staticmethod
    def aplicar_efeitos( autor , alvo ):
        autor + Velocidade(2)
        autor + Ataque(1)

        return None

    @property
    def dano(_) -> int:
        return super().dano

    @dano.setter
    def definir_dano(_, novo: int):
        _.dano = novo

    @property
    def coordenadas_imagem(_) -> set:
        return None

    def mostrar_animacao(_, coordenadas: tuple) -> Projetil:
        return Projetil(coordenadas,[ _.imagem( Linkzin( _.caminho , nome ) ) for nome in _.todos_nomes ])


'=== TESTES ==='


if __name__ == "__main__":
    # Example file showing a basic pygame "game loop"
    import pygame
    from pygame.event   import get as capturar_evento
    from pygame.time    import Clock as Relogio
    from pygame.display import set_mode as definir_janela , set_caption as definir_titulo

    # pygame setup
    pygame.init()
    F = Fumaça()
    F_anim = F.mostrar_animacao(((100,100),(100,200)))

    screen = definir_janela((1280, 720))
    definir_titulo("IntroBattle")


    clock = Relogio()
    running = True

    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in capturar_evento():
            if event.type == pygame.QUIT:
                running = False

            
        # fill the screen with a color to wipe away anything from last frame
        screen.fill("purple")
        # RENDER YOUR GAME HERE

        if F_anim.running == False:
            F_anim.running = True
        
        F_anim(screen)
        

        # flip() the display to put your work on screen
        pygame.display.flip()

        clock.tick(60)  # limits FPS to 60

    pygame.quit()

    