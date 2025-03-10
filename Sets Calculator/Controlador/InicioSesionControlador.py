import re
from Modelo.BaseDeDatos import BaseDeDatos

class InicioSesionControlador():
    def __init__(self, vista):
        self.vista = vista
        self.modelo = BaseDeDatos("Modelo//Datos.json")

    def inicio_sesion(self, nombre, contraseña):
        mensaje = self.modelo.iniciar_sesion(nombre, contraseña)
        if (mensaje == "exito"):
            pass
        elif (mensaje == "incorrecta"):
            self.vista.menu.usuario_existe_var.set("Contraseña Incorrecta") 
        else:
            self.vista.menu.usuario_existe_var.set("Usuario No Existe") 

    def registrar_usuario(self, nombre, contraseña):
        if (self.validar_usuario(nombre) == False):
            self.vista.menu.usuario_existe_var.set("Usuario Inválido: (4-15 caracteres no especiales)") 
        elif (self.validar_contraseña(contraseña) == False):
            self.vista.menu.usuario_existe_var.set("Contraseña inválida: (8-20 caracteres)") 
        else:
            mensaje = self.modelo.registrar_usuario(nombre, contraseña)
            if (mensaje == False):
                self.vista.menu.usuario_existe_var.set("Usuario ya existe") 

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