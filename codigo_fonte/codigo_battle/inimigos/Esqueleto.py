from sys import path as caminho
from pathlib import Path as Caminhozão

arquivo = Caminhozão(__file__).resolve()
parente , raiz = arquivo.parent, arquivo.parents[1]
caminho.append(str(raiz))

# ESSENCIAIS
from battle_exterior            import Caixa_Texto , texto_decorador
from battle_exterior            import Linkzin

# ALIADOS
from battle_exterior            import Inimigo

# PYGAME
from pygame                     import Color    as Cor
from pygame.image               import load     as carregar_imagem

# IMPORTAÇÕES GERAIS
from os                         import getcwd


'== CÓDIGO REAL =='


class Esqueleto(Inimigo):
    def __init__( _ ):
        super().__init__( ('caveira',) , "E" )

    @staticmethod
    def cor_assinatura() -> Cor:
        return Cor( 135 , 135 , 135 )

    @texto_decorador(carregar_imagem(Linkzin( getcwd() , 'banco_dados' , 'Personagens' , 'inimigos' , 'caveira' , 'idle.png')),Cor(135, 135, 135))
    def falar( _ , frase: str, cor: tuple) -> Caixa_Texto:
        return frase , cor

    def __repr__( _ ):
        return super().repr_inimigo( "O" , "morto-vivo" , "Esqueleto enfim voltou a dormir" )


'== TESTES =='


if __name__ == "__main__":
    E = Esqueleto()
    print(E.vida)
    E - 1

    print(E)

    '''# Example file showing a basic pygame "game loop"
    import pygame
    from pygame.event   import get as capturar_evento
    from pygame.time    import Clock as Relogio
    from pygame.display import set_mode as definir_janela , set_caption as definir_titulo
    
    # pygame setup
    pygame.init()
    C = Esqueleto()
    CC: Caixa_Texto = C.falar('aaaaaaaaaaaaaa',Cor(100,100,100))
    C.estado_atual = Estado.Selecionada
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
        
        CC(screen)
        
        # RENDER YOUR GAME HERE

        # flip() the display to put your work on screen
        pygame.display.flip()

        clock.tick(60)  # limits FPS to 60

    pygame.quit()'''
    
    

    



