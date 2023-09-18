naam = input ('wat is je naam?')
leeftijd_in_jaren = (input)(f'{naam} wat is je leeftijd in jaren?')
paspoort = input('heeft u een paspoort? (ja/nee)')
rijbewijs = input('heeft u een rijbewijs? (ja/nee)')


if rijbewijs == 'ja' and paspoort == 'ja':
    print('u mag met de auto naar engeland!')
elif paspoort == 'ja':
    print('u mag naar engeland zonder auto!')
else:
    print('u mag engeland niet in!')
    # X = 1
# while X <= 10:
#     print(X)
#     X += 1 


    
