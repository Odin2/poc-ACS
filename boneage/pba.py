from output_predictions import Predict
import numpy as np
import cv2

class Estimador:
    def __init__(self):
        # The constructor
        self.predecir = None

    def estimar(self, sexo):
        self.predecir = Predict()
        self.predecir.star()
        resultado = self.predecir.predict(sexo)
        return resultado



import sys
sys.path.append('poc-ACS/boneage')

##img= cv2.imread("/dataset/test")
##n= Paciente()
##n.estimar_edad("F","/dataset/test", img)
print("Test: estimar")
estimador = Estimador()
valor=estimador.estimar("F")
print(valor[0][0])

##n= Paciente()
##n.estimar_edad("F","/dataset/test", img)

##cv2.imshow('image', imagen)
##cv2.waitKey(0)
##cv2.destroyAllWindows()


