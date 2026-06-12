# This class handles sprite sheets
# This was taken from www.scriptefun.com/transcript-2-using
# sprite-sheets-and-drawing-the-background
# I've added some code to fail if the file wasn't found..
# Note: When calling images_at the rect is the format:
# (x, y, x + offset, y + offset)

from pygame import image , Rect , Surface , RLEACCEL 



def imagem_unica( sheet: Surface , coordenada : tuple, colorkey : tuple = None): # Carrega uma imagem expecifica de um coordenada expecifica
    "Carrega a imagem de x,y,x+offset,y+offset"
    # coordenada = ( x , y , comprimento , largura )

    rect  =  Rect(*coordenada)  
    image =  Surface(rect.size).convert()

    image.blit( sheet , (0, 0) , rect )
    
    if colorkey != None:
        if colorkey == -1:
            colorkey = image.get_at((0,0))

        image.set_colorkey(colorkey, RLEACCEL)

    return image

    
def porcao_imagens( sheet : Surface , dict_coordenadas: dict , colorkey = None) -> list: # Carrega uma porção de imagens e retorna uma lista
    "Carrega multiplas imagens, supply a list of coordinates" 
    # coordenada = ( x , y , comprimento , largura )
    # dict_coordenadas = {
    #       0 : ( x , y , comprimento , largura )
    #       1 : ( x , y , comprimento , largura )
    #       2 : ( x , y , comprimento , largura )
    # }

    return [ imagem_unica( sheet , dict_coordenadas[ordem], colorkey ) for ordem in range(len(dict_coordenadas)) ]
    
    
def carregar_tira( sheet : Surface , coordenadas: tuple , contagem_imagens: int , colorkey = None) -> list: # Carrega a tira inteira de imagens
    "Carrega uma tira de imagens e as retorna como uma lista"        
    # coordenada = ( x , y , comprimento , largura )
    dict_coordenadas = {}
    x , y , largura , comprimento = coordenadas

    for contagem in range(contagem_imagens):
        'print( x*(contagem+1))'

        dict_coordenadas.update({ contagem : ( x*(contagem+1) , y , comprimento , largura ) })

    return porcao_imagens( sheet , dict_coordenadas , colorkey )


if __name__ == "__main__":
    from os import path, getcwd

    def Linkzin(*path_pasta, act_dir = False) -> str: # criar um link igual o Windows Explorer faz
        " Linkzin( 'um' , 'dois' , 'quatro' ) -> 'um\dois\quatro' "
        
        if act_dir:
            current_dir = path.split( getcwd() )
            path_pasta = current_dir + path_pasta
        
        return path.join(*path_pasta)

    # Example file showing a basic pygame "game loop"
    import pygame

    # pygame setup
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))

    pygame.display.set_caption("IntroBattle")

    clock = pygame.time.Clock()
    running = True

    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # fill the screen with a color to wipe away anything from last frame
        screen.fill("black")
        # RENDER YOUR GAME HERE

        
        img   = image.load(Linkzin(getcwd(),'codigo_fonte','essenciais','Fire Breath hit effect SpriteSheet.png'))
        img_2 = porcao_imagens(img,{0:(0,0,100,48),1:(100,0,100,48)},-1)


        screen.blit(img_2[1],(100,100))


        # flip() the display to put your work on screen
        pygame.display.flip()

        clock.tick(60)  # limits FPS to 60

    pygame.quit()