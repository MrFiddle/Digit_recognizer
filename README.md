# Clasificador de números con bordes | Semana TEC

Modelo modificado de: https://keras.io/examples/vision/mnist_convnet/ <br/>
Author: fchollet <br/>
https://github.com/keras-team/keras-io/blob/master/examples/vision/mnist_convnet.py <br/>

## Librerias utilizdas para el programa

* Python 3.8 <br/>
* OpenCV 4.5.1.48<br/>
* NumPy 1.19.5<br/>
* Pillow 8.1.2<br/>
* Tensorflow 2.4.1<br/>
* Matplotlib 3.3.4<br/>


### TKinter en Linux

TKinter viene instalado por default con Python, mas sin embargo para sistemas operativos basados en Linux, es necesario bajar una dependencia para poder visualizar la aplicación una vez que la ejecutamos

    apt-get install python-tk

### Correr programa
Para correr el programa solo es necesario correr el archivo "proyecto.py" que usa la función "predice" dentro de "Predictor.py" que a su vez importa la red neuronal convolucional del archivo "CNN.h5".
