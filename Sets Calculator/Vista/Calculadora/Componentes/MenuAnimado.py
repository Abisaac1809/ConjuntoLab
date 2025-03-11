import customtkinter as ctk
import tkinter as tk
from PIL import Image
from Vista.Calculadora.Componentes.Generales.Animacion import WidgetAnimado
from Vista.Calculadora.Componentes.Generales.Lista import ListaConjunto
from Vista.Calculadora.Componentes.Ventanas.VentanaOpcion import VentanaOpcion


class MenuAnimado(ctk.CTkFrame):
    def __init__(self, padre, recorrido, alto, controlador):
        super().__init__(master=padre)
        self.padre = padre
        self.tema = ctk.StringVar(value="dark")
        self.controlador = controlador
        self.universal_existe = False
        
        self.crear_widgets()
        self.crear_boton_externo(padre)
        self.pack_widgets()

        self.frame_animado = WidgetAnimado(self, recorrido, alto)
        
    def crear_boton_externo(self, padre):
        boton_imagen = ctk.CTkImage(
            light_image=Image.open("Vista//Materiales//barras_dark.ico").resize((128, 128)),
            dark_image=Image.open("Vista//Materiales//barras_dark.ico").resize((128, 128))
            )
        
        self.boton_externo = ctk.CTkButton(
            padre,
            text="",
            command=self.animar_menu,
            fg_color=("#b4bcc1", "#2e3135"),
            corner_radius=0,
            image=boton_imagen
            )
        
        self.boton_externo.place(relx=0.0, rely=0.05, relwidth=0.05, relheight=0.05)
        self.boton_activado = True

    def crear_widgets(self):
        self.switch = ctk.CTkSwitch(
            self,
            text="Modo Oscuro",
            command=lambda :ctk.set_appearance_mode(self.tema.get()),
            variable=self.tema,
            onvalue="dark",
            offvalue="light"
            )

        self.menu_label = ctk.CTkLabel(
            self,
            text="Conjuntos",
            font=("Century Gothic", 40)
            )
        
        self.menu_boton = ctk.CTkButton(
            self,
            text="Nuevo Conjunto",
            font=("Century Gothic", 18),
            command=self.crear_ventana
            )
        
        self.lista_conjuntos = ListaConjunto(self, self.controlador)

    def pack_widgets(self):
        self.switch.place(relx=0.5, rely=0.0, relwidth=0.5, relheight=0.11)
        self.menu_label.pack(fill="x", pady = (50,20))
        self.menu_boton.pack(ipady=5)
        self.lista_conjuntos.pack(fill="both", expand=True, padx=20, pady=30)

    def animar_menu(self):
        self.frame_animado.animar()
        
    def crear_ventana(self):
        if (not "U" in self.lista_conjuntos.get_elementos()):
            self.universal_existe = False
            VentanaOpcion(self, self.controlador, self.universal_existe, self.lista_conjuntos)
            self.universal_existe = True
        else:
            VentanaOpcion(self, self.controlador, self.universal_existe, self.lista_conjuntos)