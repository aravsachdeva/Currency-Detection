from keras.models import load_model
from PIL import Image, ImageOps
import numpy as np
import os

def predictingDenomination(image):
    # Load the model
    PROJECT_PATH = os.path.realpath(os.path.dirname(__file__))
    model = load_model(os.path.join(PROJECT_PATH,'keras_model.h5'))

    # # Create the array of the right shape to feed into the keras model
    # # The 'length' or number of images you can put into the array is
    # # determined by the first position in the shape tuple, in this case 1.
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    # # Replace this with the path to your image
    # image = Image.open(image)
    # #resize the image to a 224x224 with the same strategy as in TM2:
    # #resizing the image to be at least 224x224 and then cropping from the center
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.ANTIALIAS)

    # #turn the image into a numpy array
    image_array = np.asarray(image)
    # Normalize the image
    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
    # # Load the image into the array
    print(np.shape(normalized_image_array))
    data[0] = normalized_image_array[:,:,0:3]

    # print(model.evaluate())
    # print(model.summary())
    # run the inference
    prediction = model.predict(data)
    print(prediction)
    print(np.argmax(prediction))

    termIndex = np.argmax(prediction)

    if termIndex == 0:
        result = '1 DOLLAR BILL'
    elif termIndex == 1:
        result = '5 DOLLAR BILL'
    elif termIndex == 2:
        result = '10 DOLLAR BILL'
    elif termIndex == 3:
        result = '20 DOLLAR BILL'
    elif termIndex == 4:
        result = '50 DOLLAR BILL'
    elif termIndex == 5:
        result = '100 DOLLAR BILL'

    print(result)
    
    maxValue = (np.max(prediction))
    print(maxValue)
    return(result, maxValue)


if __name__ == "__main__":
    PROJECT_PATH = os.path.realpath(os.path.dirname(__file__))
    image = Image.open(os.path.join(PROJECT_PATH,"100.png")).convert("RGB")
    predictingDenomination(image)



# 0 : 
# 1 : 
# 2 : 
# 3 : 
# 4 : 
# 5 : 1 dollar f
# 6 : 
# 7 : 20 dollar
# 8 : 
# 9 : 10 dollar f
# 0 : 
# 0 : 
# 0 : 
# 12 : 5 dolalr f

