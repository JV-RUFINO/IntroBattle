from sys import path as caminho
from pathlib import Path as Caminhozão

arquivo = Caminhozão(__file__).resolve()
parente , raiz = arquivo.parent, arquivo.parents[1]
caminho.append(str(raiz))

try:
    from Ataque     import Ataque
    from Carga      import Carga
    from Defesa     import Defesa
    from Velocidade import Velocidade
    from Vida       import Vida
except ModuleNotFoundError:
    from .Ataque     import Ataque
    from .Carga      import Carga
    from .Defesa     import Defesa
    from .Velocidade import Velocidade
    from .Vida       import Vida

if __name__ == "__main__":
    ...