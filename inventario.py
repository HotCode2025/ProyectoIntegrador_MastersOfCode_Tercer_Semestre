import sqlite3
from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from PIL import Image, ImageTk
import sys
import os



class Inventario(tk.Frame):
    
    def __init__(self, padre, controlador):
        super().__init__(padre)
        self.controlador = controlador
        self.widgets()
        self.articulos_combobox()
        #aqui si no esta creada la carpeta fotos le pedimos al sistema que la cree
        self.image_folder = "fotos"
        if not os.path.exists(self.image_folder):
            os.makedirs(self.image_folder)
        
        
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

        btn1 = tk.Button(lblframe_botones, text="Agregar", font="arial 14 bold", command=self.agregar_articulo)
        btn1.place(x=20, y=20, width=180, height=40)

        btn2 = tk.Button(lblframe_botones, text="Editar", font="arial 14 bold")
        btn2.place(x=20, y=80, width=180, height=40)

    #************************************************************************************************

    #Creamos una funcion para cargar las imagenes
    def load_image(self):
        file_path = filedialog.askopenfilename()
        if file_path :
            image = Image.open(file_path)
            image = image.resize((200,200), Image.LANCZOS)
            image_name = os.path.basename(file_path)
            image_save_path = os.path.join(self.image_folder, image_name)
            image.save(image_save_path)
            self.image_tk = ImageTk.PhotoImage(image)
            self.product_image = self.image_tk
            self.image_path = image_save_path

            img_label = tk.Label(self.frameimg, image = self.image_tk)
            img_label.place(x=0, y=0, width=200, height=200)

    def articulos_combobox(self):
        self.con = sqlite3.connect('database.db')
        self.cur = self.con.cursor()
        self.cur.execute("SELECT articulo FROM articulos")
        self.articulos = [row[0] for row in self.cur.fetchall()]
        self.comboboxbuscar['values'] = self.articulos

    #creamos una funcion para cargar articulos
    def agregar_articulo(self):
        top= tk.Toplevel(self)
        top.title("Agregar Articulo")
        top.geometry("700x400+200+50")
        top.config(bg="#FFE4E0")
        top.resizable(False, False)
        #este metodo bloquea para que el usuario no pueda tocar ninguna otra opcion que no este en la parte
        #de agregar articulos hasta que se cierre
        top.transient(self.master)
        top.grab_set()
        top.focus_set()
        top.lift()

        tk.Label(top, text="Articulos:", font="arial 12 bold",bg="#FF7E63").place(x=20,y=20,height=25)
        entry_articulo = ttk.Entry(top, font="arial 12 bold")
        entry_articulo.place(x=120,y=20, width=250, height=30)

        tk.Label(top, text="Precio: ", font="arial 12 bold", bg="#FF7E63").place(x=20, y=60, width=80, height=25)
        entry_precio = ttk.Entry(top, font="arial 12 bold")
        entry_precio.place(x=120, y=60, width=250, height=30)

        tk.Label(top, text="Costo: ", font="arial 12 bold", bg="#FF7E63").place(x=20, y=100, width=80, height=25)
        entry_costo = ttk.Entry(top, font="arial 12 bold")
        entry_costo.place(x=120, y=100, width=250, height=30)

        tk.Label(top, text="Stock: ", font="arial 12 bold", bg="#FF7E63").place(x=20, y=140, width=80, height=25)
        entry_stock = ttk.Entry(top, font="arial 12 bold")
        entry_stock.place(x=120, y=140, width=250, height=30)

        tk.Label(top, text="Estado: ", font="arial 12 bold", bg="#FF7E63").place(x=20, y=180, width=80, height=25)
        entry_estado = ttk.Entry(top, font="arial 12 bold")
        entry_estado.place(x=120, y=180, width=250, height=30)

        self.frameimg = tk.Frame(top, bg="white",highlightbackground="gray",highlightthickness=1)
        self.frameimg.place(x=440, y=30, width=200, height=200)

        btnimage = tk.Button(top, text="Cargar Imagen", font="arial 12 bold",command=self.load_image)
        btnimage.place(x=470,y=260,width=150,height=40)

        #Creamos una funcion dentro de la funcion agregar articulos para guardar
        def guardar():
            articulo = entry_articulo.get()
            precio = entry_precio.get()
            costo = entry_costo.get()
            stock = entry_stock.get()
            estado = entry_estado.get()


            if not articulo or not precio or not costo or not stock or not estado:
                messagebox.showerror("Error", "Todos los campos deben ser completados")
                return
            
            try:
                precio = float(precio)
                costo = float(costo)
                stock = int(stock)
            except ValueError:
                messagebox.showerror("Error", "Precio, costo y stock deben ser numeros validos")
                return
            if hasattr(self, 'image_path'):
                image_path = self.image_path
                #Foto que aparecera por default si no cargamos ninguna foto en producto
            else:
                image_path = (r"fotos/default.jpeg")
            
            try:
                self.cur.execute("INSERT INTO articulos(articulo, precio, costo, stock, estado, image_path) VALUES(?,?,?,?,?,?)",
                                 (articulo, precio, costo, stock, estado, image_path))
                self.con.commit()
                messagebox.showinfo("Exito","Articulo agregado exitosamente")
                top.destroy()
            except sqlite3.Error as e:
                print("Error al cargar el articulo:", e)
                messagebox.showerror("Error", "Error al agregar el articulo")
        tk.Button(top,text="Guardar",font="arial 12 bold", command=guardar).place(x=50,y=260,width=150,height=40)
        tk.Button(top,text="Cancelar",font="arial 12 bold", command=top.destroy).place(x=260,y=260,width=150,height=40)


