from numpy import random

def transmision(framen, p):
    print("transmision: ")
    i = 0
    x = framen
    for numbers in framen:
        temp = random.randint(1000)
        if temp >= p*1000: # w zależnosci od wartosci parametru prawdopodobienstwa
            if numbers == 1:
                x[i] = 0
            else:
                x[i] = 1
        i += 1

    return x