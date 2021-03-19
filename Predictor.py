# -*- coding: utf-8 -*-
from PIL.Image import Image
import tensorflow as tf
import numpy as np
import cv2

model = tf.keras.models.load_model('CNN.h5')
def predice(entrada):
    entrada = entrada.astype("float32") / 255
    img = np.resize(entrada, (28,28,1))
    im2arr = np.array(img)
    im2arr = im2arr.reshape(1,28,28,1)
    y_pred = model.predict_classes(im2arr)
    print(y_pred)

Image = cv2.imread("bordes.png")
predice(Image)