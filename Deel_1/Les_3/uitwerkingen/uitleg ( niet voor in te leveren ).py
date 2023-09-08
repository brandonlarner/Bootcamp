naam = input ('hoe heet je')
leeftijd = input ('Dag ' + naam + ' wat is je leeftijd?') # verschil is van type int

verschil= int(leeftijd) - 18 

print ('dag ' + naam + ' je bent ' + str(verschil) + ' jaar ouder dan 18!')

if verschil < 2: # is een conditie waar of niet waar -> true or false
    print('vraag om legitimatie')

# built in functies (bif)
# print() -> stuurt een sting naar de CLI (command line)
# input() -> vraagt een string aan de gebruiker
# int() -> stop er een string in en krijgt een int
# str() -> stop er een int of float in en krijg een string
# float() -> stop er eem string in en krijg een float
# int = een geheel getal
# string = zin of word
# float = kommagetal
