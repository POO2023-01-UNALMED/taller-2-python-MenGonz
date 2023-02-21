class Asiento:
    def __init__(self,color, precio, registro):
        self.color = color
        self.precio = precio
        self.registro = registro

    def cambiarColor(self, color):
        if color.lower() in ["verde", "rojo", "blanco", "amarillo", "negro"]:
            self.color = color

class Motor:
    def __init__(self, numeroCilindros, tipo, registro):
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro

    def  cambiarRegistro(self, registro):
        self.registro = registro

    def asignarTipo(self, tipo):
        if (tipo.lower() == "electrico") or (tipo.lower() == "gasolina"):
            self.tipo = tipo



class Auto:
    cantidadCreados = 0
    def __init__(self,modelo, precio, asientos, marca, motor, registro):
        self.modelo = modelo
        self.precio = precio
        self.asientos = asientos
        self.marca = marca
        self.motor = motor
        self.registro = registro

    def cantidadAsientos(self):
        cont = 0
        for x in self.asientos:
            if x != None:
                cont += 1
        
        return cont

    def verificarIntegridad(self):
        x = True 
        reg = self.motor.registro
        for y in self.asientos:
            if y != None and reg != y.registro:
                x= False
                break
        if x and self.registro == reg:
            return "Auto original"
        else:
            return "Las piezas no son originales"