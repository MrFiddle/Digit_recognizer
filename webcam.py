from PIL import Image
import cv2
import os

def center_crop(img,dim):
    #Recorta la imagen, acorde a las dimesiones indicadas
    ancho, alto = img.shape[1], img.shape[0]
    crop_ancho = dim[0] if dim[0]<img.shape[1] else img.shape[1]
    crop_alto = dim[1] if dim[1]<img.shape[0] else img.shape[0]
    mid_x, mid_y = int(ancho/2), int(alto/2)
    crop_ancho2, crop_alto2 = int(crop_ancho/2), int(crop_alto/2) 
    cropped = img[mid_y-crop_alto2:mid_y+crop_alto2, mid_x-crop_ancho2:mid_x+crop_ancho2]
    return cropped

def cam():
    #Abrimos Camara y  tomamos captura, regresamos la imagen
    cam = cv2.VideoCapture(0)
    cwd=os.getcwd()
    test=os.listdir()

    for images in test:
        if images.endswith(".png"):
            os.remove(os.path.join(cwd, images))

    while True:
        check, frame = cam.read()
        if not check:
            print("Ha sucedido un error al abrir la Camara")
            break
        cv2.imshow("Prueba. Presiona " "Space" " para tomar imagen", frame)

        tecla = cv2.waitKey(1)
        if tecla%256 == 32:
            #Space presionado, procede a tomar captura y guarda imagen
            img_name = "imagen.png"
            cv2.imwrite(img_name, frame)
            image=cv2.imread("imagen.png")
            dim=(300,300)
            cropped=center_crop(image,dim)
            cropped=cv2.cvtColor(cropped,cv2.COLOR_BGR2GRAY)
            cv2.imwrite("imagen.png",cropped)
            print("{} ha sido capturada!".format(img_name))
            break
    cam.release()
    cv2.destroyAllWindows()
    return "imagen.png"

def pixel(image):
    #Convierte imagen en resolución 28*28 pix, con la que trabajara la red neuronal
    img = Image.open(image)
    imgSmall = img.resize((28,28),resample=Image.BILINEAR)
    result = imgSmall.resize(img.size,Image.NEAREST)
    result.save('pixel.png')

if __name__ == "__main__":
    image=cam()
    #pixel(image)

