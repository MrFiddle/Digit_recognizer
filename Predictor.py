# -*- coding: utf-8 -*-
import tensorflow as tf
import numpy as np

model = tf.keras.models.load_model('CNN.h5')
def predice(entrada):
    entrada = entrada.astype("float32") / 255
    img = np.resize(entrada, (28,28,1))
    im2arr = np.array(img)
    im2arr = im2arr.reshape(1,28,28,1)
    y_pred = model.predict_classes(im2arr)
    print(y_pred)
    