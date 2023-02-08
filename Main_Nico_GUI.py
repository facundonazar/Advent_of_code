import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import askyesno

import customtkinter

import datetime
import db

from lib import isValid
from user import User

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
        self.boton_ver_usuarios=customtkinter.CTkButton(self.sidebar_frame, text="Ver_usuarios", command=self.show_create_user_table)
        self.boton_ver_usuarios.grid(row=1,column=0, padx=20, pady=10)

        #boton "Agregar Usuarios" en panel lateral
        self.boton_agr_usuarios=customtkinter.CTkButton(self.sidebar_frame, text="Agregar_usuarios", command=self.show_edit_user_form)
        self.boton_agr_usuarios.grid(row=2,column=0, padx=20, pady=10)

        #etiqueta de menu desplegable de escala
        self.escala_label=customtkinter.CTkLabel(self.sidebar_frame, text="Escala")
        self.escala_label.grid(row=7,column=0, padx=20, pady=(10,0))
        
        #crea menu desplegable de escala
        self.escala_menu=customtkinter.CTkOptionMenu(self.sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"],
        command=self.cambiar_escala)
        self.escala_menu.grid(row=8,column=0,padx=20,pady=(10,20))
        self.escala_menu.set("100%")

        self.edit_formulario=None

        
        
        #funcion mostrar TABLA con usuarios
        self.print_table()

        self.formulario=customtkinter.CTkFrame(self, corner_radius=0, fg_color='transparent')

        self.nombre_label=customtkinter.CTkLabel(self.formulario, text='Nombre')
        self.nombre_label.grid(row=1, column=0)

        self.nombre_entry=customtkinter.CTkEntry(self.formulario)
        self.nombre_entry.grid(row=1, column=1)

        self.mail_label=customtkinter.CTkLabel(self.formulario, text='Mail')
        self.mail_label.grid(row=2, column=0)

        self.mail_entry=customtkinter.CTkEntry(self.formulario)
        self.mail_entry.bind('<Return>', command=self.validate_create_user_form, text='Create user')
        self.mail_entry.grid(row=2, column=1)

        self.boton_submit=customtkinter.CTkButton(self.formulario, command=self.validate_create_user_form, text='Create user')
        self.boton_submit.grid(row=3, column=1)

    def print_table(self):
        columnas=('ID','Mail','Nombre','creado')
        self.tabla=ttk.Treeview(columns=columnas,show='headings')
        self.tabla.grid(row=0, column=1, padx=(20, 20), pady=(20, 0), sticky='nsew')
        self.tabla.bind('<Double-1>', self.double_click_table_item)

        users=[u.serialize() for u in db.view]
        for u in users:
            self.tabla.insert('', 'end', values=(u['id'], u['nombre'], u['email'], u['creado']))

        for col in columnas:
            self.tabla.heading(col, text=col)

    def validate_create_user_form(self):
        if self.mail_entry.get() != "" and self.nombre_entry.get() != "" and isValid(self.mail_entry.get()):
            usr = User(
                id=db.getNewId(),
                mail=self.mail_entry.get(),
                nombre=self.nombre_entry.get(),
                creado=datetime.datetime.now()
            )
            
            #print('new user added:', usr.serialize())
            db.insert(usr)

            self.print_table()

            self.mail_entry.delete(0, tk.END)
            self.mail_entry.insert(0, '')
            self.nombre_entry.delete(0, tk.END)
            self.nombre_entry.insert(0, '')

    def update_user_action(self):
        usr=User(
            id=self.edit_id_entry.cget('text'),
            mail=self.edit_mail_entry.get(),
            nombre=self.edit_nombre_entry.get(),
            creado=datetime.datetime.now()
        )

        if usr.id != '' and usr.nombre != '' and isValid(usr.mail):
            db.update(usr)
            self.show_section_by_name('table')
            self.print_table()
        else:
            print('Error')

    def delete_user_action(self):
        user_id = self.edit_id_field.cget('text')
        if user_id is not None:
            db.delete(user_id)
            self.show_section_by_name('table')
            self.print_table()
        else:
            print('error')

    def confirm_delete(self):

        answer=askyesno(title='Confirmación para eliminar usuario', message='Seguro que deseas eliminar el usuario?')
        if answer:
            self.delete_user_action()

    def confirm_update(self):
        answer= askyesno(title='Confirmación para actualizar usuario', message='Desea actualizar la información del usuario?')
        if answer:
            self.update_user_action()

    def print_edit_formulario(self):
        self.edit_formulario= customtkinter.CTkFrame(self,corner_radius=0, fg_color='transparent')

        self.edit_nombre=customtkinter.CTkLabel(self.edit_formulario,text='Nombre')
        self.edit_nombre.grid(row=3, column=0)
        self.edit_nombre_entry=customtkinter.CTkEntry(self.edit_formulario)
        self.edit_nombre_entry.grid(row=3, column=1, ipadx=100, pady=5)

        self.edit_mail=customtkinter.CTkLabel(self.edit_formulario,text='Mail')
        self.edit_mail.grid(row=2, column=0)
        self.edit_mail_entry=customtkinter.CTkEntry(self.edit_formulario)
        self.edit_mail_entry.grid(row=2, column=1, ipadx=100, pady=5)

        self.edit_id=customtkinter.CTkLabel(self.edit_formulario,text='ID')
        self.edit_id.grid(row=1, column=0)
        self.edit_id_entry=customtkinter.CTkEntry(self.edit_formulario)
        self.edit_id_entry.grid(row=1, column=1, ipadx=135, pady=5)

        self.boton_atras = customtkinter.CTkButton(self.edit_formulario, command=self.show_create_user_table, text="Cancel")
        self.boton_atras.grid(row=4, column=0, padx=5, pady=10)

        self.boton_edit_submit = customtkinter.CTkButton(self.edit_formulario, command=self.confirm_update, text='Update user')
        self.boton_edit_submit.grid(row=4, column=1, padx=20, pady=10)

        self.boton_borrar=customtkinter.CTkButton(self.edit_formulario, command=self.confirm_delete, text='Delete user',
        fg_color=('#aa0000','#bb0000'),text_color=('gray10', 'gray90'), hover_color=('#990000', '#990000'))
        self.boton_borrar.grid(row=4,column=2,padx=20,pady=10)

    def double_click_table_item(self,event):
        item=self.tabla.selection()
        self.print_edit_formulario()
        self.edit_nombre_entry.delete(0, tk.END)
        self.edit_mail_entry.delete(0, tk.END)

        for i in item:
            self.edit_nombre_entry.insert(0, self.tabla.item(i,'values')[2])
            self.edit_mail_entry.insert(0, self.tabla.item(i,'values')[1])
            self.edit_id_entry.configure(text=self.tabla.item(i,'values')[0])

        self.show_section_by_name('edit_formulario')
        sleep(1)
        self.edit_nombre_entry.focus_set()
        self.edit_mail_entry.focus_set()

    def cambiar_escala(self, nueva_escala: str):
        nueva_escala_float = int(nueva_escala.replace('%',''))/100
        customtkinter.set_widget_scaling(nueva_escala_float)

    def show_section_by_name(self, section_name):
        if section_name=='tabla':
            self.tabla.grid(row=0, column=1, padx=(20, 20), pady=(20, 0), sticky='nsew')
        else:
            self.tabla.grid_forget()
        if section_name == 'formulario':
            self.formulario.grid(row=0, column=1, padx=(20, 20), pady=(20,0), sticky='nsew')
        else:
            self.formulario.grid_forget()
        if section_name == 'edit_formulario':
            self.edit_formulario.grid(row=0, column=1, padx=(20,20), pady=(20,0), sticky='nsew')
        elif self.edit_formulario is not None:
            self.edit_formulario.grid_forget()

    def show_create_user_table(self):
        self.show_section_by_name('tabla')

    def show_edit_user_form(self):
        self.show_section_by_name('formulario')

if __name__=='__main__':
    app=App()
    app.mainloop()
            