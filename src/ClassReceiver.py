from numpy import random
import zlib # kod CRC32
import copy

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

    def generateNoise(self, framen, p): # generowanie szumu/zakłóceń
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

    def receiverFrameStopAndWait(self, framecome, propability): # odebranie dla algorytmu stop and wait
        print("Algorytm: ReceiverFrameStopAndWait")
        frame = []
        frame = copy.deepcopy(framecome)
        # dodawanie bledu przy transmisji
        self.generateNoise(frame, propability)


        # wybor kodu ktory byl dodawany jaka powinna byc jego wartosc
        codeToCompere = []
        if self.typeOfCode == 1:
            codeToCompere = self.CodeParity(frame[0:self.SizeOfWindow])

        if self.typeOfCode == 2:
            codeToCompere = self.CodeMirroring(frame[0:self.SizeOfWindow])

        if self.typeOfCode == 3: 
            codeToCompere = self.CodeCRC(frame[0:self.SizeOfWindow])

        # porownanie naszej ramki
        # odpowiedznie czy ma byc ponowiona czy jest zaakceptowana 
        # jesli jest zaakceptowana to true jesli nie to false
        print("Porównuje!")
        i = 0
        for bits in codeToCompere:
            index = self.SizeOfWindow + i
            if frame[index] != bits:
                return False
            i += 1
        return True

    def receiverFrameGoBackN(self, framecome, propability, framecounter): # odebranie dla algorytmu go back n
        print("Algorytm: ReceiverFrameGoBackN")
        # dla wszystkich ramek wez kopie i dodaj zagluszenie
        allFrame = []
        allFrame = copy.deepcopy(framecome)
        # dodawanie bledu przy transmisji
        for one in allFrame:
            self.generateNoise(one, propability)

        # wybor kodu ktory byl dodawany jaka powinna byc jego wartosc a nastepne okreslenie
        #  wartosc od ktorej nalezy jeszcze raz przeslac
        print("Porównuje!")
        j = framecounter
        for oneframe in allFrame:
            codeToCompere = []
            if self.typeOfCode == 1:
                codeToCompere = self.CodeParity(oneframe[0:self.SizeOfWindow])

            if self.typeOfCode == 2:
                codeToCompere = self.CodeMirroring(oneframe[0:self.SizeOfWindow])

            if self.typeOfCode == 3: 
                codeToCompere = self.CodeCRC(oneframe[0:self.SizeOfWindow])
            i = 0
            for bits in codeToCompere:
                index = self.SizeOfWindow + i
                if oneframe[index] != bits:
                    return j
                i += 1
            j += 1
        return j

    def receiverFrameSelectiveReapeat(self, framecome, propability, confirmSend): # odebranie dla algorytmu selevtive reapeat
        print("Algorytm: ReceiverFrameSelectiveReapeat")

        allFrame = []
        allFrame = copy.deepcopy(framecome)
        # dodawanie bledu przy transmisji
        for one in allFrame:
            self.generateNoise(one, propability)
        print("Po   : ", allFrame)
        j = 0
        for oneframe in allFrame:
            codeToCompere = []
            if self.typeOfCode == 1:
                codeToCompere = self.CodeParity(oneframe[0:self.SizeOfWindow])

            if self.typeOfCode == 2:
                codeToCompere = self.CodeMirroring(oneframe[0:self.SizeOfWindow])

            if self.typeOfCode == 3: 
                codeToCompere = self.CodeCRC(oneframe[0:self.SizeOfWindow])
            i = 0
            for bits in codeToCompere:
                index = self.SizeOfWindow + i
                if oneframe[index] != bits:
                    confirmSend[j] = -1
                    continue
                i += 1
            j += 1

    def CodeParity(self, frame): # oblicza jaki jest kod bledu ktory dotarl
        # print("frame", frame)
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
        hexsstr = str(hexsbin)
        listhex = list(hexsstr)
        AddedCode = []
        for i in listhex:
            AddedCode.append(int(i)) 
        return AddedCode