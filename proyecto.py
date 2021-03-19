from tkinter import *
from tkinter import messagebox
from Predictor import predice

class App():
    def __init__(self):

        main_w = Tk()

        #Config the window app
        main_w.geometry('800x500') # Size
        main_w.configure(bg = 'white') # Background color
        main_w.title('Proyecto | Computer Vision') # Title

        def hola():

            #print("Si")
            msg = messagebox.showinfo("Botón", "Button test")
            
        #Botones
        B = Button(
            
            main_w,
            text = "Predecir número",
            command = lambda: predice(0),
            width= 50,
            justify = CENTER,
            relief = FLAT,
            font = "Arial",

            activebackground = "WHITE",
            activeforeground = "BLACK",

            background = "BLACK",
            foreground = "WHITE",
            
            ).place(x = 170, y = 250)

        S = Button(

            main_w,
            text = "Salir",
            command = quit,
            width= 50,
            justify = CENTER,
            relief = FLAT,
            font = "Arial",

            activebackground = "WHITE",
            activeforeground = "BLACK",

            background = "BLACK",
            foreground = "WHITE",
            
            ).place(x = 170, y = 300)

        #Labels

        L = Label(
            main_w,
            text = "Clasificador de números con bordes",
            bg = "white",
            pady = 40,
            font = ("Bebas Neue", 30)
        )

        L.pack()
        main_w.mainloop()

def main():

    mi_app = App()
    return 0

if __name__ == '__main__':
    main()