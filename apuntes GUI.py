
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
