kleuren_Tuple = ('rood, geel, blauw, groen')

naam = input ('wat is je naam')
favoriete_Kleur = input ('wat is je favoriete kleur? ')

if favoriete_Kleur.lower() in kleuren_Tuple:
    print (f'{naam}, de kleur {favoriete_Kleur} staat in de kleuren tuple!')
else: 
    print ('deze kleur is niet zo geweldig!')