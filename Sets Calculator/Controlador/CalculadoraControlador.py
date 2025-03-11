import re
from Modelo.Operador import OperadorConjuntos
from Modelo.GeneradorConjuntos import GeneradorConjuntos
from Vista.Calculadora.Componentes.Ventanas.VentanaMostrar import VentanaMostrar

class CalculadoraControlador():
    def __init__(self, vista):
        self.conjuntos = {}
        self.vista = vista
        self.generador_conjuntos = GeneradorConjuntos()
        self.operador_conjuntos = OperadorConjuntos()
        
    def crear_conjunto(self, nombre, conjunto):
        self.conjuntos[nombre] = conjunto
        
    def crear_conjunto_random(self, nombre, n_elementos, tipo):
        conjunto = self.generador_conjuntos.generar(tipo, int(n_elementos))
        self.conjuntos[nombre] = conjunto
        
    def get_conjunto(self, nombre):
        return self.conjuntos[nombre]
    
    def realizar_operacion(self, operacion, variable):
        if (self.validar_operacion(operacion) == False):
            variable.set("Operación inválida")
            return

        for caracter in operacion:
            if (caracter.isalpha() and caracter.isupper()):
                conjunto_existe = self.conjuntos.get(caracter, False)
                if conjunto_existe == False:
                    variable.set(f"Conjunto inválido: '{caracter}'")
                    return
        
        resultado = self.operador_conjuntos.evaluar_operacion(operacion, self.conjuntos)
        if resultado == 0:
            texto = f"Conjunto Vacío: Ø"
        else:
            conjunto_ordenado = "{"
            for x in sorted(resultado):
                if x != sorted(resultado)[-1]: conjunto_ordenado += f"{x},"
                else: conjunto_ordenado += f"{x}"; conjunto_ordenado += "}"
            texto = f"Comprensión: {{x | x ∈ {conjunto_ordenado}}}\n\n\nExtensión: {conjunto_ordenado}"
        variable.set("")
        VentanaMostrar(self.vista, "Resultado", texto)


    def validar_operacion(self, operacion):
        patron = r"^[A-Z∪∩\-'()]+$"
        if re.match(patron, operacion):
            return True
        else:
            return False