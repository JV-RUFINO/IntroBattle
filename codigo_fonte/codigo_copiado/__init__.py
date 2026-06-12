from sys import path as caminho
from pathlib import Path as Caminhozão

arquivo = Caminhozão(__file__).resolve()
parente , raiz = arquivo.parent, arquivo.parents[1]
caminho.append(str(raiz))

try:
    from criar_menus    import Menu_Conjunto , Menu_Single
    from linkzin        import Linkzin
    from spritesheet    import carregar_tira,imagem_unica, porcao_imagens
except ModuleNotFoundError:
    from .criar_menus    import Menu_Conjunto , Menu_Single
    from .linkzin        import Linkzin
    from .spritesheet    import carregar_tira,imagem_unica, porcao_imagens