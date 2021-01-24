import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
from tkinter import scrolledtext as st
from sympy import * 
import sympy as sp
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
        self.cuaderno1.grid(column=10, row=10, padx=30, pady=30) #tamaño de la pantalla
        self.ventana1.mainloop() #se detiene la ejecución de tkk
    
    def menu(self):
        self.pagina1 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina1, text="Menú") #Nombre de la pestaña
        #identificador de campo
        self.labelframe1=ttk.LabelFrame(self.pagina1, text="UNIVERSIDAD NACIONAL AUTONOMA DE MEXICO \n Métodos Numéricos I\n Pichardo Franco Marco")
        #en donde se encuentra el campo para llenar
        self.labelframe1.grid(column = 0, row = 0, padx = 4, pady = 4)

        self.label = ttk.Label(self.labelframe1, text = "Elige algun metodo")
        self.label.grid(column = 0, row = 0, padx = 0, pady = 0)

        self.boton1=ttk.Button(self.labelframe1, text="Jacobi", command=self.jacobi)
        self.boton1.grid(column=1, row=1, padx=1, pady=2)
        self.boton2 = ttk.Button(self.labelframe1, text = "Falsa posición", command = self.falsa_posicion)
        self.boton2.grid(column=2, row=2, padx=3, pady=3)

        self.boton3 = ttk.Button(self.labelframe1, text = "Newton", command = self.newton)
        self.boton3.grid(column=3, row=3, padx=4, pady=4)

        

    def jacobi(self):

        self.ventana2 = tk.Tk()
        self.ventana2.title("Jacobi")
        self.cuaderno2 = ttk.Notebook(self.ventana2)
        
        self.label1 = ttk.Label(self.ventana2, text="ecuacion:")
        self.label1.grid(column = 0, row = 2, padx = 4, pady = 4)
        self.ecuacion = tk.IntVar()
        self.entryecuacion = ttk.Entry(self.ventana2, textvariable=self.ecuacion)
        self.entryecuacion.grid(column = 1, row = 2, padx = 4, pady = 4)
        self.boton1 = ttk.Button(self.ventana2, text = "Consultar", command = self.metodo_jacobi)
        self.boton1.grid(column = 1, row = 3, padx = 4, pady = 4)
        self.scrolledtext1 = st.ScrolledText(self.ventana2, width = 30, height = 10)
        self.scrolledtext1.grid(column = 1,row = 4, padx = 10, pady = 10)
        


    def metodo_jacobi(self):
    
        self.ecuacion.get =  str(self.ecuacion)

        self.scrolledtext1.insert(tk.END, "aqui:"
                                              "\niria"+str(self.ecuacion)+
                                              "\n el "
                                              "\procedimiento:""\n\n") 


    

    def falsa_posicion(self):
        self.ventana3 = tk.Tk()
        self.ventana3.title("Falsa posicion")
        self.cuaderno3 = ttk.Notebook(self.ventana3)  
        self.label1 = ttk.Label(self.ventana3, text="ecuacion:")
        self.label1.grid(column = 0, row = 2, padx = 4, pady = 4)
        self.ecuacion = tk.IntVar()
        self.entryecuacion = ttk.Entry(self.ventana3, textvariable=self.ecuacion) #aqui falta decir que show
        self.entryecuacion.grid(column = 1, row = 2, padx = 4, pady = 4)
        self.boton1 = ttk.Button(self.ventana3, text = "Consultar", command = self.metodo_falsa_posicion) #igual aqui hay que cambiar el "self.metodo_jacobi"
        self.boton1.grid(column = 1, row = 3, padx = 4, pady = 4)
        self.scrolledtext2 = st.ScrolledText(self.ventana3, width = 30, height = 10)
        self.scrolledtext2.grid(column = 1,row = 4, padx = 10, pady = 10)


    def metodo_falsa_posicion(self):
    
        self.ecuacion.get =  str(self.ecuacion)

        self.scrolledtext2.insert(tk.END, "aqui:"
                                              "\niria"+str(self.ecuacion)+
                                              "\n el "
                                              "\procedimiento:""\n\n") 
        


    def newton(self):
        self.ventana4 = tk.Tk()
        self.ventana4.title("Newton")
        self.cuaderno4 = ttk.Notebook(self.ventana4)
        self.label1 = ttk.Label(self.ventana4, text="ecuacion:")
        self.label1.grid(column = 0, row = 2, padx = 4, pady = 4)
        self.ecuacion = tk.IntVar()
        self.entryecuacion = ttk.Entry(self.ventana4, textvariable=self.ecuacion) #aqui falta decir que show
        self.entryecuacion.grid(column = 1, row = 2, padx = 4, pady = 4)
        self.boton1 = ttk.Button(self.ventana4, text = "Consultar", command = self.metodo_newton) #igual aqui hay que cambiar el "self.metodo_jacobi"        self.boton1.grid(column = 1, row = 3, padx = 4, pady = 4)
        self.boton1.grid(column = 1, row = 3, padx = 4, pady = 4)
        self.scrolledtext3 = st.ScrolledText(self.ventana4, width = 30, height = 10)
        self.scrolledtext3.grid(column = 1,row = 4, padx = 10, pady = 10)


    def metodo_newton(self):
    
        self.ecuacion.get =  str(self.ecuacion)

        self.scrolledtext3.insert(tk.END, "aqui:"
                                              "\niria"+str(self.ecuacion)+
                                              "\n el "
                                              "\procedimiento:""\n\n") 
        

        

