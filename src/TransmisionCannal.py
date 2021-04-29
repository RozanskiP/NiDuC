from numpy import random

class Transmision:
    def __init__(self):
        pass

    def BSC(self, framen, p):
        # print("Generowanie zakłocen: ")
        i = 0
        for numbers in framen:
            temp = random.randint(1000)
            if temp >= p*1000: # w zależnosci od wartosci parametru prawdopodobienstwa
                if numbers == 1:
                    framen[i] = 0
                else:
                    framen[i] = 1
            i += 1

    def BEC(self, framen, p):
        # przyjmuje bit albo nie wie co zrobic i daje 0
        i = 0
        for numbers in framen:
            temp = random.randint(1000)
            if temp >= p*1000:
                framen[i] = 0
            i += 1

    def GilbertModel(self, framen, p):
        # raz zamienia tak a raz zamienia
        i = 0
        for numbers in framen:
            rand = random.randint(1000)
            if rand >= p:
                # stan D - wystąpienie błedu temp %
                temp = random.randint(1000)
                if temp >= p*1000: # w zależnosci od wartosci parametru prawdopodobienstwa
                    if numbers == 1:
                        framen[i] = 0
                    else:
                        framen[i] = 1
            else:
                # stan Z - wystąpienie błedu 100 %
                if numbers == 1:
                    framen[i] = 0
                else:
                    framen[i] = 1
            i += 1