from sys import path as caminho
from pathlib import Path as Caminhozão

arquivo = Caminhozão(__file__).resolve()
parente , raiz = arquivo.parent, arquivo.parents[1]
caminho.append(str(raiz))

from .BolaDeFogo import BolaDeFogo
from .Fumaca     import Fumaça
from .JadoDAgua  import JatoDAgua
from .Ventania   import Ventania

if __name__ == "__main__":
    ...