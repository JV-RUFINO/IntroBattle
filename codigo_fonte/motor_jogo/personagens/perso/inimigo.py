from sys import path as caminho
from pathlib import Path as Caminhozão

arquivo = Caminhozão(__file__).resolve()
parente , raiz = arquivo.parent, arquivo.parents[1]
caminho.append(str(raiz))

# ESSENCIAIS
from perso_exterior         import Estado , Stat , Perso
from perso_exterior         import Linkzin

# STATUS
from abstrato.status        import Status 

# STATUS
from status                 import Vida
from status                 import Ataque
from status                 import Velocidade
from status                 import Defesa
from status                 import Carga

# PERSONAGEM
from abstrato.personagem    import Personagem 

# PYGAME
from pygame                     import Surface  as Superficie , Color as Cor
from pygame.image               import load     as carregar_imagem

# IMPORTAÇÕES GERAIS
from os                         import getcwd
from json                       import load     as carregar_json


'=== CÓDIGO REAL ==='


class Inimigo(Personagem):
    def __init__( _ , classe_inimiga : tuple , posicao_roteiro : str ):
        super().__init__()

        caminho_comum : str  = Linkzin( getcwd() , 'banco_dados' , 'Personagens' , 'inimigos' )
        bifurcacao    : str  = Linkzin( caminho_comum , *classe_inimiga ) # caveira , Lady Medusa , ...
        condicao      : list = [Linkzin(caminho_comum , bifurcacao , condição + '.png' )
                                        for condição in ['down' , 'escolhivel' , 'idle' , 'selecionada']] # dowm , escolhivel , idle , selecionada
        
        # IMAGENS'
        _.imagens.update({Estado.Down           : carregar_imagem(condicao[0])}) # pygame.image.load(Linkzin( getcwd() , 'banco_dados' , 'Personagens' , 'aliados' , ... , 'idle.png'))
        _.imagens.update({Estado.Escolhivel     : carregar_imagem(condicao[1])}) # pygame.image.load(Linkzin( getcwd() , 'banco_dados' , 'Personagens' , 'aliados' , ... , 'down.png'))
        _.imagens.update({Estado.Idle           : carregar_imagem(condicao[2])}) # pygame.image.load(Linkzin( getcwd() , 'banco_dados' , 'Personagens' , 'aliados' , ... , 'escolhivel.png'))
        _.imagens.update({Estado.Selecionada    : carregar_imagem(condicao[3])}) # pygame.image.load(Linkzin( getcwd() , 'banco_dados' , 'Personagens' , 'aliados' , ... , 'selecionada.png'))

        # STATUS DO PERSONAGEM -- max 3
        with open(Linkzin( getcwd() , 'roteiro' , 'status_personagens.json' ) , 'r' ) as status:
            status_totais = carregar_json(status)
            status_perso  = status_totais[1][posicao_roteiro]

        _.STATUS.update({Stat.VIDA          : Vida(status_perso['VIDA']            )}) # VIDA(...)})
        _.STATUS.update({Stat.ATAQUE        : Ataque(status_perso['ATAQUE']        )}) # ATAQUE(...)})
        _.STATUS.update({Stat.DEFESA        : Defesa(status_perso['DEFESA']        )}) # DEFESA(...)})
        _.STATUS.update({Stat.VELOCIDADE    : Velocidade(status_perso['VELOCIDADE'])}) # VELOCIDADE(...)})
        _.STATUS.update({Stat.CARGA         : Carga( status_perso['CARGA']         )}) # CARGA(...)})

        _.vida = int(_.STATUS[Stat.VIDA]) + 1

        # DIALOGOS DO PERSONAGEM
        _.todas_falas = None
        
        # MAGIAS / HABS
        _.magias = None

        _.estado_atual      = Estado.Idle

    @staticmethod
    def TIPO( ) -> Perso:
        return None

    @staticmethod
    def cor_assinatura( cor ) -> Cor:
        return Cor( r=cor[0] , g=cor[1] , b=cor[2] )

    @property
    def imagem_atual( _ ):
        return super().imagem_atual

    @property
    def magia_imagem( _ ):
        return None

    @property
    def STATUS(_) -> dict:
        return super().STATUS

    @STATUS.getter
    def VIDA(_) -> Vida:
        return super().VIDA

    @STATUS.getter
    def ATAQUE(_) -> Ataque:
        return super().ATAQUE

    @STATUS.getter
    def DEFESA(_) -> Defesa:
        return super().DEFESA

    @STATUS.getter
    def VELOCIDADE(_) -> Velocidade:
        return super().VELOCIDADE

    @STATUS.getter
    def CARGA(_) -> Carga:
        return super().CARGA
    

    @property
    def dano_basico( _ ) -> int:
        return super().dano_basico

    @property
    def dano_magia( _ ) -> int:
        return None

    def reducao_dano( _ , dano_recebido : int) -> int: # aplicando DEFESA sobre o dano recebido
        return super().reducao_dano( dano_recebido )

    def buff_debuff( _ , efeito , buff = True ):
        return super().buff_debuff( efeito , buff )

    def ataque_basico( _ , alvo: Personagem): # ataca o alvo .Conta apenas o ATAQUE
        return super().ataque_basico( alvo )

    def falar( _ , frase: str, cor: tuple): # abre a caixa de texto e faz o personagem falar
        ...
    
    def magia( _ , alvo: Personagem):
        return None

    def mostrar_animacao(_, screen: Superficie, coordenadas: tuple, escala: tuple = None):
        return super().mostrar_animacao(screen, coordenadas, escala)

    def __hash__(_) -> int:
        return super().__hash__()

    def __sub__( _ , valor: ...):
        super().__sub__( valor )

    def __add__( _ , valor: ...):
        super().__add__( valor )

    def repr_inimigo( _ , genero : str , texto_convencional: str , texto_derrota: str ):
        return super().repr_personagem( f'{genero} {texto_convencional}' , f'{texto_derrota} :)' , ( f"Derrote-{genero.lower()}!" , "De pé.Continue atacando!" ))
       
        

'=== TESTES ==='


if __name__ == "__main__":
    ...

