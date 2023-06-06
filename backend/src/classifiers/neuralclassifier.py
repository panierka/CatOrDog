from werkzeug.datastructures import FileStorage

import tensorflow as tf
import numpy as np
import definitions
import yaml

from tensorflow import keras
from PIL import Image

with open(definitions.get_config_path()) as f:
    config = yaml.safe_load(f)
    model_path = definitions.get_project_root() / config['model path']

model = keras.models.load_model(model_path)
class_names = ['cat', 'dog']


def predict(image_storage: FileStorage):
    image = Image.open(image_storage.stream)
    img_array = keras.utils.img_to_array(image)
    predictions = model.predict(img_array)
    score = tf.nn.softmax(predictions[0])
    return class_names[np.argmax(score)]
