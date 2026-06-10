from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox, filedialog

class Inventario(tk.Frame):
    
    def __init__(self, padre, controlador):
        super().__init__(padre)
        self.controlador = controlador
        self.widgets()
        
        
    def widgets(self):
        # Creamos la "caja principal" (con título "Articulos") para meter todo adentro
        canvas_articulos = tk.LabelFrame(self, text="Articulos", font="arial 14 bold", bg="#FFB7A6")
        # Colocamos esa caja en la pantalla dándole una posición (X, Y) y un tamaño fijo
        canvas_articulos.place(x=300, y=10, width=780, height=580)

        self.canvas = tk.Canvas(canvas_articulos, bg="#FFB7A6")
        #Creamos la barra de scroll vertical física que el usuario va a arrastrar con el mouse
        self.scrollbar = tk.Scrollbar(canvas_articulos, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = tk.Frame(self.canvas, bg="#FFB7A6")
        #Aqui le decimos a python que cada vez que agreguemos un producto el panel se haga mas largo y
        #recalcule el temaño de la barra de scroll
        self.scrollable_frame.bind(
            "<Configure>",  
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )

        self.canvas.create_window((0,0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.scrollbar.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)

 #************************************************************************************************
        #creamos el widget para buscar
        lblframe_buscar = LabelFrame(self, text="Buscar", font="arial 14 bold", bg="#FFB7A6")
        lblframe_buscar.place(x=10,y=10, width=280, height=80)

        self.comboboxbuscar = ttk.Combobox(lblframe_buscar, font="Arial 12")
        self.comboboxbuscar.place(x=5, y=5, width=260, height=40)

    # ***********************************************************************************************
        lblframe_seleccion = LabelFrame(self, text="Selección", font="arial 14 bold", bg="#FFB7A6")
        lblframe_seleccion.place(x=10, y=95, width=280, height=190)

        self.label1 = tk.Label(lblframe_seleccion, text="Artículo: ", font="arial 12", bg="#FFB7A6", wraplength=300)
        self.label1.place(x=5, y=5)

        self.label2 = tk.Label(lblframe_seleccion, text="Precio: ", font="arial 12", bg="#FFB7A6")
        self.label2.place(x=5, y=40)

        self.label3 = tk.Label(lblframe_seleccion, text="Costo: ", font="arial 12", bg="#FFB7A6")
        self.label3.place(x=5, y=70)

        self.label4 = tk.Label(lblframe_seleccion, text="Stock: ", font="arial 12", bg="#FFB7A6")
        self.label4.place(x=5, y=100)

        self.label5 = tk.Label(lblframe_seleccion, text="Estado: ", font="arial 12", bg="#FFB7A6")
        self.label5.place(x=5, y=130)
    #*************************************************************************************************

        lblframe_botones = LabelFrame(self, bg="#FFB7A6", text="Opciones", font="arial 14 bold")
        lblframe_botones.place(x=10, y=290, width=280, height=300)

        btn1 = tk.Button(lblframe_botones, text="Agregar", font="arial 14 bold")
        btn1.place(x=20, y=20, width=180, height=40)

        btn2 = tk.Button(lblframe_botones, text="Editar", font="arial 14 bold")
        btn2.place(x=20, y=80, width=180, height=40)



