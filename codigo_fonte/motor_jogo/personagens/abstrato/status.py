from sys import path as caminho
from pathlib import Path as Caminhozão

arquivo = Caminhozão(__file__).resolve()
parente , raiz = arquivo.parent, arquivo.parents[1]
caminho.append(str(raiz))


# ESSENCIAIS
from perso_exterior   import Stat
from perso_exterior   import Linkzin
from perso_exterior   import Condicao

# PYGAME
from pygame import image

# IMPORTAÇÕES GERAIS
from abc import ABC , abstractmethod 
from os  import getcwd

'=== CÓDIGO REAL ==='

class Status(ABC):
    def __init__( _ ):
        _.caminho  : str      = Linkzin(getcwd(),'banco_dados','Icones','Representadores')
        _.condicao : Condicao = Condicao.Estavel


    @staticmethod
    def TIPO() -> Stat:
        ...

    @property
    @abstractmethod
    def numero( _ ) -> int:
        ...

    @numero.setter
    @abstractmethod
    def numero( _ , novo_numero) -> int:
        ...

    @property
    @abstractmethod
    def niveis_status( _ ) -> list:
        return ['muito_baixa','baixa','media','alta','muito_alta']


    @abstractmethod
    def mostrar_imagem( _ ):
        return image.load( Linkzin( _.caminho , _.niveis_status[_.numero] + '.png' ) )

    def __eq__( _ , objeto) -> bool:
        if type(objeto) == int:
            return True if objeto == _.numero else False
        elif type(objeto) == Status:
            return True if objeto == _ else False 

    def __add__( _ , numero: int):
        _.numero += numero 

    def __sub__( _ , numero: int):
        _.numero -= numero

    def __int__( _ ):
        return _.numero

    def __repr__( _ ) -> str:
        return f'Status(status = {_.condicao} & numero = {_.numero})'
    
'=== TESTES ==='

if __name__ == "__main__":
    ...
    
    