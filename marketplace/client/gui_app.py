import tkinter as tk
from tkinter import ttk, messagebox
from model.marketplace_dao import crear_tabla, borrar_tabla
from model.marketplace_dao import Marketplace, guardar, listar, editar, eliminar
from model.Buscar import main
#from client.gui_app2 import buscar



def barra_menu(root):
    barra_menu = tk.Menu(root)
    root.config(menu = barra_menu, width= 300, height = 300)

    menu_inicio = tk.Menu(barra_menu, tearoff = 0)
    barra_menu.add_cascade(label = 'Agregar', menu = menu_inicio)

    menu_inicio.add_command(label = 'Crear Registro DB', command= crear_tabla)
    menu_inicio.add_command(label = 'Eliminar Registro DB',command= borrar_tabla)

    barra_menu.add_cascade(label = 'Buscar', command=main)

    barra_menu.add_cascade(label = 'Salir', command = root.destroy)
    
class Frame(tk.Frame):
    def __init__(self, root= None):
        super().__init__(root,width = 480, height=320 )
        self.root = root
        self.pack()
        #self.config( bg = 'white')
        self.id_producto = None

        self.campos_producto()
        self.deshabilitar_campos()
        self.tabla_marketplace()

    def campos_producto(self):
        #labels de campo
        self.label_producto = tk.Label(self, text= 'Producto: ')
        self.label_producto.config(font = ('Arial', 12, 'bold'))
        self.label_producto.grid(row=0, column =0, padx = 10, pady= 10)

        self.label_precio = tk.Label(self, text= 'Precio: ')
        self.label_precio.config(font = ('Arial', 12, 'bold'))
        self.label_precio.grid(row=1, column =0, padx = 10, pady= 10)

        self.label_lugar = tk.Label(self, text= 'Ubicacion: ')
        self.label_lugar.config(font = ('Arial', 12, 'bold'))
        self.label_lugar.grid(row=2, column =0, padx = 10, pady= 10)

        #labels de entrada
        self.mi_producto = tk.StringVar()
        self.entry_producto = tk.Entry(self, textvariable=self.mi_producto)
        self.entry_producto.config(width = 50, font = ('Arial', 12) )
        self.entry_producto.grid(row=0, column= 1,  padx = 10, pady= 10, columnspan= 12)

        self.mi_precio = tk.StringVar()
        self.entry_precio = tk.Entry(self, textvariable= self.mi_precio)
        self.entry_precio.config(width = 50, font = ('Arial', 12) )
        self.entry_precio.grid(row=1, column= 1, padx = 10, pady= 10, columnspan= 12)

        self.mi_lugar = tk.StringVar()
        self.entry_lugar = tk.Entry(self, textvariable= self.mi_lugar)
        self.entry_lugar.config(width = 50, font = ('Arial', 12) )
        self.entry_lugar.grid(row=2, column= 1, padx = 10, pady= 10, columnspan= 12)

        #buttons

        self.boton_nuevo = tk.Button(self, text= 'Nuevo', command = self.habilitar_campos)
        self.boton_nuevo.config(width= 20, font = ('Arial', 12, 'bold'), fg= '#FFFFFF', bg ='#158645', cursor = 'hand2', activebackground= '#35BD6F')
        self.boton_nuevo.grid(row= 3, column=0, padx = 10, pady= 10)

        self.boton_guardar= tk.Button(self, text= 'Guardar', command = self.guardar_datos)
        self.boton_guardar.config(width= 20, font = ('Arial', 12, 'bold'), fg= '#FFFFFF', bg ='#1658A2', cursor = 'hand2', activebackground= '#3586DF')
        self.boton_guardar.grid(row= 3, column=1, padx = 10, pady= 10)

        self.boton_cancelar = tk.Button(self, text= 'Cancelar', command = self.deshabilitar_campos)
        self.boton_cancelar.config(width= 20, font = ('Arial', 12, 'bold'), fg= '#FFFFFF', bg ='#BD152E', cursor = 'hand2', activebackground= '#E15370')
        self.boton_cancelar.grid(row= 3, column=2, padx = 10, pady= 10)
        

    def habilitar_campos(self):
        self.entry_producto.config(state='normal')
        self.entry_precio.config(state='normal')
        self.entry_lugar.config(state='normal')

        self.boton_guardar.config(state='normal')
        self.boton_cancelar.config(state='normal')

    def deshabilitar_campos(self):
        self.id_producto = None
        self.mi_producto.set('')
        self.mi_precio.set('')
        self.mi_lugar.set('')

        self.entry_producto.config(state='disabled')
        self.entry_precio.config(state='disabled')
        self.entry_lugar.config(state='disabled')

        self.boton_guardar.config(state='disabled')
        self.boton_cancelar.config(state='disabled')

    def guardar_datos(self):
        
        marketplace = Marketplace(
            self.mi_producto.get(),
            self.mi_precio.get(),
            self.mi_lugar.get(),
        )

        if self.id_producto == None:
            guardar(marketplace)
        else:
            editar(marketplace, self.id_producto)

        self.tabla_marketplace()

        self.deshabilitar_campos()

    def tabla_marketplace(self):
        
        self.lista_marketplace = listar()
        self.lista_marketplace.reverse()


        self.tabla = ttk.Treeview(self, 
        column = ('Producto', 'Precio', 'Ubicacion'))
        self.tabla.grid(row=4,column=0, columnspan=4, sticky= 'nse')

        #scrollbar

        self.scroll = ttk.Scrollbar(self,
        orient = 'vertical', command = self.tabla.yview)
        self.scroll.grid(row = 4, column = 4, sticky= 'nse')
        self.tabla.configure(yscrollcommand = self.scroll.set)


        self.tabla.heading('#0', text='ID')
        self.tabla.heading('#1', text='Producto')
        self.tabla.heading('#2', text='Precio')
        self.tabla.heading('#3', text='Ubicacion')

        #iterar la lista de peliculas
        for p in self.lista_marketplace:
            self.tabla.insert('',0, text=p[0],
            values= (p[1], p[2], p[3]))

        #Botones Editar

        self.boton_editar= tk.Button(self, text= 'Editar', command= self.editar_datos)
        self.boton_editar.config(width= 20, font = ('Arial', 12, 'bold'), fg= '#FFFFFF', bg ='#1658A2', cursor = 'hand2', activebackground= '#3586DF')
        self.boton_editar.grid(row= 5, column=0, padx = 10, pady= 10)

        #Botones Eliminar

        self.boton_eliminar = tk.Button(self, text= 'Eliminar', command = self.eliminar_datos)
        self.boton_eliminar.config(width= 20, font = ('Arial', 12, 'bold'), fg= '#FFFFFF', bg ='#BD152E', cursor = 'hand2', activebackground= '#E15370')
        self.boton_eliminar.grid(row= 5, column=1, padx = 10, pady= 10)


    def editar_datos(self):
        try:
            self.id_producto = self.tabla.item(self.tabla.selection())['text']
            self.producto_marketplace = self.tabla.item(
                self.tabla.selection())['values'][0]
            self.precio_marketplace = self.tabla.item(
                self.tabla.selection())['values'][1]
            self.lugar_marketplace = self.tabla.item(
                self.tabla.selection())['values'][2]

            self.habilitar_campos()

            self.entry_producto.insert(0, self.producto_marketplace)
            self.entry_precio.insert(0, self.precio_marketplace)
            self.entry_lugar.insert(0, self.lugar_marketplace)
           
        except:
            titulo = 'Edicion de datos'
            mensaje = 'No ha seleccionado ningun registro'
            messagebox.showerror(titulo, mensaje)

    def eliminar_datos(self):
        try: 
            self.id_producto = self.tabla.item(self.tabla.selection())['text']
            eliminar(self.id_producto)

            self.tabla_marketplace()
            self.id_producto = None

        except:
            titulo = 'Eliminar un registro'
            mensaje = 'No ha seleccionado ningun regitro'
            messagebox.showerror(titulo, mensaje)


        
        
        