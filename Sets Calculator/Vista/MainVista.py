import customtkinter as ctk
from Controlador.VistasControlador import VistasControlador

class Aplicacion(ctk.CTk):
    def __init__(self, dimensiones_minimas: tuple):
        super().__init__()
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("Vista//Materiales//rime.json")
        
        self.geometry(f"{dimensiones_minimas[0]}x{dimensiones_minimas[1]}")
        self.minsize(dimensiones_minimas[0], dimensiones_minimas[1])
        self.title("Calculadora de Conjuntos")
        self.iconbitmap("Vista//Materiales//icono.ico")
        self.vistas_controlador = VistasControlador(self)
        
        self.frame_principal = self.vistas_controlador.get_frame_principal()
        self.frame_principal.pack(expand=True, fill="both")
        
        self.mainloop()

    def cambiar_frame(self, frame):
        self.frame_principal = frame
        self.frame_principal.pack(expand=True, fill="both")
        
    def olvidar_frame(self):
        self.frame_principal.pack_forget()
        self.frame_principal.destroy()