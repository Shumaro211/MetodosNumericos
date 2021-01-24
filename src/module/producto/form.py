import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
from tkinter import scrolledtext as st
#hola

#Vista/interfaz
#-Pendiente: Separar archivos en varias clases para mantenimiento


class  DatosForm:

        #constructor que envía info a main.py
    def __init__ (self):
        self.ventana1 = tk.Tk()
        self.ventana1.title("Métodos Numéricos")
        self.cuaderno1 = ttk.Notebook(self.ventana1)
        self.menu()
        self.jacobi()
        self.cuaderno1.grid(column=0, row=0, padx=10, pady=10) #tamaño de la pantalla
        self.ventana1.mainloop() #se detiene la ejecución de tkk
    
    def menu(self):
        self.pagina1 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina1, text="Menú") #Nombre de la pestaña
        #identificador de campo
        self.labelframe1=ttk.LabelFrame(self.pagina1, text="UNIVERSIDAD NACIONAL AUTONOMA DE MEXICO \n Métodos Numéricos I\n Pichardo Franco Marco")
        #en donde se encuentra el campo para llenar
        self.labelframe1.grid(column = 0, row = 0, padx = 4, pady = 4)
        
        self.labelframe2=ttk.LabelFrame(self.pagina1, text="Elige algún método")
        #en donde se encuentra el campo para llenar
        self.labelframe2.grid(column = 1, row = 1, padx = 4, pady = 4)
        
        self.boton1 = ttk.Button(self.labelframe1, text="Jacobi", command = self.jacobi)
        self.boton1.grid(column=1, row=9, padx=4, pady=4)

        self.boton2 = ttk.Button(self.labelframe2, text="Jacobi", command = self.jacobi)
        self.boton2.grid(column=1, row=10, padx=4, pady=4)



    def jacobi(self):
        self.pagina2 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina2, text = "Jacobi")
 