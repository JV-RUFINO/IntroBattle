from __future__ import annotations

from sys import path as caminho
from pathlib import Path as Caminhozão

arquivo = Caminhozão(__file__).resolve()
parente , raiz = arquivo.parent, arquivo.parents[1]
caminho.append(str(raiz))


# ESSENCIAIS
from perso_exterior import Estado , Stat, Perso , Condicao # etiquetas
from perso_exterior import Projetil

# MAGIAS
try:
    from status import Status
    from magias import Magias
except ImportError:
    from .status import Status 

# PYGAME
from pygame             import Surface  as Superficie , Color as Cor
from pygame.transform   import scale    as imagem_escala

# IMPORTAÇÕES GERAIS
from abc import ABC ,  abstractmethod


'=== CÓDIGO REAL ==='


class Personagem(ABC):
    def __init__( _ ):
        # IMAGENS 
        _.imagens = {
            Estado.Idle         : ... , # pygame.image.load(Linkzin( getcwd() , 'banco_dados' , 'Personagens' , 'aliados' , ... , 'idle.png'))
            Estado.Down         : ... , # pygame.image.load(Linkzin( getcwd() , 'banco_dados' , 'Personagens' , 'aliados' , ... , 'down.png'))
            Estado.Escolhivel   : ... , # pygame.image.load(Linkzin( getcwd() , 'banco_dados' , 'Personagens' , 'aliados' , ... , 'escolhivel.png'))
            Estado.Selecionada  : ...   # pygame.image.load(Linkzin( getcwd() , 'banco_dados' , 'Personagens' , 'aliados' , ... , 'selecionada.png'))
            }
        
        # STATUS DO PERSONAGEM
        _.__status = {
            Stat.VIDA           : ... , # VIDA(...)
            Stat.ATAQUE         : ... , # ATAQUE(...)
            Stat.DEFESA         : ... , # DEFESA(...)
            Stat.VELOCIDADE     : ... , # VELOCIDADE(...)
            Stat.CARGA          : ...   # CARGA(...)
            }

        # MAGIAS / HABS
        _.magias : Magias   = ...

        _.estado_atual      = Estado.Idle
        _.vida   : int      = ...

    @staticmethod
    def TIPO( ) -> Perso:
        ...

    @staticmethod
    def cor_assinatura( ) -> Cor:
        ...

    @property
    @abstractmethod
    def imagem_atual( _ ):
        return _.imagens[_.estado_atual]

    @property
    @abstractmethod
    def magia_imagem( _ ):
        return None

    @property
    @abstractmethod
    def STATUS( _ ) -> dict:
        return _.__status

    @STATUS.getter
    def VIDA( _ ) -> Status:
        return _.STATUS[Stat.VIDA]

    @STATUS.getter
    def ATAQUE( _ ) -> Status:
        return _.STATUS[Stat.ATAQUE]

    @STATUS.getter
    def DEFESA( _ ) -> Status:
        return _.STATUS[Stat.DEFESA]

    @STATUS.getter
    def VELOCIDADE( _ ) -> Status:
        return _.STATUS[Stat.VELOCIDADE]
    
    @STATUS.getter
    def CARGA( _ ) -> Status:
        return _.STATUS[Stat.CARGA]

    @property
    def dano_basico( _ ) -> int:
        return int( _.ATAQUE )

    @property
    def dano_magia( _ ) -> int:
        return _.magias.dano_magia( _.STATUS )

    @property
    def calculo_VidaTotal( _ ):
        return int(_.VIDA) + 1

    def reducao_dano( _ , dano_recebido : int) -> int: # aplicando DEFESA sobre o dano recebido
        dano_real = dano_recebido - int(_.DEFESA)

        if dano_real <= 1:
            dano_real = 1 # dano nunca menor que 0

        return dano_real

    def buff_debuff( _ , efeito : Status , buff = True) -> Status:
        for status in _.STATUS:
            if type(efeito) == type(_.STATUS[status]):
                _.STATUS[status].numero = _.STATUS[status].numero + int(efeito) if buff else _.STATUS[status].numero - int(efeito) 

                return _.STATUS[status]
        
        return efeito

    @abstractmethod
    def ataque_basico( _ , alvo: Personagem): # ataca o alvo .Conta apenas o ATAQUE
        alvo - _.dano_basico

        return ( None , _.dano_basico )

    @abstractmethod
    def falar( _ , frase: str, cor: tuple): # abre a caixa de texto e faz o personagem falar
        ...
    
    @abstractmethod
    def magia( _ , alvo: Personagem) -> Projetil:
        alvo - _.dano_magia
        _.magias.aplicar_efeitos( _ , alvo ) # faça você mesmo!

        return ( Projetil , _.dano_magia)

    @abstractmethod
    def mostrar_animacao( _ , screen: Superficie,coordenadas: tuple, escala: tuple = None):
        nova_imagem = _.imagem_atual
        if escala != None:
            nova_imagem = imagem_escala(_.imagem_atual , escala)
        
        return screen.blit(nova_imagem , coordenadas)

    def __hash__(_) -> int:
        return super().__hash__()

    def __sub__(_ , valor):
        if type(valor) == int:
            valor : int

            _.vida -= _.reducao_dano( valor ) # reduzindo o dano conforme a DEFESA

            if _.vida <= 0:
                _.vida = 0

        elif type(valor) in [type(_.STATUS[status]) for status in _.STATUS]:
            valor : Status

            _.buff_debuff( valor , buff = False)

        return _

    def __add__(_ , valor):
        if type(valor) == int:
            valor : int

            _.vida += valor

        elif type(valor) in [type(_.STATUS[status]) for status in _.STATUS]:
            valor : Status

            _.buff_debuff( valor , buff = True)

        return _

    def __textinho_adcional(_, con):
        reportar_status = ""

        for status in _.STATUS:
            if _.STATUS[status].condicao == con:
                reportar_status += f"{status}"
                reportar_status += " , "
        
        return reportar_status[:-3] 

    def repr_personagem( _ , print_convencional : str , para_derrota : str , vida_status : tuple ):
        if _.vida == 0:
            return para_derrota

        index_status = 1 if _.vida <= _.calculo_VidaTotal / 2 else 0

        reportar_status = ""

        bbb = [(Condicao.Nerfado , Condicao.Buffado),
                    (" Nerfados & " , " Buffados")]
        for aaa in range(0,len(bbb)):
            if bbb[0][aaa] in [_.STATUS[status].condicao for status in _.STATUS]:
                reportar_status += _.__textinho_adcional(bbb[0][aaa])
            else:
                reportar_status += "0"

            reportar_status += bbb[1][aaa]

        return f"{print_convencional} : {vida_status[index_status]}({reportar_status})"

        

'=== TESTES ==='


if __name__ == "__main__":
    ...

