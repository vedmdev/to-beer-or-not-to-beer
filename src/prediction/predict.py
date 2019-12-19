import os
from src import config
from keras.models import load_model
from keras.preprocessing.image import img_to_array

import numpy as np

class Predictor(object):
    def __init__(self):
        # self.args = args

        self.model_name = config.trained_model_name
        self.model_path = config.trained_model_file
        self.model = load_model(self.model_path)
        print("Model "+ self.model_name +" loaded Successfully")
    
    def prepare_image(self, image):
        # if the image mode is not RGB, convert it
        if image.mode != "RGB":
            image = image.convert("RGB")

        # resize the input image and convert it into expected input for the model
        image = image.resize(size=(config.img_width, config.img_height))
        image = img_to_array(image)
        image = np.expand_dims(image, axis=0)

        # return the processed image
        return image

    def predict(self, image):
        result = self.model.predict(image)[0][0]
        print("prediction->", result)
        return result
