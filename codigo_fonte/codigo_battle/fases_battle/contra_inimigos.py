from __future__ import annotations

from sys import path as caminho
from pathlib import Path as Caminhozão

arquivo = Caminhozão(__file__).resolve()
parente , raiz = arquivo.parent, arquivo.parents[1]
caminho.append(str(raiz))

# ESSENCIAIS
from battle_exterior                        import Caixa_Texto

# CELEBRO -- CRIADORES
from criadores_batalha.criar_fase           import Criar_Fase
from criadores_batalha.criar_batalha        import Criar_Batalha
from criadores_batalha.criar_opcoes         import Printar_Opções
from criadores_batalha.printar_personagens  import Printar_Chefao as BP_chefao
from criadores_batalha.anim_batalha         import Anim_AtkBasico , Anim_Magia , Animacao

# PERSONAGENS
from battle_exterior                        import Personagem
from inimigos                               import Esqueleto , Lady_Medusa , Lacaios_Desalmados

# ETIQUETAS
from battle_exterior                        import Combate , Estado

# PYGAME
import pygame
from pygame import Surface as Superficie, QUIT as SAIR_X,Color as Cor
from pygame import K_LEFT as ESQUERDA , K_RIGHT as DIREITA , K_UP as CIMA , K_DOWN as BAIXO , K_RETURN as ENTER, KEYUP as TECLA_APERTADA , KEYDOWN as TECLA_SEGURADA
from pygame.event import Event

# IMPORTAÇÕES GERAIS
import random


'=== CÓDIGO REAL ==='


def criar_esqueletos():
    return ( Esqueleto() , Esqueleto() , Esqueleto() )

def criar_lacaios(elites = (False, True, False)) -> tuple:
    return tuple([
        Lacaios_Desalmados(
                random.choice(['arqueiros','brutos','espadachins','lanceiros','soldados']),
                elitezin) 
        for elitezin in elites])

def criar_chefona():
    return (Lady_Medusa(),)

def traduzir_opcoes(printar_opcoes:Printar_Opções) -> Combate:
    opcao_escolhida     : str   = printar_opcoes.opcao_escolhida # EX: "LUTAR","MAGIA","FALAR","PULAR"
    todas_opcoes        : tuple = Printar_Opções(Cor(0,0,0)).opcoes
    opcoes_traduzidas   : list  = [Combate.Atacar,Combate.Magia,Combate.Falar,Combate.Pular]

    for numero in range(0,len(todas_opcoes)):
        if todas_opcoes[numero] == opcao_escolhida:
            return opcoes_traduzidas[numero]
    
def append_animacao( personagens : tuple , tipo_combate: Combate , inverter = False ) -> Animacao:
    # !HORA DA CENA DE BATALHA!
    if tipo_combate != Combate.Pular:
        if tipo_combate == Combate.Atacar:
            aliado = personagens[0] ; inimigo = personagens[1]
            especialidade   = aliado if inverter else inimigo
            versão_animacao = Anim_AtkBasico

        elif tipo_combate == Combate.Magia:
            especialidade   = None
            versão_animacao = Anim_Magia

        return versão_animacao( *personagens , especialidade ) 

    return None

