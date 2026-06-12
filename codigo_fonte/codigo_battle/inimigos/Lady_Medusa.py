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
from json                       import load     as carregar_json


'== CÓDIGO REAL =='


class Lady_Medusa(Inimigo):
    def __init__( _ ):
        super().__init__( ('Lady Medusa',) , "B" )

        with open(Linkzin( getcwd() , 'roteiro' , 'dialogos_perso.json') , 'r' , encoding="utf-8" ) as status:
            _.todas_falas = carregar_json(status)[1]["B"]

    @staticmethod
    def cor_assinatura() -> Cor:
        return Cor( 135 , 135 , 135 )

    @texto_decorador(carregar_imagem(Linkzin( getcwd() , 'banco_dados' , 'Personagens' , 'inimigos' , 'Lady Medusa' , 'idle.png')),Cor(135, 135, 135))
    def falar( _ , frase: str, cor: tuple):
        return frase , cor

    def julgamento_final( _ , dificuldade : int ) -> Caixa_Texto:
        cor = [ Cor( 180 , 0 , 0 ), Cor( 180 , 180 , 0 ) , Cor( 0 , 180 , 0 ) ][dificuldade]

        return _.falar( _.todas_falas[dificuldade] , cor )
        
    def __repr__( _ ):
        return super().repr_inimigo( "A" , "tirana narcisista" , "A chefona foi destronada" )


'== TESTES =='


if __name__ == "__main__":
    '''B = Lady_Medusa()
    B - 10
    print(B)'''

    with open(Linkzin( getcwd() , 'roteiro' , 'dialogos_perso.json') , 'r' ,encoding="utf-8" ) as status:
        frase_completa = carregar_json(status)[1]["B"]

        print(frase_completa[0])

    print(Linkzin( getcwd() , 'roteiro' , 'dialogos_perso.json' ))

    '''# Example file showing a basic pygame "game loop"
    import pygame
    from pygame.event   import get as capturar_evento
    from pygame.time    import Clock as Relogio
    from pygame.display import set_mode as definir_janela , set_caption as definir_titulo
    
    # pygame setup
    pygame.init()
    C = Lady_Medusa()
    CC: Caixa_Texto = C.falar('aaaaaaaaaaaaaa',Cor(100,100,100))
    C.estado_atual = Estado.Idle
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
        
        C.mostrar_animacao(screen,(100,100),(111,207))
        
        # RENDER YOUR GAME HERE

        # flip() the display to put your work on screen
        pygame.display.flip()

        clock.tick(60)  # limits FPS to 60

    pygame.quit()'''
    
    

    



