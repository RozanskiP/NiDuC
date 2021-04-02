from numpy import random

def transmision(listofbits, p):
    
    print("transmision: ")
    i = 0
    j = 0
    for list in listofbits:
        for numbers in list:
            temp = random.randint(1000)
            if temp >= p*1000: # w zależnosci od wartosci parametru prawdopodobienstwa
                if numbers == 0:
                    listofbits[i][j] = 1
                else:
                    listofbits[i][j] = 0
            j += 1
        j = 0
        i += 1