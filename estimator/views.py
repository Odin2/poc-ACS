from django.shortcuts import render
from PIL import Image
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import UploadFileForm
import io
import base64
from funciones.estimador import ran
# Create your views here.

def index(request):
    x = ran()
    return render(request, 'estimator/cover.html', {'guess': x})


def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            #handle_uploaded_file(request.FILES['file'])
            imagen = form.cleaned_data['file']
            
            imagebytes = imagen.read()

            imageopened = Image.open(io.BytesIO(imagebytes))
            
            in_mem_file = io.BytesIO()
            imageopened.save(in_mem_file, format = "PNG")
            # reset file pointer to start
            in_mem_file.seek(0)
            img_bytes = in_mem_file.read()
            
            base64_encoded_result_bytes = base64.b64encode(img_bytes)
            base64_encoded_result_str = base64_encoded_result_bytes.decode('ascii')

            x = ran()
            imgsrc = "data:image/jpeg;base64," + base64_encoded_result_str  
    else:
        imgsrc = "https://pingendo.com/assets/photos/wireframe/photo-1.jpg"
        form = UploadFileForm()
        x = ran()

    return render(request, 'estimator/cover.html', {'form': form, 'guess': x, 'imgsrc' : imgsrc})