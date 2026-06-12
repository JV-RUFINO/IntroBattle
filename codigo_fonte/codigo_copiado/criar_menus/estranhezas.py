class MenuCloneException(Exception):
    "aparece quando um MENU é criado igual outro já existente"
    
    def __init__(vo,menu_original = "SEM INFORMAÇÕES",menu_clone = "SEM INFORMAÇÕES") -> None:
        vo.CONJUNTO = []
        
        vo.titulo = "OH NÃO! existem pelo menos 2 Menus identicos um ao outro!"
        vo.primeiro_menu = f"|| PRIMEIRO: {menu_original}"
        vo.segundo_menu  = f"|| SEGUNDO : {menu_clone}"
        vo.espaço        = " ".rjust(len(vo.segundo_menu)).replace(" ", "=")
        vo.finalização   = "É RECOMENDAVEL PRESTAR ATENÇÃO"
        
        vo.MENSAGEM = ""
        for element in vo.CONJUNTO:
            vo.MENSAGEM += element
            vo.MENSAGEM += "\n"
        else:            
            super().__init__(vo.MENSAGEM)
            
    def __str__(vo) -> str:
        return super().__str__()
    
    def __setattr__(vo, __name: str, __value: ...) -> None:
        if __name.isupper() != True:
            vo.CONJUNTO.append(__value)
        
        return super().__setattr__(__name, __value)