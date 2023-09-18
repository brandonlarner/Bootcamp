getallen = [13, 56, -54, 56, 12, -10 ]

delete_index = int(input('welke index verwijderen? '))

if delete_index > len(getallen):
    print('sorry er zijn maar',len(getallen),  'getallen')

else:
    getal = getallen.pop(delete_index)
    

print(getallen)

