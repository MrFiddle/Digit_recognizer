# -*- coding: utf-8 -*-
#from os import XATTR_CREATE
import PIL
from PIL.Image import Image
from tensorflow import keras
import tensorflow as tf
import numpy as np
import cv2
import matplotlib.pyplot as plt
import random
model = tf.keras.models.load_model('CNN.h5')

def predice(i):
    (x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()
    entrada = cv2.Canny(x_test[i],100,200)
    entrada = cv2.bitwise_not(entrada)
    entrada = entrada.astype("float32") / 255
    img = np.resize(entrada, (28,28,1))
    im2arr = np.array(img)
    im2arr = im2arr.reshape(1,28,28,1)
    y_pred = model.predict_classes(im2arr)
    print(y_pred)
    plt.imshow(entrada, cmap='gray')
    plt.show()
    return y_pred

#Image = cv2.imread("bordes.png")
#predice(Image)
a = random.randrange(0, 9999, 1)
predice(a)