import json
import bcrypt
import os

class BaseDeDatos():
    def __init__(self, ruta):
        self.RUTA = ruta

    def cargar_datos(self):
        if os.path.exists(self.RUTA):
            with open(self.RUTA, "r") as archivo:
                return json.load(archivo)
        return {"usuarios": []}

    def guardar_datos(self, datos):
        with open(self.RUTA, "w") as archivo:
            json.dump(datos, archivo, indent=4)

    def registrar_usuario(self, nombre, contraseña):
        datos = self.cargar_datos()

        for usuario in datos["usuarios"]:
            if usuario["nombre"] == nombre:
                return False
        contraseña_bytes = contraseña.encode("utf-8")
        salt = bcrypt.gensalt()
        contraseña_hasheada = bcrypt.hashpw(contraseña_bytes, salt)
        nuevo_usuario = {
            "nombre": nombre,
            "contraseña": contraseña_hasheada.decode("utf-8") 
        }
        datos["usuarios"].append(nuevo_usuario)
        self.guardar_datos(datos)
        return True

    def iniciar_sesion(self,nombre, contraseña):
        datos = self.cargar_datos()
        for usuario in datos["usuarios"]:
            if usuario["nombre"] == nombre:
                contraseña_bytes = contraseña.encode("utf-8")
                contraseña_hasheada = usuario["contraseña"].encode("utf-8")
                if bcrypt.checkpw(contraseña_bytes, contraseña_hasheada):
                    return "exito"
                else:
                    return "incorrecta"
        return "no_encontrado"