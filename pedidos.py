from tkinter import *
import tkinter as tk

class Pedidos(tk.Frame):
    
    def __init__(self, padre, controlador):
        super().__init__(padre)
        self.controlador = controlador
        self.widgets()
        
    def widgets(self):
        label = Label(self, text="Pedidos")
        label.pack()