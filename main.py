import rekins

def print_info():

    print('Programma rekina sagatavosanai')

def lietotaja_ievade():

    vards = input('ieraksta savu vardu: ')
    teksts = input('ieraksti savu tekstu:')
    garums = input('cik izmers kastisti velies')
    augstums = input('Cik augstums kastisti velies?')
    platums = input('Cik platu kastisti velies? (tikai veselie skaitli): ')
    materiala = input('materiala cena')
    return vards,teksts, platums, garums, augstums, materiala

if __name__ == '__main__':
    print_info()
    while True:
       lietotaja_ievade()
       run_again = input('tu gribi velreiz? JA-1, NE-0 :')
       if run_again == 1:
           continue
       else:
           exit(0)