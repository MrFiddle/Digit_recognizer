import cv2
import numpy as np
#Procesamiento 2d de imagenes con convulucioón
def imagen_trabajo(imagen):
    imagen_trabajo=cv2.imread(imagen)
    imagen_trabajo=cv2.cvtColor(imagen_trabajo, cv2.COLOR_BGR2GRAY)
    return imagen_trabajo

def aplicar_filtro(fraccion_imagen,kernel):
    elementos= fraccion_imagen.shape[0]
    array_kernel=np.sum(kernel*fraccion_imagen)
    promedio_transformacion=  array_kernel/elementos**2
    return promedio_transformacion

def convolucion(imagen,kernel,padding=0,stride=1):
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
    