import tkinter as tk
from .conexion_db import ConexionDB
from tkinter import messagebox
#from client.gui_app2 import 
from tkinter import ttk,messagebox
      
def crear_tabla():
    conexion = ConexionDB()
    sql = '''
    CREATE TABLE marketplace(
        id_producto INTEGER,
        producto VARCHAR(100),
        precio INTEGER,
        lugar VARCHAR(100),
        PRIMARY KEY(id_producto AUTOINCREMENT)
    )'''
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
        titulo = 'Crear Registro'
        mensaje = 'Se creo la tabla en la base de datos'
        messagebox.showinfo(titulo, mensaje)
    except:
        titulo = 'Crear Registro'
        mensaje = 'La tabla ya esta creada'
        messagebox.showwarning(titulo, mensaje)

def borrar_tabla():
    conexion = ConexionDB()
    sql = 'DROP TABLE marketplace'
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
        titulo = 'Borrar Registro'
        mensaje = 'La tabla en la base de datos se borro con exito'
        messagebox.showinfo(titulo, mensaje)
    except:
        titulo = 'Borrar Registro'
        mensaje = 'No hay tabla para borrar'
        messagebox.showerror(titulo, mensaje)

class Marketplace:
    def __init__(self, producto, precio, lugar):
        self.id_producto = None
        self.producto = producto
        self.precio = precio
        self.lugar = lugar

    def __str__(self):
        return f'marketplace[{self.producto},{self.precio},{self.lugar}]'

def guardar(marketplace):
    conexion = ConexionDB()

    sql = f"""INSERT INTO marketplace (producto, precio, lugar)
    VALUES('{marketplace.producto}', '{marketplace.precio}', '{marketplace.lugar}') """

    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
    except:
        titulo = 'Conexion al registro'
        mensaje = 'La tabla marketplace no esta creada en la base de datos'
        messagebox.showerror(titulo, mensaje)

def listar():
    conexion = ConexionDB()

    lista_marketplace = []
    sql = 'SELECT * FROM marketplace'

    try:
        conexion.cursor.execute(sql)
        lista_marketplace = conexion.cursor.fetchall()
        conexion.cerrar()
    except:
        titulo = 'Conexion al registro'
        mensaje = 'Crea la tabla en la base de datos'
        messagebox.showwarning(titulo, mensaje)

    return lista_marketplace

def filtrar(valor=2500):
    conexion = ConexionDB()
    lista_marketplace = []
    sql = "SELECT * FROM marketplace WHERE precio <= {}" .format(str(valor))

    try:
        conexion.cursor.execute(sql)
        lista_marketplace = conexion.cursor.fetchall()
        conexion.cerrar()
    except:
        titulo = 'Conexion al registro'
        mensaje = 'Crea la tabla en la base de datos'
        messagebox.showwarning(titulo, mensaje)
    
    return lista_marketplace
    
def editar(marketplace, id_producto):
    conexion = ConexionDB()
    
    sql = f"""UPDATE marketplace
    SET producto = '{marketplace.producto}', precio = {marketplace.precio},
    lugar = '{marketplace.lugar}'
    WHERE id_producto = {id_producto}"""

    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
    except:
        titulo = 'Edicion de datos'
        mensaje = 'No se ha podido editar este registro'
        messagebox.showerror(titulo, mensaje)

def eliminar(id_producto):
    conexion = ConexionDB()
    sql = f'DELETE FROM marketplace WHERE id_producto = {id_producto}'

    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
    except:
        titulo = 'Eliminar de datos'
        mensaje = 'No se ha podido eliminar este registro'
        messagebox.showerror(titulo, mensaje)

    
