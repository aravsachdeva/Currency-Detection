#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Currency_Detection.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


# def take_picture():
#     videoCaptureObject = cv2.VideoCapture(0)
#     while(videoCaptureObject.isOpened()):
#         ret,frame = videoCaptureObject.read()
#         cv2.imshow('Capturing Video',frame)
#         cv2.imwrite('NewPicture.jpg',frame)
#         key=cv2.waitKey(10)
#         if key == ord('q'):
#             break
#     videoCaptureObject.release()
#     cv2.destroyAllWindows()
#     return

# def take_photo():
#     tkWindow = Tk()
#     tkWindow.geometry('250x350')
#     tkWindow.title('Take Photo of the currency')

#     button = Button(tkWindow,text = 'Click',command = take_picture)
#     button.pack()
#     tkWindow.mainloop()

if __name__ == '__main__':
    main()
