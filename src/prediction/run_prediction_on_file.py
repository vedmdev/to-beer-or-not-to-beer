import os

from src.training import config
from src.prediction.predict import Predictor

if __name__ == "__main__":
    # test_validation

    test_img_path = os.path.join(config.dataset_path, 'beer', 'test_validation', 'cat.1007.jpg')

    print("test_img_path->", test_img_path)
    predictor = Predictor()
    predictor.predict_from_file(test_img_path)
