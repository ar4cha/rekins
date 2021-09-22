import rekins

def print_info():

    print('Invoicing program')

def lietotaja_ievade():
    print("\033[94m{}\033[0m".format("A bill is proposed legislation under consideration by a legislature.\n "
                                     "A bill does not become law until it is passed by the legislature and, in most cases, approved by the executive."))
    name = input('Your Name: ')
    tekst = input('Your Tekst:')
    height = float(input('How much height does the box want?:'))
    width = float(input('How wide a box do you want? (integers only): '))
    material = float(input('material price'))
    length = float(input('How much length does the box want?'))

    darba_samaksa = 15
    PVN = 21

    produkta_cena = width/100.0 * length/100*height/100/3*material
    PVN_summa = produkta_cena + darba_samaksa * PVN / 100
    rekina_summa = produkta_cena + darba_samaksa + PVN_summa

    putin = [format(produkta_cena),format(PVN_summa),format(rekina_summa),format(name),format(tekst)]

    f = open("rekins.txt", "w")
    f.write("Your name:" + format(name))
    f.write("\n")
    f.write("Your Tekst: " + format(tekst))
    f.write("\n")
    f.write("Produkta cena: " + format(produkta_cena, ",.2f") + "€")
    f.write("\n")
    f.write("PVN summa: " + format(PVN_summa, ",.2f")+ "€")
    f.write("\n")
    f.write("rekina_summa: " + format(rekina_summa, ",.2f")+ "€")
    f.close()

    print("Produkta cena: €" + format(produkta_cena, ",.2f"))
    print("PVN summa: €" + format(PVN_summa, ",.2f"))
    print("rekina_summa: €" + format(rekina_summa, ",.2f"))

from datetime import date

today = date.today()
print("Today's date:", today)

if __name__ == '__main__':
    print_info()
    while True:
       lietotaja_ievade()
       restart = input('do you want again?').lower()
       if restart == "yes":
           print_info()
       else:
           break
