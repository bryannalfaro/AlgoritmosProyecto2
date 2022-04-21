# Recibe la configuracion y el valor a buscar
# Retorna la configuracion con el valor en la posicion 0 y el costo
def mtf(config, value):
    contador = 0
    contador_externo = 0
    for i in config:
        contador_externo+=1
        if i == value:
            contador =contador_externo
            new = config.pop(contador_externo-1)
            config.insert(0,new)
            break
    return config, contador

# Improved Move To Front
# Recibe la configuracion, el valor a buscar, la secuencia completa de solicitudes y el indice de la solicitud actual
# Retorna la configuracion con el valor en la posicion 0 y el costo
def imtf(config, value,solicitud,index):
    contador = 0
    contador_externo = 0
    cont1 = 0
    arr = []
    for i in config:
        contador_externo+=1
        if i == value:
            contador =contador_externo
            for i in range(contador-2):
                arr.append(solicitud[(i+solicitud[index]-1)%len(solicitud)])
            if len(arr)!=0:
                for i in arr:
                    if i == value:
                        cont1 +=1
                if cont1 == (contador-2):
                    new = config.pop(contador_externo-1)
                    config.insert(0,new)
                break
    return config, contador