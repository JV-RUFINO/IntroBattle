# isso aqui é pra ser usado pelos personagens
from __future__ import annotations


from sys import path as caminho
from pathlib import Path as Caminhozão

arquivo = Caminhozão(__file__).resolve()
parente , raiz = arquivo.parent, arquivo.parents[1]
caminho.append(str(raiz))


# PYGAME
from pygame             import image as imagem, Surface as Superficie, Rect as Retangulo, Color as Cor
from pygame.font        import Font as Fonte
from pygame.draw        import rect as desenhar_retangulo ,polygon as desenhar_poligono 
from pygame.transform   import scale as imagem_escala

# IMPORTAÇÕES GERAIS
from os                 import getcwd
from os.path            import join

class texto_decorador: # decorador
    def __init__( _ , imagem , cor: Cor) :
        _.cor_caixa    = cor    # isso vai ser usado pra colorir as bordas da Caixa
        _.imagem_perso = imagem # a imagem do personagem usada pra identificar a Caixa

        _.maximo_linha = 34     # cada linha na caixa de texto comporta 34 caracteres por linha
        _.linha_atual  = 0      # 0 ou 1 // a linha , de cima ou de baixo , respectivamente
        _.frase_dict   = {}     # o dict que vai ser transformado

    def virar_linha_atual( _ ):
        _.linha_atual  = 0 if _.linha_atual == 1 else 1

        return _.linha_atual

    def palavra_limite( _ , linha_texto : str , nova_palavra : str ) -> bool:
        return len( linha_texto + nova_palavra ) > _.maximo_linha

    def ListParaStr( _ , lista : list ) -> str:
        frase_str = ""
        for ff in lista:
            frase_str += ff

        return frase_str

    def StrParaDict( _ , frase : list) -> dict:
        z = ['','']
        ii = 1
        palavra = ""
        for resu in _.ListParaStr( frase ):
            palavra += resu

            if _.palavra_limite( z[_.linha_atual] , palavra ):
                if _.linha_atual == 1:
                    ii += 1
                    z   = ['','']
                
                _.virar_linha_atual()

            if resu == " ":
                z[_.linha_atual] += palavra
                palavra = ""
            
            _.frase_dict.update( { str(ii) : z } )

        return _.frase_dict

    def ListParaDict( _ , lista : list ) -> dict:
        for ii in range(len(lista)):
            _.frase_dict.update( { str( ii + 1 ) : lista[ ii ] } )

        return _.frase_dict

    def traduzir_frase_dict( _ , fonte_texto : Fonte , cor_texto: Cor) -> dict:
        for ff in _.frase_dict:
            _.frase_dict[ff] = [
                    fonte_texto.render( _.frase_dict[ff][0] , False , cor_texto ),
                    fonte_texto.render( _.frase_dict[ff][1] , False , cor_texto )]

        return _.frase_dict

    def __call__( _ , funcao ):
        def decorador(*args: str, **kwargs: Cor):
            carregar_fonte = Caixa_Texto.fonte()

            conteudo, cor_texto = funcao( *args , **kwargs )
            if type(conteudo) != dict:              
                if type(conteudo) == list:          # conteudo já é uma lista pré-pronta
                    if type(conteudo[0]) == str:    # ["Isto" , "é" , "um exemplo "]
                        conteudo[-1] += " "

                        _.StrParaDict(  conteudo )
                    elif type(conteudo[0]) == list: # [["Isto é"],["um exemplo "]]
                        _.ListParaDict( conteudo )

                elif type(conteudo) == str:         # converter a string para uma lista
                    conteudo += " "                 # "Este é um exemplo"  -> "Este é um exemplo "
                    conteudo = [conteudo]           # "Este é um exemplo " -> ["Este é um exemplo "]

                    _.StrParaDict(  conteudo )
                
            _.traduzir_frase_dict( carregar_fonte , cor_texto )

            return Caixa_Texto( _.frase_dict , _.imagem_perso , _.cor_caixa )


        return decorador


