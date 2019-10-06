import tkinter
from tkinter import filedialog

raiz = tkinter.Tk()
raiz.title("Mi programa")

#fondo
frame = tkinter.Frame(raiz)
frame.config(bg="Black",width=400,height=300)
frame.pack()

tituloMenu = "Bienvenido a mi primer programa"
etiquetaLabel = tkinter.Label(frame, text=tituloMenu)
etiquetaLabel.pack()

raiz.mainloop()
