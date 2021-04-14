

class Receiver:
    sender = None
    SizeOfWindow = 0
    typeOfProtocol = 0
    typeOfCode = 0
    
    def __init__(self):
        pass

    def showResults(self): # wyswietlenie wyniku, liczby ramek, pozytywanie i negatywnie przeslanych i ponownie doslanych
        pass

    def setSender(self, sender): # podanie wartosci sendera do odsylania bledow i proszenia o poprawke
        self.sender = sender

    def receiverFrameStopAndWait(self, frame): # odebranie dla algorytmu stop and wait

        # zakłocenie ramki

        # wybor kodu ktory byl dodawany jaka powinna byc jego wartosc


        # porownanie naszej ramki
        # odpowiedznie czy ma byc ponowiona czy jest zaakceptowana 


        return false
        pass

    def receiverFrameGoBackN(self, frame): # odebranie dla algorytmu go back n
        pass

    def receiverFrameSelectiveReapeat(self, frame): # odebranie dla algorytmu selevtive reapeat
        pass

    def CodeParity(self, frame): # oblicza jaki jest kod bledu ktory dotarl
        countonebit = 0
        AddedCode = []
        for bit in frame:
            if bit == 1:
                countonebit += 1
        if countonebit % 2 == 0:
            AddedCode.append(0)
        else:
            AddedCode.append(1)
        return AddedCode
    
    def CodeMirroring(self, frame): # oblicza jaki jest kod bledu ktory dotarl
        AddedCode = []
        for bits in frame:
            AddedCode.append(bits)
        return AddedCode

    def CodeCRC(self, frame): # oblicza jaki jest kod bledu ktory dotarl
        string = ' '
        for bits in frame:
            string += str(bits)
        hexs = int(zlib.crc32(bytes(string, 'utf-8')))
        hexsbin = format(hexs, "b")
        print(hexsbin)
        hexsstr = str(hexsbin)
        listhex = list(hexsstr)
        AddedCode = []
        for i in listhex:
            AddedCode.append(int(i)) 
        return AddedCode