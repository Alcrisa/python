import random
exit_choice="Nothing"
while exit_choice != "EXIT":
    print("¡¡Hola!! Mi nombre es Alberto, ¿que tal?")
    print("Vamos a jugar a piedra, papel o tijera")
    print("Si tenemos en cuenta que:")
    print("piedra=0")
    print("papel=1")
    print("tijera=2")
    player_choice=int(input("¿Que opción eliges?:la 0, la 1 ó la 2 : "))
    machine_choice=random.randint(0,2)
    if player_choice==machine_choice:
        print("Yo tambien, empate")
        print("Prueba de nuevo")
    elif player_choice==0 and machine_choice==2:
        print("Yo tijera. ¡¡Tu ganas!!")
        print("Prueba de nuevo")
    elif player_choice==0 and machine_choice==1:
        print("Yo papel. Pierdes")
        print("Prueba de nuevo")
    elif player_choice==1 and machine_choice==2:
        print("Yo tijera. Pierdes")
        print("Prueba de nuevo")
    elif player_choice==1 and machine_choice==0:
        print("Yo piedra. ¡¡Tu ganas!!")
        print("Prueba de nuevo")
    elif player_choice==2 and machine_choice==1:
        print("Yo papel. ¡¡Tu ganas!!")
        print("Prueba de nuevo")
    elif player_choice==2 and machine_choice==0:
        print("Yo piedra. Pierdes")
        print("Prueba de nuevo")
    else:
        print("opción no válida")
        print("Prueba de nuevo")
    exit_choice=input("Presiona enter para continuar jugando. Teclea EXIT para salir ")
    
