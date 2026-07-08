from __future__ import annotations

from sys import path as caminho
from pathlib import Path as Caminhozão

arquivo = Caminhozão(__file__).resolve()
parente , raiz = arquivo.parent, arquivo.parents[1]
caminho.append(str(raiz))

# ESSENCIAIS
from battle_exterior    import Linkzin
from battle_exterior    import Caixa_Texto

# PYGAME
import pygame
from pygame             import Surface  as Superficie , KEYDOWN as TECLA_SEGURADA , KEYUP as TECLA_APERTADA , K_LEFT as ESQUERDA , K_RIGHT as DIREITA , K_RETURN as ENTER
from pygame.image       import load     as carregar_imagem
from pygame.event       import get      as capturar_evento
from pygame.time        import Clock    as Relogio
from pygame.transform   import scale    as imagem_escala
from pygame.event       import Event    as Evento

# IMPORTAÇÕES GERAIS
from os import getcwd


' === CÓDIGO REAL === '


class Criar_Fase:
    def __init__( _ , *background: str , caminho_comum = True , tipo = ".png" , fps_limit = 60 , auto_X = True ):
        cc           = "" if caminho_comum == False else _.caminho_comum()

        _.background = carregar_imagem( Linkzin( cc , *background ) + tipo ) #

        _.fps_limit  = fps_limit
        _.auto_X     = auto_X

    @staticmethod
    def caminho_comum():
        return Linkzin( getcwd() , 'banco_dados' , 'Cenarios' )

    def __call__(_ , funcao):
        '''
        receber_screen -> argumento auto-inserido pelo decorador. É a Surface do pygame
        novo_evento    -> evento(EX: teclado do jogador) capturado. Pode ser util para a fase
            EX: () = nenhum evento
            EX: (pygame.K_ENTER) -> jogador pressionou o ENTER
        TODA FASE DEVE RETORNAR TRUE OU FALSE
        '''

        return Fase( Fase_Componentes( funcao , _.background )  , _.fps_limit , _.auto_X )

class Adicionar_Fase(Criar_Fase):
    def __init__( _ , *background: str, fonte: Fase , caminho_comum=True, tipo= ".png" ):
        super().__init__( *background , caminho_comum = caminho_comum , tipo = tipo , fps_limit = fonte.fps_limit , auto_X = fonte.auto_X )

        _.fonte = fonte

    def __call__( _ , funcao):
        _.fonte.fases_totais.todas_fases.append( funcao )
        _.fonte.fases_totais.todos_backgrounds.append( _.background )

        return _.fonte

class Fase_Componentes:
    CT              = None
    index           = 0

    def __init__( _ , fase_principal , background_principal : Superficie ):
        _.todas_fases       = [ fase_principal ]
        _.todos_backgrounds = [ background_principal ]

        _.fases_evento      = {}

    @staticmethod
    def caminho_comum():
        return Linkzin( getcwd() , 'banco_dados' , 'Cenarios' )

    @property
    def fase_atual( _ ):
        return _.todas_fases[_.index]

    @property
    def back_atual( _ ):
        return _.todos_backgrounds[_.index]

    @property
    def eventos_gravados( _ ):
        return _.fases_evento.keys()

    def gravar_evento_fase( _ , tipo_evento: Evento , fase):
        _.fases_evento.update( { tipo_evento : fase } )

    def printar_background( _ , screen : Superficie ):
        screen.blit( _.back_atual , ( 0 , 0 ) )

    def verificar_evento_fase( _ , novo_evento : list ):
        for evento in novo_evento:
            evento : Evento

            novo_index = None
            if evento.type == TECLA_APERTADA and evento.key in _.eventos_gravados:
                novo_index = evento.key
            elif evento.type in _.eventos_gravados:
                novo_index = evento.type

            if novo_index != None:
                return _.fases_evento[novo_index]
        return None

    def rodar_evento_fase( _ , receber_screen : Superficie , info_extra = None , novo_evento: list = None ):
        index_evento = _.verificar_evento_fase( novo_evento )

        if index_evento != None:
            _.todas_fases[index_evento]( receber_screen , info_extra , _ , novo_evento )

        return True

    def rodar_fase( _ , receber_screen : Superficie , info_extra = None , novo_evento: list = None):
        resultado = _.fase_atual( receber_screen , info_extra , _ , novo_evento ) # sempre retorna True ou False

        if _.index == 0:
            return resultado
        
        elif _.index > 0 and resultado == False:
            _.index = 0

        return True

    def __getitem__( _ , item ) -> ...:
        _.index = item 

        return _

    def __len__( _ ):
        return len(_.todas_fases)

    def __repr__( _ ) -> str:
        return f"FASE ATUAL: {_.fase_atual}"

