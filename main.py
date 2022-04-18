#mtf algorithm
#Universidad del Valle de Guatemala
#Analisis de Algoritmos
#Integrantes:
#Bryann Alfaro
#Diego de Jesus
#Julio Herrera
#Jose Ponce
#Gabriel Quiroz

#Referencia
#https://www.programiz.com/python-programming/methods/list/pop
#https://rosettacode.org/wiki/Move-to-front_algorithm
from mtf_functions import *

configuracion = [0,1,2,3,4]
secuencia = [0,1,2,3,4,0,1,2,3,4,0,1,2,3,4,0,1,2,3,4]

costo = 0
configuracion_after = configuracion
costo_total = 0
print('\n PARTE A \n')
for i in secuencia:
    costo = 0

    print('Configuracion inicial', configuracion_after)
    print('Se esta solicitando: ',i)
    configuracion_after, costo = mtf(configuracion_after,i)
    print('Costo: ', costo)
    costo_total += costo
    print('Configuracion con MTF: ',configuracion_after,'\n')
print('Costo total: ', costo_total)
print('Configuracion final: ',configuracion_after,'\n')

configuracion = [0,1,2,3,4]
secuencia = [4, 3, 2, 1, 0, 1, 2, 3, 4, 3, 2, 1, 0, 1, 2, 3, 4]
configuracion_after = configuracion
costo_total = 0
print('\n PARTE B \n')
for i in secuencia:
    costo = 0

    print('Configuracion inicial', configuracion_after)
    print('Se esta solicitando: ',i)
    configuracion_after, costo = mtf(configuracion_after,i)
    print('Costo: ', costo)
    costo_total += costo
    print('Configuracion con MTF: ',configuracion_after,'\n')
print('Costo total: ', costo_total,'\n')
print('Configuracion final: ',configuracion_after,'\n')


configuracion = [0,1,2,3,4]
secuencia = []
for i in range(0,20):
    secuencia.append(0)

configuracion_after = configuracion
costo_total = 0
print('\n PARTE C \n')
for i in secuencia:
    costo = 0

    print('Configuracion inicial', configuracion_after)
    print('Se esta solicitando: ',i)
    configuracion_after, costo = mtf(configuracion_after,i)
    print('Costo: ', costo)
    costo_total += costo
    print('Configuracion con MTF: ',configuracion_after,'\n')
print('Costo total: ', costo_total,'\n')
print('Configuracion final: ',configuracion_after,'\n')

configuracion = [0,1,2,3,4]
secuencia = [4,3,2,1,0,4,3,2,1,0,4,3,2,1,0,4,3,2,1,0]


configuracion_after = configuracion
costo_total = 0
print('\n PARTE D \n')
for i in secuencia:
    costo = 0

    print('Configuracion inicial', configuracion_after)
    print('Se esta solicitando: ',i)
    configuracion_after, costo = mtf(configuracion_after,i)
    print('Costo: ', costo)
    costo_total += costo
    print('Configuracion con MTF: ',configuracion_after,'\n')
print('Costo total: ', costo_total,'\n')
print('Configuracion final: ',configuracion_after,'\n')

configuracion = [0,1,2,3,4]
secuencia = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2 ]


configuracion_after = configuracion
costo_total = 0
print('\n PARTE E \n')
for i in secuencia:
    costo = 0

    print('Configuracion inicial', configuracion_after)
    print('Se esta solicitando: ',i)
    configuracion_after, costo = mtf(configuracion_after,i)
    print('Costo: ', costo)
    costo_total += costo
    print('Configuracion con MTF: ',configuracion_after,'\n')
print('Costo total: ', costo_total,'\n')
print('Configuracion final: ',configuracion_after,'\n')

configuracion = [0,1,2,3,4]
secuencia = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]


configuracion_after = configuracion
costo_total = 0
for i in secuencia:
    costo = 0

    print('Configuracion inicial', configuracion_after)
    print('Se esta solicitando: ',i)
    configuracion_after, costo = mtf(configuracion_after,i)
    print('Costo: ', costo)
    costo_total += costo
    print('Configuracion con MTF: ',configuracion_after,'\n')
print('Costo total: ', costo_total,'\n')
print('Configuracion final: ',configuracion_after,'\n')

print('\n')
configuracion = [0,1,2,3,4]
secuencia = []
secuencia = [4,3,2,1,0,4,3,2,1,0,4,3,2,1,0,4,3,2,1,0] #worst
secuencia2 = [4,3,3,3,2]
secuencia3 = [] #best
for i in range(0,20):
    secuencia3.append(0)
configuracion_after = configuracion
costo_total = 0
print('\n PARTE F BEST \n')
index = 0
for i in secuencia3:
    costo = 0

    print('Configuracion inicial', configuracion_after)
    print('Se esta solicitando: ',i)
    configuracion_after, costo =imtf(configuracion_after,i,secuencia3,index)
    index+=1
    print('Costo: ', costo)
    costo_total += costo
    print('Configuracion con IMTF: ',configuracion_after,'\n')
print('Costo total: ', costo_total,'\n')
print('Configuracion final: ',configuracion_after,'\n')

configuracion = [0,1,2,3,4]
secuencia = []
secuencia = [4,3,2,1,0,4,3,2,1,0,4,3,2,1,0,4,3,2,1,0] #worst


configuracion_after = configuracion
costo_total = 0
print('\n PARTE F WORST \n')
index = 0
for i in secuencia:
    costo = 0

    print('Configuracion inicial', configuracion_after)
    print('Se esta solicitando: ',i)
    configuracion_after, costo =imtf(configuracion_after,i,secuencia,index)
    index+=1
    print('Costo: ', costo)
    costo_total += costo
    print('Configuracion con IMTF: ',configuracion_after,'\n')
print('Costo total: ', costo_total,'\n')
print('Configuracion final: ',configuracion_after,'\n')
