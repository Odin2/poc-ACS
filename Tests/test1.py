from django.test import TestCase
import unittest
from funciones.muestra import Muestra

class DjangoTest(unittest.TestCase):
    def testMuestra(self):
        pba = Muestra()
        k=2
        cant_img=2
        muestra={"id":[1414,1406,1394,1388,1412],"age":[78,106,57,126,156],"sex":["M","F","M","F","F"]}
        ret= pba.cargar_muestra(muestra,k,cant_img)
        print(ret)
        