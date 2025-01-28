'''
crear una clase llamada Distancia que tenga como atributos dos puntos (x1,y1) y (x2,y2) y como método calcular la distancia entre los dos puntos pidiendo al usuario los numeros para capturar.
'''
class Distancia:
    # declaracion del constructor
    def __init__(self):
        self.x1 = 0
        self.y1 = 0
        self.x2 = 0
        self.y2 = 0

    # declaracion para capturar los datos
    def usuario(self):
        self.x1 = int(input("Valor de x1: "))
        self.y1 = int(input("Valor de y1: "))
        self.x2 = int(input("Valor de x2: "))
        self.y2 = int(input("Valor de y2: "))

    # declaracion para calcular la distancia
    def calcularDistancia(self):
        distancia = ((self.x2 - self.x1) ** 2 + (self.y2 - self.y1) ** 2) ** 0.5
        print("La distancia entre los dos puntos es: ", distancia)


def main():
    obj = Distancia()
    obj.usuario()
    obj.calcularDistancia()


if __name__ == "__main__":
    main()
