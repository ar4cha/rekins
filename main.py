import rekins

def print_info():

    print('Invoicing program')

def lietotaja_ievade():
    print("\033[31m{}\033[0m".format("A bill is proposed legislation under consideration by a legislature.\n "
                                     "A bill does not become law until it is passed by the legislature and, in most cases, approved by the executive."))
    name = float( input('Your Name: ') )
    tekst = float(input('Your Tekst:') )
    size = float(input('how much size box do you want:'))
    height = float(input('How much height does the box want?:'))
    width = float(input('How wide a box do you want? (integers only): '))
    material = float(input('material price'))
    length = float(input('How much length does the box want?'))

    darba_samaksa = 15
    PVN = 21

    produkta_cena = tekst * 1.2 + width / 100 * length / 100 * height / 100 / 3 * material
    PVN_summa = produkta_cena + darba_samaksa * PVN / 100
    rekina_summa = produkta_cena + darba_samaksa + PVN_summa

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
