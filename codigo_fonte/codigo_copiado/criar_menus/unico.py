from sys import path as caminho
from pathlib import Path as Caminhozão

arquivo = Caminhozão(__file__).resolve()
parente , raiz = arquivo.parent, arquivo.parents[1]
caminho.append(str(raiz))

# PYGAME MENU
from pygame_menu            import themes,Menu      as Menu_versao_original,widgets
from pygame_menu.themes     import THEME_DEFAULT    as TEMA_PADRÃO

# IRMÃS
try:
    from enumerador             import Elemento
    from linkzin_especial       import Linkzin
except ModuleNotFoundError:
    from criar_menus.enumerador import Elemento
    from criar_menus.linkzin_especial import Linkzin

# IMPORTAÇÕES GERAIS
from os.path                import join
from abc                    import ABC
from os                     import getcwd


" === CÓDIGO REAL ==="


class Menu_Funcs(Menu_versao_original, ABC):
    '''
    funções de baixo nivel ou do pygame ficam aqui.
    Algumas funções são praticamente vindas do pygame_menu,
    outras são modficadas para melhorar o sistema
    '''
    
    def frasezinha(_ , texto: str) -> None:
        'cria um pequeno paragrafo de texto no menu'
        # texto = o que vai aparecer no menu
        # lixo  = variavel que serve para
                      
        _.add.label(title=texto)
            
    def botão(_ ,titulo: str, ação: object) -> None:
        'cria um botão em um dos menus selecionados'
        # titulo= o texto central do menu
        # ação  = o evento que ocorrerá quando o botão for ativado
        
        _.add.button(
            title= titulo , 
            action= ação )
            
    def seletor(_ ,titulo: str,items : list, ação: object) -> None:
        'cria um scroll no menu'
        # titulo= o texto central do menu
        # items = as possibilidades de seleção
        #            EX = [( 'Default'  , (255, 255, 255)),
        #                   ('Black'    , (0  , 0  , 0  )),
        #                   ('Blue'     , (0  , 0  , 255)),
        #                   ('Random'   , (-1 , -1 , -1 ))]
        # ação  = o evento(vindo de uma função) que ocorrerá quando apertado o ENTER ou
        #           ou quando mover o lugar
        lista_das_opções = []
                
        for numero in range(len(items)):
            if type(items[numero]) != tuple:
                proximo = (items[numero], numero + 1)
            else:
                proximo = items[numero]    
                        
            lista_das_opções.append(proximo)
                    
        seletor = _.add.selector(
                    title   = titulo ,
                    items   = lista_das_opções ,
                    onreturn= ação, # apertar ENTER vai ativar essa função
                    onchange= ação) # mexer no seletor vai ativar essa função
                
        seletor.add_self_to_kwargs() # Callbacks will receive widget as parameter
            
    def imagem(_, caminho: list) -> None:
        'adiciona uma imagem ao menu'
        # caminho = o local onde o sprite está armazenado
                
        _.add.image(Linkzin(*caminho , act_dir= True)+".png")


class Formulador_Elementos:
    def transformador_automatico(_, materia_prima: list) -> list:
        if materia_prima != None and materia_prima != []:
            indice = 0
            for intermediario in map(_.achador_automatico,materia_prima):
                if intermediario != None:
                    materia_prima[indice] = (_.tradutor_automatico(intermediario),intermediario)
           
                indice += 1
           
            return materia_prima
        else:
            return []
    
    def achador_automatico(_,alvo: ...) -> ...:
        Listagem_ELementos = [Elemento.FRASE,
                                Elemento.BOTÃO,
                                    Elemento.IMAGEM,
                                        Elemento.SELETOR]
        
        return alvo if type(alvo) == str or all([tipo not in alvo for tipo in Listagem_ELementos]) else None
    
    def tradutor_automatico(_, elemento: ...):
        '''
        'isto é uma frase' - frase
        ('isto é um botão',função) - botão
        ('isto é um seletor',("um","dois","tres"),função) -seletor simples
        ('isto é um seletor',(("um",...),("dois",...),("tres",...)),função) -seletor complexo
        'isto/é/uma/imagem' - imagem
        '''
        FRASE   = Elemento.FRASE
        BOTÃO   = Elemento.BOTÃO
        SELETOR = Elemento.SELETOR
        IMAGEM  = Elemento.IMAGEM
        
        def função_aleatoria():
            pass
        
        if type(elemento) == str:
            return FRASE
        elif type(elemento) == tuple or type(elemento) == list:            
            verificador_de_type = [type(subelemento) for subelemento in elemento]
            
            if type(função_aleatoria) in verificador_de_type:
                if len(verificador_de_type) == 2:
                    return BOTÃO
                else:
                    return SELETOR
            else:
                return IMAGEM
                

