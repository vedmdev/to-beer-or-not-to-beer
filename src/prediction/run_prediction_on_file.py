import os

from src import config
from src.prediction.predict import Predictor
from PIL import Image

if __name__ == "__main__":
    # test_validation

    test_img_path = config.test_img_dir_file

    print("test_img_path->", test_img_path)
    predictor = Predictor()
    image = Image.open(test_img_path)
    image = predictor.prepare_image(image)

    predictor.predict(image)
