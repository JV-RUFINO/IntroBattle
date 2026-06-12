from sys import path as caminho
from pathlib import Path as Caminhozão

arquivo = Caminhozão(__file__).resolve()
parente , raiz = arquivo.parent, arquivo.parents[1]
caminho.append(str(raiz))

# INIMIGOS
try:
    from Esqueleto             import Esqueleto         
    from Lady_Medusa           import Lady_Medusa       
    from Lacaios_Desalmados    import Lacaios_Desalmados
except ModuleNotFoundError:
    from .Esqueleto            import Esqueleto         
    from .Lady_Medusa          import Lady_Medusa       
    from .Lacaios_Desalmados   import Lacaios_Desalmados

if __name__ == "__main__":
    ...