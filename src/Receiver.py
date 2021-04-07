from Sender import Sender


class Receiver:
    sender = None
    def __init__(self):
        pass

    def showResults(self): # wyswietlenie wyniku, liczby ramek, pozytywanie i negatywnie przeslanych i ponownie doslanych
        pass

    def setSender(self, sender): # podanie wartosci sendera do odsylania bledow i proszenia o poprawke
        self.sender = sender

    def receiverFrameStopAndWait(self): # odebranie dla algorytmu stop and wait
        pass

    def receiverFrameGoBackN(self): # odebranie dla algorytmu go back n
        pass

    def receiverFrameSelectiveReapeat(self): # odebranie dla algorytmu selevtive reapeat
        pass

    def CodeParity(self): # oblicza jaki jest kod bledu ktory dotarl
        pass
    
    def addCodeMirrosing(self): # oblicza jaki jest kod bledu ktory dotarl
        pass

    def addCodeCRC(self): # oblicza jaki jest kod bledu ktory dotarl
        pass