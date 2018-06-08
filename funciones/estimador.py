import numpy
# Random int.
#
#  retorna un valor entre 0 y 228 (la edad maxima de pacientes en meses).

import os
__path__=[os.path.dirname(os.path.abspath(__file__))]

from .output_predictions import Predict
import numpy as np
import cv2
'''
class Paciente:
    def __init__(self):
        self.sexo = None
        self.img= Imagen()
        self.url_imagen = None
        self.estimacion_edad= None
        self.estimador = Estimador()

    def estimar_edad(self,sexo, url_imagen,img):
        self.sexo=sexo
        self.img=img
        self.url_imagen= url_imagen
        self.estimacion_edad = self.estimador.estimar(sexo)[0][0]
        return self.estimacion_edad

class Imagen:
    def __init__(self, img=None):
        self.img = img
        self.vector = []

    def vectorizar(self):
        self.vector = self.img.T.flatten().T
        return None
    def leer_imagen(self, directorio):
        self.img = cv2.imread(directorio)
        return True
'''
class Estimador:
    def __init__(self):
        # The constructor
        self.predecir = None

    def estimar(self, sexo):
        self.predecir = Predict()
        self.predecir.star()
        resultado = self.predecir.predict(sexo)
        return resultado
    def estimar_muestra(self,sub_muestra,sexo):
        self.predecir = Predict()
        self.predecir.star()
        resultado = self.predecir.predictMod(sub_muestra,sexo)
        return resultado