class Menu_Single(Menu_Funcs, Formulador_Elementos):
    def __init__(_, nome = "", dim = [100,100],pos = [50,50],tema = TEMA_PADRÃO) -> None:
        super().__init__( nome , *dim , position=pos , theme=tema)
    
        _.__propriedades = _.get_menubar()
        
    @property
    def nome(_):
        return _.__propriedades.get_title()
    
    @nome.setter
    def nome(_, novo_nome : str):
        _.__propriedades.set_title(novo_nome)
        
    @property
    def dim(_):
        return (_.get_width(),_.get_height())
    
    @dim.setter
    def dim(_,nova_dimenção: list):
        super().resize(*nova_dimenção)
    
    @dim.setter
    def altura(_, nova: int):        
        super().resize(_.dim[0],nova)
        
    @dim.setter
    def largura(_, nova: int):
        super().resize(nova,_.dim[1])
        
    @property
    def posição(_):    
        return _.get_position()  
     
    @property
    def tema(_):
        return _.get_theme()

    @tema.setter
    def tema(_, novo_tema):
        _.tema = novo_tema
    
    @property
    def conteúdo(_):
        def achador(atuais):
            all_wids = [
                widgets.Label,
                    widgets.Button,
                        widgets.Selector,
                            widgets.Image
                        ]
            
            resultados = [
                Elemento.FRASE,
                    Elemento.BOTÃO,
                        Elemento.SELETOR,
                            Elemento.IMAGEM
                            ]
            
            try:
                indice = all_wids.index(type(atuais))
            except:
                return None
            else:
                return [resultados[indice],atuais]
        
        
        widgets_usados = _.get_widgets()
        plim = []
        for elemento, widget_expecifico in map(achador,widgets_usados):
            plim.append({elemento,widget_expecifico.get_title()})
        
        return plim
    
    def __add__(_, ELEMENTOS: list) -> None:
        '''
        OLÁ! bem vindo à sala principal de adção de elementos!
        O procedimento é separado em 3 etapas:
        ATENÇÃO: apenas as listas que não tiverem um Elemento passam pela 1° e 2° etapa
            (SIM) -> ["blabla"]
            (NÃO) -> [Elemento.FRASE,"blabla"]
            
        1° : verificação ; o(s) elemento(s) passa(m) por condições: Se é None,
                str, se já tem um Elemento nele, etc.
                    
        2° : adptação ; passado pelo "filro", a classe induz, pelo formato da lista, 
                que elemento ele deveria ser.
                EX: se for uma lista com 2 espaços e com uma função dentro -> Elemento.BOTÃO
                no fim, falta apenas por atras da lista original o Elemento
                EX: [Elemento.BOTÃO, ...]

        3° : ação ; hora de definitivamente ativar os elementos! A lista é dividida em 2: o tipo 
                do elemento e ele em si.
                EX : if tipo == Elemento.BOTÃO:
                        vo.botão(elem)
        '''
        
        ELEMENTO_100 = _.transformador_automatico( ELEMENTOS )
        
        for fração_dos_elementos in ELEMENTO_100:
            tipo,elem = fração_dos_elementos
            
            if tipo == Elemento.FRASE:
                _.frasezinha(elem)
            elif tipo == Elemento.BOTÃO:
                _.botão(*elem)
            elif tipo == Elemento.IMAGEM:
                _.imagem(elem)
            elif tipo == Elemento.SELETOR:
                _.seletor(*elem)   
    
    def __repr__(self) -> str:
        return f"{self.nome}(dim = ({self.altura},{self.largura}), tema = {self.tema}))"


'=== TESTES ==='


if __name__ == "__main__":
    ...