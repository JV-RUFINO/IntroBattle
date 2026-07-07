from sys import path as caminho
from pathlib import Path as Caminhozão

arquivo = Caminhozão(__file__).resolve()
parente , raiz = arquivo.parent, arquivo.parents[1]
caminho.append(str(raiz))

# CRIADORES BATALHA
from criadores_batalha.criar_fase           import Criar_Fase , Fase_Componentes as FC
from criadores_batalha.printar_personagens  import Printar_Seleção_Perso as PSP
from criadores_batalha.criar_opcoes         import Printar_Opções

# PERSONAGENS
from aliados.Caçadora import Caçadora
from aliados.Ladino   import Ladino
from aliados.Maga     import Maga
from aliados.Paladino import Paladino
from aliados.Suporte  import Suporte

# ESSENCIAIS
from battle_exterior import Perso

# PYGAME
import pygame
from pygame             import Surface  as Superficie, Color as Cor, Rect as Retangulo
from pygame             import KEYUP    as TECLA_APERTADA, K_LEFT as ESQUERDA , K_RIGHT as DIREITA, QUIT as SAIR_X , K_RETURN as ENTER
from pygame.event       import Event

'=== CÓDIGO REAL ==='

def todos_combatentes():
    return {
        Perso.Paladino: Paladino()  ,
        Perso.Ladino  : Ladino()    ,
        Perso.Caçadora: Caçadora()  ,
        Perso.Maga    : Maga()      ,
        Perso.Suporte : Suporte()
        }

@Criar_Fase('teste 3 ps')
def Selecionar_Personagens(
            screen :Superficie, 
                info_extra = None,
                    index : FC = None,
                        eventos:list = None):

    opcoes  : Printar_Opções = info_extra[0]
    psp     : PSP            = info_extra[1]
    armazen : list           = info_extra[2]
    pausa   : bool           = info_extra[3]

    if pausa:
        info_extra[3] : bool = False # pausa = False

        index[1]

    if len(armazen) >= 3:
        return False
    
    # AGORA SIM VEM O CÓDIGO
    combatente = todos_combatentes()

    opcoes_combatente = [Perso.Paladino,Perso.Ladino,Perso.Caçadora,Perso.Maga,Perso.Suporte]

    # PRINTANDO NA TELA
    cor_assinatura   = combatente[opcoes_combatente[opcoes.contagem]].cor_assinatura()
    opcoes.cor_geral = cor_assinatura
    
    screen.blit( 
            opcoes.fonte().render( f'ESCOLHA SEUS ALIADOS: {len(armazen)}', 
                        False , cor_assinatura ) , Retangulo(380,50,0,0))

    opcoes(screen)

    psp(screen,
        combatente,
        opcoes.contagem,
        armazen)

    # PRINTANDO NA TELA

    return True

@Selecionar_Personagens.Fase_Adicional('teste 7')
def Pausa_Personagens(
            screen :Superficie, 
                info_extra = None,
                    index : FC = None,
                        eventos:list = None):

    opcoes  : Printar_Opções = info_extra[0]
    psp     : PSP            = info_extra[1]
    armazen : list           = info_extra[2]

    for evento in eventos:
        if evento.type == TECLA_APERTADA:
            return False
    
    combatente = todos_combatentes()

    psp(screen,
        combatente,
        opcoes.contagem ,
        armazen)

    for numero in range(100,601,100):
        screen.blit( 
            opcoes.fonte().render( f'APERTE QUALQUER TECLA PARA CONTINUAR', 
                        True , opcoes.cor_borda_alt , opcoes.cor ) , Retangulo( 150 , numero , 0 , 0 ))

    return True

@Selecionar_Personagens.Fase_Evento( tipo_evento= ENTER )
def Enter_Personagens(
            screen :Superficie, 
                info_extra = None,
                    index : FC = None,
                        eventos:Event = None):

    opcoes  : Printar_Opções = info_extra[0]
    armazen : list           = info_extra[2]

    if index.index == 0:
        combatente = todos_combatentes()

        opcoes_combatente = [Perso.Paladino,Perso.Ladino,Perso.Caçadora,Perso.Maga,Perso.Suporte]

        personagem_escolhido : Perso = opcoes_combatente[opcoes.contagem]

        if all(personagem.TIPO() != personagem_escolhido for personagem in armazen):
            armazen.append(combatente[personagem_escolhido])

    return False

@Selecionar_Personagens.Fase_Evento( tipo_evento= TECLA_APERTADA )
def Mudar_Personagem(
            screen :Superficie, 
                info_extra = None,
                    index : FC = None,
                        eventos:Event = None):

    opcoes  : Printar_Opções = info_extra[0]

    if index.index == 0:
        if eventos in [ESQUERDA,DIREITA]:     # [ pygame.K_LEFT , pygame.K_RIGHT ] 
            opcoes.mudar_selecionado( eventos )    
    
    return False

'=== TESTES ==='


if __name__ == "__main__":
    from   pygame.display     import set_mode as definir_janela , set_caption as definir_titulo
    import pygame

    # pygame setup
    pygame.init()
    

    screen = definir_janela((1280, 720))
    definir_titulo("IntroBattle")


    opcoes  = Printar_Opções(Cor(100,100,175),("1",'2','3','4','5'), Retangulo(50,100,200,500),250)
    psp     = PSP()
    armazen = []
    pausa   = True

    'Pausa_Personagens(screen, [opcoes,psp,armazen])'

    Selecionar_Personagens( screen , [opcoes , psp , armazen , pausa])

    'print(armazen)'

    pygame.quit()