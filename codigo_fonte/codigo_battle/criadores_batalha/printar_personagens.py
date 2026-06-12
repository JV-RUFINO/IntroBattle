from sys import path as caminho
from pathlib import Path as Caminhozão

arquivo = Caminhozão(__file__).resolve()
parente , raiz = arquivo.parent, arquivo.parents[1]
caminho.append(str(raiz))

# ESSENCIAIS
from battle_exterior    import Estado , Perso

# CÓDIGO COPIADO
from battle_exterior    import Linkzin

# PERSONAGENS
from battle_exterior    import Personagem

# PYGAME
from pygame             import Surface  as Superficie 
from pygame.event       import Event
from pygame             import K_UP     as CIMA , K_DOWN as BAIXO
from pygame.transform   import scale    as imagem_escala
from pygame.image       import load     as carregar_imagem

# IMPORTAÇÕES GERAIS



'=== CÓGIGO REAL ==='


class Printar:
    def __init__( _ , aliados_max : int , inimigos_max : int):
        _.escolher_alvos    = None  # ALIADOS = FALSE / INIMIGOS = TRUE / NENHUM = NONE
        
        _.maximo_aliado     = aliados_max
        _.maximo_inimigo    = inimigos_max
        
        _.index_selecionada = 0

    @staticmethod
    def tamanho() -> tuple:
        ...

    @staticmethod
    def posicao() -> tuple:
        ...

    '''@property
    def contagem( _ ):
        estados = _.inimigos_estados if _.escolher_alvos else _.aliados_estados

        estados[_.CONTAGEM] = Estado.Selecionada 

        return _.CONTAGEM'''

    @property
    def alvos_idle( _ ):
        return _.escolher_alvos == None

    def mudar_selecionado( _ , evento : Event ):
        if evento == BAIXO:
            resultado = 1
        elif evento == CIMA:
            resultado = -1
        
        _.index_selecionada += resultado

        maximo = _.maximo_inimigo - 1 if _.escolher_alvos else _.maximo_aliado - 1 

        if _.index_selecionada > maximo:
            _.index_selecionada = 0
        elif _.index_selecionada < 0:
            _.index_selecionada = maximo

    @property
    def aliados_estados( _ ):
        return [ Estado.Selecionada if numero == _.index_selecionada else Estado.Escolhivel for numero in range( 0 , _.maximo_aliado ) ]
    
    @property
    def inimigos_estados( _ ):
        return [ Estado.Selecionada if numero == _.index_selecionada else Estado.Escolhivel for numero in range( 0 , _.maximo_inimigo ) ]

    def alterar_escolha( _ , nova_escolha = True):
        _.escolher_alvos = nova_escolha

    def resetar( _ ):
        _.escolher_alvos    = None # ALIADOS = FALSE / INIMIGOS = TRUE / NENHUM = NONE
        _.index_selecionada = 0

    def print_singular( _ , screen:Superficie , alvo: Personagem, numero : int, posicao: int):
        if alvo.vida == 0:
            alvo.estado_atual = Estado.Down

        posicao_alvo : tuple = _.posicao()[posicao][numero] 

        # PRINTANDO O ALVO
        alvo.mostrar_animacao( screen , posicao_alvo, _.tamanho() )
        # PRINTANDO O ALVO

        if alvo.vida > 0:
            alvo.estado_atual = Estado.Idle


    def __call__( _ , screen : Superficie, aliados: tuple , inimigos: tuple ):
        ...


    def __repr__( _ ) -> str:
        ...

class Printar_Combatentes(Printar):
    def __init__( _ ):
        super().__init__( 3 , 3 )

       
    @staticmethod
    def tamanho( ):
        return (80,80)

    @staticmethod
    def posicao( ): # usados para printar as imagens dos aliados e inimigos na tela                       
        return (((300,200),(200,300),(300,400)),            # aliados
                        ((900,200),(1000,300),(900,400)))   # inimigos

    def mudar_selecionado( _ , evento : Event ):
        super().mudar_selecionado( evento )

    @property
    def aliados_estados( _ ):
        return super().aliados_estados
    
    @property
    def inimigos_estados( _ ):
        return super().inimigos_estados

    def alterar_escolha( _ , nova_escolha = True):
        return super().alterar_escolha( nova_escolha )

    def resetar( _ ):
        super().resetar( )
                                    

    def print_singular( _ , screen:Superficie , alvo: Personagem, numero : int, posicao: int):
        super().print_singular( screen , alvo , numero, posicao)

    def __call__( _ , screen : Superficie , aliados: tuple , inimigos: tuple ):
        for numero in range(0,3):
            aliado : Personagem = aliados[numero]  
            inimigo: Personagem = inimigos[numero] 

            if _.escolher_alvos     == True:
                inimigo.estado_atual    = _.inimigos_estados[numero]
            elif _.escolher_alvos   == False:
                aliado.estado_atual     = _.aliados_estados[numero]
            elif _.escolher_alvos   == None:
                aliado.estado_atual     = Estado.Idle
                inimigo.estado_atual    = Estado.Idle
            
            _.print_singular( screen , aliado  , numero , 0 )
            _.print_singular( screen , inimigo , numero , 1 )


    def __repr__( _ ) -> str:
        return f'Printar_Combatentes()'


'=== PRINTAR CHEFÃO ==='


