from ClassSender import Sender
from ClassReceiver import Receiver
from MasterList import MasterList
from TransmisionCannal import Transmision

from Coder import coderBit
from Decoder import decodeBit
from Generator import generateBit

from ImageFormating import ImgToBitArr
from ImageFormating import BitArrToImg
from ImageFormating import ShowResultImage

def main():
    receiver = Receiver()
    sender = Sender(receiver)
    transmision = Transmision()
    receiver.setSender(sender, transmision)

    print("Program do analizy alogorytmu ARQ")

    SizeOfData = int(input("Podaj ilość danych: "))

    SizeOfWindow = int(input("Podaj wielkosc ramki: "))

    print("Podaj typ protokołu do przesyłania danych: ")
    print("1 <- Stop and Wait")
    print("2 <- Go Back N")
    print("3 <- Selective Repeat")
    chosenProtocol = int(input(">>> "))

    print("Podaj sposób kodowania do przesyłania danych: ")
    print("1 <- Kod Parzystosci")
    print("2 <- Kod Dublowania")
    print("3 <- Kod CRC32")
    print("4 <- Kod SHA256")
    chosenCode = int(input(">>> "))

    print("Podaj prawdopodobienstwo przeklamac bitów w promilach: ")
    propability = float(input(">>> "))

    print("Podaj sposób transmisji danych: ")
    print("1 <- BSC")
    print("2 <- BEC")
    print("3 <- Model Gilberta")
    transmision_id = int(input(">>> "))

    
    # SizeOfData = 1000
    # SizeOfWindow = 16
    # chosenProtocol = 2
    # chosenCode = 4
    # propability = 0.98
    # transmision_id = 3

    print("===================Zaczynam transmisje===================")

    receiver.typeOfCode = chosenCode
    receiver.typeOfProtocol = chosenProtocol
    receiver.typeOfTransmision = transmision_id
    sender.typeOfCode = chosenCode
    sender.typeOfProtocol = chosenProtocol

    # zainicjalozowanie wartosci do glownego zbiornika na dane
    Frames = []
    BER = 0
    E = 0
    ReceivedBits = 0
    time = 0

    generateBit(Frames, SizeOfData)

    masterlist = MasterList(Frames, BER, E, ReceivedBits, SizeOfWindow, chosenProtocol, chosenCode, propability, time, transmision_id)

    receiver.SizeOfWindow = SizeOfWindow
    sender.SizeOfWindow = SizeOfWindow
    if chosenProtocol == 1:
        sender.sendFrameStopAndWait(masterlist)

    if chosenProtocol == 2:
        sender.sendFrameGoBackN(masterlist)

    if chosenProtocol == 3:
        sender.sendFrameSelectiveRepeat(masterlist)

if __name__ == "__main__":
    main()

# Main którym były testowane programy
# def main(Protocol_ID ,Code_ID, Probability ,WindowSize ,Photo, Transmision_ID):
#     receiver = Receiver()
#     sender = Sender(receiver)
#     transmision = Transmision()
#     receiver.setSender(sender, transmision)

#     #WinSizeList = [2, 4, 8 , 16, 32, 64, 128 , 256]
#     WinSizeList = [32, 64, 128 , 256]
#     SizeOfWindow = WinSizeList[WindowSize]
#     chosenProtocol = Protocol_ID
#     chosenCode = Code_ID
#     ProbabilityList = [1.0, 0.99 , 0.98 , 0.97, 0.96, 0.95,0.94,0.93,0.92]
#     propability = ProbabilityList[Probability]
#     #propability = 0.90
#     Channel_Name =["NULL","BSC","BEC","Hilb"]
#     Protocol_Names = ["NULL", "Stop and wait", "Go back n","Selective Repeat"] 
#     Code_Names = ["NULL", "Kod parzystości", "Kod dublowania", "CRC32", "sha256"]
#     print(Channel_Name[trans]+" WinSize: "+str(WinSizeList[WindowSize])+" "+Protocol_Names[Protocol_ID]+" "+Code_Names[Code_ID]+" Prob: "+str(ProbabilityList[Probability]))

#     receiver.typeOfCode = chosenCode
#     receiver.typeOfProtocol = chosenProtocol
#     receiver.typeOfTransmision = Transmision_ID
#     sender.typeOfCode = chosenCode
#     sender.typeOfProtocol = chosenProtocol

#     # tutaj bedzie zdjęcie ładowane
#     Frames = []
#     SizeOfData = 8192 # zmienic na wczytywanie danych ze zdjecia
#     SizeOfData = 256 # do testowania mniejsza ilosc

#     #mozna by wywalic if i elif jesli generacje bitów byłaby przed main()
#     #a sama lista bitów wchodziła do maina(BitList, Protocol_ID ,Code_ID, Probability ,Photo) jako argument
#     #wtedy tez wybór zdjecia byłby przed mainem a nie w mainie ale to chyba nie robi roznicy
#     #komentarze usunac po zrobienniu decyzji
#     if Photo == 0:
#         generateBit(Frames, SizeOfData)

#     elif Photo == 1:
#         Frames = ImgToBitArr(FileName)

#     # zainicjalozowanie wartosci do glownego zbiornika na dane
#     BER = 0
#     E = 0
#     ReceivedBits = 0
#     time = 0

#     masterlist = MasterList(Frames, BER, E, ReceivedBits, SizeOfWindow, chosenProtocol, chosenCode, propability, time, Transmision_ID)

#     receiver.SizeOfWindow = SizeOfWindow
#     sender.SizeOfWindow = SizeOfWindow
#     if chosenProtocol == 1:
#         sender.sendFrameStopAndWait(masterlist)

#     if chosenProtocol == 2:
#         sender.sendFrameGoBackN(masterlist)

#     if chosenProtocol == 3:
#         sender.sendFrameSelectiveRepeat(masterlist)

#     if Photo == 0:
#         DataList.append(masterlist) 

#     elif Photo == 1:
#         BitArrToImg("Result.jpg", masterlist.data)

# if __name__ == "__main__":
#     print("Main started")
#     for trans in range(2,3):
#         for WinSize in range(2): #Długosc ramki/okna
#             for pr in range(1,4): #protokół
#                 for c in range(1,5): #Kod
#                     for p in range(2): #Prawdopodobienstwo
#                         main(pr,c,p,WinSize,0,trans)