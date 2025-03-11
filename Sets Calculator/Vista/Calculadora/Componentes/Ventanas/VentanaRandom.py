import customtkinter as ctk


class VentanaRandom(ctk.CTkToplevel):
    def __init__(self, master, controlador, universal_existe, lista_conjuntos):
        super().__init__(master=master)
        self.master = master
        self.transient(master)  
        self.geometry("600x600")
        self.iconbitmap("Vista//Materiales//icono.ico")
        self.controlador = controlador
        self.lista_conjuntos = lista_conjuntos
        
        self.crear_widgets()
        self.configurar_widgets()
        self.pack_widgets()
        
        if not universal_existe:
            self.title("Crear conjunto universal")
            self.nombre_entry.insert(0, "U")
            self.nombre_entry.configure(state="disabled")
        else:
            self.title("Crear Conjunto")

    def crear_widgets(self):

        self.titulo = ctk.CTkLabel(
            self,
            text="Conjunto Random",
            font=("Century Gothic", 50)
            )
        
        self.nombre_entry = ctk.CTkEntry(
            self,
            placeholder_text="Ingresa el nombre",
            font=("Century Gothic", 25),
            corner_radius=20
            )

        self.numero_elementos_entry = ctk.CTkEntry(
            self,
            placeholder_text="Ingresa el número de elementos",
            font=("Century Gothic", 25),
            corner_radius=20
            )

        self.opciones_label = ctk.CTkLabel(
            self,
            text="Elige los elementos del conjunto",
            font=("Century Gothic", 30)
            )
        
        self.caja_opciones = ctk.CTkComboBox(
            self,
            values=["Enteros", "Decimales", "Caracteres"],
            font=("Century Gothic", 25),
            dropdown_font=("Century Gothic", 25),
            state="readonly",
            corner_radius=20,
            command=self.validar_entrada_numero
            )
        
        self.crear_boton = ctk.CTkButton(
            self,
            text="Crear conjunto",
            font=("Century Gothic", 18),
            corner_radius=20
            )

    def configurar_widgets(self):
        self.caja_opciones.set("Enteros")
        
        self.nombre_entry.bind("<KeyRelease>", self.validar_entrada)
        self.numero_elementos_entry.bind("<KeyRelease>", self.validar_entrada_numero)
        self.nombre_entry.bind("<Return>", lambda evento: self.numero_elementos_entry.focus())
        self.crear_boton.bind("<Button-1>", self.crear_conjunto)

    def pack_widgets(self):
        self.titulo.pack(expand=True, fill="both", pady=20, padx=40)
        self.nombre_entry.pack(expand=True, fill="both", padx=40, pady=10)
        self.numero_elementos_entry.pack(expand=True, fill="both", padx=40, pady=10)
        self.opciones_label.pack(fill="x", pady=(20, 5))
        self.caja_opciones.pack(expand=True, fill="x", padx=40, pady=10)
        self.crear_boton.pack(expand=True, fill="both", padx=60, pady=(5, 20))

    def crear_conjunto(self, evento):
        nombre = self.nombre_entry.get()
        n_elementos = self.numero_elementos_entry.get()
        tipo = self.caja_opciones.get()
        self.controlador.crear_conjunto_random(nombre, n_elementos, tipo)
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
        if not texto.isdigit() or len(texto) > 2:
            texto_valido = "".join(filter(str.isdigit, texto))[:2]
            self.numero_elementos_entry.delete(0, ctk.END)
            self.numero_elementos_entry.insert(0, texto_valido)

        if self.caja_opciones.get() == "Caracteres":
            if texto.isdigit() and int(texto) >= 52:
                self.numero_elementos_entry.delete(0, ctk.END)
                self.numero_elementos_entry.insert(0, "51") 

    def bloquear_nombre(self):
        self.nombre_entry.insert(0, "U")
        self.nombre_entry.configure(state="disabled")