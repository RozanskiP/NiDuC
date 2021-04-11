

class Receiver:
    sender = None
    typeOfProtocol = 0
    typeOfCode = 0
    
    def __init__(self):
        pass

    def showResults(self): # wyswietlenie wyniku, liczby ramek, pozytywanie i negatywnie przeslanych i ponownie doslanych
        pass

    def setSender(self, sender): # podanie wartosci sendera do odsylania bledow i proszenia o poprawke
        self.sender = sender

    def receiverFrameStopAndWait(self, frame): # odebranie dla algorytmu stop and wait

        # zakłocenie ramki

        # wybor kodu ktory byl dodawany jaka powinna byc jego wartosc


        # porownanie naszej ramki
        # odpowiedznie czy ma byc ponowiona czy jest zaakceptowana 



        pass

    def receiverFrameGoBackN(self, frame): # odebranie dla algorytmu go back n
        pass

    def receiverFrameSelectiveReapeat(self, frame): # odebranie dla algorytmu selevtive reapeat
        pass

    def CodeParity(self, frame): # oblicza jaki jest kod bledu ktory dotarl
        pass
    
    def CodeMirroring(self, frame): # oblicza jaki jest kod bledu ktory dotarl
        pass

    def CodeCRC(self, frame): # oblicza jaki jest kod bledu ktory dotarl
        pass