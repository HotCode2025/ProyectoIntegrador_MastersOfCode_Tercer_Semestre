from tkinter import *
from tkinter import ttk
from login import Login
from login import Registro
from container import Container
import sys
import os


# definimos la clase manager con su constructor y sus parametros.
class Manager(Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Mercadito Bombal V1.0")
        self.geometry("1100x650+120+20")
        self.resizable(False, False)

        container = Frame(self)
        container.pack(side=TOP, fill=BOTH, expand=True)
        container.configure(bg="#FFE4E0")

        self.frames = {}
        for i in (Login, Registro, Container):
            # Aquí 'self' actúa como el 'controlador' que necesitan las vistas
            frame = i(container, self)
            self.frames[i] = frame
        
        # En lugar de llamar al método que falla, levantamos el frame directamente desde el diccionario:
        frame_inicial = self.frames[Login]
        frame_inicial.tkraise()

        self.style = ttk.Style()
        self.style.theme_use("clam")

    def show_frame(self, container_class):
        frame = self.frames[container_class]
        frame.tkraise()

# Esta funcion es la principal para ejecutar la aplicacion
def main():
    app = Manager()
    app.mainloop()

if __name__ == "__main__":
    main()
        
