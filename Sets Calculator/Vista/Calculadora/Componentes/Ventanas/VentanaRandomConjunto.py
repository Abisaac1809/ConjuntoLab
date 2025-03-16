import customtkinter as ctk

class VentanaRandomConjunto(ctk.CTkToplevel):
    def __init__(self, master, controlador, lista_conjuntos):
        super().__init__(master=master)
        self.protocol("WM_DELETE_WINDOW", self.destroy)
        self.master = master
        self.transient(master)  
        self.geometry("600x500")
        self.title("Crear conjunto")
        self.iconbitmap("Vista//Materiales//icono.ico")
        self.controlador = controlador
        self.lista_conjuntos = lista_conjuntos
        
        self.crear_widgets()
        self.configurar_widgets()
        self.pack_widgets()

    def crear_widgets(self):

        self.titulo = ctk.CTkLabel(
            self,
            text="Conjunto Random",
            font=("Century Gothic", 55)
            )
        
        self.nombre_entry = ctk.CTkEntry(
            self,
            placeholder_text="Ingresa el nombre",
            font=("Century Gothic", 25),
            corner_radius=20
            )
        
        self.numeros_label = ctk.CTkLabel(
            self, 
            font=("Century Gothic", 20),
            text_color="red",
            text=""
            )
        self.numero_elementos_entry = ctk.CTkEntry(
            self,
            placeholder_text="Ingresa el número de elementos",
            font=("Century Gothic", 25),
            corner_radius=20
            )
        
        self.crear_boton = ctk.CTkButton(
            self,
            text="Crear conjunto",
            font=("Century Gothic", 18),
            corner_radius=20
            )

    def configurar_widgets(self):
        self.nombre_entry.bind("<KeyRelease>", self.validar_entrada)
        self.numero_elementos_entry.bind("<KeyRelease>", self.validar_entrada_numero)
        self.nombre_entry.bind("<Return>", lambda evento: self.numero_elementos_entry.focus())
        self.numero_elementos_entry.bind("<Return>", self.crear_conjunto)
        self.crear_boton.bind("<Button-1>", self.crear_conjunto)

    def pack_widgets(self):
        self.titulo.pack(expand=True, fill="both", pady=20, padx=40)
        self.nombre_entry.pack(expand=True, fill="both", padx=40, pady=10)
        self.numeros_label.pack(fill="x", padx=40, pady=(10,0))
        self.numero_elementos_entry.pack(expand=True, fill="both", padx=40, pady=(5, 20))
        self.crear_boton.pack(expand=True, fill="both", padx=60, pady=20)

    def crear_conjunto(self, evento):
        nombre = self.nombre_entry.get()
        n_elementos = self.numero_elementos_entry.get()
        self.controlador.crear_conjunto_random(nombre, n_elementos)
        self.lista_conjuntos.agregar_conjunto(nombre)
        self.master.destroy()
        self.destroy()

    def validar_entrada(self, event):
        texto_actual = self.nombre_entry.get()

        if event.keysym == "BackSpace":
            return

        if len(texto_actual) > 1:
            self.nombre_entry.delete(1, "end") 

        if texto_actual and texto_actual.islower():
            texto_actual = texto_actual.upper()
            self.nombre_entry.delete(0, "end")
            self.nombre_entry.insert(0, texto_actual)

        elif texto_actual.isdigit():
            self.nombre_entry.delete(0, "end")

    def validar_entrada_numero(self, event):
        texto = self.numero_elementos_entry.get()
        if texto.isdigit():
            if int(texto) > len(self.controlador.get_conjunto("U")):
                self.numero_elementos_entry.delete(0, "end")
                self.numero_elementos_entry.insert(0, f"{len(self.controlador.get_conjunto("U"))}") 
                self.numeros_label.configure(text=f"Se aceptan máximo {len(self.controlador.get_conjunto("U"))} elementos")