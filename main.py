import rekins

def print_info():

    print('Invoicing program')

def lietotaja_ievade():

    name = input('Your Name: ')
    tekst = input('Your Tekst:')
    size = input('how much size box do you want:')
    height = input('How much height does the box want?:')
    width = input('How wide a box do you want? (integers only): ')
    material = input('material price')
    return name,tekst, width, height,material , size

if __name__ == '__main__':
    print_info()
    while True:
       lietotaja_ievade()
       restart = input('do you want again?').lower()
       if restart == "yes":
           print_info()
    else:
        exit()