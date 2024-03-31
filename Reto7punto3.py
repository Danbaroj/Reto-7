numero_incial = 1000 #Numero donde se empezará a descender por los numeros pares hasta llegar a 2 
numero_n = int(input("Ingrese un numero naturar menor o igual a 2: ")) #Numero natural n que limitara limitara los numeros pares

print ("Los siguientes numeros pares son menores al numero natural dado")

#Bucle que le restara 2 al numero inicial y omitirá todo los numeros que sean mayores al numero natural dado por la terminal

while numero_incial > 2:
    numero_incial -= 2
    if numero_incial > numero_n:
        continue
    print(numero_incial)

print ("Fin del listado")