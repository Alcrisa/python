import random
player_choice="nothing"
while player_choice != "EXIT":
    number=random.randint(1,10)
    adivinanza=int(input("Estoy pensando en un número entre el 1 y el 10...¿Cúal crees que es?: "))
    while adivinanza !=number:
        if adivinanza<number:
            print("Ese número es demasiado bajo")
        else:
            print("Ese número es demasiado alto")
        adivinanza=int(input("vuelve a intentarlo capullín: "))
    print("¡¡Enhorabuena!! Ése es el número correcto")
    player_choice=input("Pulsa enter para intertarlo otra vez o teclea EXIT en mayúsculas para salir: ")


