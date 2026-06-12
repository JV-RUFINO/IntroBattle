from sys import path as caminho
from pathlib import Path as Caminhozão

arquivo = Caminhozão(__file__).resolve()
parente , raiz = arquivo.parent, arquivo.parents[1]
caminho.append(str(raiz))


try:
    # ETIQUETAS
    from etiquetas                              import Combate , Condicao , Estado , Magi , Perso , Stat
    
    # ESSENCIAIS
    from essenciais.caixa_texto                 import Caixa_Texto , texto_decorador
    from essenciais.projetil                    import Projetil

    # PERSONAGENS -- abstrato
    from personagens.abstrato.magias            import Magias
    from personagens.abstrato.personagem        import Personagem
    from personagens.abstrato.status            import Status

    # PERSONAGENS -- concreto
    from personagens.status                     import Velocidade , Vida , Ataque , Defesa , Carga

    # PERSONAGENS -- PRODUTO FINAL
    from personagens.perso.aliado               import Aliado
    from personagens.perso.inimigo              import Inimigo

except ModuleNotFoundError:
    from .essenciais.caixa_texto                import Caixa_Texto , texto_decorador
    from .essenciais.projetil                   import Projetil

    # PERSONAGENS -- abstrato
    from .personagens.abstrato.magias           import Magias
    from .personagens.abstrato.personagem       import Personagem
    from .personagens.abstrato.status           import Status

    # PERSONAGENS -- concreto
    from .personagens.status                    import Velocidade , Vida , Ataque , Defesa , Carga

    # PERSONAGENS -- PRODUTO FINAL
    from .personagens.perso.aliado              import Aliado
    from .personagens.perso.inimigo             import Inimigo


if __name__ == "__main__":
    ...