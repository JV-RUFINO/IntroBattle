from sys import path as caminho
from pathlib import Path as Caminhozão

arquivo = Caminhozão(__file__).resolve()
parente , raiz = arquivo.parent, arquivo.parents[1]
caminho.append(str(raiz))


# ESSENCIAIS
from battle_exterior    import Personagem , Projetil

# PYGAME
from pygame             import Surface  as Superficie , Rect as Retangulo
from pygame.font        import Font     as Fonte
from pygame.transform   import scale    as transformar_escala

# IMPORTAÇÕES GERAIS
from os.path            import join
from os                 import getcwd


'=== CÓGIGO REAL ==='


class Animacao:
    def __init__( _ , aliado : Personagem , inimigo : Personagem , alvo : int , dano: int ):
        _.running    = True
        
        _.aliado     = aliado
        _.inimigo    = inimigo
        
        _.alvo       = alvo
        _.dano       = str( dano )

        _.velocidade = 8

    @staticmethod
    def fonte(tamanho = 64):
        return Fonte(join(getcwd(),'fonte_jogo',"fontePygame.ttf") , tamanho )

    @staticmethod
    def posicoes_iniciais() -> list:
        return (
            (320,250), # ALIADO
            (800,250)) # INIMIGO

    @staticmethod
    def tamanho(boss = False) -> tuple:
        return (150,150) if boss == False else (200,200)

    @property
    def alvo_perso( _ ) -> Personagem :
        return [ _.aliado , _.inimigo ][_.alvo]

    @property
    def autor_perso( _ ) -> Personagem:
        autor = 0 if 1 == _.alvo else 1

        return [ _.aliado , _.inimigo ][autor]

    def texto_acima( _ , screen : Superficie , nome : str) -> None:
        screen.blit( 
                _.fonte().render( nome , 
                            True , _.aliado.cor_assinatura() ) , 
                            Retangulo( screen.get_height()/2 , screen.get_width()/10 , 0 , 0))

    def mostrar_personagens( _ , screen : Superficie , posicoes: tuple , boss: bool) -> None:
        _.aliado.mostrar_animacao(  screen  , posicoes[0] , _.tamanho()     )
        _.inimigo.mostrar_animacao( screen  , posicoes[1] , _.tamanho(boss) )

    def mostrar_dano( _ , screen : Superficie , posicoes: tuple ) -> None:
        texto = _.dano          if _.alvo_perso.vida >= int(_.dano) else "MORTO"
        cor   = (150,150,150)   if _.alvo_perso.vida >= int(_.dano) else (150 ,0 ,0)

        screen.blit( 
                _.fonte(tamanho = 32).render( texto , 
                            True , cor , (0 ,0 ,0)) , 
                            Retangulo( posicoes[0] + 50 , posicoes[1] + 220 , 0 , 0 ))

    def __bool__( _ ):
        return _.running

    def __call__( _ , screen : Superficie , nome_ataque: str , posicoes: tuple , boss: bool = False) -> None:
        if _.running:
            _.texto_acima(          screen ,            nome_ataque )
            _.mostrar_personagens(  screen , posicoes , boss )
            _.mostrar_dano(         screen , posicoes[_.alvo] )

    def __repr__( _ ) -> str:
        return f'Animar( aliado = {_.aliado} & inimigo = {_.inimigo} / dano = {_.dano} & alvo = {[_.aliado,_.inimigo][_.alvo]} )'
            


class Anim_AtkBasico(Animacao):
    def __init__(_, aliado: Personagem, inimigo: Personagem , alvo : Personagem):
        super().__init__(aliado, inimigo, None , 0 )
        
        _.alvo = 0 if alvo == aliado else 1
        _.dano = str( _.alvo_perso.reducao_dano( _.autor_perso.dano_basico ) )

        _.direcao_frente = True 
        _.limite = 40

        _.__index = 1

    @property
    def index( _ ) -> int:
        return _.__index

    @index.setter
    def index( _ , novo_index ):
        _.__index = novo_index

        if _.limite <= _.__index and _.direcao_frente:
            _.direcao_frente = False

    @property
    def pos_ali( _ ) -> tuple:
        return ( _.posicoes_iniciais()[0][0] + ( _.velocidade * _.index ),
                        _.posicoes_iniciais()[0][1]) if _.alvo == 1 else _.posicoes_iniciais()[0]

    @property
    def pos_ini( _ ) -> tuple:
        return ( _.posicoes_iniciais()[1][0] - ( _.velocidade * _.index ),
                        _.posicoes_iniciais()[1][1]) if _.alvo == 0 else _.posicoes_iniciais()[1]

    def __call__( _ , screen: Superficie , boss = False):
        super().__call__( screen , "ATK. BASICO" , ( _.pos_ali , _.pos_ini ) , boss )

        if _.running:
            if _.direcao_frente:
                _.index += 3
            else:
                _.index -= 2

        if 0 >= _.index:
            _.running = False

    def __repr__( _ ) -> str:
        return super().__repr__()        

class Anim_Magia(Animacao):
    def __init__(_, aliado: Personagem, inimigo: Personagem , placeholder = None):
        super().__init__( aliado , inimigo , 1 , 0)

        _.dano = str( inimigo.reducao_dano( aliado.dano_magia ))

        _.nome_magia :str  = _.autor_perso.magia_imagem.nome
        _.magia : Projetil = _.autor_perso.magia_imagem.mostrar_animacao(((440,250),(720,250)))

        _.magia.velocidade = _.velocidade
        for a in range(len(_.magia.animacao)):
            _.magia.animacao[a] = transformar_escala(_.magia.animacao[a],(120,120))
    

    def __call__( _ , screen : Superficie , boss: bool = False):
        super().__call__( screen , _.nome_magia , ( _.posicoes_iniciais()[0] , _.posicoes_iniciais()[1] ) , boss )

        if _.magia.running:
            _.magia( screen , 3 )

        else:
            _.running = False

    def __repr__( _ ) -> str:
        return super().__repr__()


'=== TESTES ==='


if __name__ == "__main__":
    # Example file showing a basic pygame "game loop"
    import pygame
    from aliados            import Maga 
    from inimigos           import Esqueleto , Lady_Medusa
    from battle_exterior    import Linkzin

    # pygame setup
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))

    pygame.display.set_caption("IntroBattle")

    clock = pygame.time.Clock()
    running = True

    personagens = ( Maga() , Lady_Medusa() )
    anim = Anim_AtkBasico(*personagens, personagens[1] )

    '''print(anim.aliado)
    print(anim.inimigo)
    print([ anim.inimigo , anim.aliado ][anim.alvo])'''

    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # fill the screen with a color to wipe away anything from last frame
        screen.fill("purple")
        # RENDER YOUR GAME HERE

        screen.blit(
                    pygame.transform.scale(pygame.image.load(Linkzin('banco_dados','Cenarios','cena_battle.png')),(1280, 720)),
                    (0,0))

        anim(screen,boss=True)

        

        # flip() the display to put your work on screen
        pygame.display.flip()

        clock.tick(60)  # limits FPS to 60

    pygame.quit()

