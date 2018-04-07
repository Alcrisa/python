anglodiccionario={"yo": "I", "tu": "you", "querer": "want to", "follar": "fuck", "matar": "kill", "sobre": "on", "la": "the", "mesa": "table", "en": "in", "y": "and", "puta": "bitch", "comeme": "eat me", "el": "the", "polla": "dick", "coño": "pussy"}
exit_choice="nothing"
while exit_choice !="EXIT":
    hispafrase=input("Introduzca una palabra o frase en español: ")
    hispapalabra=hispafrase.lower().split()
    anglopalabra=[]
    for palabra in hispapalabra:
        if palabra in anglodiccionario:
            anglopalabra.append(anglodiccionario[palabra])
        else:
            anglopalabra.append(palabra)
    print("En inglés se dice: ", " ".join(anglopalabra))
    exit_choice=input("para continuar traducciendo pulse ENTER, para salir teclee EXIT: ")



