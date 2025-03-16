import customtkinter as ctk
from PIL import Image
from Vista.Calculadora.Componentes.Generales.Animacion import WidgetAnimado
from Vista.Calculadora.Componentes.Ventanas.VentanaDiagramaVenn import VentanaDiagramVenn


class MenuOperacionesEspeciales(ctk.CTkFrame):
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
        self.titulo = ctk.CTkLabel(
            self,
            text="Operaciones\nespeciales",
            font=("Century Gothic", 40)
            )
        
        self.boton_interseccion = ctk.CTkButton(
            self, 
            font=("Century Gothic", 20),
            corner_radius=20,
            text="Intersección total",
            command=self.interseccion_total
            )
        
        self.boton_union = ctk.CTkButton(
            self, 
            font=("Century Gothic", 20),
            corner_radius=20,
            text="Unión total",
            command=self.union_total
            )

        self.boton_diagrama_venn = ctk.CTkButton(
            self, 
            font=("Century Gothic", 20),
            corner_radius=20,
            text="Diagrama de Venn",
            command=lambda: VentanaDiagramVenn(self, self.controlador)
            )

    def pack_widgets(self):
        self.titulo.pack(expand = True, fill="x", pady=15, padx=20)
        self.boton_union.pack(expand=True, fill="both", pady=15, padx=20)
        self.boton_interseccion.pack(expand=True, fill="both", pady=15, padx=20)
        self.boton_diagrama_venn.pack(expand=True, fill="both", pady=15, padx=20)

    def animar_menu(self):
        self.frame_animado.animar()
        
    def union_total(self):
        lista_conjuntos = list(self.controlador.get_conjuntos().keys())
        operacion = ""
        
        for conjunto in lista_conjuntos:
            if conjunto == 'U':
                continue
            if conjunto != lista_conjuntos[-1]:
                operacion += f"{conjunto}∪" 
            else:
        
                operacion +=f"{conjunto}"
        
        self.controlador.realizar_operacion(operacion, None)

    def interseccion_total(self):
        lista_conjuntos = list(self.controlador.get_conjuntos().keys())
        operacion = ""
        
        for conjunto in lista_conjuntos:
            if conjunto == 'U':
                continue
            if conjunto != lista_conjuntos[-1]:
                operacion += f"{conjunto}∩" 
            else:
        
                operacion +=f"{conjunto}"
        
        self.controlador.realizar_operacion(operacion, None)
