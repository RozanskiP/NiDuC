from ClassSender import Sender
from ClassReceiver import Receiver
from MasterList import MasterList

from Coder import coderBit
from Decoder import decodeBit
from Generator import generateBit

from ImageFormating import ImgToBitArr
from ImageFormating import BitArrToImg
from ImageFormating import ShowResultImage
# from Plotter import ShowPlot

DataList = []

def main(Protocol_ID ,Code_ID, Probability ,WindowSize ,Photo):
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


    WinSizeList = [2, 4, 8 , 16, 33]
    SizeOfWindow = WinSizeList[WindowSize]
    chosenProtocol = Protocol_ID
    chosenCode = Code_ID
    ProbabilityList = [1.0, 0.99 , 0.98 , 0.97, 0.96, 0.50]
    propability = ProbabilityList[Probability]
    #propability = 0.90

    receiver.typeOfCode = chosenCode
    receiver.typeOfProtocol = chosenProtocol
    sender.typeOfCode = chosenCode
    sender.typeOfProtocol = chosenProtocol

    # tutaj bedzie zdjęcie ładowane
    Frames = []
    SizeOfData = 8192 # zmienic na wczytywanie danych ze zdjecia
    SizeOfData = 256 # do testowania mniejsza ilosc

    #mozna by wywalic if i elif jesli generacje bitów byłaby przed main()
    #a sama lista bitów wchodziła do maina(BitList, Protocol_ID ,Code_ID, Probability ,Photo) jako argument
    #wtedy tez wybór zdjecia byłby przed mainem a nie w mainie ale to chyba nie robi roznicy
    #komentarze usunac po zrobienniu decyzji
    FileName = r"FLAGA4.jpg"
    if Photo == 0:
        generateBit(Frames, SizeOfData)

    elif Photo == 1:
        Frames = ImgToBitArr(FileName)

    # zainicjalozowanie wartosci do glownego zbiornika na dane
    BER = 0
    E = 0
    ReceivedBits = 0
    time = 0

    masterlist = MasterList(Frames, BER, E, ReceivedBits, SizeOfWindow, chosenProtocol, chosenCode, propability, time)

    receiver.SizeOfWindow = SizeOfWindow
    sender.SizeOfWindow = SizeOfWindow
    if chosenProtocol == 1:
        sender.sendFrameStopAndWait(masterlist)

    if chosenProtocol == 2:
        sender.sendFrameGoBackN(masterlist)


    if chosenProtocol == 3:
        sender.sendFrameSelectiveRepeat(masterlist)

    if Photo == 0:
        DataList.append(masterlist) 

    elif Photo == 1:
        BitArrToImg("Result.jpg", masterlist.data)
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
    #main(1,3,3,0) #tak by wygladał main który zastałem przed edycją
    for WinSize in range(2): #Długosc ramki/okna
        for pr in range(1,4): #protokół
            for c in range(1,4): #Kod
                for p in range(2): #Prawdopodobienstwo
                   main(pr,c,p,WinSize,0)
                   pass

    # main(1,1,5,4,1) #Mielenie zdjecia
    # ShowResultImage() #Pokazanie zdjecia po "Mielonce"

    #ShowPlot(DataList)  #!!!! odpalac tylko jesli main jest W forach lub jest pojedynczy

    #powstaje error przy gaszeniu okna z wykresami bo niby jak okno sie odpali z innego modułu niż tym gdzie jest __main__ (chyba)
    #Fix przyjdzie szybko
    