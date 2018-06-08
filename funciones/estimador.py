import numpy
# Random int.
#
#  retorna un valor entre 0 y 228 (la edad maxima de pacientes en meses).

import os
__path__=[os.path.dirname(os.path.abspath(__file__))]

from .output_predictions import Predict
import numpy as np
import cv2

"""
Clase que realiza el acceso de las predicciones, 
recibe el sexo y la imagen, en este caso el path
default es dataset/test
todo lo retornado en medida de meses
"""
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

