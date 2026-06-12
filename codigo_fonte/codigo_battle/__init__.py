from sys import path as caminho
from pathlib import Path as Caminhozão

arquivo = Caminhozão(__file__).resolve()
parente , raiz = arquivo.parent, arquivo.parents[1]
caminho.append(str(raiz))

try:
    # CELEBRO -- CRIADORES
    from criadores_batalha.criar_opcoes         import Printar_Opções 
    from criadores_batalha.criar_batalha        import Criar_Batalha
    from criadores_batalha.printar_personagens  import Printar_Seleção_Perso
    from criadores_batalha.printar_personagens  import Printar_Combatentes
    from criadores_batalha.printar_personagens  import Printar_Chefao

    # PERSONAGENS
    from aliados                                import Paladino,Ladino,Suporte,Caçadora,Maga
    from inimigos                               import Esqueleto, Lady_Medusa

    from fases_battle.menu_inicial              import Menu_Inicial , Criar_Menu_inicial
    from fases_battle.seleção_perso             import Selecionar_Personagens , Pausa_Personagens
    from fases_battle.contra_inimigos           import Enfrentar_Inimigos , criar_chefona , criar_esqueletos , criar_lacaios
    from fases_battle.conclusao                 import Conclusao
except ModuleNotFoundError:
    # CELEBRO -- CRIADORES
    from .criadores_batalha.criar_opcoes        import Printar_Opções 
    from .criadores_batalha.criar_batalha       import Criar_Batalha
    from .criadores_batalha.printar_personagens import Printar_Seleção_Perso
    from .criadores_batalha.printar_personagens import Printar_Combatentes
    from .criadores_batalha.printar_personagens import Printar_Chefao

    # PERSONAGENS
    from .aliados                               import Paladino,Ladino,Suporte,Caçadora,Maga
    from .inimigos                              import Esqueleto, Lady_Medusa

    from .fases_battle.menu_inicial             import Menu_Inicial , Criar_Menu_inicial
    from .fases_battle.seleção_perso            import Selecionar_Personagens , Pausa_Personagens
    from .fases_battle.contra_inimigos          import Enfrentar_Inimigos , criar_chefona , criar_esqueletos , criar_lacaios
    from .fases_battle.conclusao                import Conclusao


if __name__ == "__main__":
    ...