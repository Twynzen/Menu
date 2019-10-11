
from tkinter import *

ventana = Tk()
ventana.geometry("500x200")
ventana.title("Menus")
label1 = Label(ventana, text="Bienvenido", font = ("Arial Bold",50),bg="white")
label1.grid(column = 0, row =0)

def Funcion():
    print ("Funcion Ejecutada por usuario usando el menu")

menu_general = Menu(ventana) #incrustamos un menu en la ventana, aunque todabia no es visible
ventana["menu"] = menu_general #hacemos que la ventana tenga de menu a "menu_general"

menu_archivo = Menu(menu_general) #menu archivo
menu_archivo.add_command(label = "Abrir archivo", command = Funcion)
menu_archivo.add_command(label = "Abrir carpeta", command = Funcion)
menu_archivo.add_command(label = "Buscar archivos", command = Funcion)
menu_archivo.add_separator()
menu_archivo.add_command(label = "Salir", command = ventana.destroy)
menu_general.add_cascade(label = "Archivo", menu = menu_archivo)

menu_ayuda = Menu(menu_general) #menu ayuda
menu_ayuda.add_command(label = "Acerca de...", command = Funcion)
menu_ayuda.add_command(label = "Visit my site", command = Funcion)
menu_general.add_cascade(label = "Ayuda", menu = menu_ayuda)



ventana.mainloop() #bucle del programa
