from sys import path as caminho
from pathlib import Path as Caminhozão

arquivo = Caminhozão(__file__).resolve()
parente , raiz = arquivo.parent, arquivo.parents[1]
caminho.append(str(raiz))

try:
    # CELEBRO -- CRIADORES
    from codigo_battle      import Printar_Opções 
    from codigo_battle      import Criar_Batalha
    from codigo_battle      import Printar_Seleção_Perso as PSP
    from codigo_battle      import Printar_Combatentes
    from codigo_battle      import Printar_Chefao

    # PERSONAGENS
    from codigo_battle      import Paladino,Ladino,Suporte,Caçadora,Maga
    from codigo_battle      import Esqueleto, Lady_Medusa

    # INTERAÇÃO USER
    from codigo_battle      import Menu_Inicial , Criar_Menu_inicial
    from codigo_battle      import Selecionar_Personagens , Pausa_Personagens
    from codigo_battle      import Enfrentar_Inimigos , criar_chefona , criar_esqueletos , criar_lacaios
    from codigo_battle      import Conclusao
except ModuleNotFoundError:
    # CELEBRO -- CRIADORES
    from .codigo_battle      import Printar_Opções 
    from .codigo_battle      import Criar_Batalha
    from .codigo_battle      import Printar_Seleção_Perso as PSP
    from .codigo_battle      import Printar_Combatentes
    from .codigo_battle      import Printar_Chefao

    # PERSONAGENS
    from .codigo_battle      import Paladino,Ladino,Suporte,Caçadora,Maga
    from .codigo_battle      import Esqueleto, Lady_Medusa

    # INTERAÇÃO USER
    from .codigo_battle      import Menu_Inicial , Criar_Menu_inicial
    from .codigo_battle      import Selecionar_Personagens , Pausa_Personagens
    from .codigo_battle      import Enfrentar_Inimigos , criar_chefona , criar_esqueletos , criar_lacaios
    from .codigo_battle      import Conclusao

# PYGAME
import pygame
from pygame             import Surface  as Superficie, Color as Cor, Rect as Retangulo
from pygame             import QUIT as SAIR_X , K_RETURN as ENTER , KEYUP
from pygame.event       import Event , event_name


'=== CÓDIGO REAL ==='

