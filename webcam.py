import cv2
import os
def cam():
    cam = cv2.VideoCapture(0)
    img_counter = 0
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

        key = cv2.waitKey(1)
        if key%256 == 32:
            # SPACE pressed
            img_name = "imagen.png".format(img_counter)
            cv2.imwrite(img_name, frame)
            print("{} ha sido capturada!".format(img_name))
            break
    cam.release()
    cv2.destroyAllWindows()
    return "imagen.png"

if __name__ == "__main__":
    cam()