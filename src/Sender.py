from Generator import generateBit
from Receiver import Receiver


class Sender:
    receiver = None
    Window = 10

    def __init__(self, receiver):
        # generoweane danych rand, pozniej przerobic na wczytanie zdjecia ReadFromFile.py
        generateBit(bits, 25)
        pass

    def sendFrameStopAndWait(self): # wysylanie ramki za pomoca algorytmu stop and wait
        pass

    def sendFrameGoBackN(self): # wysylanie ramki za pomoca algorytmu go back n
        pass

    def sendFrameSelectiveReapeat(self): # wysylanie ramki za pomoca algorytmu selevtive reapeat
        pass

    