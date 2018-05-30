from django.shortcuts import render
from PIL import Image
from .forms import UploadFileForm
import datetime
import io
import base64

from funciones.estimador import Estimador
# Create your views here.


# # Funcion que responde al POST de la pagina de estimar.
#
#  x representa el numero de la estimacion y se devuelve la imagen para desplegarse en imgsrc.
def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            # handle_uploaded_file(request.FILES['file'])
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

            imageopened.save(".\\poc-ACS\\boneage\\dataset\\test\\"+ imagen.name.split(".")[0]  + ".png", format = "PNG")
            #x = ran()
            imageopened.close()
            
            estimador = Estimador()
            if form.cleaned_data['Patient_Sex'] == "Female":
                valor=estimador.estimar("F")
            else:
                valor=estimador.estimar("M")
            print(valor[0][0])
            x = valor[0][0]
            
            with open("Log", "a+") as f:
                f.write(str(x) + " - " + form.cleaned_data['Patient_Name'] + " - " + form.cleaned_data['Patient_Age'] + " - " + form.cleaned_data['Patient_Sex'] + " - " + str(datetime.datetime.now()).split(".")[0] + "\n")

            imgsrc = "data:image/jpeg;base64," + base64_encoded_result_str
            
            
            
                        
            
    else:
        imgsrc = "https://pingendo.com/assets/photos/wireframe/photo-1.jpg"
        form = UploadFileForm()
        x = 0

    return render(request, 'estimator/cover.html', {'form': form, 'guess': x, 'imgsrc' : imgsrc})