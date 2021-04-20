from ClassSender import Sender
from ClassReceiver import Receiver
from MasterList import MasterList

from Generator import generateBit

from ImageFormating import ImgToBitArr
from ImageFormating import BitArrToImg
from ImageFormating import ShowResultImage
# from Plotter import ShowPlot

DataList = []

def main(Protocol_ID ,Code_ID, Probability ,Photo):
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
    SizeOfWindow = 5
    chosenProtocol = 1
    chosenCode = 1
    propability = 0.99
    # chosenProtocol = Protocol_ID
    # chosenCode = Code_ID

    # ProbabilityList = [1.0, 0.99 , 0.95 , 0.90]
    # propability = ProbabilityList[Probability]
    #propability = 0.90

    receiver.typeOfCode = chosenCode
    receiver.typeOfProtocol = chosenProtocol
    sender.typeOfCode = chosenCode
    sender.typeOfProtocol = chosenProtocol

    # tutaj bedzie zdjęcie ładowane
    Frames = []
    SizeOfData = 8192 # zmienic na wczytywanie danych ze zdjecia
    SizeOfData = 100 # do testowania mniejsza ilosc
    generateBit(Frames, SizeOfData)

    #mozna by wywalic if i elif jesli generacje bitów byłaby przed main()
    #a sama lista bitów wchodziła do maina(BitList, Protocol_ID ,Code_ID, Probability ,Photo) jako argument
    #wtedy tez wybór zdjecia byłby przed mainem a nie w mainie ale to chyba nie robi roznicy
    #komentarze usunac po zrobienniu decyzji
    # if Photo == 0:
    #     generateBit(Frames, SizeOfData)

    # elif Photo == 1:
    #     Frames = ImgToBitArr(r"FLAGA.jpg")

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

if __name__ == "__main__":
    main(1,3,3,0) #tak by wygladał main który zastałem przed edycją
    # for pr in range(1,4): #protokół
    #     for c in range(1,4): #Kod
    #         for p in range(2):#Prawdopodobienstwo
            #    main(pr,c,p,0)
            #    pass
    #main(1,3,3,1) #Mielenie zdjecia
    #ShowResultImage() #Pokazanie zdjecia po "Mielonce"

    # ShowPlot(DataList)  #!!!! odpalac tylko jesli main jest W forach lub jest pojedynczy

    #powstaje error przy gaszeniu okna z wykresami bo niby jak okno sie odpali z innego modułu niż tym gdzie jest __main__ (chyba)
    #Fix przyjdzie szybko
    