class Caixa_Texto:
    def __init__( _ , frase : str , imagem , cor : Cor ):
        '''
        frase -> {
            "1" : [  pygame.font.Font(*insira path da fonte*).render("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA",False,(0, 255, 0)),
                        pygame.font.Font(*insira path da fonte*).render("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA",False,(0, 255, 0))],
            "2" : [pygame.font.Font(*insira path da fonte*).render("BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB",False,(0, 255, 0)),
                    pygame.font.Font(*insira path da fonte*).render("BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB",False,(0, 255, 0))]
            }

        imagem -> pygame.image.load(*insira path da imagem*)

        cor -> pygame.Color( int , int , int ) 
               Cor(int , int , int)
        '''
        
        _.frase  : dict       = frase
        _.imagem : Superficie = imagem_escala(imagem,(70,66))
        _.pri_cor: Cor        = cor
        _.alt_cor: Cor        = Cor( _.pri_cor[0]+40 , _.pri_cor[1]+40 , _.pri_cor[2]+40 )

        _.alt                 = [False, False, False]
        _.__index             = 0
        _.rodando             = True


    @staticmethod
    def fonte():
        return Fonte(join(getcwd(),'fonte_jogo',"fontePygame.ttf"),32)

    @property
    def indice( _ ):
        return [a for a in _.frase.keys()][_.index]

    @property
    def sum_cor( _ ):
        return [_.alt_cor if alt else _.pri_cor for alt in _.alt]

    @property
    def index( _ ):
        return _.__index
    
    @index.setter
    def index( _ , novo : int):
        limite_min = 0
        limite_max = len(_.frase)

        if novo < limite_min:
            novo = limite_max - 1
        elif novo >= limite_max:
            novo = limite_min
        
        _.__index = novo

    def resetar_cores( _ ):
        _.alt = [False,False,False]

    def __bool__( _ ):
        return _.rodando    
        
    def __call__( _ , screen: Superficie) -> None:
        if _.rodando:    
            carregar_fonte = _.fonte()
            todas_cores    = _.sum_cor
            pos , tam      = (250, 80),(131,39)

            # == BORDAS ==

            desenhar_retangulo(screen, _.pri_cor ,      Retangulo(100,50,1100,150) , width= 7 , border_radius=10) # desenhar caixa_grande        
            desenhar_retangulo(screen, todas_cores[0] , Retangulo(1000,210,180,50) , width= 7 , border_radius=10) # desenhar caixa_menor

            desenhar_poligono(screen,  todas_cores[1] , ((180,220),(180,280),(120,245))) # desenhar as setinhas
            desenhar_poligono(screen,  todas_cores[2] , ((240,220),(240,280),(300,245))) # desenhar as setinhas

            # == TEXTO ==
            
            screen.blit( _.frase[_.indice][0] , Retangulo(*pos, *tam) ) # texto principal: de cima
            screen.blit( _.frase[_.indice][1] , Retangulo(pos[0], pos[1]+50 , *tam) ) # texto principal: de baixo

            screen.blit( carregar_fonte.render( str(_.indice) , False , (255, 255, 255)) , 
                            Retangulo(195,230,100,100) ) # indice

            screen.blit( carregar_fonte.render( "ENTER" , False , (255, 255, 255) ) , 
                        Retangulo(1020,215,100,100) ) # 'ENTER' da caixa_menor 

            # == IMAGEM ==

            screen.blit( _.imagem , (140,95))

    def __repr__( _ ) -> str:
        return f"Caixa_texto(cor = {_.pri_cor} , alt = {_.alt}, imagem = {_.imagem}"


'=== TESTES ==='


if __name__ == "__main__":
    @texto_decorador(imagem.load(join(getcwd(),"banco_dados","Personagens","inimigos","caveira","down.png")),Cor(100,0,0))  
    def falacao(frase, cor_texto):
        return frase , cor_texto

    # Example file showing a basic pygame "game loop"
    import pygame
    from pygame.event   import get as capturar_evento
    from pygame.time    import Clock as Relogio
    from pygame.display import set_mode as definir_janela , set_caption as definir_titulo

    # pygame setup
    pygame.init()
    caixa_texto = falacao( [["Hora do Show ",""],["Poraaaaaaaaaaaaaa! ",""]] , Cor(150,100,0))

    screen = definir_janela((1280, 720))
    definir_titulo("IntroBattle")

    print(bool(caixa_texto))
    '''caixa_texto = Caixa_Texto(
        frase ={"1":[  Caixa_Texto.fonte().render("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA",False,(0, 255, 0)),
                            Caixa_Texto.fonte().render("A A A A A A A AAAAAAAAAAAAAAAAAAAA",False,(0, 255, 0))],
                "2":[Caixa_Texto.fonte().render("BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB",False,(0, 255, 0)),
                        Caixa_Texto.fonte().render("BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB",False,(0, 255, 0))]
                },
        imagem= imagem.load(Linkzin(getcwd(),"banco_dados","Personagens","inimigos","caveira","down.png")),
        cor   = Cor(100,0,0)
    )'''


    clock = Relogio()
    running = True

    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in capturar_evento():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    caixa_texto.alt[2] = True
                    
                if event.key == pygame.K_LEFT:
                    caixa_texto.alt[1] = True
                
                if event.key == pygame.K_RETURN:
                    caixa_texto.alt[0] = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    caixa_texto.index += 1
                    
                if event.key == pygame.K_LEFT:
                    caixa_texto.index -= 1
    
                if event.key == pygame.K_RETURN:
                    caixa_texto.rodando = False
                    
                caixa_texto.resetar_cores()

            
        # fill the screen with a color to wipe away anything from last frame
        screen.fill("purple")
        # RENDER YOUR GAME HERE

        
        caixa_texto(screen)
        

        # flip() the display to put your work on screen
        pygame.display.flip()

        clock.tick(60)  # limits FPS to 60

    pygame.quit()