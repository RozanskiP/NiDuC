from Generator import generateBit

class Sender:
    receiver = None
    WindowOfWindow = 100
    typeOfProtocol = 0
    typeOfCode = 0


    def __init__(self, receiver):
        # generoweane danych rand, pozniej przerobic na wczytanie zdjecia ReadFromFile.py
        self.receiver = receiver
        pass

    def sendFrameStopAndWait(self, data): # wysylanie ramki za pomoca algorytmu stop and wait
        print("Algorytm: sendFrameStopAndWait")
        
        

        # pogrupuj w ramki i dodaj kod parzystosci

        # sizeOfFrames

        # tablica potwierdzonych ramek zrobic

        # podanie wartosci do odbieracza

        #wysylanie ramek po koleji
        


        pass

    def sendFrameGoBackN(self, data): # wysylanie ramki za pomoca algorytmu go back n
        print("Algorytm: sendFrameGoBackN")
        pass

    def sendFrameSelectiveRepeat(self, data): # wysylanie ramki za pomoca algorytmu selevtive reapeat
        print("Algorytm: sendFrameSelectiveRepeat")
        pass

    def addCodeParity(self, frame): # Kod parzystosci 
        pass
    
    def addCodeMirroring(self, frame): # Kod dublowania
        pass

    def addCodeCRC(self, frame): # Kod CRC
        pass