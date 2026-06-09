from tkinter import *
import tkinter as tk

class Clientes(tk.Frame):
    
    def __init__(self, padre, controlador):
        super().__init__(padre)
        self.controlador = controlador
        self.widgets()
        
    def widgets(self):
        label = Label(self, text="Clientes")
        label.pack()