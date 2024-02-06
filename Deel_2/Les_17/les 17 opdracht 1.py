from random import randint


te_raden_getal = randint(1,5)

geraden_getal = (input('kies een getal tussen de 1 en 5: '))

while geraden_getal != te_raden_getal:
    vraag = (input('wil je nog een keer raden?: '))
    if vraag in ['ja, j, yes']:
        
    
if te_raden_getal == geraden_getal:
    print('je hebt het getal goed geraden!')
else:
    print('je hebt het getal niet goed geraden, volgende keer beter!')

