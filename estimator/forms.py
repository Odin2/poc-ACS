from django import forms

## Formulario para el ingreso de informacion
#
#  Nombre y edad del paciente, y la imagen.
class UploadFileForm(forms.Form):
    Patient_Name = forms.CharField(max_length=50)
    Patient_Age = forms.CharField(max_length=50)
    CHOICES=[('Male','Male'),
         ('Female','Female')]
    Patient_Sex = forms.ChoiceField(choices=CHOICES)
    file = forms.ImageField()