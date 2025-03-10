import customtkinter as ctk

class Vista(ctk.CTkFrame):
    def __init__(self, padre):
        super().__init__(master=padre)
        menu = ctk.CTkFrame(self)
        
        menu_label = ctk.CTkLabel(menu, text="Conjuntos")
        menu_boton = ctk.CTkButton(menu, text="Nuevo Conjunto")
        menu_label.pack(fill="x")
        menu_boton.pack(fill="x")
        
        
        menu_animado = WidgetAnimado(menu, (-0.3, 0.0), 0.9)
        def animar():
            boton_animado.animar()
            menu_animado.animar()
        boton = ctk.CTkButton(self, command=animar)

        boton_animado = WidgetAnimado(boton, (0.0, 0.3), 0.05, 0.02)



"""
def mostrar_menu_contextual(event):
    # Obtener el índice del elemento seleccionado
    seleccionado = lista_conjuntos.curselection()
    if seleccionado:
        menu_contextual.post(event.x_root, event.y_root)  # Mostrar el menú en la posición del clic

# Función para mostrar el conjunto seleccionado
def mostrar_conjunto():
    seleccionado = lista_conjuntos.curselection()
    if seleccionado:
        conjunto = lista_conjuntos.get(seleccionado)
        print("Mostrar:", conjunto)

# Función para eliminar el conjunto seleccionado
def eliminar_conjunto():
    seleccionado = lista_conjuntos.curselection()
    if seleccionado:
        conjunto = lista_conjuntos.get(seleccionado)
        lista_conjuntos.delete(seleccionado)
        print("Eliminado:", conjunto)

# Crear la ventana principal
root = ctk.CTk()
root.title("Lista de Conjuntos")
root.geometry("400x300")

# Crear un frame para contener la lista
frame = ctk.CTkFrame(root)
frame.pack(fill="both", expand=True, padx=10, pady=10)

# Crear una lista de conjuntos (usando un Listbox de Tkinter)
lista_conjuntos = ctk.CTkListbox(frame)
lista_conjuntos.pack(fill="both", expand=True, padx=10, pady=10)

# Agregar algunos conjuntos de ejemplo
conjuntos = ["Conjunto 1", "Conjunto 2", "Conjunto 3"]
for conjunto in conjuntos:
    lista_conjuntos.insert("end", conjunto)

# Crear un menú contextual
menu_contextual = ctk.CTkMenu(root)
menu_contextual.add_command(label="Mostrar", command=mostrar_conjunto)
menu_contextual.add_command(label="Eliminar", command=eliminar_conjunto)

# Vincular el clic derecho a la función mostrar_menu_contextual
lista_conjuntos.bind("<Button-3>", mostrar_menu_contextual)  # Button-3 es el clic derecho



"""


    
class WidgetAnimado():
    def __init__(self, widget, recorrido, alto, ancho=None):
        self.widget = widget
        self.posicion_inicial = recorrido[0]
        self.posicion_final = recorrido[1]
        self.posicion = recorrido[0]
        if (ancho==None): self.ancho = abs(recorrido[1] - recorrido[0])
        else: self.ancho = ancho
        self.alto = alto
        self.esta_en_posicion_inicial = True
        self.widget.place(relx=recorrido[0], rely=0.05, relwidth=self.ancho, relheight=alto)

    def animar(self):
        if (self.esta_en_posicion_inicial):
            self.mostrar_frame()
        else:
            self.ocultar_frame()

    def mostrar_frame(self):
        if (self.posicion < self.posicion_final):
            self.pasos = 0.008
            self.posicion += self.pasos
            self.widget.place(relx=self.posicion, rely=0.05, relwidth=self.ancho, relheight=self.alto)
            self.widget.after(10, self.mostrar_frame)
        else:
            self.esta_en_posicion_inicial = False

    def ocultar_frame(self):
        if (self.posicion > self.posicion_inicial):
            self.pasos = 0.008
            self.posicion -= self.pasos
            self.widget.place(relx=self.posicion, rely=0.05, relwidth=self.ancho, relheight=self.alto)
            self.widget.after(10, self.ocultar_frame)
        else:
            self.esta_en_posicion_inicial = True
            
class MenuAnimado(ctk.CTkFrame):
    def __init__(self):
        super().__init__(self)
        