from matplotlib.pyplot import legend
from math import floor
import matplotlib
from MasterList import MasterList
import numpy as np
import matplotlib.pyplot as plt
# Make sure that we are using QT5
matplotlib.use('Qt5Agg')
from PyQt5 import QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar


class ScrollableWindow(QtWidgets.QMainWindow):
    def __init__(self, fig):
        self.qapp = QtWidgets.QApplication([])

        QtWidgets.QMainWindow.__init__(self)
        self.widget = QtWidgets.QWidget()
        self.setCentralWidget(self.widget)
        self.widget.setLayout(QtWidgets.QVBoxLayout())
        self.widget.layout().setContentsMargins(0,0,0,0)
        self.widget.layout().setSpacing(0)

        self.fig = fig
        self.canvas = FigureCanvas(self.fig)
        self.canvas.draw()
        self.scroll = QtWidgets.QScrollArea(self.widget)
        self.scroll.setWidget(self.canvas)

        self.nav = NavigationToolbar(self.canvas, self.widget)
        self.widget.layout().addWidget(self.nav)
        self.widget.layout().addWidget(self.scroll)

        self.show()
        exit(self.qapp.exec_()) 

def ShowPlot(DataList):
    if len(DataList) < 1: #Dla bezpieczenstwa
        return
    #DataList ma wsobie za dużo obiektów więc trzeba go troche przerzedzić
    #ma za duzo poniewaz obiekt jest generowany dla kazdej opcji prawdopobienstwa
    #wiec w DataList jest obiektów Protocol_amount * Code_amount * (ilosc opcji prawdopodobienstwa)
    #a ilosc obiektow do wykresow powinna wynosić Protocol_amount * Code_amount
    #trzeba przerobic E, BER , Prawdopodobiesntwo na listy tych parametrów inaczej wykresy sie nie zrobia
    #nie wiadomo ile jest opcji prawdopodobienstwa wiec trzeba zrobic zabezpieczenie przed List out_of_index
    Protocol_ID = DataList[0].typeOfProtocol
    Code_ID = DataList[0].typeOfCode
    Probability_List = []
    BER_List = []
    E_List = []
    Final_BER_List = []
    Final_E_List = []
    FinalDataList = []
    WindowSize = DataList[0].SizeOfWindow #jeszcze nie wiadomo czy wielkosc ramki bedzie sie zmieniac
    
    #zabezpieczenie przed innymi opcjami maina
    Protocol_Amount = []
    Code_Amount = []

    #sprawdzenie ilosci opcji prawdopodobienstwa + ilosc opcji w maine
    for obj in DataList:
        #jesli zmieni sie cos to oznacza to ze ilosc opcji prawodopodobienstwa została juz osiagnieta
        if Protocol_ID == obj.typeOfProtocol and Code_ID == obj.typeOfCode:
            Probability_List.append(1.0 - obj.propability)
        Protocol_Amount.append(obj.typeOfProtocol)
        Code_Amount.append(obj.typeOfCode)
    
    Protocol_Amount = len(np.unique(Protocol_Amount))
    Code_Amount = len(np.unique(Code_Amount))

    print("Protocol: " + str(Protocol_Amount) + " Code: " + str(Code_Amount))
    #Teraz trzeba zebrac E i BER z kazdego przypadku
    for obj in DataList:
        BER_List.append(obj.BER)
        E_List.append(obj.E)

    #do przerobienia BER_Listy i E_Listy 
    last = 0.0 
    avg = len(BER_List) / float(Code_Amount * Protocol_Amount) #9 tyle jest roznych opcji code && protocol !!! jesli zmieni sie fory w __main__ to sie wysypie

    while last < len(BER_List):
        Final_BER_List.append(BER_List[int(last):int(last + avg)])
        Final_E_List.append(E_List[int(last):int(last + avg)])
        last += avg
    #dzieki temu mamy liste list

    Iter = 0
    for pr in range(1, Protocol_Amount + 1): #protokół
        for c in range(1, Code_Amount + 1): #Kod
            #[1,0,1] poniewaz wykresom nie robi to roznicy co tam jest
            FinalDataList.append(MasterList([1,0,1], Final_BER_List[Iter], Final_E_List[Iter], [1,0,1], WindowSize, pr, c, Probability_List))
            Iter +=1

    #iteracja Kodow i protokolow jest od 1 stad "NULL"
    Protocol_Names = ["NULL", "Stop and wait", "Go back n","Selective Repeat"] 
    Code_Names = ["NULL", "Kod parzystości", "Kod dublowania", "CRC32"]

    i=0
    #dla łatwiejszego testowania poszczególnych opcji
    #Zeby nie trzeba bylo czekac az wszytkie fory sie zrobia
    if Protocol_Amount == 1 and Code_Amount == 1: 
        plt.plot(FinalDataList[0].propability, FinalDataList[0].E, label="E")
        plt.plot(FinalDataList[0].propability, FinalDataList[0].BER,  label="BER")
        plt.legend()
        plt.title(Protocol_Names[FinalDataList[0].typeOfProtocol] + " || " + Code_Names[FinalDataList[0].typeOfCode] + " || " + "Długośc ramki "+ str(FinalDataList[0].SizeOfWindow) )
        plt.xlabel('Prawodopodobieństwo błedu')
        plt.ylabel('Współczynnik:')
        plt.show()

    if Protocol_Amount == Code_Amount and not (Protocol_Amount == 1 and Code_Amount == 1):
        fig, axes = plt.subplots(ncols=Protocol_Amount, nrows=Code_Amount, figsize=(16,16))
        for ax in axes.flatten():
            ax.plot(FinalDataList[i].propability, FinalDataList[i].E, label="E")
            ax.plot(FinalDataList[i].propability, FinalDataList[i].BER,  label="BER")
            ax.legend()
            ax.set_title(Protocol_Names[FinalDataList[i].typeOfProtocol] + " || " + Code_Names[FinalDataList[i].typeOfCode] + " || " + "Długośc ramki "+ str(FinalDataList[i].SizeOfWindow) )
            ax.set_xlabel('Prawodopodobieństwo błedu')
            ax.set_ylabel('Współczynnik:')   
            i += 1

        okno = ScrollableWindow(fig)
    else:
        print("Narazie program dla innych opcji sie wysypie Module: Plotter")