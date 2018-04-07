hombre=["Mecánico", "Enfermero", "Gigoló", "Butanero"]
mujer=["Médico", "Empresaria", "Frutera", "Ama de casa"]
lugar=["Apartamento", "Hospital", "Supermercado", "Despacho"]
hombre_dice=["Ahora mismo señorita", "Con placer mi ama", "Así me gusta", "¿La meto dentro?"]
mujer_dice=["Metemelá dentro", "Pongamé esa gran inyección", "¿Le gustan así de gordas?", "Hagamé ese trabajito"]
consecuencia=["Brutal sex", "En el culete", "Trabajo hecho"]
import random
player_choice="Nothing"
while player_choice !="EXIT":
        print()
        print(random.choice(hombre), "se encuentra con una", random.choice(mujer), "en el", random.choice(lugar))
        print("Ella dice: ", random.choice(mujer_dice))
        print("El contesta: ", random.choice(hombre_dice))
        print(random.choice(consecuencia))
        print()
        player_choice=input ("presiona enter para jugar de nuevo, EXIT para salir: ")
       
        

    
