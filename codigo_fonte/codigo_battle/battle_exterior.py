from sys import path as caminho
from pathlib import Path as Caminhozão

arquivo = Caminhozão(__file__).resolve()
parente , raiz = arquivo.parent, arquivo.parents[1]
caminho.append(str(raiz))


# CÓDIGO COPIADO, TANTO DE MIM QUANTO DA INTERNET
from codigo_copiado             import Menu_Conjunto ,Menu_Single
from codigo_copiado             import Linkzin
from codigo_copiado             import carregar_tira , imagem_unica , porcao_imagens

# ETIQUETAS
from etiquetas                  import Combate , Condicao , Estado , Magi , Perso , Stat

# ESSENCIAIS
from motor_jogo                 import Caixa_Texto , texto_decorador
from motor_jogo                 import Projetil

# PERSONAGENS -- abstrato
from motor_jogo                 import Magias
from motor_jogo                 import Personagem
from motor_jogo                 import Status

# PERSONAGENS -- concreto
from motor_jogo                 import Velocidade , Vida , Ataque , Defesa , Carga

# PERSONAGENS -- PRODUTO FINAL
from motor_jogo                 import Aliado
from motor_jogo                 import Inimigo


if __name__ == "__main__":
    ...