import tkinter
import random
window=tkinter.Tk()
button1=tkinter.Button(window, text="Juego Castillo Ravenloft", width=80)
button1.pack(padx=20, pady=20)
button2=tkinter.Button(window, text="Leeme", width=80)
button2.pack(padx=20, pady=20)
button3=tkinter.Button(window, text="Bye Bye", width=80)
button3.pack(padx=20, pady=20)
def onClick_1(event):
    exitchoice="nothing"
    while exitchoice !="EXIT":
        print("Bienvenido al castillo Ravenloft, soy Alberto, el amo del calabozo. Te encuentras en una misteriosa y oscura habitación.")
        print("Delante de ti hay cuatro puertas numeradas de aspecto ominoso.")
        player_choice=input("Elige la 1, 2, 3 o 4: ")
        if player_choice=="1":
            print("¡¡Bingo!! Encontraste el tesoro del castillo Ravenloft. ¡¡Eres rico!!")
            print("¡¡Ganaste!! GAME OVER")
        elif player_choice=="2":
            print("Un terrible vampiro aparece y te ataca, drenándote toda la sangre del cuerpo.")
            print("¡¡Perdiste!! GAME OVER")
        elif player_choice=="3":
            print("Ves a un inmenso dragón dormido sobre un montón de oro.")
            print("Puedes elegir:")
            print("1)Intentar robar al dragón")
            print("2)Rodear al dragón y escapar por el otro lado.")
            dragon_choice=input("Teclea 1 o 2: ")
            if dragon_choice=="1":
                print("El dragón se despierta y te devora, estás delicioso.")
                print("Jodeté. GAME OVER")
            elif dragon_choice=="2":
                print("Silenciosamente, cruzas la estancia del dragón sin despertarlo, consiguiendo escapar.")
                print("¡¡Te salvaste!! Enhorabuena. GAME OVER")
            else:
                print("Mientras dudas como un gilipollas el dragón se despierta y te abrasa con su aliento")
                print("Perdiste por bobo. GAME OVER")
        elif player_choice=="4":
            print("Delante de ti aparece una terrible Esfinge.")
            print("La Esfinge te reta a un juego: Te pide que adivines en que número está pensando...entre el 1 y el 10.")
            print("Si aciertas podrás irte y te regalará una bolsa con diamantes, si fallas serás su esclavo sexual de por vida.")
            number=int(input("Teclea un número entre el 1 y el 10: "))
            if number==random.randint(1,10):
                print("La Esfinge se muestra muy contrariada, acertaste humano")
                print("Debo dejarte ir")
                print("La Esfinge te regala una bolsa de diamantes")
                print("¡¡Enhorabuena!! Ganaste. GAME OVER")
            else:
                print("La Esfinge sonrie de forma perversa, te equivocaste humano")
                print("Serás mi esclavo sexual para el resto de tu vida")
                print("¡¡Perdiste!! GAME OVER")
        else:
            print("No elegiste ninguna puerta...cobarde...que te den. GAME OVER")
        exitchoice=input("Para abandonar el juego teclea EXIT en mayúsculas, para continuar pulse enter: ")
def onClick_2(event):
    print("hola")
def onClick_3(event):
    exit(window)
button1.bind("<ButtonRelease>",onClick_1)
button2.bind("<ButtonRelease>",onClick_2)
button3.bind("<ButtonRelease>",onClick_3)
window.mainloop()

