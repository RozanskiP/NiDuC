from MasterList import MasterList
from matplotlib.pyplot import legend
import matplotlib.pyplot as plt
from math import floor
import matplotlib
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import matplotlib.ticker as mtick
from pathlib import Path
import time
#to do list
#horizontal image merge dla łaczenia zdjec przed i po 
#time
def VerticalImgMerge(im1 ,im2, ResultImgName): #master PNG
    Final = Image.new('RGB', (im1.width, im1.height + im2.height))
    Final.paste(im1, (0, 0))  
    Final.paste(im2, (0, im1.height))
    Final.save(ResultImgName)

def HorizontalImgMerge(im1, im2, ResultImgName): #potrzebne do zdjecia przed i po
    Final = Image.new('RGB', (im1.width + im2.width , im1.height))
    Final.paste(im1, (0, 0))  
    Final.paste(im2, (im1.width, 0))
    Final.save(ResultImgName)

def CreateMergedPhotoVert(FigNameList, ResultImage):
    if len(FigNameList) > 1: #łaczenie 
        for j in range(len(FigNameList)):
            if j == 1:
                im1 = FigNameList[j-1]
                im2 = FigNameList[j]
            elif(j > 1):
                im1 = Image.open(ResultImage)
                im2 = FigNameList[j]
            if j != 0:
                VerticalImgMerge(im1, im2, ResultImage)
                im1.close()
                im2.close()

def MergeImagesVert(FigNameList, TargetImage):
    if len(FigNameList) > 1:
        for j in range(len(FigNameList)):
            im1 = Image.open(TargetImage)
            im2 = FigNameList[j] #blad
            VerticalImgMerge(im1, im2, TargetImage)
            im1.close()
            im2.close()
    else:
        im1 = Image.open(TargetImage)
        im2 = Image.open(FigNameList[0])
        VerticalImgMerge(im1, im2, TargetImage)
        im1.close()
        im2.close()

def AddTextToImg(Content,TargetName, xPos, FontSize):
        im1 = Image.open(TargetName)
        im2 = Image.new('RGB', (2000, FontSize + 5), color = (255, 255, 255))
        fnt = ImageFont.truetype("arial.ttf", FontSize)

        d = ImageDraw.Draw(im2)
        d.text((xPos,0), Content, font=fnt, fill=(0,0,0))
        VerticalImgMerge(im1, im2, TargetName)

def DrawSubPlots(DataList, FigNameList ,WinSize_Amount ,nCol, nRow, BaseName, type, time ):
    Protocol_Names = ["NULL", "Stop and wait", "Go back n","Selective Repeat"] 
    Code_Names = ["NULL", "Kod parzystości", "Kod dublowania", "CRC32"]

    i=0

    if type >= 3 and type <= 5:
        WinSize_Amount = 1

    for WinSize in range(WinSize_Amount):        
        fig, axes = plt.subplots(ncols=nCol, nrows=nRow, figsize=(20,20))
        for ax in axes.flatten():
            if time == 0:
                ax.plot(DataList[i].propability, DataList[i].E, label="E")
                ax.plot(DataList[i].propability, DataList[i].BER,  label="BER")
                ax.set_ylabel('Współczynnik:')   
            elif time == 1:
                ax.plot(DataList[i].propability, DataList[i].time, label = "czas")
                ax.set_ylabel('Czas [s]:')   
            ax.legend()
            if type == 0:
                ax.set_title(Protocol_Names[DataList[i].typeOfProtocol] + " || " + Code_Names[DataList[i].typeOfCode] + " || " + "Długośc ramki "+ str(DataList[i].SizeOfWindow))
            if type == 1:
                ax.set_title("Srednie wartosci dla: " + Protocol_Names[DataList[i].typeOfProtocol] + " || " + "Długośc ramki "+ str(DataList[i].SizeOfWindow))
            if type == 2:
                ax.set_title("Srednie wartosci dla: " + Code_Names[DataList[i].typeOfCode] + " || " + "Długośc ramki "+ str(DataList[i].SizeOfWindow) )
            if type == 3:
                ax.set_title("Srednie wartosci dla: " + Protocol_Names[DataList[i].typeOfProtocol])
            if type == 4:
                ax.set_title("Srednie wartosci dla: " + Code_Names[DataList[i].typeOfCode])
            if type == 5:
                ax.set_title("Srednie wartosci dla: " + "Długośc ramki "+ str(DataList[i].SizeOfWindow) )
            ax.set_xlabel(r"Prawodopodobieństwo błedu [%]")
            i += 1
        plt.savefig(BaseName + str(WinSize) +".png")
        FigNameList.append(Image.open(BaseName + str(WinSize) +".png"))

