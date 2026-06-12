from sys import path as caminho
from pathlib import Path as Caminhozão

arquivo = Caminhozão(__file__).resolve()
parente , raiz = arquivo.parent, arquivo.parents[1]
caminho.append(str(raiz))

# CRIADORES -- BATALHA
from criadores_batalha.criar_fase import Criar_Fase

# CODIGO ANTIGO MEU COPIADO
from battle_exterior import Menu_Conjunto

# PYGAME
from pygame             import Surface as Superficie, QUIT as SAIR_X


'=== CÓDIGO REAL ==='


class Criar_Menu_inicial(Menu_Conjunto):
    def __init__( _ , screen: Superficie):
        _.dificuldade = 0
        _.ativo       = True

        super().__init__(screen)

        def iniciar():
            _.ativo = False

        def config():
            if _.foco == 0:
                _.foco = 1
            else:
                _.foco = 0

        def dif(*args,**kwargs):
            _.dificuldade = args[1]    

        _.novo_menu({
            "nome":     "Bem Vindo",
            'dim':      [80,80],
            'cor':      "blue",
            'elementos':[
                        ('Escolha as opções que desejar'),
                        ('INICIAR', iniciar),
                        ('=----------------='),
                        ("Configurações", config)
                        ]
                    })

        _.novo_menu({
            "nome":     "Configurações",
            'dim':      [80,80],
            'cor':      'v',
            'elementos':[
                        ('Vá, mude como desejar'),
                        ('Dificuldade:',[('Facil',0),("Médio",1),("Dificil",2)],dif),
                        ('=----------------='),
                        ("VOLTAR",config)
                        ]
                    })


@Criar_Fase(Criar_Fase.caminho_comum(),'salão.png')
def Menu_Inicial(
            screen :Superficie, 
                info_extra = None,
                    eventos:list = None):
    for event in eventos:
        if event.type == SAIR_X: # pygame.QUIT
            return False

    Menu: Criar_Menu_inicial = info_extra # só pra facilitar o entendimento

    Menu.performar(eventos)

    if Menu.ativo == False:
        return False

    return True


'=== TESTES ==='


if __name__ == "__main__":
    from   pygame.display     import set_mode as definir_janela , set_caption as definir_titulo
    import pygame

    # pygame setup
    pygame.init()
    
    screen = definir_janela((1280, 720))
    definir_titulo("IntroBattle")

    B = Criar_Menu_inicial(screen)

    A = Menu_Inicial(screen, B)

    if any([a.type == SAIR_X for a in A]):
        print(":0")

    
    pygame.quit()