class Fase:
    running             = True
    relogio             = Relogio()
    ultimo_evento       = None

    def __init__( _ , fases_totais : Fase_Componentes , fps_limit : int , auto_X = True ) -> None:
        _.fases_totais  = fases_totais
        _.fps_limit     = fps_limit
        _.auto_X        = auto_X

    @staticmethod
    def caminho_comum():
        return Linkzin( getcwd() , 'banco_dados' , 'Cenarios' )

    @property
    def index( _ ):
        return _.fases_totais.index

    @index.setter
    def index( _ , novo_index ):
        _.fases_totais.index = novo_index

    @property
    def fase_atual( _ ):
        return _.fases_totais.fase_atual

    @property
    def background_atual( _ ):
        return _.fases_totais.back_atual
    
    @background_atual.setter
    def background_atual( _ , mudar_back ):
        _.fases_totais.todos_backgrounds[_.index] = mudar_back

    @property
    def todos_backgrounds( _ ):
        return _.fases_totais.todos_backgrounds

    def Fase_Adicional( _ , *background: str , caminho_comum = True , tipo = ".png" ):
        def Second_Decorator( function ):
            @Adicionar_Fase( *background , fonte= _ , caminho_comum= caminho_comum , tipo= tipo )
            def Third_Last( *args , **kwargs ) -> bool:
                result = function( *args , **kwargs )

                return result

            return Third_Last
        
        return Second_Decorator

    def Fase_Evento( _  , tipo_evento : Evento , auto = True ):
        def Second_Decorator( function ):
            @Adicionar_Fase( 'cena_erro' , fonte = _ , caminho_comum = True , tipo = ".png" )
            def Third_Last( *args , **kwargs ) -> bool:
                a = None
                for evento in args[-1]:
                    evento : Evento

                    if evento.type == tipo_evento or evento.type == TECLA_APERTADA and evento.key == tipo_evento:
                        a = evento.key 
                    
                        break
                    
                args = list(args) ; args[-1] = a ; args = tuple(args)
                
                result = function( *args , **kwargs )

                return result

            if auto:
                _.fases_totais.gravar_evento_fase( tipo_evento , len(_.fases_totais) - 1 )

            return Third_Last
        
        return Second_Decorator

    def Fase_Caixa_Texto( _ , *background: str , caminho_comum = True , tipo = ".png" ):
        def Second_Decorator( function ):
            @Adicionar_Fase( *background , fonte= _ , caminho_comum= caminho_comum , tipo= tipo )
            def Third_Last( *args , **kwargs ) -> bool:
                _.fases_totais.CT : Caixa_Texto
                for event in args[-1]:
                    event : Evento

                    if event.type == TECLA_SEGURADA:
                        if event.key == DIREITA:
                            _.fases_totais.CT.alt[2] = True
                            
                        if event.key == ESQUERDA:
                            _.fases_totais.CT.alt[1] = True
                        
                        if event.key == ENTER:
                            _.fases_totais.CT.alt[0] = True

                    if event.type == TECLA_APERTADA:
                        if event.key == DIREITA:
                            _.fases_totais.CT.index += 1
                            
                        if event.key == ESQUERDA:
                            _.fases_totais.CT.index -= 1

                        if event.key == ENTER:
                            _.fases_totais.CT.rodando = False
                            
                        _.fases_totais.CT.resetar_cores()
                
                result = False
                if _.fases_totais.CT.rodando:
                    screen : Superficie = args[0]

                    _.fases_totais.CT( screen )

                result = function( *args , **kwargs )

                return result

            return Third_Last
        
        return Second_Decorator

    def novo_evento( _ , ev = None ):
        if ev == None:
            _.running = True

        return capturar_evento() 

    def AUTO_X( _ , todos_eventos , res ):
        for evento in todos_eventos:
            if evento.type == pygame.QUIT:
                return False

        return res

    def __call__( _ , receber_screen : Superficie , info_extra = None , index : Fase_Componentes = None ,novo_evento: list = None ):
        '''
        receber_screen -> argumento auto-inserido pelo decorador. É a Surface do pygame
        novo_evento    -> evento(EX: teclado do jogador) capturado. Pode ser util para a fase
            EX: () = nenhum evento
            EX: (pygame.K_ENTER) -> jogador pressionou o ENTER
        TODA FASE DEVE RETORNAR TRUE OU FALSE
        '''

        for numero in range( 0 , len( _.todos_backgrounds) ):
            _.index = numero

            _.background_atual = imagem_escala( _.background_atual , ( receber_screen.get_width() , receber_screen.get_height() ))

        _.index     = 0
        _.running   = True

        while _.running:
            _.ultimo_evento = _.novo_evento( novo_evento )

            # FASE SENDO CRIADA

            _.fases_totais.printar_background( receber_screen )

            _.running = _.fases_totais.rodar_evento_fase( receber_screen , info_extra , _.ultimo_evento )

            _.running = _.fases_totais.rodar_fase( receber_screen , info_extra , _.ultimo_evento ) 
            
            pygame.display.flip()
            
            # FASE SENDO CRIADA

            if _.auto_X:
                _.running = _.AUTO_X( _.ultimo_evento , _.running )

            _.relogio.tick( _.fps_limit )  # limits FPS to 60
        
        return _.ultimo_evento

    def __repr__( _ ) -> str:
        return f"FASE ATUAL: {_.fase_atual}"


' === TESTES === '


if __name__ == "__main__":
    from pygame.display     import set_mode as definir_janela , set_caption as definir_titulo
    from pygame             import K_RETURN as ENTER , KEYUP , K_LEFT

    from aliados import Caçadora

    # pygame setup
    pygame.init()
    

    screen = definir_janela((1280, 720))
    definir_titulo("IntroBattle")


    @Criar_Fase('salão')
    def fase(
            screen :Superficie, 
                info_extra = None,
                    index: Fase_Componentes = None,
                        eventos:list = None):
        for evento in eventos:
            if evento.type == KEYUP:
                if evento.key == ENTER:
                    C = Caçadora()
                    index.CT = C.dialogo_combate()

                    index[1]

        'print(index.fases_evento)'
             
        return True

    """@fase.Fase_Evento('cena_battle', tipo_evento= ENTER)
    def nova_fase( 
        screen :Superficie, 
                info_extra = None,
                    index: Fase_Componentes = None,
                        eventos:Evento = None):
        '''print("hahaha")
        if eventos == ENTER:
            print("hihihihi")
            return False'''

        return True"""
    
    @fase.Fase_Caixa_Texto( 'salão' )
    def CT(
            screen :Superficie, 
                info_extra = None,
                    index: Fase_Componentes = None,
                        eventos:list = None):

        return True

    fase(screen)
    
    pygame.quit()

