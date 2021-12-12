import keras_ocr
import os
from PIL import Image


pipeline = keras_ocr.pipeline.Pipeline()

directory = os.getcwd()
PROJECT_PATH = os.path.realpath(os.path.dirname(__file__))

img = Image.open(os.path.join(PROJECT_PATH,"Crop100.png")).convert('L')
img.save(os.path.join(PROJECT_PATH,'greyscale.png'))



images = [
    keras_ocr.tools.read(os.path.join(PROJECT_PATH,"greyscale.png"))     
]


prediction_groups = pipeline.recognize(images)

print(prediction_groups)