def AverageFrom3Lists(List1, List2, List3): #potrzebne do srednich danych protokolow lub kodow dla ramki
    if 2*len(List1) != len(List2)+len(List3):
        return

    FinalList = []
    for i in range(len(List1)):
        FinalList.append((List1[i] + List2[i] +List3[i])/3)

    if len(FinalList) != len(List1):
        print("Critical failure AverageFromList() module: Plotter")

    return FinalList

def AverageFromList(List1):
    FinalList = []
    SubListLen = len(List1[0])
    ListLen = len(List1)
    for i in range(SubListLen):
        total = 0
        for j in range(ListLen):
            total += List1[j][i]
        FinalList.append(total/ListLen)
    return FinalList

def ChopList(DataList, ChopBy): #srednia gdzie size of window nie ma znaczenia
    #musi byc warunek ze jesli (code_amount * protocol_amount) != 9 -> return 
    BER_List1 = []
    BER_List2 = []
    BER_List3 = []
    E_List1 = []
    E_List2 = []
    E_List3 = []
    Time_List1 = []
    Time_List2 = []
    Time_List3 = []
    WinSizeList = []
    x = []


    Probability_List = DataList[0].propability

    if ChopBy == 0: #protocol
        for obj in DataList:
            if obj.typeOfProtocol == 1:
                BER_List1.append(obj.BER)
                E_List1.append(obj.E)
                Time_List1.append(obj.time)

            if obj.typeOfProtocol == 2:
                BER_List2.append(obj.BER)
                E_List2.append(obj.E)
                Time_List2.append(obj.time)

            if obj.typeOfProtocol == 3:
                BER_List3.append(obj.BER)
                E_List3.append(obj.E)
                Time_List3.append(obj.time)

    if ChopBy == 1: #Code
        for obj in DataList:
             if obj.typeOfCode == 1:
                BER_List1.append(obj.BER)
                E_List1.append(obj.E)
                Time_List1.append(obj.time)

             if obj.typeOfCode == 2:
                BER_List2.append(obj.BER)
                E_List2.append(obj.E)
                Time_List2.append(obj.time)

             if obj.typeOfCode == 3:
                BER_List3.append(obj.BER)
                E_List3.append(obj.E)
                Time_List3.append(obj.time)

    if ChopBy == 2: #WinsSize
        WinSize = DataList[0].SizeOfWindow
        i = 0 
        while i < len(DataList):
            if WinSize == DataList[i].SizeOfWindow:
                BER_List1.append(DataList[i].BER)
                E_List1.append(DataList[i].E)
                Time_List1.append(DataList[i].time)
                i += 1
            else:
                BER = AverageFromList(BER_List1) # z jakiejs przyczyny BER_List1 = AverageFromList(BER_List1) nie dziala
                E = AverageFromList(E_List1) #
                Time = AverageFromList(Time_List1)
                x.append(MasterList([1,0,1], BER, E, [1,0,1], DataList[i-1].SizeOfWindow, 0, 0, Probability_List, Time))
                BER_List1.clear()
                E_List1.clear()
                Time_List1.clear()
                if i < len(DataList) - 1: #inaczej blad wyskoczy przy koncu listy
                    WinSize = DataList[i+1].SizeOfWindow

        #ostatni element nie wejdzie w else
        BER = AverageFromList(BER_List1)
        E = AverageFromList(E_List1)
        Time = AverageFromList(Time_List1)
        x.append(MasterList([1,0,1], BER, E, [1,0,1], DataList[i-1].SizeOfWindow, 0, 0, Probability_List, Time))
        #ShowListContents(x)

    if ChopBy < 2:
        BER_List1 = AverageFromList(BER_List1)
        BER_List2 = AverageFromList(BER_List2)
        BER_List3 = AverageFromList(BER_List3)
        E_List1 = AverageFromList(E_List1)
        E_List2 = AverageFromList(E_List2)
        E_List3 = AverageFromList(E_List3)
        Time_List1 = AverageFromList(Time_List1)
        Time_List2 = AverageFromList(Time_List2)
        Time_List3 = AverageFromList(Time_List3)
        #tutaj blad wywala
        x.append(MasterList([1,0,1], BER_List1, E_List1, [1,0,1], 0, 1, 1, Probability_List, Time_List1))
        x.append(MasterList([1,0,1], BER_List2, E_List2, [1,0,1], 0, 2, 2, Probability_List, Time_List2))
        x.append(MasterList([1,0,1], BER_List3, E_List3, [1,0,1], 0, 3, 3, Probability_List, Time_List3))

    return x

