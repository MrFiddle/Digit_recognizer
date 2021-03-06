import cv2
import numpy as np

cam = cv2.VideoCapture(0) #Abre la cámara default
filtro = np.array([[-1,-1,-1],[-1,8,-1],[-1,-1,-1]])
filtro_gauss = np.array([[1,4,7,4,1],[4,16,26,16,4],[7,26,41,26,6],[4,16,26,16,4],[1,4,7,4,1]]) / 273

def pad(imagen, radio, cnt):
	#output = cv2.copyMakeBorder(imagen, radio, radio, radio, radio, cv2.BORDER_CONSTANT,0)
	irows, icols = imagen.shape
	output = np.zeros((irows + radio, icols + radio))
	for row in range(irows + radio):
		for col in range(icols + radio):
			if row < radio or col < radio or row > irows or col > icols:
				output[row][col] = cnt
			else:
				output[row][col] = imagen[row - radio][col - radio]
	return output

#Implementacion de la convolucion
def convolucion(imagen, kernel):
	irows, icols = imagen.shape
	krows, kcols = kernel.shape
	radio = (krows - 1) // 2
	output = imagen
	imagen = pad(imagen, radio, 0)
	for row in np.arange(radio, irows - radio):
		for column in np.arange(radio, icols - radio):
			vecinos = imagen[row - radio : row + radio + 1, column - radio : column + radio + 1]
			output[row][column] = (vecinos*kernel).sum()
	return output

while True:
	ret_val, img = cam.read()  #Lee la cámara
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	imgBordes = convolucion(gray, filtro_gauss)
	cv2.imshow('Camera', imgBordes)  #Muestra la imagen

	if cv2.waitKey(1) == 27:
		break #Si se presiona esc, sal
cv2.destroyAllWindows()
