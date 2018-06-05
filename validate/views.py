from django.shortcuts import render
from django.http import HttpResponse
import validate.forms

def index(request):
    form = validate.forms.ValidateForm()
    #render(request, 'estimator/cover.html', {'form': form, 'guess': x, 'imgsrc' : imgsrc})
    return render(request, 'validate/cover.html', {'form': form, 'guess': 0})