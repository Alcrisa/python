exit_choice="nothing"
while exit_choice !="EXIT":
    zombies=2
    password="MARRANÁ"
    print("¡¡Alerta general!!, ¡¡Un virus zombie ha infectado Peñaranda!!")
    print("¡¡Necesitamos tu ayuda joven padawan, los zombies nos atacan!!")
    print("Espero que sepas el password para activar el sistema de defensa peñarandino")
    print()
    print("----------------------------------------------------")
    print("    BIENVENIDO AL SISTEMA DE DEFENSA PEÑARANDINO    ")
    print("----------------------------------------------------")
    guess=input("Introduzca password: ").upper()
    while guess !=password:
        print()
        print("PASSWORD INCORRECTO")
        print()
        zombies=zombies**2
        print("Hay",zombies,"zombies ahora en Peñaranda, ¡inténtalo otra vez! ¡Y ojo a la gramática!")
        if zombies>7400000000:
            break
        print()
        print("¡¡Esas cosas nos están machacando!!")
        print()
        guess=input("¡¡Por favor, vuelve a introducir el password del sistema de defensa!!: ").upper()
    if zombies>7400000000:
        print("Se acabó...Apocalipsis zombie")
    else:
        print("¡¡Victoria joder!! Nuesto semidios marraná ha exterminado a esas bestias inmundas")
    exit_choice=input("Presiona enter para jugar de nuevo, teclea EXIT para salir: ")
    

          
          


      
