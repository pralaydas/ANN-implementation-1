import tensorflow as tf
import time
import os

def create_model(LOSS_FUNCTION, OPTIMIZER, METRICS):
    model = tf.keras.models.Sequential()
    model.add(tf.keras.layers.Flatten(input_shape=[28, 28]))
    model.add(tf.keras.layers.Dense(300, activation="relu"))
    model.add(tf.keras.layers.Dense(100, activation="relu"))
    model.add(tf.keras.layers.Dense(10, activation="softmax"))

    model.summary()

    model.compile(loss=LOSS_FUNCTION,
               optimizer=OPTIMIZER,
               metrics=METRICS)
    return model # <<< untrained  model

def get_unique_filename(filename):
    unique_filename = time.strftime(f"%Y%m%d_%H%M%S_{filename}")
    return unique_filename

def save_model(model, model_name, model_dir):
    unique_filename = get_unique_filename(model_name)
    path_to_model = os.path.join(model_dir, unique_filename)
    model.save(path_to_model)