import os

class CinecoVenta:
    nombre = ""
    personas = 0 
    precio_unico = 12.00
    boletos = 0
    total = 0
    tarjeta = False
    descuento_tarj = 0
    descuento = 0
    rtd = ""
    llamada = ""

    # Constructor
    def __init__(self, nombre="", acompanantes=0, boletos=0, total=0, tarjeta=False, descuento_tarj=0, descuento=0, rtd="", llamada=""):
        self.nombre = nombre
        self.acompanantes = acompanantes
        self.boletos = boletos
        self.total = total
        self.tarjeta = tarjeta
        self.descuento_tarj = descuento_tarj
        self.descuento = descuento
        self.rtd = rtd
        self.llamada = llamada

    # metodo para correr el programa
    def run(self):
        self.borrar_contenido_archivo()
        while True:
            os.system("cls")
            print("CINECO - MENU")
            print("1.- COMPRAR BOLETOS")
            print("2.- SALIR") 
            op = input("Opcion: ")

            if op == "1":
                self.nombres()
            elif op == "2":
                self.corte_caja()
                break
            else:
                print("INTENTE NUEVAMENTE.")
                input("Presione ENTER para continuar")

    def borrar_contenido_archivo(self):
        with open("boletos.txt", "w") as archivo:
            pass  

    def nombres(self):
        os.system("cls")
        self.nombre = input("NOMBRE DE LA PERSONA QUE VA A COMPRAR: ")
        self.pedir_personas()
        self.boleto()

    def pedir_personas(self):
        while True:
            self.personas = input("¿CUANTAS PERSONAS VAN CON USTED? (incluyendose): ")
            if self.personas.isdigit():
                self.personas = int(self.personas)
                if self.personas >= 1:
                    break
                else:
                    print("Debe haber al menos una persona.")
            else:
                print("INGRESE UN VALOR VALIDO.")

    # metodo para la cantidad de boletos y si tiene tarjeta cineco
    def boleto(self):
        os.system("cls")
        while True:
            limite_boletos = 7 * self.personas
            self.boletos = input(f"CUANTOS BOLETOS DESEA COMPRAR (máximo {limite_boletos}): ")
            if self.boletos.isdigit():
                self.boletos = int(self.boletos)
                if 1 <= self.boletos <= limite_boletos:
                    self.costo()
                    break
                else:
                    print(f"SOLO PUEDE COMPRAR ENTRE 1 Y {limite_boletos} BOLETOS.")
                    opcion = input("¿Desea cambiar el número de personas? (si/no): ").strip().lower()
                    if opcion == "si":
                        self.pedir_personas()
                    else:
                        print("No se puede comprar esa cantidad de boletos. Intente nuevamente.")
            else:
                print("INGRESE UN NUMERO VALIDO.")

    def metodo_pago(self):
        os.system("cls")
        while True:
            print("CINECO - MÉTODO DE PAGO")
            print("1.- Pagar con tarjeta Cineco")
            print("2.- Pagar con efectivo")
            op = input("Opcion: ")

            if op == "1":
                self.tarjeta = True
                self.descuento_tarj = self.total * 0.10
                self.total -= self.descuento_tarj
                break
            elif op == "2":
                self.tarjeta = False
                self.descuento_tarj = 0
                break
            else:
                print("OPCIÓN NO VÁLIDA. INTENTE NUEVAMENTE.")
                input("Presione ENTER para continuar")
        self.mostrar()

    def descuentos(self):
        if 3 <= self.boletos <= 5:
            self.descuento = self.total * 0.10
            self.total -= self.descuento
        elif self.boletos > 5:
            self.descuento = self.total * 0.15
            self.total -= self.descuento
        self.metodo_pago()

    # metodo para mostrar los datos y guardarlos
    def mostrar(self):
        os.system("cls")
        print(f"Nombre: {self.nombre} | Personas: {self.personas} | Boletos: {self.boletos} | Total a pagar: ${self.total:.2f}")
        self.guardar_venta() 
        input("Presiona enter para continuar")

    def costo(self):
        self.total = self.boletos * self.precio_unico
        self.descuentos()

    def guardar_venta(self):
        with open("boletos.txt", "a") as archivo:
            archivo.write(f"{self.nombre}\t{self.boletos}\t${self.total:.2f}\n")

    # metodo para registrar el corte de caja y escribir las ventas en el archivo
    def corte_caja(self):
        if not os.path.exists("boletos.txt"):
            print("POR EL MOMENTO NO HAY VENTAS.")
            return
        total_dia = 0.0
        
        with open("boletos.txt", "r") as archivo:
            lineas = archivo.readlines()
            for linea in lineas:
                if "---" not in linea:  
                    datos = linea.strip().split("\t")
                    if len(datos) >= 3:
                        total_venta = float(datos[2].replace("$", "").strip())
                        total_dia += total_venta
        
        with open("boletos.txt", "a") as archivo:
            archivo.write("\n--- CORTE DE CAJA ---\n")
            archivo.write(f"VENTAS DEL DIA: ${total_dia:.2f}\n")
            archivo.write("-" * 30 + "\n")
        
        print(f"\nCorte de caja registrado. Total del día: ${total_dia:.2f}")

if __name__ == "__main__":
    obj = CinecoVenta()
    obj.run()