def parametros(var1):
    lista_parametros = [var1]
    lista_unicos = []
    palabra = str()
    for elemento in lista_parametros:
        if elemento !=",":
            palabra += elemento
        elif elemento == " ":
            pass
        else:
            lista_unicos.append(palabra)
            palabra = str()
    if len(lista_unicos)== 3:
        for x in lista_unicos:
            print("parametro: ",lista_unicos[x])
        return lista_parametros
    else:
        return None
    

variable1 = input("Ingrese 3 parametros separados por coma(,):")
parametros(variable1)