class Printar_Chefao(Printar):
    def __init__(_):
        super().__init__( 3 , 1 )


    @staticmethod
    def tamanho( ):
        return (80,80)

    @staticmethod
    def tamanho_chefe( ):
        return (111,207)

    @staticmethod
    def posicao( ): # usados para printar as imagens dos aliados e inimigos na tela                       
        return (((300,200),(600,400),(900,200)),        # aliados
                    ((600,150)))                        # CHEFE

    def mudar_selecionado( _ , evento : Event ):
        super().mudar_selecionado( evento )

    @property
    def aliados_estados( _ ):
        return super().aliados_estados
    
    @property
    def inimigos_estados( _ ):
        return super().inimigos_estados

    def alterar_escolha( _ , nova_escolha = True):
        return super().alterar_escolha( nova_escolha )

    def resetar( _ ):
        super().resetar( )
                                    
    def print_singular( _ , screen:Superficie , alvo: Personagem, numero : int, posicao: int):
        super().print_singular( screen , alvo , numero, posicao )

    def __call__( _ , screen : Superficie, aliados: tuple , chefe: Personagem ):
        for numero in range(0,3):
            aliado : Personagem = aliados[numero]  

            if _.escolher_alvos   == False:
                aliado.estado_atual     = _.aliados_estados[numero]
            elif _.escolher_alvos   == None:
                aliado.estado_atual     = Estado.Idle
            
            _.print_singular( screen , aliado  , numero , 0 )
            
        # PRINT DO CHEFE
        chefe : Personagem = chefe

        if _.escolher_alvos     == True:
            chefe.estado_atual  = _.inimigos_estados[0]
        elif _.escolher_alvos   == None:
            chefe.estado_atual    = Estado.Idle

        chefe.mostrar_animacao( screen , _.posicao()[1] , _.tamanho_chefe() )

    def __repr__( _ ) -> str:
        return f'Printar_Chefão()'


'=== PRINTAR SELEÇÃO PERSO ==='


class Printar_Seleção_Perso(Printar):
    def __init__( _ ):
        super().__init__( 5 , 0)

        _.__estrutura = carregar_imagem(
                    Linkzin( 'banco_dados' , 'Cenarios' , 'introcomp_menu2.png' , act_dir = True)) 

    @staticmethod
    def tamanho() -> tuple:
        return ( 100 , 100 )

    @staticmethod
    def tamanho_estrutura() -> tuple:
        return ( 200, 590 )

    @staticmethod
    def posicao( ): # usados para printar as imagens dos aliados e das estruturas na tela                       
        return (((100,120),(350,120),(600,120),(850,120),(1100,120)),            # aliados
                        ((50,100),(300,100),(550,100),(800,100),(1050,100)))     # estrutura
    @property
    def aliados_estados( _ ):
        return super().aliados_estados

    def print_singular(_, screen: Superficie, alvo: Personagem, numero: int, posicao: int):
        super().print_singular(screen, alvo, numero, posicao)

    def __call__( _ , screen : Superficie , aliados: dict , index_selecionada: int , aliados_escolhidos: list):
        _.index_selecionada = index_selecionada
        opcoes_totais = [aliados[ally].TIPO() for ally in aliados]

        for numero in range( 0 , _.maximo_aliado ):
            opção_traduzida = opcoes_totais[numero]
            
            aliado : Personagem = aliados[opção_traduzida]  
            if any([aliado.TIPO() == ally_esco.TIPO() for ally_esco in aliados_escolhidos]):
                aliado.estado_atual = _.aliados_estados[numero]
            else:
                aliado.estado_atual = Estado.Down

            screen.blit( imagem_escala( _.__estrutura , _.tamanho_estrutura() ) , _.posicao()[1][numero] )

            _.print_singular( screen , aliado , numero , 0 )

            pos = 140
            for stats in aliado.STATUS:
                status_concreto = aliado.STATUS[stats]

                screen.blit(status_concreto.mostrar_imagem(),
                        (_.posicao()[1][numero][0] + 60   ,
                         _.posicao()[1][numero][1] + pos))

            
                pos += 90


'=== TESTES ==='


if __name__ == "__main__":
    from criar_fase import Criar_Fase
    from pygame import QUIT as SAIR_X
    import pygame
    from aliados import Paladino,Ladino,Maga,Suporte,Caçadora
    from inimigos import Esqueleto , Lady_Medusa

    @Criar_Fase(Criar_Fase.caminho_comum(),'salão.png')
    def teste(
        screen :Superficie, 
                info_extra = None,
                    eventos:list = None):
        for event in eventos:
            if event.type == SAIR_X: # pygame.QUIT
                return False

        BP : Printar_Seleção_Perso    = info_extra[0]
        aliados                       = info_extra[1]
        'inimigos                    = info_extra[1][1]'
        
        '''BP(screen,
            aliados,
            *inimigos)'''

        BP(screen,   # screen -> Surface 
            aliados, # aliados -> dict
            0,       # index_selecionado -> int
            [])      # aliados_escolhidos -> list

        return True

    pygame.init()

    screen = pygame.display.set_mode((1280, 720))

    # CÓDIGO PARA TESTAR


    BP_normal = Printar_Seleção_Perso()
    'personagens = ((Paladino(),Ladino(),Maga()),(Lady_Medusa(),))'

    aliados_estrutura =  {
                Perso.Paladino: Paladino()  ,
                Perso.Ladino  : Ladino()    ,
                Perso.Caçadora: Caçadora()  ,
                Perso.Maga    : Maga()      ,
                Perso.Suporte : Suporte()
                }

    teste(screen, [BP_normal,aliados_estrutura])


    # CÓDIGO PARA TESTAR


    pygame.quit()