from Generator import generateBit
import zlib # kod CRC32
import copy
import time

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
        startTime = time.time()
        print("Algorytm: SendFrameStopAndWait")

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

        # wysylanie ramek po koleji     
        # sizeOfFrames
        i = 0
        j = 0
        for lists in listOfFrames:
            while True:
                result = self.receiver.receiverFrameStopAndWait(lists, masterlist.propability)
                masterlist.ReceivedBits += self.SizeOfWindow # wszyskie bity
                if result == True:
                    i += 1
                    masterlist.E += self.SizeOfWindow # przeslane bity z powodzeniem
                    break
                masterlist.BER += self.SizeOfWindow # przeklamane bity
                j += 1
        masterlist.time = round(time.time() - startTime, 6)

        print("Szybkie wyniki: ")    
        print("Dobrze przeslane ramki: ", i)
        print("Żle przeslane ramki: ", j)
        print("Wszyskie przeslane ramki: ", i+j)
        print("masterlist.E: ", masterlist.E)
        print("masterlist.BER: ", masterlist.BER)
        print("masterlist.ReceivedBits: ", masterlist.ReceivedBits)
        print("Czas : ", masterlist.time)

    def sendFrameGoBackN(self, masterlist): # wysylanie ramki za pomoca algorytmu go back n
        startTime = time.time()
        print("Algorytm: SendFrameGoBackN")

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

        # wysylanie wszystkich ramek 
        result = 0
        i = 0
        j = 0
        framecounter = 0
        while True:
            result = self.receiver.receiverFrameGoBackN(listOfFrames[framecounter:len(listOfFrames)], masterlist.propability, framecounter )
            masterlist.ReceivedBits += self.SizeOfWindow # wszyskie bity

            if framecounter != result:
                masterlist.E += self.SizeOfWindow # przeslane bity z powodzeniem
                i += result-framecounter
            if framecounter == result:
                masterlist.BER += self.SizeOfWindow # przeklamane bity
                j += 1
            framecounter = result
            if result == len(listOfFrames):
                break
        masterlist.time = round(time.time() - startTime, 6)

        print("Szybkie wyniki: ")    
        print("Dobrze przeslane ramki: ", i)
        print("Żle przeslane ramki: ", j)
        print("Wszyskie przeslane ramki: ", i+j)
        print("masterlist.E: ", masterlist.E)
        print("masterlist.BER: ", masterlist.BER)
        print("masterlist.ReceivedBits: ", masterlist.ReceivedBits)
        print("Czas : ", masterlist.time)


    def sendFrameSelectiveRepeat(self, masterlist): # wysylanie ramki za pomoca algorytmu selevtive reapeat
        startTime = time.time()
        print("Algorytm: SendFrameSelectiveRepeat")

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

        # wysylanie wszystkich ramek 
        confirmSend = []
        for i in listOfFrames:
            confirmSend.append(0)

        # pierwsze sprawdzenie
        i = 0
        j = 0
        while True:
            self.receiver.receiverFrameSelectiveReapeat(listOfFrames, masterlist.propability, confirmSend)
            # print("RAMKI@@@@@@@@@: ", confirmSend)
            index = None
            try:
                index = confirmSend.index(-1)
            except:
                pass
            if index == None:
                i += len(confirmSend)
                masterlist.E += self.SizeOfWindow # przeslane bity z powodzeniem
                masterlist.ReceivedBits += self.SizeOfWindow # wszyskie bity
                break
            else:
                templist = []
                tempsend = []
                k = 0
                for lists in listOfFrames:
                    if confirmSend[k] == -1:
                        j += 1
                        masterlist.BER += self.SizeOfWindow # przeklamane bity
                        masterlist.ReceivedBits += self.SizeOfWindow # wszyskie bity
                        templist.append(lists)
                    else:
                        masterlist.E += self.SizeOfWindow # przeslane bity z powodzeniem
                        masterlist.ReceivedBits += self.SizeOfWindow # wszyskie bity
                        i += 1
                    k += 1
                confirmSend = copy.deepcopy(tempsend)
                listOfFrames = copy.deepcopy(templist)
                for ni in listOfFrames:
                    confirmSend.append(0)
        masterlist.time = round(time.time() - startTime, 6)

        print("Szybkie wyniki: ")    
        print("Dobrze przeslane ramki: ", i)
        print("Żle przeslane ramki: ", j)
        print("Wszyskie przeslane ramki: ", i+j)
        print("masterlist.E: ", masterlist.E)
        print("masterlist.BER: ", masterlist.BER)
        print("masterlist.ReceivedBits: ", masterlist.ReceivedBits)
        print("Czas : ", masterlist.time)

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