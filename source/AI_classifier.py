import cv2
import numpy
from tensorflow.keras.models import load_model

class Classifier() :
    def __init__(self, model_name) :
        self.model = load_model(model_name);

    def classify(self, frame) :
        img = cv2.resize(frame, (150, 150));
        img = numpy.expand_dims(img, axis = 0);
        img = img / 255.0;

        prediction = self.model.predict(img);
        type = "styrofoam"

        return type, float(prediction);
