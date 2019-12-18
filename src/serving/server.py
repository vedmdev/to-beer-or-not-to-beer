from flask import Flask, request

from src.prediction.predict import Predictor
import tensorflow as tf
from PIL import Image
import io

app = Flask(__name__)
global graph
graph = tf.get_default_graph()
predictor = Predictor()


@app.route("/")
def root():
    return "This the root page :)"

@app.route("/health")
def health():
    return "The show is going well :D"

@app.route("/isItBeer", methods=['POST'])
def is_it_beer():
    # save_response = save_file_to_local_file_store(request=request)
    # print("save_response", save_response, save_response.get('filelocation'))
    image = request.files["image"].read()
    image = Image.open(io.BytesIO(image))

    # preprocess the image and prepare it for classification
    image = predictor.prepare_image(image)

    # It’s also necessary to set up a reference to the tensorflow graph using tf.get_default_graph().
    # If this step is omitted, an exception may occur during the predict step.
    # The condition with graph.as_default() is used to grab a threadsafe reference to the graph when making predictions
    # https://towardsdatascience.com/deploying-keras-deep-learning-models-with-flask-5da4181436a2
    with graph.as_default():
        # predictor.predict_from_file(save_response.get('filelocation'))
        prediction = predictor.predict(image)
        if prediction == 0:
            return "Tuu beer hai **!"
        else:
            return "Tuu beer nahi hai. Ja beer lekar aa."

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=4200, threaded=False)
