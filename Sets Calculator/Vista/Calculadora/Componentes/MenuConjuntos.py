import customtkinter as ctk
from Vista.Calculadora.Componentes.Generales.Lista import ListaConjunto
from Vista.Calculadora.Componentes.Ventanas.VentanaOpcion import VentanaOpcion


class MenuConjuntos(ctk.CTkFrame):
    def __init__(self, padre, coordenadas, alto, controlador):
        super().__init__(master=padre)
        self.padre = padre
        self.tema = ctk.StringVar(value="dark")
        self.controlador = controlador
        self.universal_existe = False
        
        self.crear_widgets()
        self.controlador.set_lista_conjuntos_labels(self.lista_conjuntos)
        self.pack_widgets()
        self.place(relx=coordenadas[0], rely=coordenadas[1], relwidth=0.3, relheight=alto)


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
        
    def crear_ventana(self):
        if (not "U" in self.lista_conjuntos.get_elementos()):
            self.universal_existe = False
            VentanaOpcion(self, self.controlador, self.universal_existe, self.lista_conjuntos)
            self.universal_existe = True
        else:
            VentanaOpcion(self, self.controlador, self.universal_existe, self.lista_conjuntos)