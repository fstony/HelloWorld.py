#un programa que realice un triangulo de numeros segun el numero ingresado.
num1 = int(input("Digite un numero entero:"))
if num1 < 1:
    print("Error: numero debe de ser mayor a 0")    
else:
    concatenado = ""
    for i in range (1,num1 +1):
     concatenado + str(i)+1 + ""
    print(concatenado)