exit_choice="nothing"
while exit_choice !="EXIT":
    intentos=5
    contraseña="desactivar"
    print("Te acabas de encontrar una bomba en tu casa")
    print("Explotará a menos que pongas la contraseña correcta")
    print("Tienes cinco intentos")
    guess=input("Introduzca contraseña: ")
    while guess !=contraseña:
        print()
        print("Contraseña incorrecta")
        print()
        intentos=intentos-1
        print("Te quedan ",intentos," para la explosión")
        if intentos==0:
            break
        print()
        guess=input("Introduzca contraseña nuevamente, en minúsculas: ")
    if intentos==0:
        print("¡¡BOUUM!! MUERTO")
    else:
        print("Bomba desactivada")
    exit_choice=input("presiona return si deseas reiniciar o EXIT si deseas finalizar: ")
    

        
    

