#un programa que realice un triangulo de numeros segun el numero ingresado.
n = int(input("Numero:"))
if n < 1:
    print("Error: numero debe de ser mayor a 0")  
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j , end=" ")
    print("")
