from sys import path as caminho
from pathlib import Path as Caminhozão

arquivo = Caminhozão(__file__).resolve()
parente , raiz = arquivo.parent, arquivo.parents[1]
caminho.append(str(raiz))

try:
    from unico                  import Menu_Single
    from conjunto               import Menu_Conjunto
except ModuleNotFoundError:
    from criar_menus.conjunto   import Menu_Conjunto
    from criar_menus.unico      import Menu_Single


' === TESTES === '


if __name__ == "__main__":    
    # PYGAME
    from pygame         import init     as iniciar_pygame, QUIT , quit as encerrar_pygame
    from pygame.event   import get      as receber_eventos
    from pygame.display import update   as atualizar_janela,set_mode as criar_janela
    
    # PYGAME MENU
    from pygame_menu.widgets    import Selector

    # IMPORTAÇÕES GERAIS
    from random         import randrange
    from time           import sleep
    from os             import getcwd
    
    # IMPORTAÇÕES CRIADAS
    from unico          import Menu_Single as Single
    from conjunto       import Menu_Conjunto
    from enumerador     import Elemento
    
    '----------------------'
    
    iniciar_pygame()

    def botão():
        AAA.menuzins[1].disable()
        AAA[0]
        
    def mudar_cor_do_fundo(valor_selecionado, cor, **kwargs):
        # valor_selecionado = = primeiro valor da tupla
        # cor =  = segundo valor da tupla
        value_tuple, index = valor_selecionado
        print('Mudando a cor do "widget" para:', value_tuple[0],index,kwargs)  # valor_selecionado ('cor', surface, cor)
        if cor == (-1, -1, -1):  # Generate a random cor
            cor = (randrange(0, 255), randrange(0, 255), randrange(0, 255))
        widget: Selector = kwargs.get('widget')
        widget.update_font({'selected_color': cor})
        widget.get_selection_effect().color = cor

    surface= criar_janela((500,500))

    AAA = Menu_Conjunto(surface= surface)

    print(AAA.foco)

    print("estou apresentando o Single()")
    'AAA.novo_menu(Single())'
    
    AAA.novo_menu ( {
                "nome"      : 'Bem vindo',
                "dimensao"  : (80,60), 
                "posiçao"   : 50,
                "cor"       : "v",
                "elements"  : [
                    (Elemento.SELETOR,("titulo:\t",   
                    (   ('Médio', (50, 50, 200)),
                        ('Dificil', (200, 50, 50)),
                        ('Facil', (50, 200, 50)))
                        ,mudar_cor_do_fundo)),
                    (['banco_dados',"Icones",'Representadores','ATAQUE','baixa'])
                    ]

    }
    )
    
    AAA.novo_menu({"cor":"s"})           
    AAA.nome = "Mal vindo"
    AAA.altura = 50
    AAA.largura = 100
    
    AAA[1]
    AAA + [(Elemento.FRASE,"Isto é um exemplo"),
           ('botão',botão)]
    
    
    
    Game = True
    while Game:
        evento_total = receber_eventos()
        for ev in evento_total:
            if ev.type == QUIT: # habilitando o botão de "X" da tela
                Game = False
                break
            
            AAA.performar( eventos= evento_total)
                        
            atualizar_janela()
            
    encerrar_pygame()    