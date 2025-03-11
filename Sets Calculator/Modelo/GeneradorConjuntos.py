import random
import string

class GeneradorConjuntos:
    def __init__(self):
        self.operaciones = {
            "Enteros": lambda n: self.generar_enteros(n),
            "Decimales": lambda n: self.generar_decimales(n),
            "Caracteres": lambda n: self.generar_decimales(n),
            }
        
    def generar(self, tipo, n):
        return self.operaciones[tipo](n)
    
    def generar_enteros(self, n):
        conjunto = set()
        while len(conjunto) < n:
            conjunto.add(random.randint(0, 100))
        return conjunto

    def generar_decimales(self, n):
        conjunto = set()
        while len(conjunto) < n:
            conjunto.add(round(random.uniform(0.0, 100.0), 2))
        return conjunto

    def generar_caracteres(self, n):
        letras = string.ascii_letters
        if n > len(letras):
            pass
        return set(random.sample(letras, n))