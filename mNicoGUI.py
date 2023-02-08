import tkinter as tk
from time import sleep
from tkinter import ttk
from tkinter.messagebox import askyesno

import customtkinter

import datetime
import db
from lib import isValid
#from user import User

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("User admin interface demo")
        self.geometry(f"{1100}x{580}")

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="User admin",
                                                 font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, command=self.show_create_user_table,
                                                        text="View users")
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)

        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame, command=self.show_edit_user_form,
                                                        text="Add user")
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)

        self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.scaling_option_menu = customtkinter.CTkOptionMenu(self.sidebar_frame,
                                                               values=["80%", "90%", "100%", "110%", "120%"],
                                                               command=self.change_scaling_event)
        self.scaling_option_menu.grid(row=8, column=0, padx=20, pady=(10, 20))
        self.scaling_option_menu.set("100%")

        self.edit_form = None

        # table
        self.print_table()

        self.form = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

        self.name = customtkinter.CTkLabel(self.form, text="Name")
        self.name.grid(row=2, column=0)

        self.name_field = customtkinter.CTkEntry(self.form)
        self.name_field.grid(row=2, column=1, ipadx=100, pady=5)

        self.email = customtkinter.CTkLabel(self.form, text="E-mail")
        self.email.grid(row=1, column=0)

        self.email_field = customtkinter.CTkEntry(self.form)
        self.email_field.bind("<Return>", command=self.validate_create_user_form)
        self.email_field.grid(row=1, column=1, ipadx=100, pady=5)

        self.submit_button = customtkinter.CTkButton(self.form, command=self.validate_create_user_form,
                                                     text="Create user")
        self.submit_button.grid(row=3, column=1, padx=20, pady=10)

    def print_table(self):
        cols = ('ID', 'Email', 'Name', 'Created at')
        self.table = ttk.Treeview(columns=cols, show='headings')
        self.table.grid(row=0, column=1, padx=(20, 20), pady=(20, 0), sticky="nsew")
        self.table.bind("<Double-1>", self.double_click_table_item)

        users = [u.serialize() for u in db.view()]
        for u in users:
            self.table.insert("", "end", values=(u['id'], u['name'], u['email'], u['created_at']))

        for col in cols:
            self.table.heading(col, text=col)

    def validate_create_user_form(self):
        if self.email_field.get() != "" and self.name_field.get() != "" and isValid(self.email_field.get()):
            usr = User(
                id=db.getNewId(),
                email=self.email_field.get(),
                name=self.name_field.get(),
                created_at=datetime.datetime.now()
            )
            # print('new user added: ', usr.serialize())
            db.insert(usr)

            self.print_table()

            self.email_field.delete(0, tk.END)
            self.email_field.insert(0, "")
            self.name_field.delete(0, tk.END)
            self.name_field.insert(0, "")

    def update_user_action(self):
        usr = User(
            id=self.edit_id_field.cget("text"),
            email=self.edit_email_field.get(),
            name=self.edit_name_field.get(),
            created_at=datetime.datetime.now()
        )

        if usr.id != "" and usr.name != "" and isValid(usr.email):
            db.update(usr)
            self.show_section_by_name("table")
            self.print_table()
        else:
            print("Error")

    def delete_user_action(self):
        user_id = self.edit_id_field.cget("text")
        if user_id is not None:
            db.delete(user_id)
            self.show_section_by_name("table")
            self.print_table()
        else:
            print("error")

    def confirm_delete(self):
        answer = askyesno(title='Remove user confirmation', message='Are you sure that you want to remove the user?')
        if answer:
            self.delete_user_action()

    def confirm_update(self):
        answer = askyesno(title='Update user confirmation', message='Are you sure that you want to update the user?')
        if answer:
            self.update_user_action()

    def print_edit_form(self):
        self.edit_form = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

        self.edit_name = customtkinter.CTkLabel(self.edit_form, text="Name ")
        self.edit_name.grid(row=3, column=0)
        self.edit_name_field = customtkinter.CTkEntry(self.edit_form)
        self.edit_name_field.grid(row=3, column=1, ipadx=100, pady=5)

        self.edit_email = customtkinter.CTkLabel(self.edit_form, text="E-mail ")
        self.edit_email.grid(row=2, column=0)
        self.edit_email_field = customtkinter.CTkEntry(self.edit_form)
        self.edit_email_field.grid(row=2, column=1, ipadx=100, pady=5)

        self.edit_id = customtkinter.CTkLabel(self.edit_form, text="ID")
        self.edit_id.grid(row=1, column=0)
        self.edit_id_field = customtkinter.CTkLabel(self.edit_form, text="", anchor="w")
        self.edit_id_field.grid(row=1, column=1, ipadx=135, pady=5)

        self.go_back_button = customtkinter.CTkButton(self.edit_form, command=self.show_create_user_table, text="Cancel")
        self.go_back_button.grid(row=4, column=0, padx=5, pady=10)

        self.edit_submit_button = customtkinter.CTkButton(self.edit_form, command=self.confirm_update,
                                                          text="Update user")
        self.edit_submit_button.grid(row=4, column=1, padx=20, pady=10)

        self.delete_button = customtkinter.CTkButton(self.edit_form, command=self.confirm_delete, text="Delete user",
                                                     fg_color=("#aa0000", "#bb0000"),
                                                     text_color=("gray10", "gray90"),
                                                     hover_color=("#990000", "#990000"))
        self.delete_button.grid(row=4, column=2, padx=20, pady=10)

    def double_click_table_item(self, event):
        item = self.table.selection()
        self.print_edit_form()
        self.edit_name_field.delete(0, tk.END)
        self.edit_email_field.delete(0, tk.END)

        for i in item:
            self.edit_name_field.insert(0, self.table.item(i, "values")[2])
            self.edit_email_field.insert(0, self.table.item(i, "values")[1])
            self.edit_id_field.configure(text=self.table.item(i, "values")[0])

        self.show_section_by_name("edit_form")
        sleep(1)
        self.edit_name.focus_set()
        self.edit_email_field.focus_set()

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def show_section_by_name(self, section_name):
        if section_name == "table":
            self.table.grid(row=0, column=1, padx=(20, 20), pady=(20, 0), sticky="nsew")
        else:
            self.table.grid_forget()
        if section_name == "form":
            self.form.grid(row=0, column=1, padx=(20, 20), pady=(20, 0), sticky="nsew")
        else:
            self.form.grid_forget()
        if section_name == "edit_form":
            self.edit_form.grid(row=0, column=1, padx=(20, 20), pady=(20, 0), sticky="nsew")
        else:
            if self.edit_form is not None:
                self.edit_form.grid_forget()

    def show_create_user_table(self):
        self.show_section_by_name("table")

    def show_edit_user_form(self):
        self.show_section_by_name("form")


if __name__ == "__main__":
    app = App()
    app.mainloop()