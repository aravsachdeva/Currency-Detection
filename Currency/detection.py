import keras_ocr
import os
from PIL import Image
from gtts import gTTS
from playsound import playsound



pipeline = keras_ocr.pipeline.Pipeline()

directory = os.getcwd()
PROJECT_PATH = os.path.realpath(os.path.dirname(__file__))

def showOutput(picture):
    img = Image.open(picture).convert('L')
    img.save(os.path.join(PROJECT_PATH,'greyscale.png'))
    print("converted to greyscale")

    images = [
        keras_ocr.tools.read(os.path.join(PROJECT_PATH,"greyscale.png"))     
    ]

    prediction_groups = pipeline.recognize(images)

    # washington_1 = "wash"
    # lincoln_5 = "lincole"
    # lincoln = ['linco', 'linc', ]
    # hamilton_10 = "hamil"
    # jackson_20 = "jacks"
    print('Length us: ', len(prediction_groups[0]))

    counter = 0
    for i in range(len(prediction_groups[0])):
        result = [m[0] for m in [l[i] for l in prediction_groups]]

        print(result)
        if(result[0].startswith('wash') or result[0].startswith('1') or result[0].endswith('one')):
            stringResult = '1 DOLLAR BILL'
            print(result)
            counter = 1
            break
        elif(result[0].startswith('linc') or result[0].endswith('5')):
            stringResult = '5 DOLLAR BILL'
            print(result)
            counter = 1
            break
        elif(result[0].startswith('hami') or result[0].endswith('10')):
            stringResult = '10 DOLLAR BILL'
            print(result)
            counter = 1
            break
        elif(result[0].startswith('jacks') or result[0].endswith('20')):
            stringResult = '20 DOLLAR BILL'
            print(result)
            counter = 1
            break
        elif(result[0].startswith('gran') or result[0].endswith('50')):
            stringResult = '50 DOLLAR BILL'
            print(result)
            counter = 1
            break
        elif(result[0].startswith('fran') or result[0].endswith('100')):
            stringResult = '100 DOLLAR BILL'
            print(result)
            counter = 1
            break
        else:
            stringResult = 'Please try again'

    print(stringResult)
    return stringResult

