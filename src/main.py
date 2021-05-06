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
    print("3 <- Kod SHA256")
    chosenCode = int(input(">>> "))

    print("Podaj prawdopodobienstwo przeklamac bitów w promilach: ")
    propability = float(input(">>> "))

    print("Podaj sposób transmisji danych: ")
    print("1 <- BSC")
    print("2 <- BEC")
    print("3 <- Model Gilberta")
    transmision_id = int(input(">>> "))

    
    # SizeOfData = 100
    # SizeOfWindow = 9
    # chosenProtocol = 3
    # chosenCode = 4
    # propability = 0.99
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
    