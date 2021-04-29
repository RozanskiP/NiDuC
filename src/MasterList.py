

class MasterList:
    data = [0] # wszystkie bity
    BER = 0 # suma liczb przekłamanych
    E = 0 # dane ktore byly dobrze przeslane
    ReceivedBits = 0 # wszyskie proby przeslania danych do obliczen
    SizeOfWindow = 0 # wielkosc okna
    typeOfProtocol = 0
    typeOfTransmision = 0
    typeOfCode = 0
    propability = 0 # prawdopodobienstwo
    time = 0 # czas


    def __init__(self, data, BER, E, ReceivedBits, SizeOfWindow, typeOfProtocol, typeOfCode, propability, time, typeOfTransmision):
        self.data = data
        self.BER = BER
        self.E = E
        self.ReceivedBits = ReceivedBits
        self.SizeOfWindow = SizeOfWindow
        self.typeOfProtocol = typeOfProtocol
        self.typeOfCode = typeOfCode
        self.propability = propability
        self.time = time
        self.typeOfTransmision = typeOfTransmision