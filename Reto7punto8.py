#Esta funcion se encarga de definir si los numeros entregados son numeros primos, devuelve un "True" si el numero es primo y un "False"
#si es lo contrario

def primo(numero):

    if numero <= 1:
        return False
    divisor = 2

#El bucle de la función se va a encargar de ver si los numeros son divisibles por la variable "divisor" (siendo que esta va a tomar 
#varios valores mientras que la potencia del "divisor" sea menor o igual al número que se busca saber si es primo), con el fin de 
#saber si el número es divisible, lo que quiere decir que el número no es primo devolviendo el resultado como "False", de lo 
#contrario si no es divisible por ningún número significa que es primo y devolvera el resultado como "True"

    while (divisor **2) <= numero:
        if numero % divisor == 0:
            return False
        divisor += 1
    return True

#Esta función se encargará de mostrar todos los numeros hasta un numero cualquiera dado, en este caso se limitará hasta 100 

def limite_primos(n):

    print("Números primos del 1 al " + str(n))
    
#El siguiente bucle se encargará de verificar si, a partir de la variable "num" si el número es primo usando la primera función,
#si identifica que el número es primo lo imprimirá. Además incrementará en 1 el número hasta llegar a 100.
    
    num = 2
    while num <= n:
        if primo(num):
            print(num)
        num += 1


limite_primos(100) #Limita los primos mostrados hasta 100