def ChopListByWinSize(DataList, ChopBy):
    BER_List1 = []
    BER_List2 = []
    BER_List3 = []
    E_List1 = []
    E_List2 = []
    E_List3 = []
    Time_List1 = []
    Time_List2 = []
    Time_List3 = []
    x = []

    Probability_List = DataList[0].propability
    WinSize = DataList[0].SizeOfWindow
    i = 0
    while i < len(DataList):
        if WinSize == DataList[i].SizeOfWindow:
            if ChopBy == 0: #protocol
                if DataList[i].typeOfProtocol == 1:
                    BER_List1.append(DataList[i].BER)
                    E_List1.append(DataList[i].E)
                    Time_List1.append(DataList[i].time)

                if DataList[i].typeOfProtocol == 2:
                    BER_List2.append(DataList[i].BER)
                    E_List2.append(DataList[i].E)
                    Time_List2.append(DataList[i].time)

                if DataList[i].typeOfProtocol == 3:
                    BER_List3.append(DataList[i].BER)
                    E_List3.append(DataList[i].E)
                    Time_List3.append(DataList[i].time)

            if ChopBy == 1: #Code
                if DataList[i].typeOfCode == 1:
                   BER_List1.append(DataList[i].BER)
                   E_List1.append(DataList[i].E)
                   Time_List1.append(DataList[i].time)

                if DataList[i].typeOfCode == 2:
                   BER_List2.append(DataList[i].BER)
                   E_List2.append(DataList[i].E)
                   Time_List2.append(DataList[i].time)

                if DataList[i].typeOfCode == 3:
                   BER_List3.append(DataList[i].BER)
                   E_List3.append(DataList[i].E)
                   Time_List3.append(DataList[i].time)

            i += 1
        else:
            BER1 = AverageFromList(BER_List1)
            BER2 = AverageFromList(BER_List2)
            BER3 = AverageFromList(BER_List3)
            E1 = AverageFromList(E_List1)
            E2 = AverageFromList(E_List2)
            E3 = AverageFromList(E_List3)
            Time1 = AverageFromList(Time_List1)
            Time2 = AverageFromList(Time_List2)
            Time3 = AverageFromList(Time_List3)
            x.append(MasterList([1,0,1], BER1, E1, [1,0,1], WinSize, 1, 1, Probability_List, Time1))
            x.append(MasterList([1,0,1], BER2, E2, [1,0,1], WinSize, 2, 2, Probability_List, Time2))
            x.append(MasterList([1,0,1], BER3, E3, [1,0,1], WinSize, 3, 3, Probability_List, Time3))
            BER_List1.clear()
            BER_List2.clear()
            BER_List3.clear()
            E_List1.clear()
            E_List2.clear()
            E_List3.clear()
            Time_List1.clear()
            Time_List2.clear()
            Time_List3.clear()
            if i < len(DataList) - 1: #inaczej blad wyskoczy przy koncu listy
                WinSize = DataList[i+1].SizeOfWindow
    #ostatnie dane dla ostatniej ramki nie wejda w else
    BER1 = AverageFromList(BER_List1)
    BER2 = AverageFromList(BER_List2)
    BER3 = AverageFromList(BER_List3)
    E1 = AverageFromList(E_List1)
    E2 = AverageFromList(E_List2)
    E3 = AverageFromList(E_List3)
    Time1 = AverageFromList(Time_List1)
    Time2 = AverageFromList(Time_List2)
    Time3 = AverageFromList(Time_List3)
    x.append(MasterList([1,0,1], BER1, E1, [1,0,1], WinSize, 1, 1, Probability_List, Time1))
    x.append(MasterList([1,0,1], BER2, E2, [1,0,1], WinSize, 2, 2, Probability_List, Time2))
    x.append(MasterList([1,0,1], BER3, E3, [1,0,1], WinSize, 3, 3, Probability_List, Time3))
    return x

