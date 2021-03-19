import cv2
import numpy as np

def convertirImagen(imagen):
    imagenProcesada = cv2.imread(imagen)
    src = imagenProcesada
    imagenProcesada = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
    return imagenProcesada

def promedioPonderado(seccion, kernel):
    elementosSeccion = seccion.size
    seccionMult = seccion * kernel
    promedio = (np.sum(seccionMult)) / elementosSeccion
    return promedio

def convolucion(imagen, kernel, pad = 0, stride = 1):
    kernelPix = kernel.shape[0]
    xPix = imagen.shape[1]
    yPix = imagen.shape[0]

    xFiltrada = int(((xPix - kernelPix + 2 * pad) / stride) + 1)
    yFiltrada = int(((yPix - kernelPix + 2 * pad) / stride) + 1)
    imagenFiltrada = np.zeros((yPix, xPix))

    if pad == 0:
        imagenPad = imagen
    else:
        imagenPad = np.zeros((yPix + pad * 2, xPix + pad * 2))
        imagenPad[pad:-pad, pad:-pad] = imagen

    for i in range(yFiltrada - kernelPix):
        for j in range(xFiltrada - kernelPix):

            seccion = imagenPad[i:kernelPix + i, j:kernelPix + j]
            imagenFiltrada[i, j] = promedioPonderado(seccion, kernel)
    
    return imagenFiltrada

kernel = np.array([[-1, -1, 1], [-1, 8, -1], [-1, -1, -1]])

imagen = convertirImagen('prueba.jpg')
imagen = convolucion(imagen, kernel, pad = 1)

cv2.imshow('Prueba', imagen)
cv2.waitKey(0)
