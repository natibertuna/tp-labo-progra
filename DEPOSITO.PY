class Deposito:
    def __init__(self):
        self.disponibilidad = {} 

    def obtener_disponibilidad(self, codigo_barra): #codigo de barras es único
        return self.disponibilidad.get(codigo_barra,0) #get: si no encuentra el codigo devuelve 0
    
    def agregar_disponibilidad(self, codigo_barra, cantidad):
        if codigo_barra in self.disponibilidad:
            self.disponibilidad[codigo_barra]+= cantidad #si ya esta cargado le sumo
        else:
            self.disponibilidad[codigo_barra]= cantidad
    
    def sacar_disponibilidad(self, codigo_barra, cantidad):
        if self.obtener_disponibilidad(codigo_barra)>= cantidad:
            self.disponibilidad[codigo_barra]-= cantidad
            return True
        return False #no habia suf. dispo.
