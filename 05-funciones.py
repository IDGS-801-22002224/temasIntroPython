import os

def function1():
    os.system('cls')
    num1 = int(input('numero1: '))
    num2 = int(input('numero2: '))
    res= num1 + num2
    print ('Resultado: ', res)
    input()


def function2():
    os.system('cls')
    num1 = int(input('numero1: '))
    num2 = int(input('numero2: '))
    res= num1 - num2
    print ('Resultado: ', res) 
    input()

def function3():
    os.system('cls')
    num1 = int(input('numero1: '))
    num2 = int(input('numero2: '))
    res= num1 * num2
    print ('Resultado: ', res)
    input()

def function4():
    os.system('cls')
    num1 = int(input('numero1: '))
    num2 = int(input('numero2: '))
    res= num1 / num2
    print ('Resultado: ', res)
    input()

def run():
    os.system('cls')    
    print('1.- Suma')
    print('2.- Resta')
    print('3.- Multiplicacion')
    print('4.- Division')
    op = int (input('Opcion:'))
    while op <1 or op >5:
        op = int (input('Elija una opcion:'))
    if op == 1:
        function1()
    elif op == 2:
        function2()
    elif op == 3:
        function3()
    elif op == 4:
        function4()
    else:
        print('Valor incorrecto')
        input()
    run()
            
if __name__ == "__main__":
    run()   