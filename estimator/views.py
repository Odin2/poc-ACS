from django.shortcuts import render

from funciones.estimador import ran
# Create your views here.

def index(request):
    x = ran()
    return render(request, 'estimator/cover.html', {'guess': x})

