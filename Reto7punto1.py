numero_inicial = 1 #Primer numero del listado
cuadrado_num_inicial = numero_inicial **2 # Formula para sacarle el cuadrado a cada numero

#El "while" en este caso permitirá continuar con el bucle siempre que el numero inicial sea menor o igual a 100
#Ademas se encargará de sumar 1 al numero inicial y asi pasar por cada numero hasta llegar al 100

while numero_inicial <= 100:
    print(str(numero_inicial) + " su cuadrado es " + str(cuadrado_num_inicial))  
    numero_inicial += 1 
    cuadrado_num_inicial = numero_inicial **2 

print("fin")