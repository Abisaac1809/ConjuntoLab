import customtkinter as ctk
from Controlador.InicioSesionControlador import InicioSesionControlador
from Vista.InicioDeSesion.Componentes import Menu
from Vista.InicioDeSesion.Componentes import Imagen

class InicioDeSesionFrame(ctk.CTkFrame):
    def __init__(self, padre, controlador_vista):
        super().__init__(master=padre)
        self.controlador = InicioSesionControlador(controlador_vista)
        self.menu = Menu.Menu(self, self.controlador)
        self.imagen = Imagen.Imagen(self)
        self.menu.place(relx=0.0, rely=0.0, relwidth=0.4, relheight=1)
        self.imagen.place(relx=0.4, rely=0.0, relwidth=0.6, relheight=1)