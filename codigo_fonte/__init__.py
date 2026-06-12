from sys import path as caminho
from pathlib import Path as Caminhozão

arquivo = Caminhozão(__file__).resolve()
parente , raiz = arquivo.parent, arquivo.parents[1]
caminho.append(str(raiz))


try:
    from fluxo_jogo  import Fluxo_Jogo
except ModuleNotFoundError:
    from .fluxo_jogo import Fluxo_Jogo

if __name__ == "__main__":
    from   pygame.display     import set_mode as definir_janela , set_caption as definir_titulo
    import pygame

    # pygame setup
    pygame.init()
    

    screen = definir_janela((1280, 720))
    definir_titulo("IntroBattle")

    fluxo = Fluxo_Jogo(screen)
    fluxo()

    pygame.quit()