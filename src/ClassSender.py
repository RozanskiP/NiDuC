from Generator import generateBit
import zlib # kod CRC32

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
        
        print(data)
        self.addCodeMirroring(data)
        print(data)


        # pogrupuj w ramki i dodaj kod parzystosci dla kazdej

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
        print("KOD PARZYSTOSCI!")

        countonebit = 0
        for bit in frame:
            if bit == 1:
                countonebit += 1
        if countonebit % 2 == 0:
            frame.append(0)
        else:
            frame.append(1)
    
    def addCodeMirroring(self, frame): # Kod dublowania
        print("KOD DUBLOWANIA")
        temp = []
        for bits in frame:
            temp.append(bits)

        for bits in temp:
            frame.append(bits)

        pass

    def addCodeCRC(self, frame): # Kod CRC
        print("KOD CRC32")
        string = ' '
        for bits in frame:
            string += str(bits)
        hexs = hex(zlib.crc32(bytes(string, 'utf-8')))
        frame.append(hexs)