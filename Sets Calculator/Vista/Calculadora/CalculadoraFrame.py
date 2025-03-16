import customtkinter as ctk
from Vista.Calculadora.Componentes.MenuConjuntos import MenuConjuntos
from Vista.Calculadora.Componentes.Calculadora import Calculadora 
from Vista.Calculadora.Componentes.MenuOperacionesEspeciales import MenuOperacionesEspeciales
from Controlador.CalculadoraControlador import CalculadoraControlador

class CalculadoraFrame(ctk.CTkFrame):
    def __init__(self, padre, controlador_vista):
        super().__init__(master=padre)
        self.controlador = CalculadoraControlador(padre)
        self.controlador_vista = controlador_vista
        self.menu = MenuConjuntos(self, (0.0, 0.05), 0.9, self.controlador)
        self.menu_operaciones_especiales = MenuOperacionesEspeciales(self, (-0.3, 0.0), 0.9, self.controlador)
        self.calculadora = Calculadora(self, (0.3, 0.0), 1, self.controlador)
        



