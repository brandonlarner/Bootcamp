def get_integer(zin):
        while True:
                try:
                        getal = int(input(zin))
                        break
                except ValueError:
                        print("Let op! voer een getal in")
        return getal

def get_float(zin):
        while True:
                try:
                        getal = float(input(zin))
                        break
                except ValueError:
                        print('let op! voer een getal in!')
        return getal



        