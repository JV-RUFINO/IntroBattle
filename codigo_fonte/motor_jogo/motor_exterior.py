from sys import path as caminho
from pathlib import Path as Caminhozão

arquivo = Caminhozão(__file__).resolve()
parente , raiz = arquivo.parent, arquivo.parents[1]
caminho.append(str(raiz))

# CÓDIGO COPIADO
from codigo_copiado import Linkzin 
from codigo_copiado import carregar_tira, imagem_unica , porcao_imagens
from codigo_copiado import Menu_Conjunto , Menu_Single

# ETIQUETAS
from etiquetas      import Perso , Estado , Combate , Condicao , Magi , Stat

if __name__ == "__main__":
    ...