import customtkinter as ctk
from Vista.InicioDeSesion import InicioDeSesion
from Vista.Calculadora import Vista

class Aplicacion(ctk.CTk):
    def __init__(self, dimensiones_minimas: tuple):
        super().__init__()
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("Vista//Componentes//rime.json")
        
        self.geometry(f"{dimensiones_minimas[0]}x{dimensiones_minimas[1]}")
        self.minsize(dimensiones_minimas[0], dimensiones_minimas[1])
        self.title("Calculadora de Conjuntos")
        self.iconbitmap("Vista//Componentes//icono.ico")
        
        self.frame_principal = InicioDeSesion(self)
        self.frame_principal.pack(expand=True, fill="both")
        
        self.mainloop()
        