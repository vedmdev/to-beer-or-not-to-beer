import os
from src.training import config
from keras.preprocessing import image
from keras.models import load_model

import numpy as np

class Predictor(object):
    def __init__(self):
        # self.args = args
        # self.logger = logger
        # self.project_dir = self.args.project_dir

        self.model_name = "beer/trained_model/beer_vs_catndog.h5"
        self.model_path = os.path.join(config.dataset_path, 'beer', 'trained_model', 'beer_vs_catndog.h5')
        self.model = load_model(self.model_path)
        print("Model "+ self.model_name +" loaded Successfully")

    def predict_from_file(self, file_path):
        print("Predicting from file", file_path)
        # Get test image ready
        # image = cv2.imread(file_path)
        test_image = image.load_img(file_path, target_size=(config.img_width, config.img_height))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis=0)

        # test_image = test_image.reshape(config.img_width, config.img_height*3)    # Ambiguity!
        print("prediction->", self.model.predict(test_image))
