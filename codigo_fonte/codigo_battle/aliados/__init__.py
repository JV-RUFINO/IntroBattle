from sys import path as caminho
from pathlib import Path as Caminhozão

arquivo = Caminhozão(__file__).resolve()
parente , raiz = arquivo.parent, arquivo.parents[1]
caminho.append(str(raiz))

# ALIADOS
try:
    from Caçadora               import Caçadora
    from Ladino                 import Ladino
    from Maga                   import Maga
    from Paladino               import Paladino
    from Suporte                import Suporte

    from magias.Ventania        import Ventania
    from magias.JadoDAgua       import JatoDAgua
    from magias.BolaDeFogo      import BolaDeFogo
    from magias.Fumaca          import Fumaça
except ModuleNotFoundError:
    from .Caçadora              import Caçadora
    from .Ladino                import Ladino
    from .Maga                  import Maga
    from .Paladino              import Paladino
    from .Suporte               import Suporte

    from .magias.Ventania        import Ventania
    from .magias.JadoDAgua       import JatoDAgua
    from .magias.BolaDeFogo      import BolaDeFogo
    from .magias.Fumaca          import Fumaça

if __name__ == "__main__":
    ...