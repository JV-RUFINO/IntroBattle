'''
OBJETIVO:
    -   criar um decorador onde você coloca ele em cima de uma função e ele cria a fase pra voce
    -   tipo como eu fiz pra criar o texto_decorador do Caixa_Texto

O QUE ELE VAI FAZER
    -   printar um background na tela
    -   ler e executar o que esta sendo feito dentro da função
    -   repetir em loop até que o run esteja completo
O QUE ELE VAI PRECISAR
    -   a imagem do background
    -   funcao: sempre retorna True ou False
'''

from sys import path as caminho
from pathlib import Path as Caminhozão

arquivo = Caminhozão(__file__).resolve()
parente , raiz = arquivo.parent, arquivo.parents[1]
caminho.append(str(raiz))


# PYGAME
import pygame
from pygame             import Surface  as Superficie
from pygame.image       import load     as carregar_imagem
from pygame.event       import get      as capturar_evento
from pygame.time        import Clock    as Relogio
from pygame.transform   import scale    as imagem_escala


# IMPORTAÇÕES GERAIS
from os import path , getcwd


' === CÓDIGO REAL === '


def Linkzin(*path_pasta, act_dir = False) -> str: # criar um link igual o Windows Explorer faz
    " Linkzin( 'um' , 'dois' , 'quatro' ) -> 'um\dois\quatro' "
    
    if act_dir:
        current_dir = path.split( getcwd() )
        path_pasta = current_dir + path_pasta
    
    return path.join(*path_pasta)


class Criar_Fase:
    def __init__(_ , *background: str):
        _.background = carregar_imagem(Linkzin(*background)) #
        _.background = imagem_escala(_.background,(1280, 720))

        _.running    = True
        _.relogio    = Relogio()

    @staticmethod
    def caminho_comum():
        return Linkzin(getcwd(),'banco_dados','Cenarios')

    def __call__(_ , funcao):
        '''
        receber_screen -> argumento auto-inserido pelo decorador. É a Surface do pygame
        novo_evento    -> evento(EX: teclado do jogador) capturado. Pode ser util para a fase
            EX: () = nenhum evento
            EX: (pygame.K_ENTER) -> jogador pressionou o ENTER
        TODA FASE DEVE RETORNAR TRUE OU FALSE
        '''
        def decorador(receber_screen: Superficie, info_extra = None ,novo_evento: list = None):  
            evento = None

            if evento == None:
                _.running = True

            while _.running:
                # pondo o background
                receber_screen.blit( _.background , ( 0 , 0 ) )

                # capturando eventos
                evento = capturar_evento()
                # FASE SENDO CRIADA
                
                _.running = funcao( receber_screen , info_extra , evento ) # sempre retorna True ou False

                # FASE SENDO CRIADA

                pygame.display.flip()

                _.relogio.tick(60)  # limits FPS to 60
            
            return evento
               
        return decorador


' === TESTES === '


if __name__ == "__main__":
    from pygame.display     import set_mode as definir_janela , set_caption as definir_titulo

    # pygame setup
    pygame.init()
    

    screen = definir_janela((1280, 720))
    definir_titulo("IntroBattle")


    @Criar_Fase(Criar_Fase.caminho_comum(),'salão.png')
    def fase(
            screen :Superficie, 
                info_extra = None,
                    eventos:list = None):
        for event in eventos:
            if event.type == pygame.QUIT:
                return False

        return True

    print(type(fase))

    
    pygame.quit()