class Fluxo_Jogo:
    def __init__( _ , screen : Superficie) -> None:
        _.screen : Superficie = screen
        _.rodando_jogo : bool = True
        
        _.lista_acoes_aliadas = [] # armazen das acoes que os aliados vão fazer
        
        _.batalha = Criar_Batalha( tuple() , tuple() )
        _.CMI = Criar_Menu_inicial( _.screen )

    @staticmethod
    def cor_placeholder():
        return Cor( 80 , 80 , 80 ) # só existe para ser trocado por outra cor

    @property
    def dificuldade_jogo( _ ):
        return _.CMI.dificuldade
    
    @property
    def aliados_escolhidos( _ ):
        return _.batalha.aliados

    @aliados_escolhidos.setter
    def aliados_escolhidos( _ , novos_aliados):
        _.batalha.aliados = novos_aliados

    @property
    def inimigos_escolhidos( _ ):
        return _.batalha.aliados

    @inimigos_escolhidos.setter
    def inimigos_escolhidos( _ , novos_inimigos ):
        _.batalha.boss = False if len(novos_inimigos) > 1 else True
    
        _.batalha.inimigos = novos_inimigos 

    def Molde_Fluxos( fase ):
        def decorator( _ ) -> bool:
            resultado : Event = fase( _ )

            continuar_rodando = all([a.type != SAIR_X for a in resultado]) # True / False
            _.rodando_jogo = continuar_rodando

            return continuar_rodando
            
        return decorator

    def Molde_Fluxo_Battle( inimigos ):
        def segundo_decorador( fase ):
            def decorator( _ ) -> bool:
                _.inimigos_escolhidos = inimigos()

                resultado : Event = fase( _ )

                _.lista_acoes_aliadas.clear() # só para garantir

                return resultado

            return decorator
            
        return segundo_decorador


    @Molde_Fluxos
    def tela_menu( _ ) -> bool:
        fase : Event = Menu_Inicial( _.screen , _.CMI)

        _.CMI.ativo = True # caso o loop volte

        return fase

    @Molde_Fluxos
    def selecionando_aliados( _ ) -> bool:
        opcoes  = Printar_Opções(Cor(100,100,175),("1",'2','3','4','5'), Retangulo(50,100,*PSP.tamanho_estrutura()),250)
        psp     = PSP()
        aliados_escolhidos = []

        fase : Event = Pausa_Personagens( _.screen, [ 
                    opcoes  ,
                    psp , 
                    aliados_escolhidos ])

        if all([a.type != SAIR_X for a in fase]):
            fase : Event = Selecionar_Personagens(_.screen, [ 
                    opcoes  ,
                    psp , 
                    aliados_escolhidos ])

        _.aliados_escolhidos = tuple(aliados_escolhidos)

        return fase

    @Molde_Fluxos
    @Molde_Fluxo_Battle( inimigos= criar_esqueletos )
    def inimigos_easy( _ ) -> bool:
        opcoes      = Printar_Opções( _.cor_placeholder() )
        escolher    = Printar_Combatentes()
        
        fase : Event = Enfrentar_Inimigos(_.screen,( 
                    _.batalha,
                    opcoes,
                    _.lista_acoes_aliadas, 
                    escolher ))

        return fase

    @Molde_Fluxos
    @Molde_Fluxo_Battle( inimigos = criar_lacaios )
    def inimigos_medio( _ ) -> bool:
        opcoes      = Printar_Opções( _.cor_placeholder() )
        escolher    = Printar_Combatentes()
        
        fase : Event = Enfrentar_Inimigos(_.screen,( 
                    _.batalha,
                    opcoes,
                    _.lista_acoes_aliadas, 
                    escolher ))

        return fase

    @Molde_Fluxos
    @Molde_Fluxo_Battle( inimigos = criar_chefona )
    def chefao_hard( _ ) -> bool:
        opcoes      = Printar_Opções( _.cor_placeholder() )
        escolher    = Printar_Chefao()

        fase : Event = Enfrentar_Inimigos(_.screen,(
                    _.batalha,
                    opcoes,
                    _.lista_acoes_aliadas, 
                    escolher))

        return fase

    def tela_final( _ , vitoria = True ) -> bool:
        fase = Conclusao(_.screen , ( _.aliados_escolhidos , vitoria , _.dificuldade_jogo ))

        resultado_fase = [fases.type for fases in fase]
        if KEYUP in resultado_fase:
            return None

        return all([resul != SAIR_X for resul in resultado_fase])

    
    def __call__( _ ) -> None:
        fases_iniciais = [ _.tela_menu , _.selecionando_aliados ]
        fases_batalha  = [ _.inimigos_easy , _.inimigos_medio , _.chefao_hard ]
        while _.rodando_jogo:
            for fase in fases_iniciais:
                continuar = fase()

                if continuar == False:
                    break
        
            limite_dificuldade = -1 if continuar else 999
            for fase in fases_batalha:
                limite_dificuldade += 1

                if _.dificuldade_jogo >= limite_dificuldade:
                    continuar = fase()

                    if _.batalha.vitoria:
                        continue

                    break
                            
            if continuar == True:
                continuar = _.tela_final( vitoria = _.batalha.vitoria )

            if continuar == None:
                continue
            elif continuar == False:
                break
            

'=== TESTES ==='


if __name__ == "__main__":
    from   pygame.display     import set_mode as definir_janela , set_caption as definir_titulo
    import pygame

    # pygame setup
    pygame.init()
    

    screen = definir_janela((1280, 720))
    definir_titulo("IntroBattle")

    fluxo = Fluxo_Jogo(screen)

    fluxo()
    

    pygame.quit()