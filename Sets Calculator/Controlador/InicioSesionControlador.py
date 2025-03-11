import re
from Modelo.BaseDeDatos import BaseDeDatos

class InicioSesionControlador():
    def __init__(self, controlador_vista):
        self.base_datos = BaseDeDatos("Modelo//Datos.json")
        self.controlador_vista = controlador_vista

    def inicio_sesion(self, nombre, contraseña, variable):
        mensaje = self.base_datos.iniciar_sesion(nombre, contraseña)
        if (mensaje == "exito"):
            self.controlador_vista.cambiar_frame("Calculadora")
        elif (mensaje == "incorrecta"):
            variable.set("Contraseña Incorrecta") 
        else:
            variable.set("Usuario No Existe") 

    def registrar_usuario(self, nombre, contraseña, variable):
        if (self.validar_usuario(nombre) == False):
            variable.set("Usuario Inválido: (4-15 caracteres no especiales)") 
        elif (self.validar_contraseña(contraseña) == False):
            variable.set("Contraseña inválida: (8-20 caracteres)") 
        else:
            usuario_existe = self.base_datos.registrar_usuario(nombre, contraseña)
            if usuario_existe:
                variable.set("Usuario ya existe") 
            else:
                self.controlador_vista.cambiar_frame("Calculadora")

    def validar_usuario(self, usuario):
        patron = r"^[a-zA-Z0-9_]{4,15}$"
        if re.match(patron, usuario):
            return True
        else:
            return False

    def validar_contraseña(self, contraseña):
        patron = r"^.{8,}$"
        if re.match(patron, contraseña):
            return True
        else:
            return False