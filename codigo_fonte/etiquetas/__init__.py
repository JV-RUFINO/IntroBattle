from sys import path as caminho
from pathlib import Path as Caminhozão

arquivo = Caminhozão(__file__).resolve()
parente , raiz = arquivo.parent, arquivo.parents[1]
caminho.append(str(raiz))

try:
    from codigo import Estado, Perso , Stat , Magi , Condicao , Combate
except ModuleNotFoundError:
    from .codigo import Estado, Perso , Stat , Magi , Condicao , Combate

if __name__ == "__main__":
    ...