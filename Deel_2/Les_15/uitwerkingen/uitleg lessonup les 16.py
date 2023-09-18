# leeftijd = 0

# while leeftijd == 0:
#         try:
#                 leeftijd = int(input('wat is je leeftijd?: '))
#         except ValueError:
#                 print('je moet wel een getal invoeren, probeer het nog eens')

# print(f'je leeftijd is {leeftijd}')




# leeftijd = int(input('wat is je leeftijd?: '))
# naam = input('wat is je naam: ')
# haarkleur = input('wat is je haarkleur?: ')

# if leeftijd == 16 and (naam == 'brandon' or haarkleur == 'rood'):
#     print('lekker bezig.')

# else:   
#     print('JAMMER')



def bereken_bedrag_inc(bedrag_ex):
    BTW = 1.21
    bedrag_incl = round(bedrag_ex * BTW, 2)
    return bedrag_incl

bedragen = (3.15, 2.43, 1.99)

for bedrag in bedragen:
    bedrag_in = bereken_bedrag_inc(bedrag)
    print(f'excl.: € {bedrag} incl.: € {bedrag_in}')








