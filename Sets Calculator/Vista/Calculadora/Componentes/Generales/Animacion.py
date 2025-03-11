class WidgetAnimado():
    
    def __init__(self, widget, recorrido, alto, ancho=None):
        self.widget = widget
        self.posicion_inicial = recorrido[0]
        self.posicion_final = recorrido[1]
        self.posicion = recorrido[0]
        if (ancho==None): self.ancho = abs(recorrido[1] - recorrido[0])
        else: self.ancho = ancho
        self.alto = alto
        self.esta_en_posicion_inicial = True
        self.widget.place(relx=recorrido[0], rely=0.05, relwidth=self.ancho, relheight=alto)

    def animar(self):
        if (self.esta_en_posicion_inicial):
            self.mostrar_frame()
        else:
            self.ocultar_frame()

    def mostrar_frame(self):
        if (self.posicion < self.posicion_final):
            self.pasos = 0.008
            self.posicion += self.pasos
            self.widget.place(relx=self.posicion, rely=0.05, relwidth=self.ancho, relheight=self.alto)
            self.widget.after(5, self.mostrar_frame)
        else:
            self.esta_en_posicion_inicial = False

    def ocultar_frame(self):
        if (self.posicion > self.posicion_inicial):
            self.pasos = 0.008
            self.posicion -= self.pasos
            self.widget.place(relx=self.posicion, rely=0.05, relwidth=self.ancho, relheight=self.alto)
            self.widget.after(4, self.ocultar_frame)
        else:
            self.esta_en_posicion_inicial = True
