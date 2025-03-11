import customtkinter as ctk
from Vista.Calculadora.Componentes.MenuAnimado import MenuAnimado
from Vista.Calculadora.Componentes.Calculadora import Calculadora 
from Controlador.CalculadoraControlador import CalculadoraControlador

class CalculadoraFrame(ctk.CTkFrame):
    def __init__(self, padre, controlador_vista):
        super().__init__(master=padre)
        self.controlador = CalculadoraControlador(padre)
        self.menu = MenuAnimado(self, (-0.3, 0.0), 0.9, self.controlador)
        self.calculadora = Calculadora(self, (0.3, 0.0), 1, self.controlador)
        



