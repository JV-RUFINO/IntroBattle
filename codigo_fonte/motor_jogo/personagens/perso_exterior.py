from sys import path as caminho
from pathlib import Path as Caminhozão

arquivo = Caminhozão(__file__).resolve()
parente , raiz = arquivo.parent, arquivo.parents[1]
caminho.append(str(raiz))


# CÓDIGO COPIADO POR MIM
from motor_exterior import Linkzin
from motor_exterior import imagem_unica , porcao_imagens , carregar_tira

# ESSENCIAIS
from motor_exterior   import Stat , Perso , Magi, Condicao , Estado

from essenciais.projetil    import Projetil

from essenciais.caixa_texto import Caixa_Texto,texto_decorador


if __name__ == "__main__":
    A = {Estado.Escolhivel:1,"B":2}

    for a in A:
        print(a)

    A = "abcdefgh"
    a = A[:-3]
    print(a)
    print(A)