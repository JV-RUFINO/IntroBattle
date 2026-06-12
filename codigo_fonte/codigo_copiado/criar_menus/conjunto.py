# PYGAME MENU
from pygame_menu        import themes
from pygame_menu.themes import THEME_BLUE as TEMA_AZUL , THEME_DARK as TEMA_ESCURO, THEME_GREEN as TEMA_VERDE , THEME_ORANGE as TEMA_LARANJA, THEME_DEFAULT as TEMA_PADRAO

# PYGAME
from pygame             import Surface as set_mode_Surface

# IMPORTAÇÕES GERAIS
from functools          import partial
from itertools          import combinations
from warnings           import warn as avisar

try:
    from enumerador                 import Elemento
    from estranhezas                import MenuCloneException
    from unico                      import Menu_Single
except ModuleNotFoundError:
    from criar_menus.enumerador     import Elemento
    from criar_menus.estranhezas    import MenuCloneException
    from criar_menus.unico          import Menu_Single
    
class Abstrador:
    NOME = ["nome","name","n"]
    DIMENSAO = ["dim","dimensão","dimensao","dimension","d"]
    POSICAO = ["pos","posição","posiçao","posicao","posicão","position","p"]
    COR = ["cor","cores","color","colors","c"]
    ELEMENTS = ["elemento","elementos","elements","e"]
    TEMAS = frozenset([ # aqui reside todas as opções de cores possíveis
            ("azul","blue",'a',themes.THEME_BLUE),
                ("escuro","dark",'e',themes.THEME_DARK),
                    ("verde","green",'v',themes.THEME_GREEN),
                        ("laranja","orange",'l',themes.THEME_ORANGE),
                            ("padrao","default",'padrão','p',themes.THEME_DEFAULT),
                                ("solarizado","solarized",'s',themes.THEME_SOLARIZED)
                            ])  
    
    None_NOME = ""
    None_DIM  = [100,100]
    None_POS  = [50,50]
    None_TEMA = themes.THEME_DEFAULT
    None_ELEMENT = []
    
    NOVA_ABSTRAÇÃO = None
    DISPLAY        = None
    
    def extração_de_dict(vo,dicionario: dict,indice_visado: list ) -> ...:
        # esta função visa extrair de um dicionario um certo indice
        # indice visado = uma lista de possiveis nomes para um indice do dict
        # dicionario = um dict qualquer        
        
        VARIAVEL = None # Caso não seja achado um indice com os indices visados, o valor retornado será None
        for opção in indice_visado:
            opção_generica : str = opção.casefold() # casefold = maiusculo e minusculo são iguais
            
            try:
                VARIAVEL = dicionario[opção_generica]
            except KeyError:
                continue
                    
            break
        
        return VARIAVEL
    
    def receber_display(vo, superficie):
        vo.DISPLAY = superficie
    
    def receber_abstração(vo, definições_recentes: dict):        
        vo.NOVA_ABSTRAÇÃO = partial(vo.extração_de_dict, definições_recentes)
        
    def adcionarNome(vo) -> str:
        nome = vo.NOVA_ABSTRAÇÃO(vo.NOME)
        
        if nome == None:
            nome = vo.None_NOME
        
        return nome
        
    def adcionarDimensão(vo) -> list:
            dimensão = vo.NOVA_ABSTRAÇÃO(vo.DIMENSAO)
            
            if dimensão == None:
                dimensão = vo.None_DIM
            
            pre_altura = dimensão if type(dimensão) == int else dimensão[0] # primeiro indice transformado em porcentagem(Ex: 100 -> 100%)
            pre_largura= dimensão if type(dimensão) == int else dimensão[1] # segundo  indice transformado em porcentagem(Ex: 20  -> 20%)   
                           
            LARGURA,ALTURA = vo.DISPLAY.get_width() * pre_largura, vo.DISPLAY.get_height() * pre_altura 
                
            return (LARGURA / 100 , ALTURA / 100)
        
    def adcionarPosição(vo) -> tuple:
            posição = vo.NOVA_ABSTRAÇÃO(vo.POSICAO)
            
            # === POSIÇÃO
            if posição != None:
                if type(posição) == tuple:
                    POSIÇÃO = posição
                else:
                    POSIÇÃO = tuple( [posição] * 2 )
            else:
                POSIÇÃO = vo.None_POS
            
            return POSIÇÃO
        
    def adcionarCor(vo) -> themes:
            # === TEMA_COR
            # AZUL = cor azul = pygame_menu.themes.THEME_BLUE
            # VERDE= cor verde= pygame_menu.themes.THEME_GREEN 
            tema_cor = vo.NOVA_ABSTRAÇÃO(vo.COR)
            
            if tema_cor != None:        
                for corzinha in vo.TEMAS:
                    if tema_cor in corzinha:
                        return corzinha[-1]
            else:
                return vo.None_TEMA     
            
    def adcionarElementos(vo) -> list:
        todos_tipos = [Elemento.FRASE,Elemento.BOTÃO,Elemento.IMAGEM,Elemento.SELETOR]
    
        elementos = vo.NOVA_ABSTRAÇÃO(vo.ELEMENTS)
        
        if elementos != None:
            for index in range(len(elementos)):
                if type(elementos[index]) == str:
                    elemento_modficado = (vo.achador_automatico(elementos[index]),elementos[index])
                    
                    elementos[index] = elemento_modficado
                elif all([tipo not in elementos[index] for tipo in todos_tipos]):  
                    elemento_modficado = (vo.achador_automatico(elementos[index]),elementos[index])
                    
                    elementos[index] = elemento_modficado
                
            return elementos
        else: 
            return vo.None_ELEMENT     
            
                    
    def achador_automatico(vo, elemento: ...):
        '''
        'isto é uma frase' - frase
        ('isto é um botão',função) - botão
        ('isto é um seletor',("um","dois","tres"),função) -seletor simples
        ('isto é um seletor',(("um",...),("dois",...),("tres",...)),função) -seletor complexo
        'isto/é/uma/imagem' - imagem
        '''
        def função_aleatoria():
            pass
        
        if type(elemento) == str:
            return Elemento.FRASE
        elif type(elemento) == tuple or type(elemento) == list:            
            verificador_de_type = [type(subelemento) for subelemento in elemento]
            
            if type(função_aleatoria) in verificador_de_type:
                if len(verificador_de_type) == 2:
                    return Elemento.BOTÃO
                else:
                    return Elemento.SELETOR
            else:
                return Elemento.IMAGEM

