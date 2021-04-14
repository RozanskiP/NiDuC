from Generator import generateBit
import zlib # kod CRC32

class Sender:
    receiver = None
    SizeOfWindow = 0
    typeOfProtocol = 0
    typeOfCode = 0

    def __init__(self, receiver):
        # generoweane danych rand, pozniej przerobic na wczytanie zdjecia ReadFromFile.py
        self.receiver = receiver
        pass

    def sendFrameStopAndWait(self, masterlist): # wysylanie ramki za pomoca algorytmu stop and wait
        print("Algorytm: sendFrameStopAndWait")

        print(masterlist.data)
        # maja byc pojedyncze ramki
        listOfFrames = self.splitToFrames(masterlist.data)
        print(listOfFrames)

        # pogrupuj w ramki i dodaj kod parzystosci dla kazdej
        if self.typeOfCode == 1:
            self.addCodeParity(listOfFrames)

        if self.typeOfCode == 2:
            self.addCodeMirroring(listOfFrames)

        if self.typeOfCode == 3: 
            self.addCodeCRC(listOfFrames)

        print(listOfFrames)


        # sizeOfFrames
        for list in  listOfFrames:
            receiver.receiverFrameStopAndWait()

        # tablica potwierdzonych ramek zrobic

        # podanie wartosci do odbieracza

        #wysylanie ramek po koleji

        pass

    def sendFrameGoBackN(self, masterlist): # wysylanie ramki za pomoca algorytmu go back n
        print("Algorytm: sendFrameGoBackN")
        pass

    def sendFrameSelectiveRepeat(self, masterlist): # wysylanie ramki za pomoca algorytmu selevtive reapeat
        print("Algorytm: sendFrameSelectiveRepeat")
        pass

    def splitToFrames(self, masterlist): # obcina ostatnie bity
        listOfFrames = []

        counter=0
        templist = []
        for bits in masterlist:
            counter += 1
            templist.append(bits)
            if counter == self.SizeOfWindow:
                listOfFrames.append(templist)
                templist=[]
                counter = 0
        return listOfFrames

    def addCodeParity(self, frames): # Kod parzystosci
        print("KOD PARZYSTOSCI!") # na koncu dodany jeden bit 
        for lists in frames:
            countonebit = 0
            for bit in lists:
                if bit == 1:
                    countonebit += 1
            if countonebit % 2 == 0:
                lists.append(0)
            else:
                lists.append(1)
    
    def addCodeMirroring(self, frames): # Kod dublowania
        print("KOD DUBLOWANIA") # 0101 00110011 na koncu 2 razy wiecej bitów
        for lists in frames:
            temp = []
            for bits in lists:
                temp.append(bits)

            for bits in temp:
                lists.append(bits)


    def addCodeCRC(self, frames): # Kod CRC na koncu 32 bity
        print("KOD CRC32")
        for lists in frames:
            string = ' '
            for bits in lists:
                string += str(bits)
            hexs = int(zlib.crc32(bytes(string, 'utf-8')))
            hexsbin = format(hexs, "b")
            hexsstr = str(hexsbin)
            listhex = list(hexsstr)
            listint = []
            for i in listhex:
                listint.append(int(i)) 
            for i in listint:
                lists.append(i)