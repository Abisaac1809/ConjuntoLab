import customtkinter as ctk
from Vista.Calculadora.Componentes.Ventanas.VentanaCrear import VentanaCrear
from Vista.Calculadora.Componentes.Ventanas.VentanaRandomUniversal import VentanaRandomUniversal
from Vista.Calculadora.Componentes.Ventanas.VentanaRandomConjunto import VentanaRandomConjunto

class VentanaOpcion(ctk.CTkToplevel):
    def __init__(self, master, controlador, universal_existe, lista_conjuntos):
        super().__init__(master=master)
        self.protocol("WM_DELETE_WINDOW", self.destroy)
        self.master = master
        self.transient(master)  
        self.geometry("400x200")
        self.iconbitmap("Vista//Materiales//icono.ico")
        self.title("Crear conjunto")
        self.controlador = controlador
        self.universal_existe = universal_existe
        self.lista_conjuntos = lista_conjuntos
        
        self.crear_widgets()
        self.pack_widgets()

    def crear_widgets(self):
        self.label = ctk.CTkLabel(
            self,
            text="Crear conjunto",
            font=("Century Gothic", 40)
            )
        
        self.opciones_frame = ctk.CTkFrame(
            self,
            fg_color=("#ebebeb", "#242424")
            )

        self.generar_boton = ctk.CTkButton(
            self.opciones_frame,
            text="Random",
            font=("Century Gothic", 15),
            command=self.conjunto_random
            )
        
        self.propio_boton = ctk.CTkButton(
            self.opciones_frame,
            text="Propio",
            font=("Century Gothic", 15),
            command=self.conjunto_propio
            )
        
    def pack_widgets(self):
        self.label.pack(fill="x",padx=20, pady=(20, 0))
        self.opciones_frame.pack(expand=True, fill="both",padx=20, pady=20)
        self.generar_boton.pack(side="left", expand=True, fill="both", padx=10, pady=10)
        self.propio_boton.pack(side="left", expand=True, fill="both", padx=10, pady=10)
    
    def conjunto_propio(self):
        if self.universal_existe:
            VentanaCrear(self, self.controlador, self.lista_conjuntos)
        else:
            VentanaCrear(self, self.controlador, self.lista_conjuntos, nombre_conjunto='U')
        
    def conjunto_random(self):
        if self.universal_existe:
            VentanaRandomConjunto(self, self.controlador, self.lista_conjuntos)
        else:
            VentanaRandomUniversal(self, self.controlador, self.lista_conjuntos)