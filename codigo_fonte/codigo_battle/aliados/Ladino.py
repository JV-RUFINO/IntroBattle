from sys import path as caminho
from pathlib import Path as Caminhozão

arquivo = Caminhozão(__file__).resolve()
parente , raiz = arquivo.parent, arquivo.parents[1]
caminho.append(str(raiz))

from battle_exterior            import Perso
from battle_exterior            import Caixa_Texto , texto_decorador
from battle_exterior            import Linkzin

# ALIADOS
from battle_exterior            import Aliado

# MAGIAS
try:
    from magias                 import Fumaça
except ModuleNotFoundError:
    from .magias                import Fumaça

# PYGAME
from pygame                     import Color as Cor
from pygame.image               import load as carregar_imagem

# IMPORTAÇÕES GERAIS
from os                         import getcwd


'== CÓDIGO REAL =='


class Ladino(Aliado):
    def __init__( _ ):
        super().__init__( 'rougue 2nd version' , "L" , Fumaça )

    @staticmethod
    def TIPO() -> Perso:
        return Perso.Ladino 

    @staticmethod
    def cor_assinatura() -> Cor:
        return Cor( 170 , 0 , 0 )

    @texto_decorador(carregar_imagem(Linkzin( getcwd() , 'banco_dados' , 'Personagens' , 'aliados' , 'rougue 2nd version' , 'idle.png')),Cor(170, 0, 0))
    def falar( _ , frase: str, cor: tuple):
        return frase , cor

    def dialogo_combate( _ , cor = Cor( 100 , 0 , 0 ) ) -> Caixa_Texto:
        return _.falar( _.todas_falas , cor )

    def __repr__( _ ):
        return super().repr_aliado( "O" , "assassino" , "Ladino" )



'== TESTES =='


if __name__ == "__main__":
    # Example file showing a basic pygame "game loop"
    import pygame
    from pygame.event   import get as capturar_evento
    from pygame.time    import Clock as Relogio
    from pygame.display import set_mode as definir_janela , set_caption as definir_titulo
    
    # pygame setup
    pygame.init()
    L = Ladino()
    LL: Caixa_Texto = L.dialogo_combate()

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

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    LL.alt[2] = True
                    
                if event.key == pygame.K_LEFT:
                    LL.alt[1] = True
                
                if event.key == pygame.K_RETURN:
                    LL.alt[0] = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    LL.index += 1
                    
                if event.key == pygame.K_LEFT:
                    LL.index -= 1
    
                if event.key == pygame.K_RETURN:
                    LL.rodando = False
                    
                LL.resetar_cores()

            
        # fill the screen with a color to wipe away anything from last frame
        screen.fill("purple")

        # RENDER YOUR GAME HERE
        
        LL(screen)
        
        # RENDER YOUR GAME HERE

        # flip() the display to put your work on screen
        pygame.display.flip()

        clock.tick(60)  # limits FPS to 60

    pygame.quit()
    
    

    



