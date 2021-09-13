import rekins

def print_info():

    print('Programma rekina sagatavosanai')

def lietotaja_ievade():

    vards = input('ieraksta savu vardu: ')
    teksts = input('ieraksti savu tekstu:')
    garums = input('cik izmers kastisti velies')
    augstums = input('Cik augstums kastisti velies?')
    platums = input('Cik platu kastisti velies? (tikai veselie skaitli): ')
    kokmateriala_cena = input('Kokmateriala cena')
    return vards,teksts, platums, garums, augstums, kokmateriala_cena

if __name__ == '__main__':
    print_info()
    while 1>0:
       lietotaja_ievade()
       rekins = rekins.Rekins()
       run_again = input('Vai velies sagatavot rekinu velreiz? JAA - 1, NEE - 0')
