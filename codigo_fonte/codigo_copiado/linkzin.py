from os import path , getcwd

def Linkzin(*path_pasta, act_dir = False) -> str: # criar um link igual o Windows Explorer faz
    " Linkzin( 'um' , 'dois' , 'quatro' ) -> 'um\dois\quatro' "
    
    if act_dir:
        current_dir = path.split( getcwd() )
        path_pasta = current_dir + path_pasta
    
    return path.join(*path_pasta)