class Menu_Container:
    __MENUS = [] # aqui ficarão os menus em si(no caso, Menu_Single)
    __ARMAZENAMENTO = [] 
    __FOCO          = 0  # o FOCO possibilitará alternar entre menus
    
    @property
    def menuzins(vo):
        return vo.__MENUS
    
    @property
    def menu_focado(vo) -> Menu_Single:
        return vo.__MENUS[vo.__FOCO] 
    
    @property
    def conteudo_focado(vo) -> tuple:
        return vo.__ARMAZENAMENTO[vo.__FOCO]
    
    @property
    def foco(vo) -> __FOCO:
        if vo.__MENUS != []:
            return vo.__FOCO
        else:
            avisar("ERRO! é impossivel focar enquanto não houver um Menu!",UserWarning)
            
            return None
    
    @foco.setter
    def foco(vo, indice: int) -> None:
        try:
            if type(indice) != bool:
                indice = int(indice)
            else:
                int("asçfljasçgf")
            
        except (ValueError , TypeError):
            raise SyntaxError("Apenas numeros são permitidos.")
        
        if len(vo.__MENUS) <= indice:
            avisar("CUIDADO! o numero de foco foi maior que o existente. O mais próximo foi posto no lugar.",SyntaxWarning)
            indice = len(vo.__MENUS) - 1 
                
        vo.__FOCO = indice
        
                
            
    def receber_menu(vo, novo_menu: Menu_Single) -> None:
        if type(novo_menu) == Menu_Single:
            chekzin = [novo_menu.nome, novo_menu.dim, novo_menu.posição, novo_menu.tema,novo_menu.conteúdo]
            
            def passou_no_teste():
                vo.__MENUS.append(novo_menu)
                vo.__ARMAZENAMENTO.append(chekzin)
            
            if len(vo.__MENUS) <= 1:
                passou_no_teste()
            else:
                for testador in vo.__ARMAZENAMENTO:
                    if testador == chekzin:
                        MenuCloneException(testador, chekzin)
                else:
                    passou_no_teste()
                    
    def atualizar_informações(vo):
        segurança = vo.foco
        
        for index in range(len(vo.__ARMAZENAMENTO)):
            vo.foco = index
            
            vo.__ARMAZENAMENTO[index] = [vo.menu_focado.nome, vo.menu_focado.dim, vo.menu_focado.posição, vo.menu_focado.tema,vo.menu_focado.conteúdo]
        
        for original, clone in filter(lambda x: x[0] == x[1],combinations(vo.__ARMAZENAMENTO,2)):
            raise MenuCloneException(original,clone)
        else:
            vo.foco = segurança

