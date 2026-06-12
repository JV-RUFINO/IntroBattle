dic = {}
lista = [[1,2],[3,4,5]]
for a in range(len(lista)):
    dic.update( {str(a + 1) : lista[a] } )

print(dic)