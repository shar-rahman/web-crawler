# api endpoint for the vgg16 model through keras
import tensorflow as tf
import numpy as np
from keras.applications.imagenet_utils import decode_predictions
import pandas as pd

class classifier:

    model = tf.keras.applications.vgg16.VGG16(weights='imagenet')

    # input: list of dictionaries of predictions
    # output: json format of list of dictionaries
    #
    # converts list into pandas dictionary and makes use of .to_json() function in pandas
    def dict_list_to_json(self, data):
        df = pd.DataFrame(data)
        return df.to_json()


    # input: image path
    # output: dictionary of prediction values
    #
    # performs prediction on vgg16 model in keras
    def classify_image(self, image_path):
        print('performing classification on ' + str(image_path))
        response = {}
        # predict on keras model
        X = tf.keras.preprocessing.image.load_img(image_path, target_size=(224,224))
        X = np.expand_dims(X, axis=0)
        X = tf.keras.applications.imagenet_utils.preprocess_input(X)

        y = self.model.predict(X)

        # retrieves best prediction
        # result: [('', class_name, confidence)]
        result = decode_predictions(y, top=1)
        print('finished classification')

        # create dictionary of prediction values - follows the following format:
        # image_path: path to image on disk
        # label: predicted classification of image by vgg16
        # confidence: confidence of label by model
        classification = {
                        'image_path': image_path, 
                        'label': result[0][0][1],
                        'confidence': result[0][0][2]
                        }
        return classification
