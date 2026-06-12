from sys import path as caminho
from pathlib import Path as Caminhozão

arquivo = Caminhozão(__file__).resolve()
parente , raiz = arquivo.parent, arquivo.parents[1]
caminho.append(str(raiz))

# ESSENCIAIS
from battle_exterior            import Perso
from battle_exterior            import Caixa_Texto , texto_decorador
from battle_exterior            import Linkzin

# ALIADOS
from battle_exterior            import Aliado

# MAGIAS
try:
    from magias                 import BolaDeFogo
except ModuleNotFoundError:
    from .magias                import BolaDeFogo

# PYGAME
from pygame                     import Color    as Cor
from pygame.image               import load     as carregar_imagem

# IMPORTAÇÕES GERAIS
from os                         import getcwd


'== CÓDIGO REAL =='


class Maga(Aliado):
    def __init__( _ ):
        super().__init__( 'wizard' , "M" , BolaDeFogo )

    @staticmethod
    def TIPO() -> Perso:
        return Perso.Maga

    @staticmethod
    def cor_assinatura() -> Cor:
        return Cor( 120 , 20 , 120 )

    @texto_decorador(carregar_imagem(Linkzin( getcwd() , 'banco_dados' , 'Personagens' , 'aliados' , 'wizard' , 'idle.png')),Cor(120, 20, 120))
    def falar( _ , frase: str, cor: tuple):
        return frase , cor

    def dialogo_combate( _ , cor = Cor( 100 , 0 , 100 )) -> Caixa_Texto:
        return _.falar( _.todas_falas ,cor)

    def __repr__( _ ):
        return super().repr_aliado( "A" , "grande anciã" , "Maga" )


'== TESTES =='


if __name__ == "__main__":
    # Example file showing a basic pygame "game loop"
    import pygame
    from pygame.event   import get as capturar_evento
    from pygame.time    import Clock as Relogio
    from pygame.display import set_mode as definir_janela , set_caption as definir_titulo
    
    # pygame setup
    pygame.init()
    M = Maga()
    MM: Caixa_Texto = M.dialogo_combate()

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
                    MM.alt[2] = True
                    
                if event.key == pygame.K_LEFT:
                    MM.alt[1] = True
                
                if event.key == pygame.K_RETURN:
                    MM.alt[0] = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    MM.index += 1
                    
                if event.key == pygame.K_LEFT:
                    MM.index -= 1
    
                if event.key == pygame.K_RETURN:
                    MM.rodando = False
                    
                MM.resetar_cores()

            
        # fill the screen with a color to wipe away anything from last frame
        screen.fill("purple")

        # RENDER YOUR GAME HERE
        
        """M.mostrar_animacao(screen,(300,200),(80,80))
        M.mostrar_animacao(screen,(600,400),(80,80))
        M.mostrar_animacao(screen,(900,200),(80,80))
        
        M.mostrar_animacao(screen,(600,200),(80,80))"""
        
        MM(screen)
        
        # RENDER YOUR GAME HERE

        # flip() the display to put your work on screen
        pygame.display.flip()

        clock.tick(60)  # limits FPS to 60

    pygame.quit()
    
    

    



