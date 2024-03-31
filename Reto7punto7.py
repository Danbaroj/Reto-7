numero = int(input("Ingrese un numero de 2 a 50: "))
divisor = 50 #Variable desde donde se iniciará a revisar 

#Bucle en el que se dividira el numero dado en la terminal con los numeros del 2 al 50 (debido a que la variable "divisor" se ira restando 1 tras cada división) 
# y se obtendra el residuo que genera la división, en el que se imprimiran solo los numeros en el que su residuo sea igual a 0 
while divisor > 1  :
    if numero % divisor == 0 :
        print (divisor)

    divisor -= 1