@Criar_Fase(Criar_Fase.caminho_comum(),'salão.png')
def Enfrentar_Inimigos(
            screen :Superficie, 
                info_extra = None,
                    eventos:list = None):
    for event in eventos:
        if event.type == SAIR_X: # pygame.QUIT
            return False

    # INSIRA O CÓDIGO AQUI

    batalha : Criar_Batalha = info_extra[0] # Criar_Batalha(aliados=(...) , inimigos=(...), boss = False)
    opcoes  : Printar_Opções= info_extra[1] # Printar_Opções(cor_geral=(int,int,int),opcoes = (str,str,...), _Printar_Opções__CONTAGEM=0)
    armazen : list          = info_extra[2] # [(0, <Combate.Atacar: 1>, 0),(1, <Combate.Falar: 3>, None),(2, <Combate.Magia: 2>, 2)] :.Exemplo
    escolha : BP_chefao     = info_extra[3] # BPN([False,0])
    
    if batalha.vitoria == None:
        # PRINTAR OS PERSONAGENS NA TELA
        if batalha.boss:
            escolha(
                    screen,                 # <Surface(...x...x.. SW)>
                    batalha.aliados,        # (Ladino(),Maga(),Suporte()) :.Exemplo
                    *batalha.inimigos)      # (Lady_Medusa())
        else:
            escolha(
                    screen,                 # <Surface(...x...x.. SW)>
                    batalha.aliados,        # (Ladino(),Maga(),Suporte()) :.Exemplo
                    batalha.inimigos)      # ((Esqueleto(),Esqueleto(),Esqueleto()))
        # PRINTAR OS PERSONAGENS NA TELA

        if len(armazen) < 3: 
            aliado_escolhido : Personagem = batalha.aliados[len(armazen)]

            if aliado_escolhido.estado_atual != Estado.Down:
                AtacarMagiaFalarPular : bool = escolha.alvos_idle # True ou False

                eventos_key = [ESQUERDA,DIREITA] if AtacarMagiaFalarPular else [CIMA,BAIXO]
                mexendo     = opcoes if AtacarMagiaFalarPular else escolha

                for event in eventos:
                    event : Event

                    if event.type == TECLA_APERTADA:        # pygame.KEY_UP
                        if event.key in eventos_key: # [ pygame.K_LEFT , pygame.K_RIGHT ] ou [ pygame.K_UP , pygame.DOWN ]
                            mexendo.mudar_selecionado( event.key )    

                        elif event.key == ENTER:            # pygame.RETURN
                            opcao_escolhida : Combate = traduzir_opcoes(opcoes)
                            alteração       = escolha.alterar_escolha if AtacarMagiaFalarPular else escolha.resetar
                            adição          = ( opcao_escolhida , len(armazen) , escolha.index_selecionada )
      
                            if not(all([ AtacarMagiaFalarPular , any([opcao_escolhida == Combate.Atacar , opcao_escolhida == Combate.Magia ])])):
                                armazen.append(adição)

                            if all([opcao_escolhida != Combate.Falar , opcao_escolhida != Combate.Pular]):
                                alteração()

                if AtacarMagiaFalarPular:    
                    # PRINTAR OS BOTÕES NA TELA 
                    opcoes.cor_geral = aliado_escolhido.cor_assinatura()
                    opcoes(screen)
                    # PRINTAR OS BOTÕES NA TELA

            else:
                armazen.append(( Combate.Pular , len(armazen)  , escolha.index_selecionada )) # morto não age 

                
        else:
            mini_fase = Battle( screen , ( armazen , batalha , escolha)) # armazen sempre sai vazio

    else: 
        return False

    # INSIRA O CÓDIGO AQUI

    return True

@Criar_Fase(Criar_Fase.caminho_comum(),'cena_battle.png')
def Battle(
            screen :Superficie, 
                info_extra = None,
                    eventos:list = None):
    for event in eventos:
        event : Event

        if event.type == SAIR_X: # pygame.QUIT
            return False

    armazen : list          = info_extra[0]    # [(Combate.Atacar,0,1),(Combate.Falar,1,None),(Combate.Pular,1,None)]
    batalha : Criar_Batalha = info_extra[1]    # Criar_Batalha(aliados=(..., ... , ...), inimigos=(..., ..., ...), boss=False)
    escolha : BP_chefao     = info_extra[2]


    # RENOMEANDO AS VARIAVEIS
    dec_ali : list = armazen                   # [(Combate.Atacar,0,1),(Combate.Falar,1,None),(Combate.Pular,1,None)]
    dec_ini : list = batalha.decisao_inimiga   # [(Combate.Atacar,0,2),(Combate.Atacar,1,1),(Combate.Atacar,2,0)]
    # RENOMEANDO AS VARIAVEIS

    anim = []
    for individual in batalha.fila: # [Personagem , Personagem , ...] -> EX: [Caçadora , Esqueleto , Paladino, ...]
        individual : Personagem

        if individual.vida > 0:
            # PROCESSANDO A AÇÃO
            inverter           : bool = True if individual in batalha.inimigos else False

            index_autor        : int  = batalha.inimigos.index(individual) if inverter else batalha.aliados.index(individual)
            decisao_individual : list = dec_ini[index_autor]               if inverter else dec_ali[index_autor]

            if decisao_individual[0] == Combate.Falar:
                CC = individual.dialogo_combate()

                Falar( screen , (CC , batalha , escolha))

                continue

            resul = batalha.combate( decisao_individual , inverter = inverter )
            # PROCESSANDO A AÇÃO

            # ADICIONANDO A NOVA ANIMAÇÃO PRO "ANIM"
            aliado  : Personagem = batalha.aliados[ decisao_individual[2]] if inverter else batalha.aliados[ decisao_individual[1]]
            inimigo : Personagem = batalha.inimigos[decisao_individual[1]] if inverter else batalha.inimigos[decisao_individual[2]]

            nova_anim : Animacao = append_animacao( (aliado , inimigo) , decisao_individual[0] , inverter )

            if nova_anim != None:
                anim.append(nova_anim)
            # ADICIONANDO A NOVA ANIMAÇÃO PRO "ANIM"

        for anim_expecifica in anim:
            Cena_Battle(screen , ( anim_expecifica , batalha.boss )) # os que estiverem running.false não vão rodar
        
        # !HORA DA CENA DE BATALHA!

    # LIMPANDO AS AÇÕES
    armazen.clear()
    # LIMPANDO AS AÇÕES

    return False

