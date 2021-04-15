from ClassSender import Sender
from ClassReceiver import Receiver
from MasterList import MasterList

from Generator import generateBit

def main():
    receiver = Receiver()
    sender = Sender(receiver)
    receiver.setSender(sender)

    # print("Program do analizy alogorytmu ARQ")
    # SizeOfWindow = int(input("Podaj wielkosc ramki: "))
    # print("Size: ", SizeOfWindow )


    # print("Podaj typ protokołu do przesyłania danych: ")
    # print("1 <- Stop and Wait")
    # print("2 <- Go Back N")
    # print("3 <- Selective Repeat")
    # chosenProtocol = int(input(">>> "))

    # print("Podaj sposob kodowania do przesyłania danych: ")
    # print("1 <- Kod Parzystosci")
    # print("2 <- Kod Dublowania")
    # print("3 <- Kod CRC32")
    # chosenCode = int(input(">>> "))

    # print("Podaj prawdopodobienstwo przeklamac bitów w promilach: ")
    # propability = float(input(">>> "))
    SizeOfWindow = 9
    chosenProtocol = 3
    chosenCode = 1
    propability = 0.90

    receiver.typeOfCode = chosenCode
    receiver.typeOfProtocol = chosenProtocol
    sender.typeOfCode = chosenCode
    sender.typeOfProtocol = chosenProtocol

    # tutaj bedzie zdjęcie ładowane
    Frames = []
    SizeOfData = 8192 # zmienic na wczytywanie danych ze zdjecia
    SizeOfData = 100 # do testowania mniejsza ilosc
    generateBit(Frames, SizeOfData)

    # zainicjalozowanie wartosci do glownego zbiornika na dane
    BER = 0
    E = 0
    ReceivedBits = 0 

    masterlist = MasterList(Frames, BER, E, ReceivedBits, SizeOfWindow, chosenProtocol, chosenCode, propability)

    receiver.SizeOfWindow = SizeOfWindow
    sender.SizeOfWindow = SizeOfWindow

    if chosenProtocol == 1:
        sender.sendFrameStopAndWait(masterlist)
        

    if chosenProtocol == 2:
        sender.sendFrameGoBackN(masterlist)


    if chosenProtocol == 3:
        sender.sendFrameSelectiveRepeat(masterlist)


    # Szybkie testowanie 
    # Frames = []
    # SizeOfData = 4
    # generateBit(Frames, SizeOfData)
    # sender.sendFrameStopAndWait(Frames)

    # print(bits)
    # # listofbits = coderBit(bits, n)                                                     
    # print("List of list: ")
    # print(listofbits)

    # transmision(listofbits, 0.3) # minimalnie 0.001 (1 promil) im mniej tym bardziej zmienia
    # print(listofbits)

    # decodeBit(listofbits, n)

if __name__ == "__main__":
    main()
