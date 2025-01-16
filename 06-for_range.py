range(20) 
x = range(10,20)
x = range(10,20,2)
for i in range(20):
    print(i)


    '''usando el ciclo for hacer que el usuario ingrese el numero de la tabla de multiplicar e imprima la tablas de multiplicar''' 

    numeroApedir = int(input("Ingrese el numero de la tabla que desea ver: "))
    for i in range(1,11):
        print(numeroApedir, "x", i, "=", numeroApedir*i)