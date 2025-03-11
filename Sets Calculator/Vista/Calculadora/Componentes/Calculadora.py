import customtkinter as ctk

class Calculadora(ctk.CTkFrame):
    def __init__(self, master, coordenadas, alto, controlador):
        super().__init__(master=master, fg_color=("#c0c8ce", "#2d2f33"))
        self.place(relx=coordenadas[0], rely=coordenadas[1], relwidth=abs(1-coordenadas[0]), relheight=alto)
        self.frame_contenido = ctk.CTkFrame(self, fg_color=("#b4bcc1", "#2e3135"))
        self.frame_contenido.place(relx=0.1, rely=0.05, relwidth=0.8, relheight=0.9)
        self.controlador = controlador
        
        self.crear_widgets()
        self.configurar_widgets()
        self.pack_widgets()
    
    def crear_widgets(self):
        self.operacion_entry = ctk.CTkEntry(
            self.frame_contenido,
            font=("Century Gothic", 70),
            corner_radius=20
            )
        
        self.error_variable = ctk.StringVar(value="")
        
        self.error_label = ctk.CTkLabel(
            self.frame_contenido,
            textvariable=self.error_variable,
            font=("Century Gothic", 18),
            text_color="red",
            )

        self.botones_frame = Teclado(self.frame_contenido, self.operacion_entry, self.controlador, self.error_variable)
    
    def configurar_widgets(self):
        self.operacion_entry.bind("<KeyRelease>", self.validar_entrada)
    
    def pack_widgets(self):
        self.operacion_entry.pack(padx=40, pady=20, expand=True, fill="both")
        self.error_label.pack(padx=40, fill="x")
        self.botones_frame.pack(padx=40,pady=20, expand=True, fill="both")

    def validar_entrada(self, event):
        if event.keysym == "BackSpace":  
            return
        texto_actual = self.operacion_entry.get()
        texto_filtrado = "".join(c for c in texto_actual if (c.isupper() or c in "∪∩-'()"))
        self.operacion_entry.delete(0, "end")
        self.operacion_entry.insert(0, texto_filtrado)

class Teclado(ctk.CTkFrame):
    def __init__(self, master, entry, controlador, label):
        super().__init__(master=master, fg_color=("#b4bcc1", "#2e3135"))
        self.master = master
        self.entry = entry
        self.controlador = controlador
        self.label = label
        self.rowconfigure((0,1), weight=1)
        self.columnconfigure((0,1,2,3), weight=1)
        
        self.crear_widgets()
        self.configurar_widgets()
        self.grid_widgets()

    def crear_widgets(self):
        self.boton_union = Boton(self, "∪", self.entry, True)
        self.boton_interseccion = Boton(self, "∩", self.entry, True)
        self.boton_diferencia = Boton(self, "-", self.entry, True)
        self.boton_complemento = Boton(self, "'", self.entry, True)
        self.boton_parentesis_abre = Boton(self, "(", self.entry, True)
        self.boton_parentesis_cierra = Boton(self, ")", self.entry, True)
        self.boton_borrar = Boton(self, "AC", self.entry, False)
        self.boton_igual = Boton(self, "=", self.entry, False)
    
    def configurar_widgets(self):
        self.boton_borrar.bind("<Button-1>", lambda e: self.entry.delete(0, "end"))
        self.boton_igual.bind("<Button-1>", self.realizar_operacion)
        self.entry.bind("<Return>", self.realizar_operacion)

    def grid_widgets(self):
        self.boton_union.grid(row=0, column=0, sticky="nswe", padx=5, pady=5)
        self.boton_interseccion.grid(row=0, column=1, sticky="nswe", padx=5, pady=5)
        self.boton_diferencia.grid(row=0, column=2, sticky="nswe", padx=5, pady=5)
        self.boton_complemento.grid(row=0, column=3, sticky="nswe", padx=5, pady=5)
        self.boton_parentesis_abre.grid(row=1, column=0, sticky="nswe", padx=5, pady=5)
        self.boton_parentesis_cierra.grid(row=1, column=1, sticky="nswe", padx=5, pady=5)
        self.boton_borrar.grid(row=1, column=2, sticky="nswe", padx=5, pady=5)
        self.boton_igual.grid(row=1, column=3, sticky="nswe", padx=5, pady=5)

    def realizar_operacion(self, evento):
        operacion = self.entry.get()
        self.entry.delete(0, "end")
        self.controlador.realizar_operacion(operacion, self.label)

class Boton(ctk.CTkButton):
    def __init__(self, master, signo, entry, puede_escribir):
        super().__init__(master=master)
        self.entry = entry
        self.configure(
            font=("Century Gothic", 40),
            text=signo,
            corner_radius=20
            )
        if (puede_escribir): self.configure(command=self.escribir)
    
    def escribir(self):
        texto_escrito = self.entry.get()
        self.entry.delete(0, "end")
        self.entry.insert(0, (texto_escrito + self._text))