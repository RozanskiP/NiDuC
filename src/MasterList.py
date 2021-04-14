

class MasterList:
    data = [0] # wszystkie bity
    BER = 0 # suma liczb przekłamanych
    E = 0 # dane ktore byly dobrze przeslane
    SizeOfWindow = 0 # wielkosc okna
    typeOfProtocol = 0
    typeOfCode = 0
    propability = 0 # prawdopodobienstwo

    def __init__(self, data, BER, E, SizeOfWindow, typeOfProtocol, typeOfCode, propability):
        self.data = data
        self.BER = BER
        self.E = E
        self.SizeOfWindow = SizeOfWindow
        self.typeOfProtocol = typeOfProtocol
        self.typeOfCode = typeOfCode
        self.propability = propability
