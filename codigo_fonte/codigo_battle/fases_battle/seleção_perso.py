from sys import path as caminho
from pathlib import Path as Caminhozão

arquivo = Caminhozão(__file__).resolve()
parente , raiz = arquivo.parent, arquivo.parents[1]
caminho.append(str(raiz))

# CRIADORES BATALHA
from criadores_batalha.criar_fase           import Criar_Fase
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


@Criar_Fase(Criar_Fase.caminho_comum(),'teste 7.png')
def Pausa_Personagens(
            screen :Superficie, 
                info_extra = None,
                    eventos:list = None):

    opcoes  : Printar_Opções = info_extra[0]
    psp     : PSP            = info_extra[1]
    armazen : list           = info_extra[2]

    combatente = {
                Perso.Paladino: Paladino()  ,
                Perso.Ladino  : Ladino()    ,
                Perso.Caçadora: Caçadora()  ,
                Perso.Maga    : Maga()      ,
                Perso.Suporte : Suporte()
                }

    psp(screen,
        combatente,
        opcoes.contagem ,
        armazen)

    screen.blit( 
            opcoes.fonte().render( f'APERTE QUALQUER TECLA PARA CONTINUAR', 
                        True , opcoes.cor_borda_alt , opcoes.cor ) , Retangulo(150,200,0,0))
    
    screen.blit( 
            opcoes.fonte().render( f'APERTE QUALQUER TECLA PARA CONTINUAR', 
                        True , opcoes.cor_borda_alt , opcoes.cor ) , Retangulo(150,300,0,0))

    screen.blit( 
            opcoes.fonte().render( f'APERTE QUALQUER TECLA PARA CONTINUAR', 
                        True , opcoes.cor_borda_alt , opcoes.cor ) , Retangulo(150,400,0,0))

    for event in eventos:
        event: Event

        if event.type == SAIR_X:                    # pygame.QUIT
            return False

        if event.type == TECLA_APERTADA:            # pygame.KEY_UP
            return False

    return True

@Criar_Fase(Criar_Fase.caminho_comum(),'teste 3 ps.png')
def Selecionar_Personagens(
            screen :Superficie, 
                info_extra = None,
                    eventos:list = None):

    opcoes  : Printar_Opções = info_extra[0]
    psp     : PSP            = info_extra[1]
    armazen : list           = info_extra[2]

    if len(armazen) >= 3:
        return False
    
    # AGORA SIM VEM O CÓDIGO
    combatente = {
                Perso.Paladino: Paladino()  ,
                Perso.Ladino  : Ladino()    ,
                Perso.Caçadora: Caçadora()  ,
                Perso.Maga    : Maga()      ,
                Perso.Suporte : Suporte()
                }

    opcoes_combatente = [Perso.Paladino,Perso.Ladino,Perso.Caçadora,Perso.Maga,Perso.Suporte]

    for event in eventos:
        event: Event

        if event.type == SAIR_X:                    # pygame.QUIT
            return False

        if event.type == TECLA_APERTADA:            # pygame.KEY_UP
            if event.key in [ESQUERDA,DIREITA]:     # [ pygame.K_LEFT , pygame.K_RIGHT ] 
                opcoes.mudar_selecionado( event.key )    
            
            elif event.key == ENTER:                # pygame.RETURN
                personagem_escolhido : Perso = opcoes_combatente[opcoes.contagem]

                if all(personagem.TIPO() != personagem_escolhido for personagem in armazen):
                    armazen.append(combatente[personagem_escolhido])

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

    'Pausa_Personagens(screen, [opcoes,psp,armazen])'

    Selecionar_Personagens( screen , [opcoes , psp , armazen])

    print(armazen)

    pygame.quit()