import tensorflow as tf

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