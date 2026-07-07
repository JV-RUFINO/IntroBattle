class B:
    def __init__( _ , str : str) -> None:
        _.str = str

    def __call__(_, funcao):
        def decorador():
            print(_.str)

            return funcao()

        return decorador

class A:

    seg_valor = "NO"

    def __init__( _ ,value ):
        _.value = value

    '''def First( values ):
        def Second_Decorator( self , function ):
            print(self.value)

            def Third_Last( *args , **kwargs ) -> bool:
                result = function( *args , **kwargs )

                return result

            return Third_Last  

        return Second_Decorator'''  
    def First( self , valores ):
        def Second_Decorator( function ):
            print(self.value)

            def Third_Last( *args , **kwargs ) -> bool:
                result = function( *args , **kwargs )

                return result

            return Third_Last
        
        return Second_Decorator

    '''def First( valores ):
        return '''

    '''@classmethod
    def Second_Decorator( cls , function ):
        def Third_Last( *args , **kwargs ) -> bool:


            result = function( *args , **kwargs )

            return result

        return Third_Last'''

        
    '''def First_Decorator( content ):
        def Second_Decorator( function ):
            def Third_Last( ) -> bool:
                print(content)

                # ERROR
                print(_.value)
                # ERROR

                result = function(  )

                return result

            return Third_Last
            
        return Second_Decorator'''

    
    '''def First( hahaha ):
        def Second( fase ):
            print(hahaha)

            def Third( self ) -> bool:
                print(self.value)
                print(self.seg_valor)
                

                resultado = fase(  )

                return resultado

            return Third
            
        return Second

    @classmethod
    def cls_decorator(cls, function):
        def wrapper(*args, **kwargs):
            print(cls.clsa_1, cls.clsa_2)
            return function(*args, *kwargs)
        return wrapper

    def instance_decorator(self, function):
        def wrapper(*args, **kwargs):
            print(self.ina_1, self.ina_2)
            return function(*args, *kwargs)
        return wrapper


    @First( "Example" )
    def Example( self ):
        return ">)"'''

class C:
    uno = 1
    dos = 2

    def __init__(self) -> None:
        self.tres = 3
        self.qua  = 4

    @classmethod
    def blabla( cls , funcao):
        def decorator(*args , **kwargs):
            print(cls.uno)
            print(cls.dos)

            return funcao(*args, **kwargs)

        return decorator

    def instance_decorator(self, function):
        def wrapper(*args, **kwargs):

            print(self.tres, self.qua)

            return function(*args, *kwargs)

        return wrapper
        
'''a = A("Exemplo")

b = a.First('conteudo')

@a.First('conteudo')
def blabla():
    return "Hello"'''

a = ["ha" , "haaaaa" , "hahahaha"]

for aa in range(0,len(a)):
    print(aa)

v = {"A":1,"B":2}
print(v.keys())
'''@C.blabla
def f(x):
  return x ** 2

@C.instance_decorator
def g(x):
    return 1 - 2 * x

g(3)

print(f)'''

'''a = A(10)
a.Example()'''
'''@A.First_Decorator(5000)
def blablabla():
    print(10)'''

'blablabla()'