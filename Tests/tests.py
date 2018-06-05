from django.test import TestCase
from funciones.csvpy import datoscsv

from funciones.estimador import Estimador
import unittest
import csv
from selenium import webdriver
from django.contrib.auth.models import User
# Create your tests here.

class DjangoTest(unittest.TestCase):
    '''
    def test_1(self):
        print("Test1: Cargar imagen")
        imagen = Imgl()
        imagen.cargar_imagen("/bonage/dataset/test") 
    '''
    
    '''
    '''
    
    def test_2(self):
        print("Test2: estimar")
        estimador = Estimador()
        valor=estimador.estimar("F")
        print(valor[0][0])
        
    def test_3(self):
        print("Test3: csv")
        from funciones.csvpy import train
        
        
        
if __name__ == '__main__':
    unittest.main
    
class SeleniumTest(unittest.TestCase):
    
    def test_5(self):
        print("Test: login como usuario")
        browser = webdriver.Chrome()
        browser.get('localhost:8000')
        browser.find_element_by_name("username").send_keys("user1")
        browser.find_element_by_name("password").send_keys("a1s2d3f4")
        browser.find_element_by_name("loginbtn").click()
        
                
    def test_6(self):
        print("Test: Crear Usuario")
        
        browser = webdriver.Chrome()
        browser.get('http://localhost:8000/admin/')
        browser.find_element_by_name("username").send_keys("admin")
        browser.find_element_by_name("password").send_keys("a1s2d3f4")
        browser.find_element_by_name("username").send_keys(u'\ue007')
        browser.get('http://localhost:8000/admin/auth/user/add/')
        browser.find_element_by_name("username").send_keys('testuser')
        browser.find_element_by_name("password1").send_keys("a1s2d3f4")
        browser.find_element_by_name("password2").send_keys("a1s2d3f4")
        browser.find_element_by_name("_save").click()
        if __name__ == '__main__':
            unittest.main
            
class IntegrationTest(unittest.TestCase):
    '''
    def test_7(self):            
        user=User.objects.create_user('IntegrationUser', password='a1s2d3f4')
        user.is_superuser=False
        user.is_staff=False
        user.save()
        
    def test_8(self):            
        user=User.objects.create_user('IntegrationAdmin', password='a1s2d3f4')
        user.is_superuser=True
        user.is_staff=True
        user.save()
        '''