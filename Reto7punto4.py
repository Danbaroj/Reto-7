pais_a = 25000000 #Cantidad país A
pais_b = 18900000 #Cantidad país B
año = 2023

#Bucle encargado de aumentar la tasa de crecimiento anual de la población tras cada año, con lo cual el bucle terminará hasta que
#el país B superé al país A

while pais_b < pais_a: 
    pais_b *= 1.03
    pais_a *= 1.02
    año += 1

print("En el año " + str(año) + " el pais B superara a el pais A ")