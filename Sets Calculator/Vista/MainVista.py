import customtkinter as ctk

class Aplicacion(ctk.CTk):
    def __init__(self, dimensiones_minimas: tuple):
        super().__init__()
        self.geometry(f"{dimensiones_minimas[0]}x{dimensiones_minimas[1]}")
        self.minsize(dimensiones_minimas[0], dimensiones_minimas[1])

        self.mainloop()