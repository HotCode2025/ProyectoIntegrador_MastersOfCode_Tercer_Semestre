from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox

class Clientes(tk.Frame):
    
    def __init__(self, padre, controlador):
        super().__init__(padre)
        self.controlador = controlador
        self.widgets()
        
    def widgets(self):
        self.labelframe = tk.LabelFrame(self, text="Clientes", font="sans 20 bold", bg="#FFE4E0")
        self.labelframe.place(x=20, y=20, width=250, height=560)

        lblnombre = tk.Label(self.labelframe, text="Nombre: ", font="sans 14 bold", bg="#FFE4E0")
        lblnombre.place(x=10, y=20)
        self.nombre = ttk.Entry(self.labelframe, font="sans 14 bold")
        self.nombre.place(x=10, y=50, width=220, height=40)

        lbldni = tk.Label(self.labelframe, text="DNI: ", font="sans 14 bold", bg="#FFE4E0")
        lbldni.place(x=10, y=100)
        self.dni = ttk.Entry(self.labelframe, font="sans 14 bold")
        self.dni.place(x=10, y=130, width=220, height=40)

        lblcelular = tk.Label(self.labelframe, text="Celular: ", font="sans 14 bold", bg="#FFE4E0")
        lblcelular.place(x=10, y=180)
        self.celular = ttk.Entry(self.labelframe, font="sans 14 bold")
        self.celular.place(x=10, y=210, width=220, height=40)

        lbldireccion = tk.Label(self.labelframe, text="Dirección: ", font="sans 14 bold", bg="#FFE4E0")
        lbldireccion.place(x=10, y=260)
        self.direccion = ttk.Entry(self.labelframe, font="sans 14 bold")
        self.direccion.place(x=10, y=290, width=220, height=40)

        lblcorreo = tk.Label(self.labelframe, text="Correo: ", font="sans 14 bold", bg="#FFE4E0")
        lblcorreo.place(x=10, y=340)
        self.correo = ttk.Entry(self.labelframe, font="sans 14 bold")
        self.correo.place(x=10, y=370, width=220, height=40)


        btn1 = Button(self.labelframe, fg="Black", text="Ingresar", font="sans 16 bold")
        btn1.place(x=10, y=420, width=220, height=40)

        btn2 = Button(self.labelframe, fg="Black", text="Modificar", font="sans 16 bold")
        btn2.place(x=10, y=470, width=220, height=40)


        treFrame = Frame(self, bg="white")
        treFrame.place(x=280, y=20, width=800, height=560)


        scrol_y = ttk.Scrollbar(treFrame)
        scrol_y.pack(side=RIGHT, fill=Y)

        scrol_x = ttk.Scrollbar(treFrame, orient=HORIZONTAL)
        scrol_x.pack(side=BOTTOM, fill=X)

        self.tre = ttk.Treeview(treFrame, yscrollcommand=scrol_y.set, xscrollcommand=scrol_x.set, height=40,
                                columns=("ID", "Nombre", "DNI", "Celular", "Dirección", "Correo"), show="headings")
        self.tre.pack(expand=True, fill=BOTH)

        scrol_y.config(command=self.tre.yview)
        scrol_x.config(command=self.tre.xview)

        self.tre.heading("ID", text="ID")
        self.tre.heading("Nombre", text="Nombre")
        self.tre.heading("DNI", text="DNI")
        self.tre.heading("Celular", text="Celular")
        self.tre.heading("Dirección", text="Dirección")
        self.tre.heading("Correo", text="Correo")

        self.tre.column("ID", width=50, anchor="center")
        self.tre.column("Nombre", width=150, anchor="center")
        self.tre.column("DNI", width=120, anchor="center")
        self.tre.column("Celular", width=120, anchor="center")
        self.tre.column("Dirección", width=200, anchor="center")
        self.tre.column("Correo", width=200, anchor="center")

