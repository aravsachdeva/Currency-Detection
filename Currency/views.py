from django.http import HttpResponse, StreamingHttpResponse
from django.shortcuts import render

# Create your views here.
from Currency.camera import VideoCamera, IPWebCam


def index(request):
    # return HttpResponse("Hello everyone")
    return render(request, 'Currency/index.html')


# Every time you call the phone and laptop camera method gets frame
# More info found in camera.py
def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


# Method for laptop camera
def video_feed(request):
    return StreamingHttpResponse(gen(VideoCamera()),
                                 content_type='multipart/x-mixed-replace; boundary=frame')


# Method for phone camera
def webcam_feed(request):
    return StreamingHttpResponse(gen(IPWebCam()),
                                 # video type
                                 content_type='multipart/x-mixed-replace; boundary=frame')
