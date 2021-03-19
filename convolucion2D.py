#Título: "Procesamiento de imagenes 2d con convolución"
#Autor: Brandon Josué Magaña Mendoza 

import cv2
import numpy as np

def imagen_trabajo(imagen):
    """
    Se encarga de cargar la imagen y procesarla para trabajar con ella 
    a lo largo del programa.

    Args:
        imagen: string que indica el path al archivo

    Return:
        imagen_trabajo: imagen convertida a array
    """
    imagen_trabajo=cv2.imread(imagen)
    imagen_trabajo=cv2.cvtColor(imagen_trabajo, cv2.COLOR_BGR2GRAY)

    return imagen_trabajo

def aplicar_filtro(fraccion_imagen,kernel):
    """
    Aplica la multiplicación del kernel por una fracción de la imagen del mismo tamaño
    para calcular su promedio y regresarlo.

    Args:
        fraccion_imagen:numpy array, representa una fracción de la imagen original.
        kernel: numpy array, representa la convolución aplicada a la imagen.

    Return:
        Promedio resultante de la multiplicación kernel*fracción_imagen

    """
    elementos= fraccion_imagen.shape[0]
    array_kernel=np.sum(kernel*fraccion_imagen)
    promedio_transformacion=  array_kernel/elementos**2

    return promedio_transformacion

def convolucion(imagen,kernel,padding=0,stride=1):
    """
    Realiza la convolución a la imagen. Regresa Imagen con el filtro aplicado.
    NOTA: Se le puede asignar un padding.

    Args:
        imagen: numpy array, representa la imagen
        kernel: numpy array, representa la convolución aplicada a la imagen.
        padding: representa el borde que se le añadira a la imagen para ser procesada
        stride:paso entre cada convolución

    Return:
        imagen_filtro: numpy array, imagen con el filtro aplicado

    """
    dimension_kernel=kernel.shape[0]
    columnas=imagen.shape[1]
    filas=imagen.shape[0]
    columnas_filtro=int(((columnas-dimension_kernel+ 2*padding)/stride)+1)
    filas_filtro=int(((filas-dimension_kernel+2*padding)/stride)+1)
    imagen_filtro=np.zeros((filas,columnas))

    imagen_padding=imagen

    if padding !=0:
        imagen_padding=np.zeros((filas_filtro+2*padding,columnas_filtro+2*padding))
        imagen_padding[padding:-padding, padding:-padding]=imagen
    for i in range(filas-dimension_kernel):
        for j in range(columnas-dimension_kernel):
            fraccion=imagen_padding[i:dimension_kernel+i, j:dimension_kernel+j]
            imagen_filtro[i,j]=aplicar_filtro(fraccion, kernel)
            
    return imagen_filtro

if __name__ == '__main__':
    imagen=imagen_trabajo("foto.jpg")
    kernel=np.array([[0,1,0],[1,-4,1],[0,1,0]])
    imagen=convolucion(imagen,kernel,1)
    cv2.imshow("image",imagen)
    cv2.waitKey(0)  
    