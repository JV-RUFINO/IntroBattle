from sys import path as caminho
from pathlib import Path as Caminhozão

arquivo = Caminhozão(__file__).resolve()
parente , raiz = arquivo.parent, arquivo.parents[1]
caminho.append(str(raiz))

# ESSENCIAIS

from battle_exterior        import Perso
from battle_exterior        import Caixa_Texto , texto_decorador
from battle_exterior        import Linkzin

# ALIADOS
from battle_exterior        import Aliado

# MAGIAS
try:
    from magias             import Ventania
except ModuleNotFoundError:
    from .magias            import Ventania

# PYGAME
from pygame                 import Color    as Cor
from pygame.image           import load     as carregar_imagem

#IMPORTAÇÕES GERAIS
from os                     import getcwd


'== CÓDIGO REAL =='


class Caçadora(Aliado):
    def __init__( _ ):
        super().__init__( 'hunter' , "C" , Ventania )

    @staticmethod
    def TIPO() -> Perso:
        return Perso.Caçadora

    @staticmethod
    def cor_assinatura() -> Cor:
        return Cor( 15 , 135 , 40 )

    @texto_decorador(carregar_imagem(Linkzin( getcwd() , 'banco_dados' , 'Personagens' , 'aliados' , 'hunter' , 'idle.png')),Cor(15, 135, 40))
    def falar( _ , frase: str, cor: tuple):
        return frase , cor

    def dialogo_combate( _ , cor = Cor( 0 , 100 , 0 ) ) -> Caixa_Texto:
        return _.falar( _.todas_falas , cor )

    def __repr__( _ ):
        return super().repr_aliado( "A" , "destemida caçadora" , "Atiradora" )


'== TESTES =='


if __name__ == "__main__":
    # Example file showing a basic pygame "game loop"
    import pygame
    from pygame.event   import get as capturar_evento
    from pygame.time    import Clock as Relogio
    from pygame.display import set_mode as definir_janela , set_caption as definir_titulo

    # pygame setup
    pygame.init()
    C = Caçadora()
    '''CC: Caixa_Texto = C.falar('aaaaaaaaaaaaaa',Cor(100,100,100))'''

    CC = C.dialogo_combate()
    
    '''print(type(C.estado_atual))
    print(type(Estado.Idle))
    if C.estado_atual != Estado.Idle:
        print(":(")
    C.estado_atual = Estado.Idle'''
    C - 4
    print(C)

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
                    CC.alt[2] = True
                    
                if event.key == pygame.K_LEFT:
                    CC.alt[1] = True
                
                if event.key == pygame.K_RETURN:
                    CC.alt[0] = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    CC.index += 1
                    
                if event.key == pygame.K_LEFT:
                    CC.index -= 1
    
                if event.key == pygame.K_RETURN:
                    CC.rodando = False
                    
                CC.resetar_cores()

            
        # fill the screen with a color to wipe away anything from last frame
        screen.fill("purple")

        # RENDER YOUR GAME HERE
        
        'C.mostrar_animacao(screen,(100,100))'

        CC(screen)
        
        
        'print(C.ATAQUE)'

        # RENDER YOUR GAME HERE

        # flip() the display to put your work on screen
        pygame.display.flip()

        clock.tick(60)  # limits FPS to 60

    pygame.quit()
    
    

    



