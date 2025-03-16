import tkinter as tk
import customtkinter as ctk
from Vista.Calculadora.Componentes.Ventanas.VentanaMostrar import VentanaMostrar

class ListaConjunto(ctk.CTkScrollableFrame):
    def __init__(self, padre, controlador=None):
        super().__init__(master=padre)
        self.conjunto_label = {}
        self.controlador = controlador

        self.menu_contextual = tk.Menu(self, tearoff=0)
        self.menu_contextual.add_command(label="Eliminar", command=self.eliminar_conjunto)
        if controlador != None:
            self.menu_contextual.add_command(label="Mostrar", command=self.mostrar_conjunto)

    def agregar_conjunto(self, nombre_conjunto):
        
        label = ctk.CTkLabel(self, text=nombre_conjunto, cursor="hand2", font=("Century Gothic", 20))
        label.pack(fill="x", padx=10, pady=5)
        label.bind("<Button-3>", lambda evento, x=nombre_conjunto: self.mostrar_menu_contextual(evento, x))
        self.conjunto_label[nombre_conjunto] = label

    def mostrar_menu_contextual(self, event, conjunto):
        self.conjunto_seleccionado = conjunto
        self.menu_contextual.post(event.x_root, event.y_root)

    def mostrar_conjunto(self):
        nombre_conjunto = self.conjunto_seleccionado
        titulo = f"Conjunto {nombre_conjunto}"
        conjunto = self.controlador.get_conjunto(nombre_conjunto)
        texto = f"Comprensión: {{x | x ∈ {sorted(conjunto)}}}\n\n\nExtensión: {sorted(conjunto)}"
        VentanaMostrar(self, titulo, texto)

    def eliminar_conjunto(self):
        conjunto = self.conjunto_seleccionado
        widget = self.conjunto_label[conjunto]
        widget.destroy()
        self.conjunto_label.pop(conjunto)
        if self.controlador != None:
            if self.conjunto_seleccionado == 'U':
                for widget in self.conjunto_label.values():
                    widget.destroy()
                self.conjunto_label.clear()
        
    def get_elementos(self):
        return set(self.conjunto_label.keys())