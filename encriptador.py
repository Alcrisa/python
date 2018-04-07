alfabeto="ABCDEFGHIJKLMNÑOPQRSTUVWXYZ1234567890ABCDEFGHIJKLMNÑOPQRSTUVWXYZ1234567890"
print("Bienvenidos al encriptador Alcrisa")
print("Éste programa le ayudará a encriptar información textual valiosa")
user_choice="nothing"
while user_choice !="EXIT":
    original=input("Por favor, introduzca la palabra o frase a encriptar: ")
    original=original.upper()
    clave=int(input("Por favor, introduzca un número entero entre el 1 y el 36, y no lo olvide: "))
    if clave>36 or clave==0 or clave<-36:
        print("número no válido")
        print("Reinicie programa")
        break
    encriptada=""
    for currentcharacter in original:
        posicion=alfabeto.find(currentcharacter)
        nuevaposicion=posicion+clave
        if currentcharacter in alfabeto:
            encriptada=encriptada+alfabeto[nuevaposicion]
        else:
            encriptada=encriptada+currentcharacter
    print("La palabra o frase ya encriptada es: ", encriptada)
    print("Gracias por usar el encriptador Alcrisa, mi nombre es Alberto y os quiero a todos. ")
    print("Si desea desencriptar la información, introduzca la frase encriptada y la clave original con el signo opuesto delante.")
    user_choice=input("Para continuar encriptando o desencriptando pulse ENTER, para salir del programa teclee EXIT: ")
    