@Criar_Fase(Criar_Fase.caminho_comum(),'cena_battle.png')
def Cena_Battle(
            screen :Superficie, 
                info_extra = None,
                    eventos:list = None):

    for event in eventos:
        event : Event

        if event.type == SAIR_X: # pygame.QUIT
            return False

    animacao : Animacao = info_extra[0]
    boss     : bool     = info_extra[1]
    if animacao.running:
        animacao(screen , boss = boss)

        return True
    else:
        return False

@Criar_Fase(Criar_Fase.caminho_comum(),'salão.png')
def Falar(
            screen :Superficie, 
                info_extra = None,
                    eventos:list = None):

    CC      : Caixa_Texto    = info_extra[0]
    batalha : Criar_Batalha  = info_extra[1]
    printar : BP_chefao      = info_extra[2]

    for event in eventos:
        event : Event

        if event.type == SAIR_X: # pygame.QUIT
            return False

        if event.type == TECLA_SEGURADA:
            if event.key == DIREITA:
                CC.alt[2] = True
                
            if event.key == ESQUERDA:
                CC.alt[1] = True
            
            if event.key == ENTER:
                CC.alt[0] = True

        if event.type == TECLA_APERTADA:
            if event.key == DIREITA:
                CC.index += 1
                
            if event.key == ESQUERDA:
                CC.index -= 1

            if event.key == ENTER:
                CC.rodando = False
                
            CC.resetar_cores()
    
    
    if CC.rodando:
        CC( screen )

        if type(printar) == BP_chefao:
            printar(
                    screen,                 # <Surface(...x...x.. SW)>
                    batalha.aliados,        # (Ladino(),Maga(),Suporte()) :.Exemplo
                    *batalha.inimigos)      # (Lady_Medusa())
        else:
            printar(
                    screen,                 # <Surface(...x...x.. SW)>
                    batalha.aliados,        # (Ladino(),Maga(),Suporte()) :.Exemplo
                    batalha.inimigos)      # ((Esqueleto(),Esqueleto(),Esqueleto()))

    return CC.rodando


'=== TESTES ==='


if __name__ == "__main__":
    from   pygame.display     import set_mode as definir_janela , set_caption as definir_titulo
    import pygame
    from aliados import Paladino,Ladino,Suporte,Caçadora,Maga

    from criadores_batalha.printar_personagens import Printar_Combatentes as PC

    # pygame setup
    pygame.init()
    

    screen = definir_janela((1280, 720))
    definir_titulo("IntroBattle")


    aliados     = (Paladino(),Ladino(),Maga()) 
    inimigos    = criar_chefona()
    'inimigos    = criar_lacaios()'
    batalha     = Criar_Batalha(aliados,inimigos)
    opcoes      = Printar_Opções(Cor(80, 80, 80))
    armazen     = []
    escolher    = BP_chefao()
    'escolher    = PC()'

    batalha.boss = True

    print(aliados[2].dano_magia)
    print(batalha.inimigos[0].reducao_dano(aliados[2].dano_magia))

    Enfrentar_Inimigos(screen,(batalha,opcoes,armazen, escolher))

    pygame.quit()

    '''tupla = (Lady_Medusa(),)
    print(tupla.index(tupla[0]))'''

