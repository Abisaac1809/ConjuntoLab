from Vista.InicioDeSesion.InicioDeSesion import InicioDeSesionFrame
from Vista.Calculadora.CalculadoraFrame import CalculadoraFrame

class VistasControlador():
    def __init__(self, ventana_principal):
        self.ventana_principal = ventana_principal
        self.frames = {
            "Inicio": lambda: InicioDeSesionFrame(self.ventana_principal, self),
            "Calculadora": lambda: CalculadoraFrame(self.ventana_principal, self)
            }
        
    def get_frame_principal(self):
        return InicioDeSesionFrame(self.ventana_principal, self)
    
    def cambiar_frame(self, frame):
        frame = self.frames.get(frame)()
        self.ventana_principal.olvidar_frame()
        self.ventana_principal.cambiar_frame(frame)