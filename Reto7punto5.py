x = 1 #Esta variable va a permitir multiplicar cada uno de numeros anteriores al numero "n"
factorial= 1 #Esta variable se va a multiplicar con cada numero anterior al numero "n" y va a tomar ese valor
n = int(input("Ingrese un numero natural para factorizarlo: ")) #Es el numero al que se le va a sacar el factorial

#Bucle en el que "factorial" se multiplicara con cada numero anterior a "n" siempre y cuando "x" sea menor o igual a "n"
while x <= n:
    factorial *= x
    x += 1

print("El factorial de " + str(n) + " es " + str(factorial))    