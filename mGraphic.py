import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import askyesno

import customtkinter

#import datetime
#import db

#from lib import isValid
#from user import User

from time import sleep
import pandas as pd
#---------------------- Menu Superior -------------------------

class App(customtkinter.CTk):

    def __init__(self):        
        super().__init__()        

        #configura ventana
        self.title("User admin interface demo")
        self.geometry(f"{1100}x{580}")
        
        #configura grid 4x4
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2,3), weight=0)
        self.grid_rowconfigure((0,1,2), weight=1)
        
        #crea y configura panel lateral(frame)
        self.sidebar_frame= customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0,column=0,rowspan=4,sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4,weight=1)

        #crea y configura label user
        self.logo_label=customtkinter.CTkLabel(self.sidebar_frame, text="User admin", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20,10))

        #boton "Ver Usuarios" en panel lateral
        self.boton_ver_usuarios=customtkinter.CTkButton(self.sidebar_frame, text="Ver_usuarios")
        self.boton_ver_usuarios.grid(row=1,column=0, padx=20, pady=10)

        #boton "Agregar Usuarios" en panel lateral
        self.boton_agr_usuarios=customtkinter.CTkButton(self.sidebar_frame, text="Agregar_usuarios")
        self.boton_agr_usuarios.grid(row=2,column=0, padx=20, pady=10)

        #

        ventana=Tk()

        barraMenu=Menu(ventana)
        ventana.config(menu=barraMenu, width=300, height=300)

        bbddMenu=Menu(barraMenu, tearoff=0)
        bbddMenu.add_command(label="Conectar")
        bbddMenu.add_command(label="Salir")

        borrarMenu=Menu(barraMenu, tearoff=0)
        borrarMenu.add_command(label="Borrar campos")

        crudMenu=Menu(barraMenu, tearoff=0)
        crudMenu.add_command(label="Crear")
        crudMenu.add_command(label="Leer")
        crudMenu.add_command(label="Actualizar")
        crudMenu.add_command(label="Borrar")


        ayudaMenu=Menu(barraMenu, tearoff=0)
        ayudaMenu.add_command(label="Licencia")
        ayudaMenu.add_command(label="Acerca de...")

        barraMenu.add_cascade(label="BBDD", menu=bbddMenu)
        barraMenu.add_cascade(label="Borrar", menu=borrarMenu)
        barraMenu.add_cascade(label="CRUD", menu=crudMenu)
        barraMenu.add_cascade(label="Ayuda", menu=ayudaMenu)

        #--------------------- campos a completar----------------------------

        frameCampos=Frame(ventana)
        frameCampos.pack()

        labelUsuario=Label(frameCampos, text='Usuario', anchor=E)
        labelUsuario.grid(row=0, column=0, sticky=E, padx=10, pady=10)

        entryUsuario=Entry(frameCampos)
        entryUsuario.grid(row=0, column=1, padx=10, pady=10)

        labelSector=Label(frameCampos, text='Sector', anchor=E)
        labelSector.grid(row=1, column=0, sticky=E, padx=10, pady=10)

        entrySector=Entry(frameCampos)
        entrySector.grid(row=1, column=1, padx=10, pady=10)

        labelOC=Label(frameCampos, text='OC', anchor=E)
        labelOC.grid(row=2, column=0, sticky=E, padx=10, pady=10)

        txtOC=Text(frameCampos, width=16, height=5)
        txtOC.grid(row=2, column=1, padx=10, pady=10)

        scrollVert=Scrollbar(frameCampos, command=txtOC.yview)
        scrollVert.grid(row=2, column=2, sticky="nsew")

        txtOC.config(yscrollcommand=scrollVert.set)

    #-------------------------Botones------------------------------

        frameBotones=Frame(ventana)
        frameBotones.pack()

        botonCrear=Button(frameBotones, text="Crear")
        botonCrear.grid(row=0, column=0, sticky=E, padx=10, pady=10)

        botonLeer=Button(frameBotones, text="Leer")
        botonLeer.grid(row=0, column=1, sticky=E, padx=10, pady=10)

        botonActualizar=Button(frameBotones, text="Actualizar")
        botonActualizar.grid(row=0, column=2, sticky=E, padx=10, pady=10)

        botonBorrar=Button(frameBotones, text="Borrar")
        botonBorrar.grid(row=0, column=3, sticky=E, padx=10, pady=10)

        ventana.mainloop()

#---------------------- Funciones ------------------------------

class Conexion():
    
    def __init__(self):