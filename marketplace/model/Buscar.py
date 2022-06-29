import tkinter as tk
from client.gui_app2 import Frame,barra_menu
def main(): 
    root = tk.Tk()
    root.title('Navegador')
    root.iconbitmap('img/ico.ico')
    root.resizable(0,0)
    barra_menu(root)
    
    app=Frame(root=root)
    ##Botones 
    root.mainloop()
    
if __name__ == '__main__':
    main() 