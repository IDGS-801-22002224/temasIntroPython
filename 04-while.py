'''
x = 0

while x<10:
    print(x)
    x = x + 1
'''
''' 
operacion de multiplicacion de a x b utilizando sumas 
    a= 3
    b= 4
    salida: 3+3+3+3=12

'''
a = 3
b = 4
x = 0
result = 0
while x < b:
    result = result + a
    if x < b-1:
        print(a, end="+")
    else:
        print(a, end="=")
    x = x + 1
print(result) 