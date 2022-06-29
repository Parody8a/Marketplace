import tkinter as tk
from tkinter import ttk
from model.conexion_db import ConexionDB
from model.marketplace_dao import filtrar

def barra_menu(root):
    barra_menu = tk.Menu(root)
    root.config(menu = barra_menu, width= 300, height = 300)
    barra_menu.add_cascade(label = 'Salir', command = root.destroy)

class Frame(tk.Frame):
    def __init__(self, root= None):
        super().__init__(root,width = 480, height=320 )
        self.root = root
        self.pack()
        self.cositas()
        self.deshabilitar_campos()
        self.tabla_marketplace()
        
    def cositas (self):
        self.boton_nuevo = tk.Button(self, text= 'Nuevo', command=self.habilitar_campos)
        self.boton_nuevo.config(width= 20, font = ('Arial', 12, 'bold'), fg= '#FFFFFF', bg ='#158645', cursor = 'hand2', activebackground= '#35BD6F')
        self.boton_nuevo.grid(row= 3, column=0, padx = 10, pady= 10)        
        
        self.boton_guardar= tk.Button(self, text= 'Filtrar',command=self.final)
        self.boton_guardar.config(width= 20, font = ('Arial', 12, 'bold'), fg= '#FFFFFF', bg ='#1658A2', cursor = 'hand2', activebackground= '#3586DF')
        self.boton_guardar.grid(row= 3, column=1, padx = 10, pady= 10)

        self.boton_cancelar = tk.Button(self, text= 'Cancelar',command=self.deshabilitar_campos)
        self.boton_cancelar.config(width= 20, font = ('Arial', 12, 'bold'), fg= '#FFFFFF', bg ='#BD152E', cursor = 'hand2', activebackground= '#E15370')
        self.boton_cancelar.grid(row= 3, column=2, padx = 10, pady= 10)
        

        
        ##labels
        
        self.label_producto = tk.Label(self, text= 'Producto: ')
        self.label_producto.config(font = ('Arial', 12, 'bold'))
        self.label_producto.grid(row=0, column =0, padx = 10, pady= 10)

        self.label_precio = tk.Label(self, text= 'Precio: ')
        self.label_precio.config(font = ('Arial', 12, 'bold'))
        self.label_precio.grid(row=1, column =0, padx = 10, pady= 10)

        self.label_lugar = tk.Label(self, text= 'Ubicacion: ')
        self.label_lugar.config(font = ('Arial', 12, 'bold'))
        self.label_lugar.grid(row=2, column =0, padx = 10, pady= 10)
        
        ##Entrys
        
        self.mi_producto = tk.StringVar()
        self.entry_producto = tk.Entry(self, textvariable=self.mi_producto)
        self.entry_producto.config(width = 50, font = ('Arial', 12) )
        self.entry_producto.grid(row=0, column= 1,  padx = 10, pady= 10, columnspan= 12)

        self.mi_precio = tk.StringVar()
        self.entry_precio = tk.Entry(self, textvariable=self.mi_precio)
        self.entry_precio.config(width = 50, font = ('Arial', 12) )
        self.entry_precio.grid(row=1, column= 1, padx = 10, pady= 10, columnspan= 12)

        self.mi_lugar = tk.StringVar()
        self.entry_lugar = tk.Entry(self, textvariable=self.mi_lugar)
        self.entry_lugar.config(width = 50, font = ('Arial', 12) )
        self.entry_lugar.grid(row=2, column= 1, padx = 10, pady= 10, columnspan= 12)
       
      
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
    
   
    def tabla_marketplace(self):
        
        self.lista_producto  = filtrar(valor=4000)
        self.lista_producto .reverse()


        self.tabla = ttk.Treeview(self, 
        column = ('Producto', 'Precio', 'Ubicacion'))
        self.tabla.grid(row=4,column=0, columnspan=3, sticky= 'nse')

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
        for p in self.lista_producto :
            self.tabla.insert('',0, text=p[0],
            values= (p[1], p[2], p[3]))

    def final (self):
        x=self.mi_precio.get()
        print("2500",x,type(x))
        y=str(x)
        print(y,type(y))

