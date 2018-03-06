#!/usr/bin/python
# -*- coding: utf-8 -*-
import csv



class datoscsv:

    def __init__(self,id1,boneage,male):
        self.id1 = id1
        self.boneage = boneage
        self.male = male
        
## Ejemplo de lectura y manipulacion de datos en un csv.
#
#  Imprime todos los datos a la consola de python.
def train():
    lista = []
    with open('train.csv') as csvarchivo:  # Abrir archivo csv
        entrada = csv.reader(csvarchivo)  # Leer todos los registros
        for reg in entrada:  # Leer registro (lista)

        # print(reg)  # Mostrar registro

        # Leer campos

            m = datoscsv(reg[0], reg[1], reg[2])
            lista.append(m)
            print(m.id1 + ' ' + m.boneage + ' ' + m.male)  # mostrar objeto

    csvarchivo.close()



            