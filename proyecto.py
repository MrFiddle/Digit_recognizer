from tkinter import *
from tkinter import messagebox

main_w = Tk()

#Config the window app
main_w.geometry('500x500') # Size
main_w.configure(bg = 'white') # Background color
main_w.title('Proyecto | Computer Vision') # Title

def hola():

    msg = messagebox.showinfo("Hello Python", "Hello World")

def hola_c():

    print("Hola")

#Botones
B = Button(main_w, text = "Boton", command = lambda: hola()).place(x = 50, y = 50)

main_w.mainloop()