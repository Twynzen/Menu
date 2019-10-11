import tkinter
import getpass

root = tkinter.Tk()
texto = "Bienvenido %s a Codigo Python" % getpass.getuser()
etiqueta = tkinter.Label(root, text=texto)
etiqueta.grid(row=1, column=1)
root.mainloop()
