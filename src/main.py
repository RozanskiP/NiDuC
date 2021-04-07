from Generator import generateBit
from Coder import coderBit
from TransmisionCannal import transmision
from Decoder import decodeBit

def main():
    bits = []
    n = 10 # po ile elemntow
    generateBit(bits, 25)
    print(bits)
    listofbits = coderBit(bits, n)
    print("List of list: ")
    print(listofbits)

    transmision(listofbits, 0.3) # minimalnie 0.001 (1 promil) im mniej tym bardziej zmienia
    print(listofbits)

    decodeBit(listofbits, n)

if __name__ == "__main__":
    main()
