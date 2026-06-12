from sys import path as caminho
from pathlib import Path as Caminhozão

arquivo = Caminhozão(__file__).resolve()
parente , raiz = arquivo.parent, arquivo.parents[1]
caminho.append(str(raiz))

# ESSENCIAIS
from battle_exterior    import Estado , Combate 

# PERSONAGENS
from battle_exterior    import Personagem

# IMPORTAÇÕES GERAIS
from dataclasses        import dataclass
from random             import randint


'=== CÓDIGO REAL ==='


@dataclass
class Criar_Batalha:
    aliados     : tuple # sempre 3
    inimigos    : tuple # 3 se boss for normal, 1 se for boss
    boss        : bool  = False

    @staticmethod
    def tamanho_normal(  ):
        return (80,80)

    @staticmethod
    def tamanho_chafe(  ):
        return (111,207)#(185,345)
    
    @property
    def posicao_combate( _ ): # usados para printar as imagens dos aliados e inimigos na tela
        if _.boss:
            return (((300,200),(600,400),(900,200)),        # aliados
                        ((600,200)))                        # CHEFE
        
        return (((300,200),(200,300),(300,400)),            # aliados
                        ((900,200),(1000,300),(900,400)))   # inimigos
    

    @property
    def vitoria( _ ) -> bool:
        if all([aliado.vida  <= 0 for aliado  in _.aliados ]):
            return False
        if all([inimigo.vida <= 0 for inimigo in _.inimigos]):
            return True

        return None

    @property
    def fila( _ ):
        resultado_semi = sorted(
                        [(int(aliado.VELOCIDADE)  , hash(aliado))  for aliado  in _.aliados ] +
                        [(int(inimigo.VELOCIDADE) , hash(inimigo)) for inimigo in _.inimigos]
                    , reverse= True)

        resultado = []
        for rrr in resultado_semi:
            for rrr2 in filter(lambda x: rrr[1] == hash(x),[*_.aliados + _.inimigos]):
                resultado.append(rrr2)


        return resultado

    @property
    def decisao_inimiga( _ ):
        return [(escolha[1],escolha[0],randint(0,2)) for escolha in enumerate(
                        [Combate.Atacar if inimigo.estado_atual != Estado.Down else Combate.Pular for inimigo in _.inimigos])]
        
        
    def combate( _ , acao: tuple , inverter = False ):
        'Esta função não comporta Combate.Falar'
        'acao = (Combate , int , int) // EX: (Combate.Magia , 1 , 1),' 
        cbt : Combate = acao[0]

        autor : Personagem = _.aliados[acao[1]]  if inverter == False else _.inimigos[acao[1]]
        alvo  : Personagem = _.inimigos[acao[2]] if inverter == False else _.aliados[acao[2]]

        resultado = None
        if cbt != Combate.Pular:
            acoes = [ autor.ataque_basico , autor.magia ]

            resultado = acoes[(Combate.Atacar,Combate.Magia).index(cbt)](alvo)

        return resultado


'=== TESTES ==='


if __name__ == "__main__":
    from aliados  import Caçadora , Paladino , Ladino , Maga , Suporte 
    from inimigos import Esqueleto
    A = Criar_Batalha((Caçadora(),Ladino(),Maga()),(Esqueleto(),Esqueleto(),Esqueleto()))
    
    print(A.inimigos[0].vida)

    A.aliados[2].magia(A.inimigos[0])

    print(A.aliados[2])
    print(A.inimigos[0].vida)
    '''print(A)
    print(A.inimigos[1].vida)
    
    A.combate((Combate.Atacar,0,1))

    print(A.inimigos[1].vida)

    vivos = [False,True,True]
    maximo = len(vivos) - 1
    minimo = 0

    setup = [range( 0 , maximo ), range( maximo , 0 , -1 )]
    rrr   = [1 , -1]

    r = 0
    for resultado in [ maximo , minimo ]:
        for numero in setup[r]:
            if vivos[numero] == False:
                resultado += rrr[r]
            
            break

        r += 1
    '''
    '''print(maximo)
    print(minimo)

    for numero in range( 0 , maximo ):
        if vivos[numero] == False:
            minimo += 1
        
        break

    for numero in range( maximo , 0 , -1):
        if vivos[numero] == False:
            maximo -= 1
        
        break

    print(maximo)
    print(minimo)'''