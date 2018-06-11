from django.shortcuts import render
from django.http import HttpResponse
import validate.forms
from funciones.muestra import Muestra
from funciones.csvpy import datoscsv
import csv
import io

"""
    Metodo que maneja la respuesta al usuario de la validacion
    
    Args:
        request en el que se reciben la informacion ingresada del formulario
        
    Returns:
        HttpResponse con la respuesta de la validacion
"""
def index(request):
    form = validate.forms.ValidateForm()
    if request.method == 'POST':
        form = validate.forms.ValidateForm(request.POST, request.FILES)
        if form.is_valid():
            csvP = form.cleaned_data['csv']
            path = form.cleaned_data['path'].split('\\')[1]
            Particiones = form.cleaned_data['Particiones']
            Cantidad_Imagenes_por_Particion = form.cleaned_data['Cantidad_Imagenes_por_Particion']
            
            csvf = csvP.read().decode()
            csvf = csvf.split("\r\n")
            csvf = csvf[1:]
            muestra={"id":[],"age":[],"sex":[]} 
            for entrada in csvf:
                if entrada != "":
                    reg = entrada.split(",")
                    
                    muestra.get("id").append(int(reg[0]))
                    muestra.get("age").append(int(reg[1]))
                    if reg[2] == "True":
                        muestra.get("sex").append("M")
                    else:
                        muestra.get("sex").append("F")
                
            print(str(muestra))
            pba = Muestra()
            ret= pba.cargar_muestra(muestra,Particiones,Cantidad_Imagenes_por_Particion)
            return render(request, 'validate/cover.html', {'form': form, 'guess': ret})
            #print(form.cleaned_data['path'].split('\\')[1])
    else:
        form = validate.forms.ValidateForm()
    return render(request, 'validate/cover.html', {'form': form, 'guess': "Input your data"})