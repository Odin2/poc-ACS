from django import forms

## Formulario para el ingreso de informacion
#
#  Nombre y edad del paciente, y la imagen.
class UploadFileForm(forms.Form):
    Patient_Name = forms.CharField(max_length=50)
    Patient_Age = forms.CharField(max_length=50)
    file = forms.ImageField()