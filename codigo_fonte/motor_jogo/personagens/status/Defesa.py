from sys import path as caminho
from pathlib import Path as Caminhozão

arquivo = Caminhozão(__file__).resolve()
parente , raiz = arquivo.parent, arquivo.parents[1]
caminho.append(str(raiz))

# ESSENCIAIS
from perso_exterior     import Stat
from perso_exterior     import Linkzin
from perso_exterior     import Condicao

# ABSTRATOS
from abstrato.status    import Status


'=== CÓDIGO REAL ==='


class Defesa(Status):
    def __init__( _ , numero: int ):
        super().__init__(  )

        _.caminho = Linkzin( _.caminho , 'DEFESA' )
        _.__numero = [numero,numero]

    @staticmethod
    def TIPO() -> Stat:
        return Stat.DEFESA

    @property
    def numero( _ ) -> int:
        return _.__numero[0]

    @numero.setter
    def numero( _ , novo_numero):
        _.__numero[0] = novo_numero
        backup        = _.__numero[1]

        nova_condicao = Condicao.Estavel
        if _.numero   > backup:
            nova_condicao = Condicao.Buffado
        elif _.numero < backup:
            nova_condicao = Condicao.Nerfado

        _.condicao = nova_condicao

    @property
    def niveis_status( _ ) -> list:
        return super().niveis_status

    def mostrar_imagem( _  ):
        return super().mostrar_imagem(  )


'=== TESTES ==='


if __name__ == "__main__":
    A = Defesa(5)

    print(A.caminho)