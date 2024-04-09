def funcion(n):
    longitud = len(str(n))
    print(longitud)
    for i in range(longitud//2):
        
        if str(n)[i] != str(n)[longitud-i-1]:
            print(str(n)[i])
            print(str(n)[longitud-i-1])
            return False
print(funcion(555))


def funcion2(i,t):
    return list(range(i,i+t))
print(funcion2(2,7))


dic = {"a":1,"b":2}
print("c"in dic)

def funcion3(n):
    if type(n) !=int or n <1:
        return None
    if n==1:
        resultado = n*funcion3(n-1)
        return resultado
print(funcion3(0))

numeros = [1,2,3,4,5]
p = 1
for n in numeros:
    p *= n
print(p)