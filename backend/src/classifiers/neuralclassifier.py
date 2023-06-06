from tempfile import SpooledTemporaryFile, NamedTemporaryFile

import tensorflow as tf
import numpy as np
import definitions
import yaml

from tensorflow import keras
from PIL import Image

tf.get_logger().setLevel('ERROR')

with open(definitions.get_config_path()) as f:
    config = yaml.safe_load(f)
    model_path = definitions.get_project_root() / config['model path']
    size_x = config['size x']
    size_y = config['size y']

model = keras.models.load_model(model_path)
class_names = ['cat', 'dog']


def predict(image_storage: SpooledTemporaryFile):
    image = Image.open(image_storage).resize((size_x, size_y))
    img_array = keras.utils.img_to_array(image)
    img_array = np.expand_dims(img_array, axis=0)
    predictions = model.predict(img_array)
    score = tf.nn.softmax(predictions[0])
    return class_names[np.argmax(score)]
