print ("Elije un numero entre 1 y 100.")

#Se define el valor de igual como "False" por defecto para que cuando se tome que igual es verdadero este finalice el bucle

Igual = False 

#Bucle hecho a punta de condicionales, que van preguntando si un numero es mayor, menor o igual a un numero.
#El bucle se finalizara cuando la variable Igual sea equivalente a "True" que sera cuando la terminal pregunte si el numero es igual al que se busca que la maquina "adivine"/"acierte"

while not Igual :
    print ('Para responder las siguientes preguntas, responda con un "SI" o con un "NO" según corresponda con su número elegido')
    primer_igual = input('Su número es igual a 50?: ')

    if primer_igual == "SI":
        Igual = True
        print ("Su numero es: 50 ")

    else:
        mayor_mitad = input('Su número es mayor a 50?: ')
        if mayor_mitad == "SI":
            segundo_igual = input('Su número es igual a 75?: ')
            if segundo_igual == "SI":
                Igual = True
                print("Su numero es: 75")

            else:
                if segundo_igual == "NO":
                    mitad_mayor_mitad = input ('Su número es mayor a 75?: ')
                    if mitad_mayor_mitad == "SI":
                        tercer_igual = input('Su número es igual a 85?: ')
                        if tercer_igual == "SI":
                            Igual = True
                            print("Su numero es: 85")
                        
                        else:

                            mitad_mayor_mitad_mayor = input ('Su número es mayor a 85?: ') 
                            if mitad_mayor_mitad_mayor == "SI":
                                adivinar_primero= 86
                                while Igual == False and adivinar_primero <= 100 :
                                    adiv = input("Su número es igual a " + str(adivinar_primero) + "?: ")
                                    adivinar_primero += 1
                                    if adiv == "SI":
                                        adivinar_primero -=1 #Soltaba el numero que va despues, entonces se usa para corregir ese error (muy probablemente mio y no lo noto)
                                        print("Su número es: " + str(adivinar_primero))
                                        Igual = True

                            elif mitad_mayor_mitad_mayor == "NO":
                                    adivinar_segundo = 84
                                    while Igual == False and adivinar_segundo >= 76 :
                                        adiv_segundo = input("Su número es igual a " + str(adivinar_segundo)+ "?: ")
                                        adivinar_segundo -= 1
                                        if adiv_segundo == "SI":
                                            adivinar_segundo += 1 #Mismo caso al anterior (pone el numero anterior)
                                            print("Su número es: " + str(adivinar_segundo))
                                            Igual = True
                    else:
                        if mitad_mayor_mitad == "NO":
                            adivinar_tercero = 74
                            while Igual == False and adivinar_tercero >= 51 :
                                adiv_tercero = input("Su número es igual a " + str(adivinar_tercero) + "?: ")
                                adivinar_tercero -= 1
                                if adiv_tercero == "SI":
                                    adivinar_tercero +=1
                                    print("Su número es: " + str(adivinar_tercero))
                                    Igual = True
        
        else:
            if mayor_mitad == "NO":
                cuarto_igual = input ("Su número es igual a 25?: ")
                if cuarto_igual == "SI":
                    Igual = True
                    print("Su número es 25")
                
                else:
                    if cuarto_igual == "NO":
                        mitad_menor_mitad = input ("Su número es mayor a 25?: ")
                        if mitad_menor_mitad == "SI":
                            quinto_igual = input ("Su número es igual a 37?: ")
                            if quinto_igual == "SI":
                                Igual = True
                                print("Su número es 37")

                            else:

                                if quinto_igual == "NO":
                                    mitad_menor_mitad_mayor = input ("Su número es mayor a 37?: ")
                                    if mitad_menor_mitad_mayor == "SI":
                                        adivinar_cuarto = 38
                                        while Igual == False and adivinar_cuarto <= 49:
                                            adiv_cuarto= input("Su número es igual a " + str(adivinar_cuarto) + " ?: " )
                                            adivinar_cuarto += 1
                                            if adiv_cuarto == "SI":
                                                adivinar_cuarto -=1
                                                print("Su número es: " + str(adivinar_cuarto))
                                                Igual = True
                                    
                                    else:

                                        if mitad_menor_mitad_mayor == "NO":
                                            adivinar_quinto = 36
                                            while Igual == False and adivinar_quinto >= 26:
                                                adiv_quinto = input("Su número es igual a " + str(adivinar_quinto)+ " ?: ")
                                                adivinar_quinto -= 1
                                                if adiv_quinto == "SI":
                                                    adivinar_quinto += 1
                                                    print("Su número es: " + str(adivinar_quinto))
                                                    Igual = True
                    
                        else: 

                            if mitad_menor_mitad == "NO":
                                mitad_menor_mitad_menor = input("Su número es menor a 25?: ")
                                if mitad_menor_mitad_menor == "SI":
                                    sexto_igual = input("Su número es igual a 12?: ")
                                    if sexto_igual == "SI":
                                        Igual = True
                                        print("Su número es 12")

                                    else:

                                        if sexto_igual == "NO":
                                            mitad_menor_de_la_mitad = input("Su numero es mayor a 12?: ")
                                            if mitad_menor_de_la_mitad == "SI":
                                                adivinar_sexto = 13
                                                while Igual == False and adivinar_sexto <= 24:
                                                    adiv_sexto = input("Su número es igual a " + str(adivinar_sexto)+ " ?: ")
                                                    adivinar_sexto += 1
                                                    if adiv_sexto == "SI":
                                                        adivinar_sexto -= 1
                                                        print("Su número es: " + str(adivinar_sexto))
                                                        Igual = True
                                        
                                            else:
                                                if mitad_menor_de_la_mitad == "NO":
                                                    adivinar_sept = 12
                                                    while Igual == False and adivinar_sept >= 1:
                                                        adiv_sept = input("Su número es igual a " + str(adivinar_sept)+ " ?: ")
                                                        adivinar_sept -= 1 
                                                        if adiv_sept == "SI":
                                                            adivinar_sept += 1
                                                            print("Su número es: "+ str(adivinar_sept))
                                                            Igual = True
                                                    