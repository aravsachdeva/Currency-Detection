import PIL
from django.http import HttpResponse, StreamingHttpResponse
from django.shortcuts import render, redirect
from PIL import Image


# Create your views here.
# from Currency.camera import VideoCamera, IPWebCam
from Currency.forms import ImageForm
# from Currency.ml import predictingValue
from .detection import showOutput
from .ml import predictingDenomination


def index(request):

    form = ImageForm(request.POST, request.FILES)
    print("request recieved")

    if request.method == 'POST':
        print("post request")
        if True:
            print(form)
            image = form.cleaned_data.get('file')
            print("recieved image")
            img = Image.open(image).convert("RGB")

            model1 = predictingDenomination(img)

            modelPredict = model1[0]
            modelAccuracy = model1[1]

            output = showOutput(image)
            print(output)
            
            return render(request, 'Currency/index.html', {'output' : output, 'modelOutput' : modelPredict, 'modelAccuracy' : modelAccuracy})
    form = ImageForm()
    return render(request, 'Currency/index.html', {'form' : form})


# Every time you call the phone and laptop camera method gets frame
# More info found in camera.py
def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


# # Method for laptop camera
# def video_feed(request):
#     return StreamingHttpResponse(gen(VideoCamera()),
#                                  content_type='multipart/x-mixed-replace; boundary=frame')


# # Method for phone camera
# def webcam_feed(request):
#     return StreamingHttpResponse(gen(IPWebCam()),
#                                  # video type
#                                  content_type='multipart/x-mixed-replace; boundary=frame')