def ShowListContents(DataList):
    for obj in DataList:
        print("P: " + str(obj.typeOfProtocol) + " C: " + str(obj.typeOfCode) + " WS: " + str(obj.SizeOfWindow) + " lenProb: " + str(len(obj.propability)) + " lenBER: " + str(len(obj.BER)))

def ShowPlot(DataList):
    if len(DataList) < 1: #Dla bezpieczenstwa
        return
    print("Generowanie wykresow...")
    #DataList ma wsobie za dużo obiektów więc trzeba go troche przerzedzić
    #ma za duzo poniewaz obiekt jest generowany dla kazdej opcji prawdopobienstwa
    #wiec w DataList jest obiektów Protocol_amount * Code_amount * (ilosc opcji prawdopodobienstwa)
    #a ilosc obiektow do wykresow powinna wynosić Protocol_amount * Code_amount
    #trzeba przerobic E, BER , Prawdopodobiesntwo na listy tych parametrów inaczej wykresy sie nie zrobia
    #nie wiadomo ile jest opcji prawdopodobienstwa wiec trzeba zrobic zabezpieczenie przed List out_of_index
    Protocol_ID_List = []
    Code_ID_List = []
    Probability_List = []
    BER_List = []
    E_List = []
    Final_BER_List = []
    Final_E_List = []
    FinalDataList = []
    WindowSize = [] 
    Time_List = []
    Final_Time_List = []

    FigNameList =[]
    
    #zabezpieczenie przed innymi opcjami maina
    Protocol_Amount = []
    Code_Amount = []
    WinSize_Amount = []

    #sprawdzenie ilosci opcji prawdopodobienstwa + ilosc opcji w maine
    for obj in DataList:
        Probability_List.append((1.0 - obj.propability)*100)
        Protocol_ID_List.append(obj.typeOfProtocol)
        Code_ID_List.append(obj.typeOfCode)
        WindowSize.append(obj.SizeOfWindow)
        BER_List.append(obj.BER/float(len(obj.data)))   
        E_List.append(obj.E/(obj.ReceivedBits))
        Time_List.append(obj.time)

        #print("test recived - data")
        #print(str(obj.ReceivedBits - len(obj.data)) + " P: " + str(obj.typeOfProtocol) +" C: " + str(obj.typeOfCode))

    Protocol_Amount = len(np.unique(Protocol_ID_List))
    Code_Amount = len(np.unique(Code_ID_List))
    WinSize_Amount = len(np.unique(WindowSize))

    Protocol_ID_List = np.unique(Protocol_ID_List)
    Code_ID_List = np.unique(Code_ID_List)
    Probability_List = np.unique(Probability_List)
    WindowSize = np.unique(WindowSize)
    #do przerobienia BER_Listy i E_Listy 
    last = 0.0 
    avg = len(BER_List) / float(Code_Amount * Protocol_Amount * WinSize_Amount) #9 tyle jest roznych opcji code && protocol !!! jesli zmieni sie fory w __main__ to sie wysypie

    while last < len(BER_List):
        Final_BER_List.append(BER_List[int(last):int(last + avg)])
        Final_E_List.append(E_List[int(last):int(last + avg)])
        Final_Time_List.append(Time_List[int(last):int(last + avg)])
        last += avg
    #dzieki temu mamy liste list
    Iter = 0
    #Jest blad code_amount nie odpowiada protokolom ktore mogly byc dane. Do poprawy
    for WinSize in range(WinSize_Amount): #winsize
        for pr in range(Protocol_Amount): #protokół
            for c in range(Code_Amount): #Kod
                #[1,0,1] poniewaz wykresom nie robi to roznicy co tam jest
                FinalDataList.append(MasterList([1,0,1], Final_BER_List[Iter], Final_E_List[Iter], [1,0,1], WindowSize[WinSize], Protocol_ID_List[pr], Code_ID_List[c], Probability_List, Final_Time_List[Iter]))
                Iter +=1         

    #dla łatwiejszego testowania poszczególnych opcji
    #Zeby nie trzeba bylo czekac az wszytkie fory sie zrobia
    if Protocol_Amount == 1 and Code_Amount == 1: 
        plt.plot(FinalDataList[0].propability, FinalDataList[0].E, label="E")
        plt.plot(FinalDataList[0].propability, FinalDataList[0].BER,  label="BER")
        plt.legend()
        plt.title(Protocol_Names[FinalDataList[0].typeOfProtocol] + " || " + Code_Names[FinalDataList[0].typeOfCode] + " || " + "Długośc ramki "+ str(FinalDataList[0].SizeOfWindow) )
        plt.xlabel(r"Prawodopodobieństwo błedu [%]")
        plt.ylabel('Współczynnik:')
        plt.savefig("fig1.png")
        plt.show()

    if Protocol_Amount == Code_Amount and not (Protocol_Amount == 1 and Code_Amount == 1):
        startTime = time.time()
        print("Generowanie PlotsPerParams 1/12")
        DrawSubPlots(FinalDataList, FigNameList, WinSize_Amount, Protocol_Amount, Code_Amount, "PlotsPerParams" , 0, 0)
        CreateMergedPhotoVert(FigNameList, "AllFigs.png")

        print("Generowanie PlotsPerParamsTime 2/12")
        FigNameList = []
        DrawSubPlots(FinalDataList, FigNameList, WinSize_Amount, Protocol_Amount, Code_Amount, "PlotPerParamsTime" , 0, 1)
        CreateMergedPhotoVert(FigNameList, "AllFigsTime.png")

        AddTextToImg("Srednie wartosci dla protokolow dla danej wielkosci ramki","AllFigs.png", 300, 50)
        AddTextToImg("Srednie wartosci dla protokolow dla danej wielkosci ramki","AllFigsTime.png", 300, 50)

        print("Generowanie AvgPerProtByWinSize 3/12")
        ChoppedList = ChopListByWinSize(FinalDataList, 0)
        FigNameList = []
        DrawSubPlots(ChoppedList, FigNameList, WinSize_Amount, 1, 3, "AvgPerProtByWinSize" , 1, 0)
        MergeImagesVert(FigNameList, "AllFigs.png")

        print("Generowanie AvgPerProtByWinSizeTime 4/12")
        FigNameList = []
        DrawSubPlots(ChoppedList, FigNameList, WinSize_Amount, 1, 3, "AvgPerProtByWinSizeTime" , 1, 1)
        MergeImagesVert(FigNameList, "AllFigsTime.png")

        AddTextToImg("Srednie wartosci dla kodow dla danej wielkosci ramki","AllFigs.png", 300, 50)
        AddTextToImg("Srednie wartosci dla kodow dla danej wielkosci ramki","AllFigsTime.png", 300, 50)

        print("Generowanie AvgPerCodeByWinSize 5/12")
        ChoppedList = ChopListByWinSize(FinalDataList, 1)
        FigNameList = []
        DrawSubPlots(ChoppedList, FigNameList, WinSize_Amount, 1, 3, "AvgPerCodeByWinSize" , 2, 0)
        MergeImagesVert(FigNameList, "AllFigs.png")

        print("Generowanie AvgPerCodeByWinSizeTime 6/12")
        FigNameList= []
        DrawSubPlots(ChoppedList, FigNameList, WinSize_Amount, 1, 3, "AvgPerCodeByWinSizeTime" , 2, 1)
        MergeImagesVert(FigNameList, "AllFigsTime.png")

        AddTextToImg("Srednie wartosci dla poszczegolnych opcji","AllFigs.png", 500, 50)
        AddTextToImg("Srednie wartosci dla poszczegolnych opcji","AllFigsTime.png", 500, 50)

        print("Generowanie AvgPerProt 7/12")
        ChoppedList = ChopList(FinalDataList, 0)

        FigNameList = []
        DrawSubPlots(ChoppedList, FigNameList, WinSize_Amount, 1, Protocol_Amount, "AvgPerProt" , 3, 0)
        im1 = Image.open("AllFigs.png")
        im2 = FigNameList[0]
        VerticalImgMerge(im1, im2, "AllFigs.png")

        print("Generowanie AvgPerProtTime 8/12")
        FigNameList = []
        DrawSubPlots(ChoppedList, FigNameList, WinSize_Amount, 1, Protocol_Amount, "AvgPerProtTime" , 3, 1)
        im1 = Image.open("AllFigsTime.png")
        im2 = FigNameList[0]
        VerticalImgMerge(im1, im2, "AllFigsTime.png")


        print("Generowanie AvgPerCode 9/12")
        ChoppedList = ChopList(FinalDataList, 1)
        FigNameList = []
        DrawSubPlots(ChoppedList, FigNameList, WinSize_Amount, 1, Code_Amount, "AvgPerCode" , 4, 0)
        im1 = Image.open("AllFigs.png")
        im2 = FigNameList[0]
        VerticalImgMerge(im1, im2, "AllFigs.png")

        print("Generowanie AvgPerCodeTime 10/12")
        FigNameList = []
        DrawSubPlots(ChoppedList, FigNameList, WinSize_Amount, 1, Code_Amount, "AvgPerCodeTime" , 4, 1)
        im1 = Image.open("AllFigsTime.png")
        im2 = FigNameList[0]
        VerticalImgMerge(im1, im2, "AllFigsTime.png")

        print("Generowanie AvgPerWs 11/12")
        ChoppedList = ChopList(FinalDataList, 2)
        FigNameList = []
        DrawSubPlots(ChoppedList, FigNameList, WinSize_Amount, 1, WinSize_Amount, "AvgPerWinSize" , 5, 0)
        im1 = Image.open("AllFigs.png")
        im2 = FigNameList[0]
        VerticalImgMerge(im1, im2, "AllFigs.png")

        print("Generowanie AvgPerWs 12/12")
        FigNameList = []
        DrawSubPlots(ChoppedList, FigNameList, WinSize_Amount, 1, WinSize_Amount, "AvgPerWinSize" , 5, 1)
        im1 = Image.open("AllFigsTime.png")
        im2 = FigNameList[0]
        VerticalImgMerge(im1, im2, "AllFigsTime.png")

        round(time.time() - startTime, 6)
        print("Wykresy wygenerowane w " + str(round(time.time() - startTime, 6)) + "sekund")

        print("Laczenie wszytkiego w AllDataMerged.png")
        im1 = Image.open("AllFigs.png")
        im2 = Image.open("AllFigsTime.png")
        HorizontalImgMerge(im1, im2, "AllDataMerged.png")

        File = Path("Result.jpg") #dla laczenie zdjec przed i po
        if File.is_file():
            print("Istnieje")

    else:
        print("Narazie program dla innych opcji sie wysypie Module: Plotter")