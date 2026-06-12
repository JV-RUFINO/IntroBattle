from sys import path as caminho
from pathlib import Path as Caminhozão

arquivo = Caminhozão(__file__).resolve()
parente , raiz = arquivo.parent, arquivo.parents[1]
caminho.append(str(raiz))


# ESSENCIAIS
from perso_exterior import Magi             # etiquetas'
from perso_exterior import Linkzin          # linkzin
from perso_exterior import porcao_imagens   # spritesheet
from perso_exterior import Projetil         # projetil

# PYGAME 
from pygame import image , Surface          

# IMPORTAÇÕES GERAIS
from abc import ABC , abstractmethod 
from os  import getcwd


'=== CÓDIGO REAL ==='


class Magias(ABC):
    def __init__( _ ):
        _.caminho : str     = Linkzin(getcwd(),'banco_dados','Icones','Magias')
        _.imagem  : Surface = image.load
        _.__dano  : int     = 0

        _.nome    : str     = ""

    @staticmethod
    def TIPO( ) -> Magi:
        ...

    @staticmethod
    @abstractmethod
    def dano_magia( STATUS ):
        ...

    @staticmethod
    @abstractmethod
    def aplicar_efeitos( autor , alvo ):
        ...
        
    @property
    @abstractmethod
    def dano( _ ) -> int:
        return _.__dano
    
    @dano.setter
    def definir_dano( _ , novo: int):
        _.__dano = novo

    @property
    @abstractmethod
    def coordenadas_imagem( _ ) -> set:
        ...

    @abstractmethod
    def mostrar_animacao( _ , coordenadas: tuple) -> Projetil:
        return Projetil(coordenadas , porcao_imagens( _.imagem, _.coordenadas_imagem , -1))


'=== TESTES ==='


if __name__ == "__main__":
    for a in range(1,5+1):
        print(a)