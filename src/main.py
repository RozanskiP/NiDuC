from ClassSender import Sender
from ClassReceiver import Receiver

from Coder import coderBit
from TransmisionCannal import transmision
from Decoder import decodeBit
from Generator import generateBit

def main():
    receiver = Receiver()
    sender = Sender(receiver)
    receiver.setSender(sender)


    Frames = []
    SizeOfData = 4
    generateBit(Frames, SizeOfData)
    sender.sendFrameStopAndWait(Frames)

    # print("Program do analizy alogorytmu ARQ")
    # sender.SizeOfWindow = int(input("Podaj wielkosc ramki: "))
    # print("Size: ", sender.SizeOfWindow )


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

    # receiver.typeOfCode = chosenCode
    # receiver.typeOfProtocol = chosenProtocol
    # sender.typeOfCode = chosenCode
    # sender.typeOfProtocol = chosenProtocol

    # Frames = []
    # SizeOfData = 8192 # zmienic na wczytywanie danych ze zdjecia
    # SizeOfData = 100
    # generateBit(Frames, SizeOfData)
    # print(Frames)


    # if chosenProtocol == 1:
    #     sender.sendFrameStopAndWait(Frames)
        

    # if chosenProtocol == 2:
    #     sender.sendFrameGoBackN(Frames)


    # if chosenProtocol == 3:
    #     sender.sendFrameSelectiveRepeat(Frames)


    # print(bits)
    # # listofbits = coderBit(bits, n)                                                     
    # print("List of list: ")
    # print(listofbits)

    # transmision(listofbits, 0.3) # minimalnie 0.001 (1 promil) im mniej tym bardziej zmienia
    # print(listofbits)

    # decodeBit(listofbits, n)

if __name__ == "__main__":
    main()