class Menu_Conjunto(Menu_Container):
    '''
    - abstração dos elementos de menu(em vez de convocar o elemento, você convoca uma abstração dele)
        'isto é uma frase' - frase
        ('isto é um botão',função) - botão
        'isto/é/uma/imagem' - imagem
        ('isto é um seletor',("um","dois","tres"),função) -seletor simples
        ('isto é um seletor',(("um",...),("dois",...),("tres",...)),função) -seletor complexo
        
        EX: {
            "nome"      : 'Bem vindo',
            "dimensao"  : [450, 350], 
            "posiçao"   : (50, 50),
            "cor"       : "azul",
            "caminho"   : [('frase',("isto é uma frase")),
                        ("botão",('botão',botão)),
                        ("seletor",("titulo:\t",   
                        (('Médio', (50, 50, 200)),
                        ('Dificil', (200, 50, 50)),
                        ('Facil', (50, 200, 50)))
                        ,mudar_cor_do_fundo)),
                        ("imagem",(["Icones",'Representadores','ATAQUE','baixa']))]}
                            
    - armazenamento dos Menus_Single, junto com sua 'formação morfológica' na memoria
    '''
    
    def __init__(vo, surface: set_mode_Surface) -> None:
        vo.__surface = surface
        vo.__Abstrador = Abstrador()
        
        vo.__Abstrador.receber_display(vo.__surface)
        
    def __getitem__(vo,indice: int): 
        vo.foco = indice
        
        print(vo.foco)
        
        vo.__Abstrador.receber_abstração(vo.conteudo_focado)

        return vo.menu_focado
                 
    def __add__(vo, novo_conteúdo:list):   
        vo.menu_focado + novo_conteúdo
        
        vo.conteudo_focado[-1] = vo.menu_focado.conteúdo 
    
    def novo_menu(vo,definições_recentes: dict): # função para modificar ela ao bel prazer
        if type(definições_recentes) != Menu_Single:  
            vo.__Abstrador.receber_abstração(definições_recentes= definições_recentes)
            
            novo_menuzin : Menu_Single = vo.BASE_PARA_MENU()
            
            novo_menuzin + vo.__Abstrador.NOVA_ABSTRAÇÃO(vo.__Abstrador.ELEMENTS)
        else:
            novo_menuzin = definições_recentes
            
        vo.receber_menu(novo_menuzin)    
                
    def BASE_PARA_MENU(vo) -> Menu_Single:        
        NOME    = vo.__Abstrador.adcionarNome()
        DIMENSÃO= vo.__Abstrador.adcionarDimensão()
        POSIÇÃO = vo.__Abstrador.adcionarPosição()
        COR     = vo.__Abstrador.adcionarCor()

        return Menu_Single(
            nome= NOME,
            dim = DIMENSÃO,
            pos = POSIÇÃO,
            tema= COR
        )   
                
    def performar(vo, eventos: list) -> None:
        vo.atualizar_informações()
        
        vo.menu_focado.draw(vo.__surface)
        vo.menu_focado.update( eventos )
    
    @property
    def nome(vo):
        return vo.menu_focado.nome
    
    @nome.setter
    def nome(vo, novo_nome: str):
        vo.menu_focado.nome = novo_nome
        
        vo.conteudo_focado[0] = novo_nome
        
    @property
    def dimensão(vo):
        return vo.menu_focado.dim
    
    @dimensão.setter
    def dimensão(vo, nova_dimensão: list) -> None:
        dimensão_abstraida = vo.__base_para_dimensão(nova_dimensão= nova_dimensão)
        
        vo.menu_focado.dim = dimensão_abstraida
    
    @dimensão.setter
    def altura(vo, nova_altura: int) -> None:
        dimensão_abstraida = vo.__base_para_dimensão(nova_dimensão= nova_altura)
        
        vo.menu_focado.altura = dimensão_abstraida[1]
        
    @dimensão.setter
    def largura(vo, nova_largura: int) -> None:
        dimensão_abstraida = vo.__base_para_dimensão(nova_dimensão= nova_largura)
        
        vo.menu_focado.largura = dimensão_abstraida[0]
        
    def __base_para_dimensão(vo, nova_dimensão: list) -> list:
        dim_dict = {"dimensão": nova_dimensão}
        
        vo.__Abstrador.receber_abstração(dim_dict)
        
        return vo.__Abstrador.adcionarDimensão()
    
        