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