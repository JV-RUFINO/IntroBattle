from sys import path as caminho
from pathlib import Path as Caminhozão

arquivo = Caminhozão(__file__).resolve()
parente , raiz = arquivo.parent, arquivo.parents[1]
caminho.append(str(raiz))

# CODIGO COPIADO
from battle_exterior            import imagem_unica
from battle_exterior            import Linkzin

# ESSENCIAIS
from battle_exterior            import Caixa_Texto , texto_decorador

# ALIADOS
from battle_exterior            import Inimigo

# PYGAME
from pygame                     import Surface  as Superficie , Color as Cor , Rect as Retangulo
from pygame.image               import load     as carregar_imagem
from pygame.transform           import scale    as imagem_escala

# IMPORTAÇÕES GERAIS
from os                         import getcwd


'== CÓDIGO REAL =='


class Lacaios_Desalmados(Inimigo):
    def __init__(_, especializacao : str , elite = False):
        _.__especializacao = especializacao # arqueiros , brutos , espadachins , lanceiros , soldados
        palavra_chave = 'cinza' if elite == False else 'elite'

        super().__init__( ('lacaios_desalmados', especializacao , palavra_chave) , f"L-{especializacao}" )

        # STATUS DO PERSONAGEM
        
        for stat in _.STATUS:
            _.STATUS[stat].numero += 0 if elite == False else 1

    @staticmethod
    def cor_assinatura() -> Cor:
        return Cor( 100 , 100 , 100 )

    @texto_decorador(carregar_imagem(Linkzin( getcwd() , 'banco_dados' , 'Personagens' , 'inimigos' , 'Lady Medusa' , 'idle.png')),Cor(135, 135, 135))
    def falar( _ , frase: str, cor: tuple) -> Caixa_Texto:
        return frase , cor

    def mostrar_animacao(_, screen: Superficie, coordenadas: tuple, escala: tuple = None):
        numero_escala = escala if escala != None else ( 30 , 30 )

        nova_imagem = imagem_escala( 
                imagem_unica( _.imagem_atual , Retangulo( 126 , 0 , 18 , 20 ) , -1) ,
                        numero_escala )
        
        return screen.blit(nova_imagem , coordenadas)

    def __repr__( _ ):
        return super().repr_inimigo( "Os" , f"{_.__especializacao} sem alma nem coração" , "Lacaio bom é lacaio morto" )


'== TESTES =='


if __name__ == "__main__":
    '''# Example file showing a basic pygame "game loop"
    import pygame
    from pygame.event   import get as capturar_evento
    from pygame.time    import Clock as Relogio
    from pygame.display import set_mode as definir_janela , set_caption as definir_titulo
    
    # pygame setup
    pygame.init()
    C = Lacaios_Desalmados('lanceiros' , False)
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
        
        'C.mostrar_animacao(screen,(100,100),(100,100))'
        CC(screen)
        
        # RENDER YOUR GAME HERE

        # flip() the display to put your work on screen
        pygame.display.flip()

        clock.tick(60)  # limits FPS to 60

    pygame.quit()'''
    
    a = {}

    a.update({"A":1})

    a.update({"A":a["A"]+2})
    print(a)

    



