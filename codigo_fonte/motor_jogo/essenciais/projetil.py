from pygame import Surface as Superficie

# SPRITESHEET

'=== CÓDIGO REAL ==='

class Projetil:
    def __init__( _ , coordenadas : tuple, animacao: list):
        # coordenadas -> ((x,y),(x2,y2))
        # animacao    -> [ <Surface(43x48x32 SW)>, <Surface(43x48x32 SW)>, <Surface(43x48x32 SW)>,
        #                  <Surface(43x48x32 SW)>, <Surface(43x48x32 SW)>, <Surface(43x48x32 SW)>, 
        #                  <Surface(43x48x32 SW)>, <Surface(43x48x32 SW)>, <Surface(43x48x32 SW)>]
        # index       -> 1 , 2 , 3 , 4 , ...

        _.running       = True
        
        _.animacao      = animacao
        _.__coordenadas = coordenadas

        _.velocidade    = 1
        _.delay_animacao= 0
        _.posicao_atual = _.__coordenadas[0]
        _.__index       = [ 0 , len(_.animacao)-1  ]

    @property
    def index( _ ):
        return _.__index[0]

    @index.setter
    def index( _ , novo_index ):
        _.__index[0] = novo_index

        if _.__index[0] > _.__index[1]:
            _.__index[0] = 0 

    @property
    def coordenadas( _ ) -> tuple:
        return _.__coordenadas

    @coordenadas.getter
    def começo( _ ) -> tuple:
        return _.__coordenadas[0]

    @coordenadas.getter
    def chegada( _ ) -> tuple:
        return _.__coordenadas[1]

    @coordenadas.getter
    def distancia( _ ) -> tuple:
        return (_.chegada[0] - _.começo[0],
                    _.chegada[1] - _.começo[1])

    @coordenadas.getter
    def aumento( _ )   -> int:
        if _.distancia[0] == 0 and _.distancia[1] == 0: # é um projetil imovel
            return ( 0, 0 )             # não vai a lugar nenhum                                                            
        elif _.distancia[0] == 0:   # é uma linha reta horizontal
            return ( 0 , _.velocidade ) # só vai pra horizontal
        elif _.distancia[1] == 0: # é uma linha reta vertical
            return ( _.velocidade , 0 ) # só vai pra vertical

    def animar( _ , screen: Superficie , index = 0):
        # coordenada_expecifica -> (x, y) / ex: ( 100 , 100)
        # index -> 0 , 1 , 2 , ...
        _.index = index

        screen.blit(_.animacao[_.index],
                        _.posicao_atual)


    def __call__( _ , screen: Superficie, delay = 1):
        if _.running:
            _.animar( screen , _.index )

            novo_aumento = _.aumento
            _.posicao_atual = ( _.posicao_atual[0] + novo_aumento[0] , _.posicao_atual[1] + novo_aumento[1] )

            if _.posicao_atual == _.chegada:
                _.running = False
                _.index   = 0
                _.posicao_atual = _.começo
            else:
                _.delay_animacao += 1

                if _.delay_animacao == delay:
                    _.index += 1

                    _.delay_animacao = 0

    def __repr__( _ ):
        return f"Projetil( posicao = {_.posicao_atual} II animação = {_.animacao[_.index]} )"


'=== TESTES ==='


if __name__ == "__main__":
    # Example file showing a basic pygame "game loop"
    import pygame

    # pygame setup
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))

    pygame.display.set_caption("IntroBattle")

    clock = pygame.time.Clock()
    running = True

    
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

    

        # flip() the display to put your work on screen
        pygame.display.flip()

        clock.tick(60)  # limits FPS to 60

    pygame.quit()

