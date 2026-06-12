from sys import path as caminho
from pathlib import Path as Caminhozão

arquivo = Caminhozão(__file__).resolve()
parente , raiz = arquivo.parent, arquivo.parents[1]
caminho.append(str(raiz))

# ESSENCIAIS
from perso_exterior      import Stat
from perso_exterior      import Linkzin
from perso_exterior      import Condicao

# ABSTRATOS
from abstrato.status     import Status


'=== CÓDIGO REAL ==='


class Ataque(Status):
    def __init__( _ , numero: int ):
        super().__init__(  )

        _.caminho = Linkzin( _.caminho , 'ATAQUE' )
        _.__numero = [numero,numero]

    @staticmethod
    def TIPO() -> Stat:
        return Stat.ATAQUE
    
    @property
    def numero( _ ) -> int:
        return _.__numero[0]

    @numero.setter
    def numero( _ , novo_numero):
        _.__numero[0] = novo_numero
        backup        = _.__numero[1]

        nova_condicao = Condicao.Estavel
        if _.numero   > backup:
            nova_condicao = Condicao.Buffado
        elif _.numero < backup:
            nova_condicao = Condicao.Nerfado

        _.condicao = nova_condicao

    @property
    def niveis_status( _ ) -> list:
        return super().niveis_status

    def mostrar_imagem( _ ):
        return super().mostrar_imagem( )


'=== TESTES ==='

if __name__ == "__main__":
    """from os import path, getcwd
    from pygame import image

    def Linkzin(*path_pasta, act_dir = False) -> str: # criar um link igual o Windows Explorer faz
        " Linkzin( 'um' , 'dois' , 'quatro' ) -> 'um\dois\quatro' "
        
        if act_dir:
            current_dir = path.split( getcwd() )
            path_pasta = current_dir + path_pasta
        
        return path.join(*path_pasta)

    # Example file showing a basic pygame "game loop"
    import pygame

    # pygame setup
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))

    pygame.display.set_caption("IntroBattle")

    clock = pygame.time.Clock()
    running = True

    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # fill the screen with a color to wipe away anything from last frame
        screen.fill("purple")
        # RENDER YOUR GAME HERE

        
        img   = image.load(Linkzin(getcwd(),'codigo_fonte','essenciais','Fire Breath hit effect SpriteSheet.png'))
        'img_2 = carregar_tira(img,(0,0,40,40),3,-1)'

        '''print(img_2)

        screen.blit(img_2[0],(100,100))'''


        # flip() the display to put your work on screen
        pygame.display.flip()

        clock.tick(60)  # limits FPS to 60

    pygame.quit()"""