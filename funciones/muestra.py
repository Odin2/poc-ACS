from .estimador import Estimador
import random
import numpy as np

"""
Clase encargada del conjunto de muestras y 
las diferentes metricas
"""


class Muestra:
    def __init__(self):
        # The constructor.
        self.muestra = []
        self.estimador = Estimador()
        self.sub_muestra =[]
        
        # self.estimador = Estimador()
    """
    Metodo de calcular metrica MAE
    """
    def calcular_MAE(self,y1,y2):
        y_1=np.array(y1)
        y_2=np.array(y2)
        mae = (1/len(y1))*sum(np.abs(y_1-y_2))
        return mae
    """
    Metodo de calcular metrica MSE
    """
    def calcular_MSE(self,y1,y2):
        y_1=np.array(y1)
        y_2=np.array(y2)
        mae = (1/len(y1))*sum((y_1-y_2)**2)
        return mae
        return True
    """
    Metodo de cargar conjunto de prueba
    Retorna un array con los diferentes aspectos
    """
    def cargar_muestra(self,muestra,k,cant_img):
        self.sub_muestra=[]
        for i in range(k):
            self.sub_muestra.append([])
            for j in range(cant_img):
                self.sub_muestra[i].append([])
                self.sub_muestra[i].append([])
                self.sub_muestra[i].append([])
                cambio=True
                while(cambio):
                    valor=random.choice(muestra.get("id"))
                    if valor in self.sub_muestra[i][0]:
                        cambio=True
                    else:
                        index=muestra.get("id").index(valor)
                        self.sub_muestra[i][0].append(valor)
                        self.sub_muestra[i][1].append(muestra.get("age")[index])
                        self.sub_muestra[i][2].append(muestra.get("sex")[index])
                        cambio=False
        
        self.muestra=muestra
        resultado={"sub":self.sub_muestra,"mae":[],"mse":[],"res":[],"mean":[],"std":[],"var":[]}
        
        x = ""
        y = 1
        for i in self.sub_muestra:
            estimacion=self.estimador.estimar_muestra(i[0],i[2])
            res = str(estimacion)
            mae = str(self.calcular_MAE(estimacion,i[1]))
            mse = str(self.calcular_MSE(estimacion,i[1]))
            mean = str(np.mean(estimacion))
            std = str(np.std(estimacion))
            var = str(np.var(estimacion))
            x = x + "Resultado particion " + str(y) + ": " + res + "\n" + "Muestra: " + str(self.sub_muestra[y-1][:3]) + "\n" + "MAE: " + mae + "\n" + "MSE: " + mse + "\n" + "Mean: "+ mean +"\n" + "std: " + std + "\n" + "variance: " + var + "\n"
            y += 1
        return x
