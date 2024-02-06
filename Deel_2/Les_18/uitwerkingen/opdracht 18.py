import random

def is_geldig_gokgetal(gok, min_waarde, max_waarde):
    return min_waarde <= gok <= max_waarde

min_waarde = 1
max_waarde = 100

te_raden_getal = random.randint(min_waarde, max_waarde)

pogingen = 0

while True:
    print("Raad het getal tussen {} en {}: ".format(min_waarde, max_waarde))
    gok = int(input())
    
    if is_geldig_gokgetal(gok, min_waarde, max_waarde):
        pogingen += 1
        
        if gok == te_raden_getal:
            print("Gefeliciteerd! Je hebt het juiste getal geraden in {} pogingen.".format(pogingen))
            break
        elif gok < te_raden_getal:
            print("Probeer een hoger getal.")
        else:
            print("Probeer een lager getal.")
    else:
        print("Ongeldige gok. Probeer opnieuw.")




