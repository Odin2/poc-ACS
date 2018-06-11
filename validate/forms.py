from django import forms

"""
    Clase del formulario del modulo de validacion

"""
class ValidateForm(forms.Form):
    csv = forms.FileField()
    path = forms.FilePathField(path="pocAcs/funciones/dataset",allow_files=False,allow_folders=True)
    Particiones = forms.IntegerField()
    Cantidad_Imagenes_por_Particion = forms.IntegerField()