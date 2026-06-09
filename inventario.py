from tkinter import *
import tkinter as tk

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

