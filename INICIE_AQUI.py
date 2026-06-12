from sys import path as caminho
from pathlib import Path as Caminhozão

arquivo = Caminhozão(__file__).resolve()
parente , raiz = arquivo.parent, arquivo.parents[1]
caminho.append(str(raiz))

# IMPORTANDO O JOGO
from codigo_fonte       import Fluxo_Jogo
# IMPORTANDO O JOGO

from pygame             import init     as iniciar_pygame   , quit          as encerrar_pygame
from pygame.display     import set_mode as definir_janela   , set_caption   as definir_titulo , set_icon as definir_icone
from pygame.image       import load

from os                 import getcwd
import json

'=== CÓDIGO REAL ==='

def iniciar_jogo():
    iniciar_pygame()

    screen = definir_janela((1280, 720))
    definir_titulo("IntroBattle")

    icone = load(getcwd()+"\Icone-Introbattle.ico")
    definir_icone(icone)

    fluxo = Fluxo_Jogo(screen)
    fluxo()

    encerrar_pygame()

iniciar_jogo()
