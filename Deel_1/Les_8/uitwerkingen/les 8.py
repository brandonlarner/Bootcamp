
cijfer = float(input("Voer een cijfer tussen 1 en 10 in: "))

if 1 <= cijfer <= 10:

    omschrijvingen = {
        10: "uitmuntend",
        9: "zeer goed",
        8: "goed",
        7: "ruim voldoende",
        6: "voldoende",
        5: "bijna voldoende",
        4: "onvoldoende",
        3: "gering",
        2: "slecht",
        1: "zeer slecht",
    }


    omschrijving = omschrijvingen[cijfer]

    if cijfer >= 6:
        print(f"Gefeliciteerd, {omschrijving} je resultaat is een {cijfer}")
    else:
        print(f"Jammer, {omschrijving} je resultaat is een {cijfer}")
else:
    print("Dit kan ik niet omzetten!")
