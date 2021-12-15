import keras_ocr
import os
from PIL import Image
from gtts import gTTS
from playsound import playsound



pipeline = keras_ocr.pipeline.Pipeline()

directory = os.getcwd()
PROJECT_PATH = os.path.realpath(os.path.dirname(__file__))

img = Image.open(os.path.join(PROJECT_PATH,"100Dollars.png")).convert('L')
img.save(os.path.join(PROJECT_PATH,'greyscale.png'))

images = [
    keras_ocr.tools.read(os.path.join(PROJECT_PATH,"greyscale.png"))     
]


prediction_groups = pipeline.recognize(images)

washington_1 = "wash*"
lincoln_5 = "lincole"
hamilton_10 = "hamil"
jackson_20 = "jacks"
print('Lenght us: ', len(prediction_groups[0]))
for i in range(len(prediction_groups[0])):
    result = [ m[0] for m in [l[i] for l in prediction_groups]]
    print(result)
    #if(washington_1 in result):
    if(result[0].startswith('wash')):
        print(result)
        obj = gTTS(text='1 DOLLAR BILL', lang='en', slow=False)
        obj.save('/tmp/currency.mp3')
        playsound('/tmp/currency.mp3')
    elif(result[0].startswith('linc')):
        print(result)
        obj = gTTS(text='5 DOLLAR BILL', lang='en', slow=False)
        obj.save('/tmp/currency.mp3')
        playsound('/tmp/currency.mp3')
    elif(result[0].startswith('hami')):
        print(result)
        obj = gTTS(text='10 DOLLAR BILL', lang='en', slow=False)
        obj.save('/tmp/currency.mp3')
        playsound('/tmp/currency.mp3')
    elif(result[0].startswith('jacks')):
        print(result)
        obj = gTTS(text='20 DOLLAR BILL', lang='en', slow=False)
        obj.save('/tmp/currency.mp3')
        playsound('/tmp/currency.mp3')
    elif(result[0].startswith('gran')):
        print(result)
        obj = gTTS(text='50 DOLLAR BILL', lang='en', slow=False)
        obj.save('/tmp/currency.mp3')
        playsound('/tmp/currency.mp3')
    elif(result[0].startswith('fran')):
        print(result)
        obj = gTTS(text='100 DOLLAR BILL', lang='en', slow=False)
        obj.save('/tmp/currency.mp3')
        playsound('/tmp/currency.mp3')



